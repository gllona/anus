"""
Anus - Autonomous Networked Utility System
Main entry point for the Anus AI agent framework
"""

import argparse
import sys
from anus.core.orchestrator import AgentOrchestrator
from anus.ui.cli import CLI

# Define version
__version__ = "0.1.0"

def main():
    """Main entry point for the Anus AI agent"""
    parser = argparse.ArgumentParser(description="Anus AI - Autonomous Networked Utility System")
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Common arguments for all commands
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("--config", type=str, default="config.yaml", help="Path to configuration file")
    parent_parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    # Interactive mode command
    interactive_parser = subparsers.add_parser("interactive", parents=[parent_parser], 
                                              help="Start ANUS in interactive mode")
    
    # Task execution command
    task_parser = subparsers.add_parser("run", parents=[parent_parser],
                                       help="Execute a specific task")
    task_parser.add_argument("task", type=str, help="Task description")
    task_parser.add_argument("--mode", type=str, default="single", choices=["single", "multi"], 
                            help="Agent mode (single or multi)")
    
    # Add version argument to main parser
    parser.add_argument("--version", action="version", version=f"ANUS version {__version__}")
    
    # For backward compatibility, add task argument to main parser
    parser.add_argument("--task", type=str, help="Task description (deprecated, use 'run' command instead)")
    parser.add_argument("--mode", type=str, default="single", choices=["single", "multi"], 
                       help="Agent mode (deprecated, use with 'run' command)")
    
    args = parser.parse_args()
    
    # Initialize the CLI
    cli = CLI(verbose=getattr(args, 'verbose', False))
    
    # Display welcome message
    cli.display_welcome()
    
    # Initialize the agent orchestrator
    config_path = getattr(args, 'config', 'config.yaml')
    orchestrator = AgentOrchestrator(config_path=config_path)
    
    # Handle commands
    if args.command == "interactive" or (not args.command and not getattr(args, 'task', None)):
        # Start interactive mode
        cli.start_interactive_mode(orchestrator)
    elif args.command == "run":
        # Execute the specified task
        result = orchestrator.execute_task(args.task, mode=getattr(args, 'mode', 'single'))
        cli.display_result(result)
    elif getattr(args, 'task', None):
        # Backward compatibility for --task argument
        result = orchestrator.execute_task(args.task, mode=args.mode)
        cli.display_result(result)
    else:
        # No command specified, show help
        parser.print_help()

if __name__ == "__main__":
    main()
