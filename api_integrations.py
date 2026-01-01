"""
API Integrations Module
Integrates with external APIs for enhanced functionality.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import requests
from typing import Dict, Optional
from datetime import datetime
import json


class APIIntegrations:
    """
    Handles integrations with external APIs.
    """
    
    def __init__(self):
        """Initialize API integrations."""
        self.weather_api_key = None  # Set your API key if needed
        self.news_api_key = None  # Set your API key if needed
        self.timeout = 5  # Request timeout in seconds
    
    def get_weather(self, location: str) -> Dict:
        """
        Get weather information for a location.
        
        Args:
            location: Location name or city
            
        Returns:
            Dictionary with weather information or error message
        """
        # Mock weather response (replace with actual API call)
        # Example: OpenWeatherMap API
        if not location:
            return {
                'success': False,
                'error': 'Location not provided'
            }
        
        # Mock response for demonstration
        # In production, use: https://api.openweathermap.org/data/2.5/weather
        return {
            'success': True,
            'location': location,
            'temperature': '22°C',
            'condition': 'Partly Cloudy',
            'humidity': '65%',
            'wind_speed': '10 km/h',
            'note': 'This is a mock response. Configure API key for real data.'
        }
    
    def get_news(self, topic: Optional[str] = None, limit: int = 5) -> Dict:
        """
        Get news articles.
        
        Args:
            topic: News topic (optional)
            limit: Number of articles to return
            
        Returns:
            Dictionary with news articles or error message
        """
        # Mock news response (replace with actual API call)
        # Example: NewsAPI
        mock_articles = [
            {
                'title': 'Technology Advances in AI',
                'description': 'Recent developments in artificial intelligence...',
                'source': 'Tech News',
                'published_at': datetime.now().isoformat()
            },
            {
                'title': 'Python Programming Trends',
                'description': 'Latest trends in Python development...',
                'source': 'Dev News',
                'published_at': datetime.now().isoformat()
            }
        ]
        
        if topic:
            mock_articles = [a for a in mock_articles if topic.lower() in a['title'].lower()]
        
        return {
            'success': True,
            'articles': mock_articles[:limit],
            'count': len(mock_articles[:limit]),
            'note': 'This is a mock response. Configure API key for real data.'
        }
    
    def get_joke(self) -> Dict:
        """
        Get a random joke.
        
        Returns:
            Dictionary with joke or error message
        """
        # Mock joke (replace with actual API call)
        # Example: JokeAPI or icanhazdadjoke.com
        jokes = [
            {
                'setup': 'Why did the Python programmer not respond?',
                'punchline': 'Because they were stuck in an infinite loop!'
            },
            {
                'setup': 'How do you comfort a JavaScript bug?',
                'punchline': 'You console it!'
            },
            {
                'setup': 'Why do programmers prefer dark mode?',
                'punchline': 'Because light attracts bugs!'
            }
        ]
        
        import random
        joke = random.choice(jokes)
        
        return {
            'success': True,
            'joke': joke,
            'note': 'This is a mock response. Configure API for real jokes.'
        }
    
    def get_quote(self) -> Dict:
        """
        Get an inspirational quote.
        
        Returns:
            Dictionary with quote or error message
        """
        # Mock quote (replace with actual API call)
        # Example: Quotable API or ZenQuotes API
        quotes = [
            {
                'text': 'The only way to do great work is to love what you do.',
                'author': 'Steve Jobs'
            },
            {
                'text': 'Innovation distinguishes between a leader and a follower.',
                'author': 'Steve Jobs'
            },
            {
                'text': 'Code is like humor. When you have to explain it, it\'s bad.',
                'author': 'Cory House'
            }
        ]
        
        import random
        quote = random.choice(quotes)
        
        return {
            'success': True,
            'quote': quote,
            'note': 'This is a mock response. Configure API for real quotes.'
        }
    
    def calculate(self, expression: str) -> Dict:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression: Mathematical expression to evaluate
            
        Returns:
            Dictionary with calculation result or error
        """
        try:
            # Simple calculation (use with caution in production)
            # For production, use a proper math parser
            result = eval(expression.replace('^', '**'))
            return {
                'success': True,
                'expression': expression,
                'result': result
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Invalid expression: {str(e)}'
            }
    
    def set_weather_api_key(self, api_key: str):
        """Set weather API key."""
        self.weather_api_key = api_key
    
    def set_news_api_key(self, api_key: str):
        """Set news API key."""
        self.news_api_key = api_key

