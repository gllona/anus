#!/usr/bin/env python3
"""
Simple test script for the ANUS application.
"""

from anus.core.orchestrator import AgentOrchestrator

def main():
    """Run a simple test task with the ANUS application."""
    print("Initializing ANUS orchestrator...")
    orchestrator = AgentOrchestrator(config_path="config.yaml")
    
    # Define a simple task
    task = "Tell me a joke about programming"
    
    print(f"\nExecuting task: {task}")
    result = orchestrator.execute_task(task, mode="single")
    
    print("\nTask completed!")
    print("Result:")
    print(result.get("answer", "No answer provided"))
    
    # Try a more complex task
    complex_task = "Find information about Python programming language and summarize its key features"
    
    print(f"\nExecuting complex task: {complex_task}")
    result = orchestrator.execute_task(complex_task, mode="multi")
    
    print("\nComplex task completed!")
    print("Result:")
    print(result.get("answer", "No answer provided"))

if __name__ == "__main__":
    main() 