"""
Conversation History Management
Manages storage and retrieval of conversation history for the chatbot.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from config import HISTORY_FILE, MAX_HISTORY_ENTRIES, ENABLE_HISTORY


class ConversationHistory:
    """
    Manages conversation history storage and retrieval.
    """
    
    def __init__(self, session_id: str = "default"):
        """
        Initialize conversation history manager.
        
        Args:
            session_id: Unique identifier for the conversation session
        """
        self.session_id = session_id
        self.history_file = HISTORY_FILE
        self.history: List[Dict] = []
        self.enabled = ENABLE_HISTORY
        
        if self.enabled:
            self.load_history()
    
    def add_message(self, user_message: str, bot_response: str, 
                   intent: Optional[str] = None, entities: Optional[Dict] = None):
        """
        Add a message exchange to the conversation history.
        
        Args:
            user_message: The user's input message
            bot_response: The bot's response
            intent: Detected intent (optional)
            entities: Extracted entities (optional)
        """
        if not self.enabled:
            return
        
        entry = {
            'timestamp': datetime.now().isoformat(),
            'session_id': self.session_id,
            'user_message': user_message,
            'bot_response': bot_response,
            'intent': intent,
            'entities': entities
        }
        
        self.history.append(entry)
        
        # Limit history size
        if len(self.history) > MAX_HISTORY_ENTRIES:
            self.history = self.history[-MAX_HISTORY_ENTRIES:]
        
        self.save_history()
    
    def get_history(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Get conversation history.
        
        Args:
            limit: Maximum number of entries to return
            
        Returns:
            List of conversation entries
        """
        if limit:
            return self.history[-limit:]
        return self.history.copy()
    
    def get_recent_messages(self, count: int = 5) -> List[Dict]:
        """
        Get recent conversation messages.
        
        Args:
            count: Number of recent messages to retrieve
            
        Returns:
            List of recent conversation entries
        """
        return self.history[-count:] if self.history else []
    
    def clear_history(self):
        """Clear conversation history."""
        self.history = []
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
    
    def save_history(self):
        """Save conversation history to file."""
        if not self.enabled:
            return
        
        try:
            # Load existing history from file
            all_history = []
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    all_history = json.load(f)
            
            # Update or add session history
            session_found = False
            for i, session in enumerate(all_history):
                if session.get('session_id') == self.session_id:
                    all_history[i] = {
                        'session_id': self.session_id,
                        'messages': self.history
                    }
                    session_found = True
                    break
            
            if not session_found:
                all_history.append({
                    'session_id': self.session_id,
                    'messages': self.history
                })
            
            # Save to file
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(all_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def load_history(self):
        """Load conversation history from file."""
        if not self.enabled:
            return
        
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    all_history = json.load(f)
                    
                # Find this session's history
                for session in all_history:
                    if session.get('session_id') == self.session_id:
                        self.history = session.get('messages', [])
                        break
        except Exception as e:
            print(f"Error loading history: {e}")
            self.history = []

