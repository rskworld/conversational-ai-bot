"""
Example Usage of Conversational AI Bot
Demonstrates various features and capabilities of the chatbot.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from chatbot import ConversationalAIBot


def example_basic_conversation():
    """Example of basic conversation."""
    print("=" * 60)
    print("Example 1: Basic Conversation")
    print("=" * 60)
    
    bot = ConversationalAIBot()
    
    messages = [
        "Hello",
        "My name is John",
        "What's my name?",
        "What can you do?",
        "Thank you",
        "Goodbye"
    ]
    
    for message in messages:
        print(f"\nUser: {message}")
        response = bot.chat(message)
        print(f"Bot: {response}")
    
    print("\n")


def example_context_awareness():
    """Example demonstrating context awareness."""
    print("=" * 60)
    print("Example 2: Context Awareness")
    print("=" * 60)
    
    bot = ConversationalAIBot()
    
    # First conversation
    print("\nUser: My name is Alice")
    print(f"Bot: {bot.chat('My name is Alice')}")
    
    # Later in conversation, bot remembers
    print("\nUser: What's my name?")
    print(f"Bot: {bot.chat('What\'s my name?')}")
    
    # Context summary
    print(f"\nContext Summary: {bot.get_context_summary()}")
    print("\n")


def example_entity_extraction():
    """Example demonstrating entity extraction."""
    print("=" * 60)
    print("Example 3: Entity Extraction")
    print("=" * 60)
    
    bot = ConversationalAIBot()
    
    messages = [
        "My name is Sarah Johnson",
        "I live in New York",
        "My email is sarah@example.com",
        "Call me at +1-555-123-4567"
    ]
    
    for message in messages:
        print(f"\nUser: {message}")
        response = bot.chat(message)
        print(f"Bot: {response}")
    
    # Show extracted entities
    context = bot.context_manager.get_context()
    print(f"\nExtracted Entities: {context.get('entities', {})}")
    print("\n")


def example_multi_turn_dialogue():
    """Example of multi-turn dialogue."""
    print("=" * 60)
    print("Example 4: Multi-turn Dialogue")
    print("=" * 60)
    
    bot = ConversationalAIBot()
    
    conversation = [
        ("Hello, how are you?", "Greeting"),
        ("My name is Michael", "Name introduction"),
        ("What's my name?", "Name query"),
        ("What time is it?", "Time query"),
        ("What's the date?", "Date query"),
        ("Thank you for your help", "Compliment"),
        ("Goodbye", "Farewell")
    ]
    
    for message, intent_type in conversation:
        print(f"\nUser: {message}")
        response = bot.chat(message)
        print(f"Bot: {response}")
    
    print("\n")


def example_conversation_history():
    """Example showing conversation history."""
    print("=" * 60)
    print("Example 5: Conversation History")
    print("=" * 60)
    
    bot = ConversationalAIBot()
    
    # Have a conversation
    bot.chat("Hello")
    bot.chat("My name is David")
    bot.chat("What can you do?")
    
    # Retrieve history
    history = bot.get_conversation_history()
    
    print("\nConversation History:")
    for i, entry in enumerate(history, 1):
        print(f"\n{i}. User: {entry.get('user_message')}")
        print(f"   Bot: {entry.get('bot_response')}")
        print(f"   Intent: {entry.get('intent', 'N/A')}")
        if entry.get('entities'):
            print(f"   Entities: {entry.get('entities')}")
    
    print("\n")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("Conversational AI Bot - Example Usage")
    print("Developer: RSK World (https://rskworld.in)")
    print("=" * 60 + "\n")
    
    examples = [
        example_basic_conversation,
        example_context_awareness,
        example_entity_extraction,
        example_multi_turn_dialogue,
        example_conversation_history
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"Error in {example_func.__name__}: {e}\n")
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

