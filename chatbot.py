import sys
import random

def simple_chatbot():
    DEFAULT_RESPONSES = [
        "That's interesting! Tell me more.",
        "I see. How does that make you feel?",
        "Ah, I'm not sure how to respond to that. Can you ask about a topic?",
        "Let's change the subject. What are you learning today?"
    ]

    print("--- Rule-Based Chatbot Initialized ---")
    print("Hello! I'm a simple chatbot. You can ask me about Python, say 'hello', or say 'bye' to exit.")
    print("-" * 38)

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Come back anytime.")
            sys.exit(0)

        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: Hello there! I'm a simple rule-based AI.")

        elif "who are you" in user_input or "your name" in user_input:
            print("Chatbot: I am a simple Python chatbot created using if-else statements.")

        elif "python" in user_input and "best" in user_input:
            print("Chatbot: Python is fantastic for automation and scripting! I was built with it.")
            
        elif "python" in user_input:
            print("Chatbot: Python is a high-level, interpreted programming language.")

        else:
            response = random.choice(DEFAULT_RESPONSES)
            print(f"Chatbot: {response}")

if __name__ == '__main__':
    simple_chatbot()