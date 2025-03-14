#!/bin/bash

# ANUS - Autonomous Networked Utility System
# Command-line shortcut for the ANUS framework

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if the first argument is "run"
if [ "$1" == "run" ]; then
    # Remove the "run" argument and pass the rest to the Python module
    shift
    python -m anus.main --task "$*" --verbose
else
    # Pass all arguments to the Python module
    python -m anus.main "$@"
fi 