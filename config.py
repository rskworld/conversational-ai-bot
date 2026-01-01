"""
Configuration settings for Conversational AI Bot
Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

# Bot Configuration
BOT_NAME = "Conversational AI Bot"
BOT_VERSION = "1.0.0"
DEFAULT_RESPONSE = "I'm sorry, I didn't understand that. Could you please rephrase?"

# Context Management
MAX_CONTEXT_HISTORY = 10  # Maximum number of previous messages to keep in context
CONTEXT_TIMEOUT = 3600  # Context timeout in seconds (1 hour)

# Intent Recognition
INTENT_CONFIDENCE_THRESHOLD = 0.6  # Minimum confidence score for intent recognition

# Entity Extraction
SUPPORTED_ENTITIES = ['PERSON', 'DATE', 'TIME', 'LOCATION', 'ORGANIZATION', 'MONEY', 'PERCENT']

# Conversation History
ENABLE_HISTORY = True
HISTORY_FILE = "conversation_history.json"
MAX_HISTORY_ENTRIES = 100

# NLP Settings
LANGUAGE = "en"
USE_LEMMATIZATION = True
REMOVE_STOPWORDS = True

# Developer Information
DEVELOPER_NAME = "RSK World"
DEVELOPER_WEBSITE = "https://rskworld.in"
DEVELOPER_EMAIL = "help@rskworld.in"
DEVELOPER_PHONE = "+91 93305 39277"
YEAR = 2026

