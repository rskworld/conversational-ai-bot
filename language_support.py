"""
Multi-Language Support Module
Provides translation and multi-language support for the chatbot.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from typing import Dict, Optional
import re


class LanguageSupport:
    """
    Provides multi-language support and language detection.
    """
    
    def __init__(self):
        """Initialize language support."""
        # Supported languages
        self.supported_languages = {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'hi': 'Hindi',
            'zh': 'Chinese',
            'ja': 'Japanese',
            'ar': 'Arabic'
        }
        
        # Language detection patterns
        self.language_patterns = {
            'hi': r'[\u0900-\u097F]',  # Devanagari script
            'zh': r'[\u4e00-\u9fff]',  # Chinese characters
            'ja': r'[\u3040-\u309F\u30A0-\u30FF]',  # Hiragana/Katakana
            'ar': r'[\u0600-\u06FF]',  # Arabic script
        }
        
        # Common phrases in different languages
        self.greetings = {
            'en': ['hello', 'hi', 'hey', 'greetings'],
            'es': ['hola', 'buenos días', 'buenas tardes'],
            'fr': ['bonjour', 'salut', 'bonsoir'],
            'de': ['hallo', 'guten tag', 'guten morgen'],
            'hi': ['नमस्ते', 'नमस्कार', 'हैलो'],
            'zh': ['你好', '您好'],
            'ja': ['こんにちは', 'こんばんは'],
            'ar': ['مرحبا', 'السلام عليكم']
        }
        
        self.current_language = 'en'
    
    def detect_language(self, text: str) -> str:
        """
        Detect language of input text.
        
        Args:
            text: Input text
            
        Returns:
            Language code (e.g., 'en', 'es', 'hi')
        """
        if not text:
            return 'en'
        
        # Check for script-based languages
        for lang_code, pattern in self.language_patterns.items():
            if re.search(pattern, text):
                return lang_code
        
        # Check for common phrases
        text_lower = text.lower()
        for lang_code, phrases in self.greetings.items():
            for phrase in phrases:
                if phrase.lower() in text_lower:
                    return lang_code
        
        # Default to English
        return 'en'
    
    def set_language(self, language_code: str) -> bool:
        """
        Set current language.
        
        Args:
            language_code: Language code (e.g., 'en', 'es')
            
        Returns:
            True if language is supported, False otherwise
        """
        if language_code in self.supported_languages:
            self.current_language = language_code
            return True
        return False
    
    def get_language(self) -> str:
        """Get current language code."""
        return self.current_language
    
    def get_language_name(self, language_code: Optional[str] = None) -> str:
        """
        Get language name.
        
        Args:
            language_code: Language code (uses current if not provided)
            
        Returns:
            Language name
        """
        code = language_code or self.current_language
        return self.supported_languages.get(code, 'Unknown')
    
    def get_supported_languages(self) -> Dict[str, str]:
        """
        Get all supported languages.
        
        Returns:
            Dictionary mapping language codes to names
        """
        return self.supported_languages.copy()
    
    def translate_greeting(self, language_code: str) -> str:
        """
        Get greeting in specified language.
        
        Args:
            language_code: Target language code
            
        Returns:
            Greeting in target language
        """
        greetings = {
            'en': 'Hello! How can I help you?',
            'es': '¡Hola! ¿Cómo puedo ayudarte?',
            'fr': 'Bonjour! Comment puis-je vous aider?',
            'de': 'Hallo! Wie kann ich Ihnen helfen?',
            'hi': 'नमस्ते! मैं आपकी कैसे मदद कर सकता हूं?',
            'zh': '你好！我能为你做什么？',
            'ja': 'こんにちは！何かお手伝いできますか？',
            'ar': 'مرحبا! كيف يمكنني مساعدتك؟'
        }
        return greetings.get(language_code, greetings['en'])
    
    def is_supported(self, language_code: str) -> bool:
        """
        Check if language is supported.
        
        Args:
            language_code: Language code to check
            
        Returns:
            True if supported, False otherwise
        """
        return language_code in self.supported_languages

