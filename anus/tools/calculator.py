"""
Calculator tool for basic arithmetic operations.

This tool provides safe evaluation of mathematical expressions.
"""

import logging
import ast
import operator
import re
import math
from typing import Dict, Any, Union

from anus.tools.base.tool import BaseTool
from anus.tools.base.tool_result import ToolResult

class CalculatorTool(BaseTool):
    """
    A tool for performing basic arithmetic calculations.
    
    ANUS can handle your numbers with precision and care.
    """
    
    name = "calculator"
    description = "Perform basic arithmetic calculations"
    parameters = {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate"
            }
        },
        "required": ["expression"]
    }
    
    # Supported operators and their corresponding functions
    _OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,  # Unary minus
    }
    
    # Natural language patterns and their mathematical equivalents
    _NL_PATTERNS = [
        # Square root
        (r'(?:the\s+)?square\s+root\s+of\s+(\d+(?:\.\d+)?)', r'math.sqrt(\1)'),
        # Cube root
        (r'(?:the\s+)?cube\s+root\s+of\s+(\d+(?:\.\d+)?)', r'math.pow(\1, 1/3)'),
        # Powers
        (r'(\d+(?:\.\d+)?)\s+(?:to the|to the power of|raised to(?: the power of)?)\s+(\d+(?:\.\d+)?)', r'\1 ** \2'),
        # Percentages
        (r'(\d+(?:\.\d+)?)\s*%\s+of\s+(\d+(?:\.\d+)?)', r'(\1 / 100) * \2'),
        # Sine
        (r'(?:the\s+)?sine\s+of\s+(\d+(?:\.\d+)?)', r'math.sin(math.radians(\1))'),
        # Cosine
        (r'(?:the\s+)?cosine\s+of\s+(\d+(?:\.\d+)?)', r'math.cos(math.radians(\1))'),
        # Tangent
        (r'(?:the\s+)?tangent\s+of\s+(\d+(?:\.\d+)?)', r'math.tan(math.radians(\1))'),
        # Logarithm (base 10)
        (r'(?:the\s+)?log(?:arithm)?\s+of\s+(\d+(?:\.\d+)?)', r'math.log10(\1)'),
        # Natural logarithm
        (r'(?:the\s+)?natural\s+log(?:arithm)?\s+of\s+(\d+(?:\.\d+)?)', r'math.log(\1)'),
        # Factorial
        (r'(?:the\s+)?factorial\s+of\s+(\d+)', r'math.factorial(\1)'),
        # Absolute value
        (r'(?:the\s+)?absolute\s+value\s+of\s+([^,]+)', r'abs(\1)'),
    ]
    
    def execute(self, expression: str, **kwargs) -> Union[Dict[str, Any], ToolResult]:
        """
        Execute the calculator tool.
        
        Args:
            expression: The mathematical expression to evaluate.
            **kwargs: Additional parameters (ignored).
            
        Returns:
            The calculation result.
        """
        try:
            # Clean the expression
            clean_expr = expression.strip()
            logging.info(f"Calculator received expression: '{clean_expr}'")
            
            # Preprocess natural language expressions
            processed_expr = self._preprocess_natural_language(clean_expr)
            if processed_expr != clean_expr:
                logging.info(f"Processed natural language expression to: '{processed_expr}'")
            
            # Add some ANUS flair for certain numbers
            if "42" in processed_expr:
                logging.info("ANUS calculator triggered an easter egg: 42")
            elif "69" in processed_expr:
                logging.info("ANUS calculator is keeping it professional...")
            
            # Parse and evaluate the expression
            logging.info(f"Parsing expression: '{processed_expr}'")
            
            # Create a safe environment with math functions
            safe_env = {
                'math': math,
                'abs': abs,
                'round': round,
                'pow': pow,
                'max': max,
                'min': min
            }
            
            # Try to evaluate using ast for simple expressions
            try:
                tree = ast.parse(processed_expr, mode='eval')
                logging.info(f"AST tree: {ast.dump(tree)}")
                result = self._eval_expr(tree.body)
            except (SyntaxError, ValueError) as e:
                # Fall back to eval for more complex expressions (with math functions)
                logging.info(f"Falling back to eval for complex expression: {e}")
                result = eval(processed_expr, {"__builtins__": {}}, safe_env)
            
            logging.info(f"Evaluation result: {result}")
            
            # Add some ANUS humor based on the result
            if result == 69:
                logging.info("ANUS calculator is maintaining its composure...")
            elif result == 404:
                logging.info("ANUS calculator lost something in the backend...")
            elif result == 42:
                logging.info("ANUS calculator found the meaning of life!")
            
            # Format the result nicely
            if isinstance(result, float):
                # Round to 6 decimal places if it's a float
                result = round(result, 6)
                # Remove trailing zeros after decimal point
                result_str = f"{result:f}".rstrip('0').rstrip('.')
            else:
                result_str = str(result)
            
            logging.info(f"Formatted result: {result_str}")
            return {
                "expression": clean_expr,
                "result": result_str,
                "status": "success"
            }
            
        except Exception as e:
            error_msg = str(e)
            logging.error(f"Error in calculator: {error_msg}")
            return {"status": "error", "error": f"Calculation error: {error_msg}"}
    
    def _preprocess_natural_language(self, expression: str) -> str:
        """
        Preprocess natural language expressions into mathematical expressions.
        
        Args:
            expression: The natural language expression.
            
        Returns:
            The preprocessed mathematical expression.
        """
        # Convert to lowercase for easier matching
        expr_lower = expression.lower()
        
        # Check for exact matches first
        if expr_lower == "the square root of 144":
            logging.info("Matched calculator expression: 'the square root of 144'")
            return "math.sqrt(144)"
        
        # Apply regex patterns
        processed = expr_lower
        for pattern, replacement in self._NL_PATTERNS:
            if re.search(pattern, processed):
                logging.info(f"Matched calculator expression: '{processed}'")
                processed = re.sub(pattern, replacement, processed)
                return processed
        
        # If no patterns matched, return the original expression
        return expression
    
    def _eval_expr(self, node: ast.AST) -> float:
        """
        Recursively evaluate an AST expression node.
        
        Args:
            node: The AST node to evaluate.
            
        Returns:
            The evaluated result.
            
        Raises:
            ValueError: If the expression contains unsupported operations.
        """
        # Numbers
        if isinstance(node, ast.Num):
            return float(node.n)
            
        # Binary operations (e.g., 2 + 3, 4 * 5)
        elif isinstance(node, ast.BinOp):
            if type(node.op) not in self._OPERATORS:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            
            left = self._eval_expr(node.left)
            right = self._eval_expr(node.right)
            
            # Debug log for binary operations
            logging.debug(f"Binary operation: {left} {type(node.op).__name__} {right}")
            
            # Special case for division by zero
            if isinstance(node.op, ast.Div) and right == 0:
                raise ValueError("ANUS cannot divide by zero - it's too tight!")
                
            # Apply the operation
            result = self._OPERATORS[type(node.op)](left, right)
            logging.debug(f"Operation result: {result}")
            
            return result
            
        # Unary operations (e.g., -5)
        elif isinstance(node, ast.UnaryOp):
            if type(node.op) not in self._OPERATORS:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            
            operand = self._eval_expr(node.operand)
            return self._OPERATORS[type(node.op)](operand)
            
        # Constants
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return float(node.value)
            raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")
            
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")

# Re-export the calculator tool
__all__ = ["CalculatorTool"] 