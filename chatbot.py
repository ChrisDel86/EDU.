import random

# define possible responses for the chatbot
greetings = ["hello", "hi", "hey"]
farewells = ["bye", "goodbye", "see you"]
questions = {
    "what is a firewall?": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.",
    "what is a router?": "A router is a networking device that forwards data packets between computer networks.",
    "what is an IP address?": "An IP address is a unique identifier assigned to devices on a network to facilitate communication between them."
}

# define function to handle user input and generate response
def respond(user_input):
    if user_input.lower() in greetings:
        return random.choice(greetings)
    elif user_input.lower() in farewells:
        return random.choice(farewells)
    else:
        for question in questions:
            if user_input.lower() in question:
                return questions[question]
        return "I'm sorry, I don't understand your question."

# main loop to keep the chatbot running
while True:
    user_input = input("Ask me a question about IT: ")
    response = respond(user_input)
    print(response)
