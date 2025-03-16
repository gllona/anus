#!/usr/bin/env python3
"""
Web interface for the ANUS (Autonomous Networked Utility System).
This application provides a user-friendly interface to interact with the ANUS tool.
"""

from flask import Flask, render_template, request, jsonify
# Commenting out ANUS import that's causing issues
# from anus.core.orchestrator import AgentOrchestrator
import logging
import os
import json
import time
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Mock orchestrator for demo purposes
class MockOrchestrator:
    def execute_task(self, task, mode='auto'):
        """Mock execution of a task."""
        logger.info(f"Mock executing task: '{task}' in {mode} mode")
        
        # Simulate processing time
        time.sleep(1)
        
        # Calculate mock complexity
        complexity = min(9.5, len(task) * 0.1 + random.uniform(1, 3))
        
        # Select mode based on complexity or user selection
        used_mode = mode
        if mode == 'auto':
            used_mode = 'single' if complexity < 3.0 else 'multi'
            
        # Generate mock responses
        responses = {
            'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs!',
            'what is python': 'Python is a high-level, interpreted programming language known for its readability and simplicity.',
            'how are you': 'As an AI assistant integrated with ANUS, I\'m functioning optimally. How can I assist you today?',
            'what time is it': f'The current server time is {time.strftime("%H:%M:%S")}',
            'who created you': 'I am an interface for ANUS (Autonomous Networked Utility System), designed to provide an intuitive way to interact with AI agents.'
        }
        
        # Try to find a matching response or generate a generic one
        result = None
        for key, value in responses.items():
            if key in task.lower():
                result = value
                break
                
        if not result:
            if 'calculate' in task.lower() or 'compute' in task.lower() or 'math' in task.lower():
                result = "I would perform this calculation, but my calculator tool needs maintenance."
            elif 'search' in task.lower() or 'find' in task.lower() or 'look up' in task.lower():
                result = "I would search for this information, but my search tool is currently offline."
            else:
                result = f"I've processed your request: '{task}'. In a fully implemented system, you would receive a detailed response here."
        
        return {
            'answer': result,
            'mode': used_mode,
            'complexity': f"{complexity:.1f}/10"
        }

# Initialize the mock orchestrator
orchestrator = MockOrchestrator()
logger.info("Mock orchestrator initialized successfully")

@app.route('/')
def index():
    """Render the main page of the web interface."""
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_task():
    """Execute a task using the orchestrator."""
    try:
        data = request.json
        task = data.get('task', '')
        mode = data.get('mode', 'auto')
        
        logger.info(f"Executing task: '{task}' in {mode} mode")
        
        # Execute the task using the orchestrator
        result = orchestrator.execute_task(task, mode=mode)
        
        # Format the response
        response = {
            'success': True,
            'result': result.get('answer', 'No answer provided'),
            'mode_used': result.get('mode', mode),
            'task_complexity': result.get('complexity', 'Unknown')
        }
        
        return jsonify(response)
    
    except Exception as e:
        logger.error(f"Error executing task: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    """Get the history of executed tasks."""
    try:
        # Mock history data
        history = [
            {"task": "Tell me a joke about programming", "result": "Why do programmers prefer dark mode? Because light attracts bugs!"},
            {"task": "What is Python?", "result": "Python is a high-level programming language known for its readability and versatility."},
            {"task": "How does ANUS work?", "result": "ANUS works by assessing task complexity and dynamically choosing between single-agent and multi-agent processing modes."},
            {"task": "Calculate the square root of 144", "result": "The square root of 144 is 12."},
            {"task": "Find information about artificial intelligence", "result": "Artificial intelligence (AI) refers to intelligence demonstrated by machines..."}
        ]
        
        return jsonify({
            'success': True,
            'history': history
        })
    
    except Exception as e:
        logger.error(f"Error fetching history: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 