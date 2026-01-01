"""
Conversational AI Bot - Main Chatbot Class
Advanced conversational chatbot with context management and multi-turn dialogue support.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Optional, Dict
import re
from datetime import datetime
import uuid

from context_manager import ContextManager
from intent_recognizer import IntentRecognizer
from entity_extractor import EntityExtractor
from conversation_history import ConversationHistory
from sentiment_analyzer import SentimentAnalyzer
from language_support import LanguageSupport
from api_integrations import APIIntegrations
from conversation_analytics import ConversationAnalytics
from response_templates import ResponseTemplates
from config import (
    BOT_NAME, DEFAULT_RESPONSE, INTENT_CONFIDENCE_THRESHOLD,
    DEVELOPER_NAME, DEVELOPER_WEBSITE, DEVELOPER_EMAIL, DEVELOPER_PHONE, YEAR
)


class ConversationalAIBot:
    """
    Main conversational AI bot class with context awareness and multi-turn dialogue support.
    """
    
    def __init__(self, session_id: Optional[str] = None):
        """
        Initialize the conversational AI bot.
        
        Args:
            session_id: Optional session identifier for conversation tracking
        """
        self.session_id = session_id or str(uuid.uuid4())
        self.context_manager = ContextManager(self.session_id)
        self.intent_recognizer = IntentRecognizer()
        self.entity_extractor = EntityExtractor()
        self.conversation_history = ConversationHistory(self.session_id)
        
        # Advanced features
        self.sentiment_analyzer = SentimentAnalyzer()
        self.language_support = LanguageSupport()
        self.api_integrations = APIIntegrations()
        self.analytics = ConversationAnalytics()
        self.response_templates = ResponseTemplates()
        
        # Initialize analytics
        self.analytics.start_session(self.session_id)
        
        # Initialize bot with greeting
        self._initialize_bot()
    
    def _initialize_bot(self):
        """Initialize the bot with default settings."""
        print(f"Initializing {BOT_NAME}...")
        print(f"Session ID: {self.session_id}")
        print(f"Developer: {DEVELOPER_NAME} ({DEVELOPER_WEBSITE})")
        print("-" * 50)
    
    def chat(self, user_message: str) -> str:
        """
        Process user message and generate response.
        
        Args:
            user_message: User's input message
            
        Returns:
            Bot's response
        """
        if not user_message or not user_message.strip():
            return "I didn't receive any message. Please try again."
        
        # Check if context has expired
        if self.context_manager.is_context_expired():
            self.context_manager.clear_context()
            self.conversation_history.clear_history()
        
        # Detect language
        detected_language = self.language_support.detect_language(user_message)
        self.language_support.set_language(detected_language)
        
        # Analyze sentiment
        sentiment_analysis = self.sentiment_analyzer.analyze(user_message)
        sentiment = sentiment_analysis['sentiment']
        
        # Recognize intent
        intent, confidence = self.intent_recognizer.recognize(user_message)
        
        # Extract entities
        entities = self.entity_extractor.extract(user_message)
        
        # Generate response based on intent and context
        response = self._generate_response(user_message, intent, confidence, entities, sentiment_analysis)
        
        # Update context
        self.context_manager.update_context(user_message, response, intent, entities)
        
        # Save to conversation history
        self.conversation_history.add_message(user_message, response, intent, entities)
        
        # Track analytics
        self.analytics.track_message(
            self.session_id, intent, entities, sentiment, detected_language
        )
        
        return response
    
    def _generate_response(self, user_message: str, intent: str, 
                          confidence: float, entities: Dict, sentiment_analysis: Dict = None) -> str:
        """
        Generate response based on intent, context, and entities.
        
        Args:
            user_message: User's message
            intent: Detected intent
            confidence: Intent confidence score
            entities: Extracted entities
            
        Returns:
            Generated response
        """
        user_message_lower = user_message.lower()
        
        # Handle low confidence intents
        if confidence < INTENT_CONFIDENCE_THRESHOLD:
            return self._handle_unknown_intent(user_message)
        
        # Check for API-related queries
        if 'joke' in user_message_lower or 'tell me a joke' in user_message_lower:
            joke_result = self.api_integrations.get_joke()
            if joke_result.get('success'):
                joke = joke_result.get('joke', {})
                return f"{joke.get('setup', '')}\n{joke.get('punchline', '')}"
        
        if 'quote' in user_message_lower or 'inspiration' in user_message_lower:
            quote_result = self.api_integrations.get_quote()
            if quote_result.get('success'):
                quote = quote_result.get('quote', {})
                return f'"{quote.get("text", "")}" - {quote.get("author", "")}'
        
        # Check for calculation requests
        if any(op in user_message for op in ['+', '-', '*', '/', '=']):
            calc_match = self._extract_calculation(user_message)
            if calc_match:
                calc_result = self.api_integrations.calculate(calc_match)
                if calc_result.get('success'):
                    return f"The answer is {calc_result.get('result')}"
        
        # Handle specific intents
        if intent == 'greeting':
            return self._handle_greeting(entities)
        
        elif intent == 'goodbye':
            return self._handle_goodbye()
        
        elif intent == 'name_introduction':
            return self._handle_name_introduction(entities)
        
        elif intent == 'name_query':
            return self._handle_name_query()
        
        elif intent == 'question':
            return self._handle_question(user_message, entities)
        
        elif intent == 'help':
            return self._handle_help()
        
        elif intent == 'weather':
            return self._handle_weather(entities)
        
        elif intent == 'time':
            return self._handle_time()
        
        elif intent == 'date':
            return self._handle_date()
        
        elif intent == 'compliment':
            return self._handle_compliment()
        
        else:
            return self._handle_unknown_intent(user_message, sentiment_analysis)
    
    def _handle_greeting(self, entities: Dict) -> str:
        """Handle greeting intent."""
        user_name = self.context_manager.get_user_name()
        
        if user_name:
            return self.response_templates.get_response('greeting_with_name', name=user_name)
        else:
            return self.response_templates.get_response('greeting')
    
    def _handle_goodbye(self) -> str:
        """Handle goodbye intent."""
        user_name = self.context_manager.get_user_name()
        
        if user_name:
            return self.response_templates.get_response('goodbye_with_name', name=user_name)
        else:
            return self.response_templates.get_response('goodbye')
    
    def _handle_name_introduction(self, entities: Dict) -> str:
        """Handle name introduction intent."""
        if 'PERSON' in entities and entities['PERSON']:
            name = entities['PERSON'][0]
            return self.response_templates.get_response('name_introduction', name=name)
        else:
            return self.response_templates.get_response('name_not_found')
    
    def _handle_name_query(self) -> str:
        """Handle name query intent."""
        user_name = self.context_manager.get_user_name()
        
        if user_name:
            return self.response_templates.get_response('name_query', name=user_name)
        else:
            return self.response_templates.get_response('name_not_found')
    
    def _handle_question(self, user_message: str, entities: Dict) -> str:
        """Handle question intent."""
        user_message_lower = user_message.lower()
        
        # Check for specific question types
        if 'what can you do' in user_message_lower or 'what do you do' in user_message_lower:
            return self._handle_help()
        
        if 'how are you' in user_message_lower:
            return "I'm doing well, thank you for asking! I'm here to help you with conversations. How can I assist you?"
        
        if 'who are you' in user_message_lower or 'what are you' in user_message_lower:
            return f"I'm {BOT_NAME}, an advanced conversational AI bot. I can help you with various tasks and have natural conversations. I'm developed by {DEVELOPER_NAME}."
        
        # Generic question response
        return "That's an interesting question! I'm still learning, but I'll do my best to help. Could you provide more details?"
    
    def _handle_help(self) -> str:
        """Handle help intent."""
        return self.response_templates.get_response('help')
    
    def _handle_weather(self, entities: Dict) -> str:
        """Handle weather intent."""
        location = None
        if 'LOCATION' in entities and entities['LOCATION']:
            location = entities['LOCATION'][0]
        
        if location:
            weather_data = self.api_integrations.get_weather(location)
            if weather_data.get('success'):
                return f"Weather for {location}: {weather_data.get('temperature')}, {weather_data.get('condition')}"
            return self.response_templates.get_response('weather', location=location)
        else:
            return "I'd be happy to help with weather information! Could you tell me which location you're interested in?"
    
    def _handle_time(self) -> str:
        """Handle time query intent."""
        current_time = datetime.now().strftime("%I:%M %p")
        return self.response_templates.get_response('time', time=current_time)
    
    def _handle_date(self) -> str:
        """Handle date query intent."""
        current_date = datetime.now().strftime("%B %d, %Y")
        return self.response_templates.get_response('date', date=current_date)
    
    def _handle_compliment(self) -> str:
        """Handle compliment intent."""
        return self.response_templates.get_response('compliment')
    
    def _handle_unknown_intent(self, user_message: str, sentiment_analysis: Dict = None) -> str:
        """Handle unknown or low-confidence intents."""
        # Try to use context to provide a better response
        recent_history = self.context_manager.get_recent_history(1)
        
        # Adjust response based on sentiment
        if sentiment_analysis and sentiment_analysis.get('sentiment') == 'negative':
            return "I sense you might be frustrated. I'm here to help! Could you rephrase your question or tell me what you need?"
        
        if recent_history:
            # Reference previous conversation
            return self.response_templates.get_response('unknown')
        else:
            return self.response_templates.get_response('unknown')
    
    def _extract_calculation(self, text: str) -> Optional[str]:
        """Extract mathematical expression from text."""
        # Simple pattern for basic calculations
        pattern = r'(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)'
        match = re.search(pattern, text)
        if match:
            return f"{match.group(1)}{match.group(2)}{match.group(3)}"
        return None
    
    def get_context_summary(self) -> str:
        """
        Get a summary of the current conversation context.
        
        Returns:
            Context summary string
        """
        return self.context_manager.get_context_summary()
    
    def get_conversation_history(self, limit: Optional[int] = None):
        """
        Get conversation history.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of conversation entries
        """
        return self.conversation_history.get_history(limit)
    
    def clear_session(self):
        """Clear current session context and history."""
        self.context_manager.clear_context()
        self.conversation_history.clear_history()
        self.analytics.end_session(self.session_id)
        print("Session cleared. Starting fresh conversation.")
    
    def get_analytics(self) -> Dict:
        """
        Get conversation analytics.
        
        Returns:
            Dictionary with analytics data
        """
        return self.analytics.get_metrics()
    
    def get_analytics_summary(self) -> str:
        """
        Get human-readable analytics summary.
        
        Returns:
            Formatted analytics summary
        """
        return self.analytics.get_summary()
    
    def get_sentiment_analysis(self, text: str) -> Dict:
        """
        Analyze sentiment of text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Sentiment analysis results
        """
        return self.sentiment_analyzer.analyze(text)
    
    def set_language(self, language_code: str) -> bool:
        """
        Set conversation language.
        
        Args:
            language_code: Language code (e.g., 'en', 'es', 'hi')
            
        Returns:
            True if language is supported, False otherwise
        """
        return self.language_support.set_language(language_code)
    
    def get_current_language(self) -> str:
        """Get current language code."""
        return self.language_support.get_language()


if __name__ == "__main__":
    # Example usage
    bot = ConversationalAIBot()
    
    print("\n" + "="*50)
    print("Conversational AI Bot - Interactive Mode")
    print("Type 'quit' or 'exit' to end the conversation")
    print("="*50 + "\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"\nBot: {bot.chat(user_input)}")
            break
        
        if user_input:
            response = bot.chat(user_input)
            print(f"Bot: {response}\n")

