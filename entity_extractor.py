"""
Entity Extraction Module
Extracts entities such as names, dates, locations, etc. from user messages.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import re
from typing import Dict, List, Optional
from datetime import datetime
from dateutil import parser as date_parser


class EntityExtractor:
    """
    Extracts entities from natural language text.
    """
    
    def __init__(self):
        """Initialize the entity extractor."""
        # Common patterns for entity extraction
        self.patterns = {
            'PERSON': [
                r'\b(?:my name is|i am|i\'m|call me|name\'s)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
                r'\b([A-Z][a-z]+\s+[A-Z][a-z]+)\b',  # First Last name pattern
            ],
            'DATE': [
                r'\b(today|tomorrow|yesterday|next week|last week|next month|last month)\b',
                r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b',  # Date formats
                r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}',
            ],
            'TIME': [
                r'\b(\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?)\b',
                r'\b(\d{1,2}\s*(?:o\'clock|am|pm|AM|PM))\b',
            ],
            'LOCATION': [
                r'\b(in|at|from|to)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b',
            ],
            'MONEY': [
                r'\$(\d+(?:\.\d{2})?)',
                r'\b(\d+)\s*(?:dollars|rupees|euros|pounds)\b',
            ],
            'EMAIL': [
                r'\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b',
            ],
            'PHONE': [
                r'\b(\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9})\b',
            ],
        }
    
    def extract(self, text: str) -> Dict[str, List[str]]:
        """
        Extract entities from text.
        
        Args:
            text: Input text to extract entities from
            
        Returns:
            Dictionary mapping entity types to extracted values
        """
        entities = {}
        text_lower = text.lower()
        
        # Extract PERSON names
        entities['PERSON'] = self._extract_person(text)
        
        # Extract DATES
        entities['DATE'] = self._extract_dates(text)
        
        # Extract TIME
        entities['TIME'] = self._extract_time(text)
        
        # Extract LOCATION
        entities['LOCATION'] = self._extract_location(text)
        
        # Extract MONEY
        entities['MONEY'] = self._extract_money(text)
        
        # Extract EMAIL
        entities['EMAIL'] = self._extract_email(text)
        
        # Extract PHONE
        entities['PHONE'] = self._extract_phone(text)
        
        # Remove empty entity lists
        entities = {k: v for k, v in entities.items() if v}
        
        return entities
    
    def _extract_person(self, text: str) -> List[str]:
        """Extract person names from text."""
        names = []
        
        # Pattern: "my name is John" or "I am John"
        patterns = [
            r'(?:my name is|i am|i\'m|call me|name\'s)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)',
            r'\b([A-Z][a-z]+\s+[A-Z][a-z]+)\b',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    name = ' '.join(match).strip()
                else:
                    name = match.strip()
                if name and name not in names:
                    names.append(name)
        
        return names
    
    def _extract_dates(self, text: str) -> List[str]:
        """Extract dates from text."""
        dates = []
        text_lower = text.lower()
        
        # Relative dates
        relative_dates = ['today', 'tomorrow', 'yesterday', 'next week', 'last week', 
                         'next month', 'last month', 'next year', 'last year']
        for rel_date in relative_dates:
            if rel_date in text_lower:
                dates.append(rel_date)
        
        # Date patterns
        date_patterns = [
            r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b',
            r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?(?:,\s+\d{4})?\b',
        ]
        
        for pattern in date_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            dates.extend(matches)
        
        return list(set(dates))
    
    def _extract_time(self, text: str) -> List[str]:
        """Extract time from text."""
        times = []
        
        patterns = [
            r'\b(\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?)\b',
            r'\b(\d{1,2}\s*(?:o\'clock|am|pm|AM|PM))\b',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            times.extend(matches)
        
        return list(set(times))
    
    def _extract_location(self, text: str) -> List[str]:
        """Extract locations from text."""
        locations = []
        
        # Simple location extraction (can be enhanced with NER)
        pattern = r'\b(in|at|from|to)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
        matches = re.findall(pattern, text)
        
        for match in matches:
            location = match[1] if isinstance(match, tuple) else match
            if location and location not in locations:
                locations.append(location)
        
        return locations
    
    def _extract_money(self, text: str) -> List[str]:
        """Extract money amounts from text."""
        amounts = []
        
        patterns = [
            r'\$(\d+(?:\.\d{2})?)',
            r'\b(\d+)\s*(?:dollars|rupees|euros|pounds|USD|INR|EUR|GBP)\b',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            amounts.extend(matches)
        
        return list(set(amounts))
    
    def _extract_email(self, text: str) -> List[str]:
        """Extract email addresses from text."""
        pattern = r'\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b'
        matches = re.findall(pattern, text)
        return list(set(matches))
    
    def _extract_phone(self, text: str) -> List[str]:
        """Extract phone numbers from text."""
        pattern = r'\b(\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9})\b'
        matches = re.findall(pattern, text)
        return list(set(matches))

