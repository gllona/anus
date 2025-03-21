#!/usr/bin/env python3
"""
Script to generate a simple SVG logo for the ANUS web interface.
Run this script to create anus_logo.svg in the current directory.
"""

import os

def generate_anus_logo():
    """Generate a simple geometric SVG logo for ANUS."""
    svg_content = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <!-- ANUS Logo -->
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4a56e2;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#ff6b6b;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Main circular outline -->
    <circle cx="100" cy="100" r="90" fill="none" stroke="url(#grad1)" stroke-width="8" />
    
    <!-- Inner circle -->
    <circle cx="100" cy="100" r="45" fill="url(#grad1)" opacity="0.7" />
    
    <!-- Connecting lines -->
    <g stroke="url(#grad1)" stroke-width="6">
        <!-- A -->
        <line x1="55" y1="70" x2="145" y2="70" />
        <line x1="55" y1="70" x2="70" y2="130" />
        <line x1="145" y1="70" x2="130" y2="130" />
        <line x1="70" y1="100" x2="130" y2="100" />
        
        <!-- N -->
        <line x1="60" y1="70" x2="60" y2="130" />
        <line x1="60" y1="70" x2="140" y2="130" />
        <line x1="140" y1="70" x2="140" y2="130" />
        
        <!-- U -->
        <line x1="70" y1="70" x2="70" y2="120" />
        <line x1="70" y1="120" x2="130" y2="120" />
        <line x1="130" y1="70" x2="130" y2="120" />
        
        <!-- S -->
        <path d="M80,70 C60,70 60,100 80,100 C100,100 100,130 80,130" fill="none" />
    </g>
</svg>'''
    
    # Write the SVG to a file
    output_path = 'anus_logo.svg'
    with open(output_path, 'w') as f:
        f.write(svg_content)
    
    print(f"Logo created at {output_path}")
    return output_path

if __name__ == "__main__":
    generate_anus_logo() 