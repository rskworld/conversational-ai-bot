"""
Conversational AI Bot - Main Entry Point
Advanced conversational chatbot with context management and multi-turn dialogue support.

Developer: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

from chatbot import ConversationalAIBot
from colorama import init, Fore, Style
import sys

# Initialize colorama for Windows
init(autoreset=True)


def print_banner():
    """Print welcome banner."""
    banner = f"""
{Fore.CYAN}{'='*60}
{Fore.CYAN}     Conversational AI Bot - Advanced Chatbot System
{Fore.CYAN}{'='*60}
{Fore.GREEN}Features:
{Fore.WHITE}  • Context-aware conversations
{Fore.WHITE}  • Multi-turn dialogue support
{Fore.WHITE}  • Intent recognition
{Fore.WHITE}  • Entity extraction
{Fore.WHITE}  • Conversation history

{Fore.YELLOW}Developer: {Fore.WHITE}RSK World
{Fore.YELLOW}Website: {Fore.WHITE}https://rskworld.in
{Fore.YELLOW}Email: {Fore.WHITE}help@rskworld.in
{Fore.YELLOW}Phone: {Fore.WHITE}+91 93305 39277
{Fore.YELLOW}Year: {Fore.WHITE}2026

{Fore.CYAN}{'='*60}
{Fore.WHITE}Type 'help' for commands, 'quit' or 'exit' to end
{Fore.CYAN}{'='*60}
"""
    print(banner)


def print_help():
    """Print help information."""
    help_text = f"""
{Fore.GREEN}Available Commands:
{Fore.WHITE}  help              - Show this help message
{Fore.WHITE}  context            - Show current conversation context
{Fore.WHITE}  history            - Show conversation history
{Fore.WHITE}  clear              - Clear conversation history
{Fore.WHITE}  quit / exit        - Exit the chatbot

{Fore.GREEN}Example Interactions:
{Fore.WHITE}  • "Hello" - Greet the bot
{Fore.WHITE}  • "My name is John" - Introduce yourself
{Fore.WHITE}  • "What's my name?" - Ask the bot to recall your name
{Fore.WHITE}  • "What can you do?" - Learn about bot capabilities
{Fore.WHITE}  • "What time is it?" - Get current time
{Fore.WHITE}  • "What's the date?" - Get current date
"""
    print(help_text)


def main():
    """Main function to run the chatbot."""
    print_banner()
    
    # Initialize bot
    bot = ConversationalAIBot()
    
    print(f"{Fore.GREEN}Bot initialized successfully!{Fore.WHITE}\n")
    
    # Main conversation loop
    while True:
        try:
            user_input = input(f"{Fore.CYAN}You: {Fore.WHITE}").strip()
            
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'context':
                context_summary = bot.get_context_summary()
                print(f"{Fore.GREEN}Context: {Fore.WHITE}{context_summary}\n")
                continue
            
            elif user_input.lower() == 'history':
                history = bot.get_conversation_history(limit=10)
                if history:
                    print(f"{Fore.GREEN}Recent Conversation History:{Fore.WHITE}")
                    for entry in history[-5:]:
                        print(f"  {Fore.YELLOW}You: {Fore.WHITE}{entry.get('user_message', 'N/A')}")
                        print(f"  {Fore.CYAN}Bot: {Fore.WHITE}{entry.get('bot_response', 'N/A')}")
                        print()
                else:
                    print(f"{Fore.YELLOW}No conversation history yet.{Fore.WHITE}\n")
                continue
            
            elif user_input.lower() == 'clear':
                bot.clear_session()
                print(f"{Fore.GREEN}Conversation history cleared.{Fore.WHITE}\n")
                continue
            
            elif user_input.lower() in ['quit', 'exit', 'bye']:
                response = bot.chat(user_input)
                print(f"{Fore.CYAN}Bot: {Fore.WHITE}{response}\n")
                print(f"{Fore.GREEN}Thank you for using Conversational AI Bot!{Fore.WHITE}")
                print(f"{Fore.YELLOW}Developed by RSK World - https://rskworld.in{Fore.WHITE}\n")
                break
            
            # Process user message
            response = bot.chat(user_input)
            print(f"{Fore.CYAN}Bot: {Fore.WHITE}{response}\n")
        
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Interrupted by user.{Fore.WHITE}")
            print(f"{Fore.GREEN}Thank you for using Conversational AI Bot!{Fore.WHITE}")
            print(f"{Fore.YELLOW}Developed by RSK World - https://rskworld.in{Fore.WHITE}\n")
            sys.exit(0)
        
        except Exception as e:
            print(f"{Fore.RED}Error: {Fore.WHITE}{str(e)}\n")
            continue


if __name__ == "__main__":
    main()

