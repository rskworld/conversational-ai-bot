"""
Test script for Conversational AI Bot
Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import unittest
from chatbot import ConversationalAIBot
from intent_recognizer import IntentRecognizer
from entity_extractor import EntityExtractor
from context_manager import ContextManager


class TestIntentRecognizer(unittest.TestCase):
    """Test intent recognition functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.recognizer = IntentRecognizer()
    
    def test_greeting_intent(self):
        """Test greeting intent recognition."""
        intent, confidence = self.recognizer.recognize("Hello")
        self.assertEqual(intent, "greeting")
        self.assertGreater(confidence, 0.5)
    
    def test_question_intent(self):
        """Test question intent recognition."""
        intent, confidence = self.recognizer.recognize("What is this?")
        self.assertEqual(intent, "question")
        self.assertGreater(confidence, 0.5)
    
    def test_name_introduction(self):
        """Test name introduction intent."""
        intent, confidence = self.recognizer.recognize("My name is John")
        self.assertEqual(intent, "name_introduction")
        self.assertGreater(confidence, 0.5)


class TestEntityExtractor(unittest.TestCase):
    """Test entity extraction functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = EntityExtractor()
    
    def test_person_extraction(self):
        """Test person name extraction."""
        entities = self.extractor.extract("My name is John Doe")
        self.assertIn("PERSON", entities)
        self.assertGreater(len(entities["PERSON"]), 0)
    
    def test_email_extraction(self):
        """Test email extraction."""
        entities = self.extractor.extract("My email is test@example.com")
        self.assertIn("EMAIL", entities)
        self.assertIn("test@example.com", entities["EMAIL"])


class TestContextManager(unittest.TestCase):
    """Test context management functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.context_manager = ContextManager("test_session")
    
    def test_context_update(self):
        """Test context update."""
        self.context_manager.update_context(
            "My name is Alice",
            "Nice to meet you, Alice!",
            "name_introduction",
            {"PERSON": ["Alice"]}
        )
        
        self.assertEqual(self.context_manager.get_user_name(), "Alice")
    
    def test_context_persistence(self):
        """Test context persistence across updates."""
        self.context_manager.update_context(
            "Hello",
            "Hi there!",
            "greeting",
            {}
        )
        
        history = self.context_manager.get_recent_history(1)
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["user_message"], "Hello")


class TestChatbot(unittest.TestCase):
    """Test main chatbot functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.bot = ConversationalAIBot("test_session")
    
    def test_basic_greeting(self):
        """Test basic greeting."""
        response = self.bot.chat("Hello")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
    
    def test_name_remembering(self):
        """Test name remembering functionality."""
        self.bot.chat("My name is Bob")
        response = self.bot.chat("What's my name?")
        self.assertIn("Bob", response)
    
    def test_context_awareness(self):
        """Test context awareness."""
        self.bot.chat("Hello")
        self.bot.chat("My name is Charlie")
        
        context_summary = self.bot.get_context_summary()
        self.assertIsInstance(context_summary, str)
        self.assertGreater(len(context_summary), 0)


def run_tests():
    """Run all tests."""
    print("=" * 60)
    print("Running Conversational AI Bot Tests")
    print("Developer: RSK World (https://rskworld.in)")
    print("=" * 60 + "\n")
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestIntentRecognizer))
    suite.addTests(loader.loadTestsFromTestCase(TestEntityExtractor))
    suite.addTests(loader.loadTestsFromTestCase(TestContextManager))
    suite.addTests(loader.loadTestsFromTestCase(TestChatbot))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"Tests completed with {len(result.failures)} failures and {len(result.errors)} errors")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()

