"""
Dummy Action tool for testing purposes.

This tool provides a simple action that always succeeds.
"""

import logging
from typing import Dict, Any, Union

from anus.tools.base.tool import BaseTool
from anus.tools.base.tool_result import ToolResult

class DummyActionTool(BaseTool):
    """
    A dummy tool for testing purposes.
    
    ANUS needs a simple tool to test its backend functionality.
    """
    
    name = "dummy_action"
    description = "A dummy action that always succeeds"
    parameters = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "A message to include in the response"
            }
        },
        "required": ["message"]
    }
    
    def execute(self, message: str, **kwargs) -> Union[Dict[str, Any], ToolResult]:
        """
        Execute the dummy action.
        
        Args:
            message: A message to include in the response.
            **kwargs: Additional parameters (ignored).
            
        Returns:
            A success response with the provided message.
        """
        logging.info(f"Dummy action executed with message: '{message}'")
        return {
            "status": "success",
            "message": message,
            "result": "Dummy action completed successfully"
        }

# Re-export the dummy action tool
__all__ = ["DummyActionTool"] 