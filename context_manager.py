"""
Context Management Module
Manages conversation context for multi-turn dialogues.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from config import MAX_CONTEXT_HISTORY, CONTEXT_TIMEOUT


class ContextManager:
    """
    Manages conversation context for maintaining state across multiple turns.
    """
    
    def __init__(self, session_id: str = "default"):
        """
        Initialize context manager.
        
        Args:
            session_id: Unique identifier for the conversation session
        """
        self.session_id = session_id
        self.context: Dict[str, Any] = {
            'user_name': None,
            'entities': {},
            'previous_intents': [],
            'conversation_history': [],
            'session_start': datetime.now(),
            'last_activity': datetime.now(),
        }
        self.max_history = MAX_CONTEXT_HISTORY
        self.timeout = CONTEXT_TIMEOUT
    
    def update_context(self, user_message: str, bot_response: str, 
                      intent: Optional[str] = None, entities: Optional[Dict] = None):
        """
        Update context with new conversation turn.
        
        Args:
            user_message: User's input message
            bot_response: Bot's response
            intent: Detected intent
            entities: Extracted entities
        """
        # Update last activity time
        self.context['last_activity'] = datetime.now()
        
        # Add to conversation history
        self.context['conversation_history'].append({
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': datetime.now().isoformat(),
            'intent': intent,
            'entities': entities
        })
        
        # Limit history size
        if len(self.context['conversation_history']) > self.max_history:
            self.context['conversation_history'] = \
                self.context['conversation_history'][-self.max_history:]
        
        # Update entities
        if entities:
            self.context['entities'].update(entities)
        
        # Track previous intents
        if intent:
            self.context['previous_intents'].append(intent)
            if len(self.context['previous_intents']) > 5:
                self.context['previous_intents'] = \
                    self.context['previous_intents'][-5:]
        
        # Extract and store user name if mentioned
        if entities and 'PERSON' in entities:
            names = entities['PERSON']
            if names:
                self.context['user_name'] = names[0]
    
    def get_context(self) -> Dict[str, Any]:
        """
        Get current context.
        
        Returns:
            Current context dictionary
        """
        return self.context.copy()
    
    def get_user_name(self) -> Optional[str]:
        """
        Get stored user name from context.
        
        Returns:
            User name if available, None otherwise
        """
        return self.context.get('user_name')
    
    def get_entities(self) -> Dict[str, Any]:
        """
        Get stored entities from context.
        
        Returns:
            Dictionary of stored entities
        """
        return self.context.get('entities', {}).copy()
    
    def get_recent_history(self, count: int = 3) -> List[Dict]:
        """
        Get recent conversation history.
        
        Args:
            count: Number of recent messages to retrieve
            
        Returns:
            List of recent conversation entries
        """
        history = self.context.get('conversation_history', [])
        return history[-count:] if history else []
    
    def get_previous_intent(self) -> Optional[str]:
        """
        Get the most recent intent.
        
        Returns:
            Most recent intent if available, None otherwise
        """
        intents = self.context.get('previous_intents', [])
        return intents[-1] if intents else None
    
    def clear_context(self):
        """Clear all context data."""
        self.context = {
            'user_name': None,
            'entities': {},
            'previous_intents': [],
            'conversation_history': [],
            'session_start': datetime.now(),
            'last_activity': datetime.now(),
        }
    
    def is_context_expired(self) -> bool:
        """
        Check if context has expired based on timeout.
        
        Returns:
            True if context has expired, False otherwise
        """
        last_activity = self.context.get('last_activity')
        if not last_activity:
            return False
        
        if isinstance(last_activity, str):
            last_activity = datetime.fromisoformat(last_activity)
        
        elapsed = (datetime.now() - last_activity).total_seconds()
        return elapsed > self.timeout
    
    def get_context_summary(self) -> str:
        """
        Get a human-readable summary of the current context.
        
        Returns:
            Context summary string
        """
        summary_parts = []
        
        if self.context.get('user_name'):
            summary_parts.append(f"User name: {self.context['user_name']}")
        
        if self.context.get('entities'):
            summary_parts.append(f"Entities: {len(self.context['entities'])} stored")
        
        history_count = len(self.context.get('conversation_history', []))
        summary_parts.append(f"Conversation turns: {history_count}")
        
        return ", ".join(summary_parts) if summary_parts else "No context available"

