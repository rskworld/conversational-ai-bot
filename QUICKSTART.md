# Quick Start Guide

<!--
Project: Conversational AI Bot
Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
-->

## Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Download NLTK Data

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Step 3: Run the Bot

```bash
python main.py
```

That's it! You're ready to chat.

## Basic Usage

### Interactive Mode

```bash
python main.py
```

Then type your messages and press Enter.

### Programmatic Usage

```python
from chatbot import ConversationalAIBot

# Create bot instance
bot = ConversationalAIBot()

# Chat with the bot
response = bot.chat("Hello, my name is John")
print(response)

# Bot remembers context
response = bot.chat("What's my name?")
print(response)  # Output: "Your name is John..."
```

## Example Commands

When running in interactive mode, you can use:

- `help` - Show available commands
- `context` - Show current conversation context
- `history` - Show conversation history
- `clear` - Clear conversation history
- `quit` or `exit` - Exit the chatbot

## Example Conversations

### Example 1: Basic Introduction

```
You: Hello
Bot: Hello! I'm a conversational AI bot. How can I assist you today?

You: My name is Alice
Bot: Nice to meet you, Alice! I'll remember that. How can I help you today?

You: What's my name?
Bot: Your name is Alice. I remember you from our previous conversation!
```

### Example 2: Asking Questions

```
You: What can you do?
Bot: I'm a conversational AI bot with the following capabilities:
     • Context-aware conversations
     • Multi-turn dialogue support
     • Intent recognition
     • Entity extraction
     • Conversation history

You: What time is it?
Bot: The current time is 03:45 PM.

You: What's the date?
Bot: Today's date is January 01, 2026.
```

## Run Examples

To see more examples:

```bash
python example_usage.py
```

## Run Tests

To run the test suite:

```bash
python test_chatbot.py
```

## Need Help?

- Check the full [README.md](README.md) for detailed documentation
- See [INSTALLATION.md](INSTALLATION.md) for installation help
- Visit https://rskworld.in for more resources

## Contact

- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

© 2026 RSK World. All rights reserved.

