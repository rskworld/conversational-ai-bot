# Conversational AI Bot

<!--
Project: Conversational AI Bot
Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
-->

Advanced conversational chatbot with context management and multi-turn dialogue support.

## Features

### Core Features
- **Context-aware conversations**: Maintains context across multiple turns
- **Multi-turn dialogue support**: Handles complex conversation flows
- **Intent recognition**: Identifies user intentions from natural language
- **Entity extraction**: Extracts important information from user messages
- **Conversation history**: Stores and retrieves past conversations

### Advanced Features
- **Sentiment Analysis**: Analyzes user sentiment to provide better responses
- **Multi-language Support**: Detects and supports multiple languages (English, Spanish, French, German, Hindi, Chinese, Japanese, Arabic)
- **API Integrations**: Weather, news, jokes, quotes, and calculations
- **Conversation Analytics**: Tracks metrics, intent distribution, and session statistics
- **Response Templates**: Template-based response system for consistent interactions
- **Web Interface**: Beautiful Flask-based web interface for easy interaction
- **Real-time Analytics**: Track conversation patterns and user engagement

## Technologies

- Python 3.8+
- Natural Language Processing (NLP)
- Machine Learning
- Rasa (optional integration)
- Dialogflow (optional integration)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd conversational-ai-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python main.py
```

## Usage

### Basic Usage

```python
from chatbot import ConversationalAIBot

bot = ConversationalAIBot()
response = bot.chat("Hello, how are you?")
print(response)
```

### Advanced Usage with Context

```python
from chatbot import ConversationalAIBot

bot = ConversationalAIBot()
bot.chat("My name is John")
response = bot.chat("What's my name?")
print(response)  # The bot remembers your name
```

### Using Advanced Features

```python
from chatbot import ConversationalAIBot

bot = ConversationalAIBot()

# Sentiment Analysis
sentiment = bot.get_sentiment_analysis("I'm feeling great today!")
print(sentiment['sentiment'])  # 'positive'

# Language Support
bot.set_language('es')  # Set to Spanish
current_lang = bot.get_current_language()

# Analytics
analytics = bot.get_analytics()
summary = bot.get_analytics_summary()
print(summary)

# API Integrations
response = bot.chat("Tell me a joke")
response = bot.chat("What's 25 + 17?")
response = bot.chat("Weather in New York")
```

### Web Interface

Start the web interface:

```bash
python app.py
```

Then open your browser to `http://localhost:5000`

## Project Structure

```
conversational-ai-bot/
├── main.py                    # Main CLI entry point
├── app.py                     # Flask web interface
├── chatbot.py                 # Core chatbot class
├── context_manager.py         # Context management
├── intent_recognizer.py       # Intent recognition
├── entity_extractor.py        # Entity extraction
├── conversation_history.py    # Conversation history management
├── sentiment_analyzer.py     # Sentiment analysis
├── language_support.py        # Multi-language support
├── api_integrations.py        # External API integrations
├── conversation_analytics.py # Analytics and metrics
├── response_templates.py      # Response templates
├── config.py                  # Configuration settings
├── example_usage.py           # Usage examples
├── test_chatbot.py            # Test suite
├── templates/                 # Web interface templates
│   └── index.html            # Main web interface
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Features

### Context Management
The bot maintains conversation context, allowing it to reference previous messages and maintain coherent multi-turn dialogues.

### Intent Recognition
Uses pattern matching and machine learning techniques to identify user intentions from natural language input.

### Entity Extraction
Extracts entities such as names, dates, locations, and other important information from user messages.

### Conversation History
Stores conversation history for each session, enabling the bot to reference past interactions.

## License

This project is provided by RSK World (https://rskworld.in) for educational and development purposes.

## Contact

- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

© 2026 RSK World. All rights reserved.

