"""
Intent Recognition Module
Recognizes user intentions from natural language input.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, List, Tuple, Optional
from collections import Counter
import re


class IntentRecognizer:
    """
    Recognizes user intentions from natural language text.
    """
    
    def __init__(self):
        """Initialize the intent recognizer with predefined patterns."""
        # Intent patterns with keywords and confidence scores
        self.intent_patterns = {
            'greeting': {
                'keywords': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 
                           'good evening', 'greetings', 'howdy'],
                'patterns': [
                    r'\b(hello|hi|hey|greetings)\b',
                    r'good\s+(morning|afternoon|evening)',
                ],
                'confidence': 0.9
            },
            'goodbye': {
                'keywords': ['bye', 'goodbye', 'see you', 'farewell', 'later', 
                           'take care', 'adios'],
                'patterns': [
                    r'\b(bye|goodbye|see you|farewell)\b',
                    r'take\s+care',
                ],
                'confidence': 0.9
            },
            'question': {
                'keywords': ['what', 'when', 'where', 'who', 'why', 'how', 'which', 
                           'can you', 'could you', 'would you'],
                'patterns': [
                    r'^(what|when|where|who|why|how|which)',
                    r'\?',
                    r'can\s+you|could\s+you|would\s+you',
                ],
                'confidence': 0.8
            },
            'name_introduction': {
                'keywords': ['my name is', 'i am', 'i\'m', 'call me', 'name\'s'],
                'patterns': [
                    r'my\s+name\s+is',
                    r'i\s+am\s+[A-Z]',
                    r'i\'m\s+[A-Z]',
                    r'call\s+me',
                ],
                'confidence': 0.85
            },
            'name_query': {
                'keywords': ['what is my name', 'what\'s my name', 'do you know my name', 
                            'remember my name'],
                'patterns': [
                    r'what(\'s|\s+is)\s+my\s+name',
                    r'do\s+you\s+know\s+my\s+name',
                ],
                'confidence': 0.9
            },
            'help': {
                'keywords': ['help', 'assist', 'support', 'guide', 'how to', 'what can you'],
                'patterns': [
                    r'\bhelp\b',
                    r'what\s+can\s+you\s+do',
                    r'how\s+can\s+you\s+help',
                ],
                'confidence': 0.8
            },
            'weather': {
                'keywords': ['weather', 'temperature', 'rain', 'sunny', 'cloudy', 'forecast'],
                'patterns': [
                    r'weather',
                    r'temperature',
                    r'forecast',
                ],
                'confidence': 0.75
            },
            'time': {
                'keywords': ['time', 'what time', 'current time', 'clock'],
                'patterns': [
                    r'what\s+time',
                    r'current\s+time',
                    r'time\s+is',
                ],
                'confidence': 0.8
            },
            'date': {
                'keywords': ['date', 'what date', 'today\'s date', 'current date'],
                'patterns': [
                    r'what\s+date',
                    r'today\'s\s+date',
                    r'current\s+date',
                ],
                'confidence': 0.8
            },
            'compliment': {
                'keywords': ['thank', 'thanks', 'appreciate', 'great', 'awesome', 'good job'],
                'patterns': [
                    r'thank\s+you',
                    r'thanks',
                    r'great\s+job',
                ],
                'confidence': 0.7
            },
            'unknown': {
                'keywords': [],
                'patterns': [],
                'confidence': 0.0
            }
        }
    
    def recognize(self, text: str) -> Tuple[str, float]:
        """
        Recognize intent from text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Tuple of (intent_name, confidence_score)
        """
        if not text or not text.strip():
            return 'unknown', 0.0
        
        text_lower = text.lower().strip()
        intent_scores = {}
        
        # Calculate scores for each intent
        for intent_name, intent_data in self.intent_patterns.items():
            if intent_name == 'unknown':
                continue
            
            score = 0.0
            keywords = intent_data.get('keywords', [])
            patterns = intent_data.get('patterns', [])
            base_confidence = intent_data.get('confidence', 0.5)
            
            # Check keyword matches
            keyword_matches = sum(1 for keyword in keywords if keyword in text_lower)
            if keyword_matches > 0:
                score += (keyword_matches / len(keywords)) * base_confidence
            
            # Check pattern matches
            pattern_matches = sum(1 for pattern in patterns 
                                if re.search(pattern, text_lower, re.IGNORECASE))
            if pattern_matches > 0:
                score += (pattern_matches / len(patterns)) * base_confidence
            
            # Normalize score
            if keyword_matches > 0 or pattern_matches > 0:
                intent_scores[intent_name] = min(score, 1.0)
        
        # Return the intent with highest score
        if intent_scores:
            best_intent = max(intent_scores.items(), key=lambda x: x[1])
            return best_intent[0], best_intent[1]
        
        return 'unknown', 0.0
    
    def get_intent_confidence(self, intent: str) -> float:
        """
        Get base confidence score for an intent.
        
        Args:
            intent: Intent name
            
        Returns:
            Confidence score
        """
        return self.intent_patterns.get(intent, {}).get('confidence', 0.0)
    
    def get_all_intents(self) -> List[str]:
        """
        Get list of all supported intents.
        
        Returns:
            List of intent names
        """
        return [intent for intent in self.intent_patterns.keys() if intent != 'unknown']

