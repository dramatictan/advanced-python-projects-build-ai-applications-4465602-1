from textblob import TextBlob

# Define intents and their corresponding responses based on keywords
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9AM to 5AM, Monday to Friday."
    },
    "return": {
        "keywords": ["refund", "money back", "return"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    }
}

def get_response(message):
    # Convert the message to lowercase for consistent keyword matching
    message = message.lower()

    # Check if the message contains any keywords associated with defined intents
    for intent_data in intents.values():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]

    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity
    # Return a response based on the sentiment score (+ means happy, - means unhappy)
    if sentiment > 0:
        return "That's great to hear!"
    elif sentiment < 0:
        return "I am so sorry to hear that. How can I help?"
    else:
        return "I see. Can you tell me more about that?"

def chat():
    # Greet the user and prompt for input
    print("Chatbot: Hi, how can I help you today?")

    # Continuously prompt the user for input until they choose to exit
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in ['exit', 'quit', 'bye']:
            break
        print(f"\nChatbot: {get_response(user_message)}")

    # Thank the user for chatting when they exit
    print("Chatbot: Thank you for chatting. Have a great day!")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed