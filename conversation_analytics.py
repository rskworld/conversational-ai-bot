"""
Conversation Analytics Module
Tracks and analyzes conversation metrics and statistics.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, List
from datetime import datetime, timedelta
from collections import Counter, defaultdict


class ConversationAnalytics:
    """
    Tracks and analyzes conversation metrics.
    """
    
    def __init__(self):
        """Initialize conversation analytics."""
        self.metrics = {
            'total_conversations': 0,
            'total_messages': 0,
            'total_sessions': 0,
            'average_messages_per_session': 0.0,
            'intent_distribution': Counter(),
            'entity_distribution': Counter(),
            'sentiment_distribution': Counter(),
            'most_common_intents': [],
            'most_common_entities': [],
            'session_durations': [],
            'peak_hours': Counter(),
            'language_distribution': Counter()
        }
        
        self.session_start_times = {}
        self.session_messages = defaultdict(int)
    
    def track_message(self, session_id: str, intent: str = None, 
                     entities: Dict = None, sentiment: str = None,
                     language: str = 'en'):
        """
        Track a message in analytics.
        
        Args:
            session_id: Session identifier
            intent: Detected intent
            entities: Extracted entities
            sentiment: Sentiment analysis result
            language: Language code
        """
        self.metrics['total_messages'] += 1
        self.session_messages[session_id] += 1
        
        # Track intent
        if intent:
            self.metrics['intent_distribution'][intent] += 1
        
        # Track entities
        if entities:
            for entity_type, entity_values in entities.items():
                if entity_values:
                    self.metrics['entity_distribution'][entity_type] += 1
        
        # Track sentiment
        if sentiment:
            self.metrics['sentiment_distribution'][sentiment] += 1
        
        # Track language
        self.metrics['language_distribution'][language] += 1
        
        # Track peak hours
        current_hour = datetime.now().hour
        self.metrics['peak_hours'][current_hour] += 1
    
    def start_session(self, session_id: str):
        """
        Track session start.
        
        Args:
            session_id: Session identifier
        """
        self.session_start_times[session_id] = datetime.now()
        self.metrics['total_sessions'] += 1
    
    def end_session(self, session_id: str):
        """
        Track session end and calculate duration.
        
        Args:
            session_id: Session identifier
        """
        if session_id in self.session_start_times:
            start_time = self.session_start_times[session_id]
            duration = (datetime.now() - start_time).total_seconds()
            self.metrics['session_durations'].append(duration)
            del self.session_start_times[session_id]
    
    def get_metrics(self) -> Dict:
        """
        Get all analytics metrics.
        
        Returns:
            Dictionary with all metrics
        """
        # Calculate average messages per session
        if self.metrics['total_sessions'] > 0:
            self.metrics['average_messages_per_session'] = \
                self.metrics['total_messages'] / self.metrics['total_sessions']
        
        # Get most common intents
        self.metrics['most_common_intents'] = \
            self.metrics['intent_distribution'].most_common(10)
        
        # Get most common entities
        self.metrics['most_common_entities'] = \
            self.metrics['entity_distribution'].most_common(10)
        
        return self.metrics.copy()
    
    def get_summary(self) -> str:
        """
        Get human-readable analytics summary.
        
        Returns:
            Formatted summary string
        """
        metrics = self.get_metrics()
        
        summary = f"""
Conversation Analytics Summary
{'=' * 50}
Total Sessions: {metrics['total_sessions']}
Total Messages: {metrics['total_messages']}
Average Messages per Session: {metrics['average_messages_per_session']:.2f}

Top Intents:
"""
        for intent, count in metrics['most_common_intents'][:5]:
            summary += f"  - {intent}: {count}\n"
        
        summary += "\nTop Entities:\n"
        for entity, count in metrics['most_common_entities'][:5]:
            summary += f"  - {entity}: {count}\n"
        
        if metrics['sentiment_distribution']:
            summary += "\nSentiment Distribution:\n"
            for sentiment, count in metrics['sentiment_distribution'].items():
                summary += f"  - {sentiment}: {count}\n"
        
        if metrics['session_durations']:
            avg_duration = sum(metrics['session_durations']) / len(metrics['session_durations'])
            summary += f"\nAverage Session Duration: {avg_duration:.2f} seconds\n"
        
        return summary
    
    def reset(self):
        """Reset all analytics."""
        self.metrics = {
            'total_conversations': 0,
            'total_messages': 0,
            'total_sessions': 0,
            'average_messages_per_session': 0.0,
            'intent_distribution': Counter(),
            'entity_distribution': Counter(),
            'sentiment_distribution': Counter(),
            'most_common_intents': [],
            'most_common_entities': [],
            'session_durations': [],
            'peak_hours': Counter(),
            'language_distribution': Counter()
        }
        self.session_start_times = {}
        self.session_messages = defaultdict(int)

