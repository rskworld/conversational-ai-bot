# Installation Guide

<!--
Project: Conversational AI Bot
Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
-->

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd conversational-ai-bot

# Or extract the ZIP file if downloaded
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data (Required)

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 5. Run the Chatbot

```bash
python main.py
```

## Alternative Installation (Using setup.py)

```bash
pip install -e .
```

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: NLTK Data Not Found

**Solution**: Download required NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Issue: Colorama Not Working on Windows

**Solution**: Colorama should work automatically on Windows. If not, ensure it's installed:
```bash
pip install colorama
```

## Running Examples

To see example usage:

```bash
python example_usage.py
```

## Development

For development, install in editable mode:

```bash
pip install -e .
```

## Contact

For issues or questions:
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

© 2026 RSK World. All rights reserved.

