#!/bin/bash

# ANUS - Autonomous Networked Utility System
# Command-line shortcut for the ANUS framework

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Function to check if a string is an option (starts with --)
is_option() {
    [[ "$1" == --* ]]
}

# Check the first argument to determine the command
if [ "$1" == "run" ]; then
    # Remove the "run" command from arguments
    shift
    
    # Initialize arrays for options and task parts
    options=()
    task_parts=()
    
    # Process all arguments
    while [ $# -gt 0 ]; do
        if is_option "$1"; then
            # If it's an option (--something), add it and its value to options
            options+=("$1")
            if [ $# -gt 1 ] && ! is_option "$2"; then
                options+=("$2")
                shift
            fi
        else
            # Otherwise, it's part of the task
            task_parts+=("$1")
        fi
        shift
    done
    
    # Combine task parts into a single quoted string
    task="${task_parts[*]}"
    
    # Run the command with proper argument handling
    python -m anus.main run "$task" "${options[@]}" --verbose
    
elif [ "$1" == "interactive" ]; then
    # Start interactive mode
    shift
    python -m anus.main interactive "$@" --verbose
else
    # Pass all arguments to the Python module
    python -m anus.main "$@"
fi 