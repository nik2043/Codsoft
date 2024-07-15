from nltk.chat.util import Chat, reflections

# Define pattern-response pairs
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm doing well, thank you! How about you?"]],
    ["bye|goodbye", ["Goodbye!", "Take care!"]],
    # Add more patterns and responses as needed
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    print("Chatbot:", chatbot.respond(user_input))
