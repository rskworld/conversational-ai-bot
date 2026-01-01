"""
Sentiment Analysis Module
Analyzes sentiment of user messages to provide better responses.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, Tuple
import re
from collections import Counter


class SentimentAnalyzer:
    """
    Analyzes sentiment of text using lexicon-based approach.
    Can be extended with ML models for better accuracy.
    """
    
    def __init__(self):
        """Initialize sentiment analyzer with sentiment lexicons."""
        # Positive words
        self.positive_words = {
            'good', 'great', 'excellent', 'awesome', 'fantastic', 'wonderful',
            'amazing', 'perfect', 'love', 'like', 'happy', 'glad', 'pleased',
            'delighted', 'satisfied', 'thankful', 'grateful', 'appreciate',
            'wonderful', 'brilliant', 'outstanding', 'superb', 'marvelous',
            'terrific', 'fabulous', 'splendid', 'nice', 'cool', 'fine',
            'okay', 'ok', 'yes', 'yeah', 'sure', 'definitely', 'absolutely'
        }
        
        # Negative words
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'dislike',
            'sad', 'angry', 'mad', 'frustrated', 'disappointed', 'upset',
            'annoyed', 'irritated', 'depressed', 'miserable', 'unhappy',
            'disgusting', 'pathetic', 'useless', 'stupid', 'dumb', 'idiot',
            'no', 'not', 'never', 'can\'t', 'won\'t', 'don\'t', 'doesn\'t',
            'shouldn\'t', 'wouldn\'t', 'couldn\'t', 'isn\'t', 'aren\'t'
        }
        
        # Intensifiers
        self.intensifiers = {
            'very', 'extremely', 'really', 'quite', 'rather', 'too', 'so',
            'incredibly', 'absolutely', 'completely', 'totally', 'utterly'
        }
        
        # Negation words
        self.negations = {
            'not', 'no', 'never', 'none', 'nobody', 'nothing', 'nowhere',
            'neither', 'nor', 'cannot', 'can\'t', 'won\'t', 'don\'t'
        }
    
    def analyze(self, text: str) -> Dict[str, any]:
        """
        Analyze sentiment of text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with sentiment analysis results:
            {
                'sentiment': 'positive' | 'negative' | 'neutral',
                'score': float (-1.0 to 1.0),
                'confidence': float (0.0 to 1.0),
                'positive_words': list,
                'negative_words': list
            }
        """
        if not text or not text.strip():
            return {
                'sentiment': 'neutral',
                'score': 0.0,
                'confidence': 0.0,
                'positive_words': [],
                'negative_words': []
            }
        
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        positive_count = 0
        negative_count = 0
        found_positive = []
        found_negative = []
        
        # Check for negations
        has_negation = any(neg in text_lower for neg in self.negations)
        
        # Analyze each word
        for i, word in enumerate(words):
            # Check for positive words
            if word in self.positive_words:
                # Check if negated
                if has_negation and i > 0 and words[i-1] in self.negations:
                    negative_count += 1
                    found_negative.append(word)
                else:
                    positive_count += 1
                    found_positive.append(word)
            
            # Check for negative words
            elif word in self.negative_words:
                # Check if negated
                if has_negation and i > 0 and words[i-1] in self.negations:
                    positive_count += 1
                    found_positive.append(word)
                else:
                    negative_count += 1
                    found_negative.append(word)
        
        # Calculate sentiment score
        total_sentiment_words = positive_count + negative_count
        if total_sentiment_words == 0:
            score = 0.0
            sentiment = 'neutral'
            confidence = 0.0
        else:
            score = (positive_count - negative_count) / max(total_sentiment_words, 1)
            
            if score > 0.1:
                sentiment = 'positive'
            elif score < -0.1:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            
            confidence = min(abs(score) * 2, 1.0)
        
        return {
            'sentiment': sentiment,
            'score': round(score, 3),
            'confidence': round(confidence, 3),
            'positive_words': list(set(found_positive)),
            'negative_words': list(set(found_negative))
        }
    
    def get_sentiment_label(self, text: str) -> str:
        """
        Get simple sentiment label.
        
        Args:
            text: Input text
            
        Returns:
            'positive', 'negative', or 'neutral'
        """
        analysis = self.analyze(text)
        return analysis['sentiment']
    
    def is_positive(self, text: str) -> bool:
        """Check if text has positive sentiment."""
        return self.get_sentiment_label(text) == 'positive'
    
    def is_negative(self, text: str) -> bool:
        """Check if text has negative sentiment."""
        return self.get_sentiment_label(text) == 'negative'

