"""
Flask Web Interface for Conversational AI Bot
Provides a web-based interface for the chatbot.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from flask import Flask, render_template, request, jsonify, session
from chatbot import ConversationalAIBot
import uuid
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Store bot instances per session
bot_instances = {}


def get_bot():
    """Get or create bot instance for current session."""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    session_id = session['session_id']
    
    if session_id not in bot_instances:
        bot_instances[session_id] = ConversationalAIBot(session_id)
    
    return bot_instances[session_id]


@app.route('/')
def index():
    """Render main chat interface."""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat API requests."""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Message is required'
            }), 400
        
        bot = get_bot()
        response = bot.chat(user_message)
        
        # Get additional metadata
        sentiment = bot.get_sentiment_analysis(user_message)
        context = bot.get_context_summary()
        
        return jsonify({
            'success': True,
            'response': response,
            'sentiment': sentiment.get('sentiment'),
            'sentiment_score': sentiment.get('score'),
            'context': context
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history."""
    try:
        bot = get_bot()
        limit = request.args.get('limit', 10, type=int)
        history = bot.get_conversation_history(limit=limit)
        
        return jsonify({
            'success': True,
            'history': history
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get conversation analytics."""
    try:
        bot = get_bot()
        analytics = bot.get_analytics()
        summary = bot.get_analytics_summary()
        
        return jsonify({
            'success': True,
            'analytics': analytics,
            'summary': summary
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/clear', methods=['POST'])
def clear_session():
    """Clear conversation session."""
    try:
        bot = get_bot()
        bot.clear_session()
        
        return jsonify({
            'success': True,
            'message': 'Session cleared successfully'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/language', methods=['POST'])
def set_language():
    """Set conversation language."""
    try:
        data = request.get_json()
        language_code = data.get('language', 'en')
        
        bot = get_bot()
        success = bot.set_language(language_code)
        
        return jsonify({
            'success': success,
            'language': bot.get_current_language(),
            'message': f'Language set to {language_code}' if success else 'Invalid language code'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

