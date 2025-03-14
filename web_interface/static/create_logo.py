#!/usr/bin/env python3
"""
Script to create a simple PNG logo for the ANUS web interface using Pillow.
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def create_anus_logo():
    """Create a simple circular gradient logo for ANUS."""
    # Create a blank image with a white background
    size = 200
    image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw outer circle
    outer_circle_color = (74, 86, 226, 255)  # #4a56e2
    draw.ellipse((10, 10, size-10, size-10), outline=outer_circle_color, width=8)
    
    # Draw inner circle
    inner_circle_color = (255, 107, 107, 180)  # #ff6b6b with some transparency
    draw.ellipse((size//2 - 45, size//2 - 45, size//2 + 45, size//2 + 45), fill=inner_circle_color)
    
    # Create simple shapes to form "ANUS" instead of using text
    # These are simple geometric shapes arranged to suggest the letters
    
    # A shape
    draw.polygon([(60, 130), (80, 70), (100, 130)], fill=(255, 255, 255, 200))
    draw.line([(70, 110), (90, 110)], fill=(255, 255, 255, 200), width=3)
    
    # N shape
    draw.line([(110, 70), (110, 130)], fill=(255, 255, 255, 200), width=3)
    draw.line([(110, 70), (130, 130)], fill=(255, 255, 255, 200), width=3)
    draw.line([(130, 70), (130, 130)], fill=(255, 255, 255, 200), width=3)
    
    # U shape
    draw.line([(140, 70), (140, 120)], fill=(255, 255, 255, 200), width=3)
    draw.line([(140, 120), (160, 120)], fill=(255, 255, 255, 200), width=3)
    draw.line([(160, 70), (160, 120)], fill=(255, 255, 255, 200), width=3)
    
    # S shape (simplified)
    draw.arc([(170, 70), (190, 90)], 180, 0, fill=(255, 255, 255, 200), width=3)
    draw.arc([(170, 110), (190, 130)], 0, 180, fill=(255, 255, 255, 200), width=3)
    
    # Apply a slight blur for a softer look
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    
    # Save the image
    output_path = 'anus_logo.png'
    image.save(output_path)
    
    print(f"Logo created at {output_path}")
    return output_path

if __name__ == "__main__":
    create_anus_logo() 