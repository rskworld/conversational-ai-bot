"""
Response Templates Module
Manages response templates for consistent bot responses.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, Optional, List
import random


class ResponseTemplates:
    """
    Manages response templates for the chatbot.
    """
    
    def __init__(self):
        """Initialize response templates."""
        self.templates = {
            'greeting': [
                "Hello! I'm a conversational AI bot. How can I assist you today?",
                "Hi there! How can I help you today?",
                "Greetings! What can I do for you?",
                "Hello! Nice to meet you. How may I assist you?",
                "Hey! I'm here to help. What do you need?"
            ],
            'greeting_with_name': [
                "Hello {name}! Nice to see you again. How can I help you today?",
                "Hi {name}! Great to have you back. What can I do for you?",
                "Hey {name}! How can I assist you today?",
                "Welcome back, {name}! How may I help you?"
            ],
            'goodbye': [
                "Goodbye! It was nice talking to you. Have a great day!",
                "See you later! Take care!",
                "Farewell! Have a wonderful day!",
                "Goodbye! Hope to chat with you again soon!",
                "Bye! It was a pleasure talking to you!"
            ],
            'goodbye_with_name': [
                "Goodbye {name}! It was nice talking to you. Have a great day!",
                "See you later, {name}! Take care!",
                "Farewell {name}! Have a wonderful day!",
                "Goodbye {name}! Hope to chat with you again soon!"
            ],
            'name_introduction': [
                "Nice to meet you, {name}! I'll remember that. How can I help you today?",
                "Hello {name}! I'm pleased to meet you. How may I assist you?",
                "Great to meet you, {name}! I'll keep that in mind. What can I do for you?",
                "Hi {name}! Nice to know your name. How can I help you today?"
            ],
            'name_query': [
                "Your name is {name}. I remember you from our previous conversation!",
                "I have your name as {name}. Nice to see you again!",
                "You told me your name is {name}. I remember that!",
                "Your name is {name}. I'm glad I could recall that!"
            ],
            'name_not_found': [
                "I don't have your name stored yet. Could you tell me your name?",
                "I haven't learned your name yet. What should I call you?",
                "I don't know your name. Could you introduce yourself?",
                "I'd love to know your name! What should I call you?"
            ],
            'help': [
                """I'm a conversational AI bot with the following capabilities:

• Context-aware conversations - I remember our previous messages
• Multi-turn dialogue support - I can handle complex conversation flows
• Intent recognition - I understand what you're trying to say
• Entity extraction - I can extract names, dates, locations, and more
• Conversation history - I keep track of our conversations

You can ask me questions, introduce yourself, or just have a conversation. How can I help you today?"""
            ],
            'unknown': [
                "I'm sorry, I didn't understand that. Could you please rephrase?",
                "I'm not sure I understand. Could you try saying that differently?",
                "That's interesting, but I'm not entirely sure how to respond. Could you provide more details?",
                "I'm still learning. Could you rephrase your question or statement?",
                "I didn't quite catch that. Could you try again?"
            ],
            'compliment': [
                "Thank you! I appreciate your kind words. Is there anything else I can help you with?",
                "That's very kind of you to say! I'm glad I could help. Anything else?",
                "Thanks! I'm happy to assist. What else can I do for you?",
                "Thank you for the compliment! I'm here whenever you need help."
            ],
            'time': [
                "The current time is {time}.",
                "It's {time} right now.",
                "The time is {time}.",
                "Right now it's {time}."
            ],
            'date': [
                "Today's date is {date}.",
                "The date today is {date}.",
                "It's {date} today.",
                "Today is {date}."
            ],
            'weather': [
                "I don't have access to real-time weather data, but I'd love to help you find weather information for {location}. You might want to check a weather service for current conditions.",
                "For weather information about {location}, I'd recommend checking a weather service. I don't have real-time weather access.",
                "I can't provide real-time weather data, but you can find weather information for {location} on weather websites."
            ],
            'error': [
                "I'm sorry, I encountered an error. Please try again.",
                "Something went wrong. Could you please try again?",
                "I apologize, but I'm having trouble processing that. Please try again."
            ]
        }
    
    def get_response(self, template_name: str, **kwargs) -> str:
        """
        Get a response from a template.
        
        Args:
            template_name: Name of the template
            **kwargs: Variables to fill in the template
            
        Returns:
            Formatted response string
        """
        if template_name not in self.templates:
            return self.get_response('unknown')
        
        templates = self.templates[template_name]
        template = random.choice(templates)
        
        try:
            return template.format(**kwargs)
        except KeyError as e:
            # If template variable is missing, return template as-is
            return template
    
    def add_template(self, template_name: str, templates: List[str]):
        """
        Add custom templates.
        
        Args:
            template_name: Name of the template category
            templates: List of template strings
        """
        if template_name not in self.templates:
            self.templates[template_name] = []
        
        self.templates[template_name].extend(templates)
    
    def get_all_templates(self) -> Dict[str, List[str]]:
        """
        Get all available templates.
        
        Returns:
            Dictionary of all templates
        """
        return self.templates.copy()
    
    def has_template(self, template_name: str) -> bool:
        """
        Check if a template exists.
        
        Args:
            template_name: Name of the template
            
        Returns:
            True if template exists, False otherwise
        """
        return template_name in self.templates

