# ANUS Web Interface

A modern web interface for the ANUS (Autonomous Networked Utility System) AI agent framework.

## Features

- Clean, modern UI with a responsive design
- Task submission and real-time response display
- Support for various agent modes (single, multi, auto)
- Task history tracking
- Settings management
- About page with framework information

## Installation

1. Make sure you have Python 3.11+ installed
2. Install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure the main ANUS package is installed
2. Run the web interface:

```bash
python app.py
```

3. Open a web browser and navigate to `http://localhost:3000`

## Development

The web interface is built with:

- Flask (backend)
- Bootstrap 5 (responsive UI)
- Pure JavaScript (no frameworks)
- CSS3 with custom styling

## Structure

- `app.py` - Main Flask application
- `templates/` - HTML templates
- `static/` - Static files (CSS, JavaScript, images) 