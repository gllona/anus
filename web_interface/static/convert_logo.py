#!/usr/bin/env python3
"""
Script to convert the SVG logo to PNG for better compatibility.
"""

import cairosvg
import os

def convert_svg_to_png():
    """Convert the ANUS logo from SVG to PNG format."""
    svg_path = 'anus_logo.svg'
    png_path = 'anus_logo.png'
    
    # Make sure the SVG file exists
    if not os.path.exists(svg_path):
        print(f"Error: {svg_path} not found.")
        return None
    
    # Convert SVG to PNG
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=200, output_height=200)
    print(f"PNG logo created at {png_path}")
    return png_path

if __name__ == "__main__":
    convert_svg_to_png() 