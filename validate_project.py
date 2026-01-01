"""
Project Validation Script
Validates all project files and checks for errors.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import os
import sys
import importlib.util
from pathlib import Path


def check_file_exists(filepath):
    """Check if file exists."""
    if os.path.exists(filepath):
        print(f"[OK] {filepath}")
        return True
    else:
        print(f"[MISSING] {filepath}")
        return False


def check_import(module_name):
    """Check if module can be imported."""
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            print(f"[FAIL] Cannot import {module_name}")
            return False
        print(f"[OK] {module_name} - Import successful")
        return True
    except Exception as e:
        print(f"[FAIL] {module_name} - Import failed: {e}")
        return False


def check_syntax(filepath):
    """Check Python file syntax."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            compile(f.read(), filepath, 'exec')
        print(f"[OK] {filepath} - Syntax OK")
        return True
    except SyntaxError as e:
        print(f"[ERROR] {filepath} - Syntax Error: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] {filepath} - Error: {e}")
        return False


def main():
    """Main validation function."""
    print("=" * 60)
    print("Conversational AI Bot - Project Validation")
    print("Developer: RSK World (https://rskworld.in)")
    print("=" * 60)
    print()
    
    errors = []
    
    # Required Python files
    print("Checking Required Files:")
    print("-" * 60)
    required_files = [
        'chatbot.py',
        'main.py',
        'app.py',
        'config.py',
        'context_manager.py',
        'intent_recognizer.py',
        'entity_extractor.py',
        'conversation_history.py',
        'sentiment_analyzer.py',
        'language_support.py',
        'api_integrations.py',
        'conversation_analytics.py',
        'response_templates.py',
        'requirements.txt',
        'README.md',
        'setup.py',
        '__init__.py'
    ]
    
    for file in required_files:
        if not check_file_exists(file):
            errors.append(f"Missing file: {file}")
    
    print()
    
    # Check directories
    print("Checking Required Directories:")
    print("-" * 60)
    required_dirs = ['templates', 'static']
    for dir_name in required_dirs:
        if os.path.exists(dir_name) and os.path.isdir(dir_name):
            print(f"[OK] {dir_name}/")
        else:
            print(f"[MISSING] {dir_name}/")
            errors.append(f"Missing directory: {dir_name}")
    
    print()
    
    # Check Python syntax
    print("Checking Python Syntax:")
    print("-" * 60)
    python_files = [f for f in required_files if f.endswith('.py')]
    for file in python_files:
        if os.path.exists(file):
            if not check_syntax(file):
                errors.append(f"Syntax error in: {file}")
    
    print()
    
    # Check imports
    print("Checking Module Imports:")
    print("-" * 60)
    modules_to_check = [
        'chatbot',
        'context_manager',
        'intent_recognizer',
        'entity_extractor',
        'conversation_history',
        'sentiment_analyzer',
        'language_support',
        'api_integrations',
        'conversation_analytics',
        'response_templates',
        'config'
    ]
    
    for module in modules_to_check:
        if not check_import(module):
            errors.append(f"Import error: {module}")
    
    print()
    
    # Summary
    print("=" * 60)
    if errors:
        print(f"[FAILED] Validation FAILED - {len(errors)} error(s) found:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("[PASSED] Validation PASSED - All checks successful!")
        return True
    print("=" * 60)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

