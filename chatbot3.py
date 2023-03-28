import random

# Define a dictionary of possible questions and answers
questions = {
    "What is your computer's operating system?": ["Windows", "Mac", "Linux"],
    "What is the error message you are seeing?": ["Can't connect to internet", "Blue screen of death", "Program won't open"],
    "Have you tried restarting your computer?": ["Yes", "No"]
}

# Define a function to handle user input and generate a response
def chatbot():
    # Ask the user for their name
    name = input("Hi! What's your name? ")

    # Greet the user
    print(f"Nice to meet you, {name}! I'm here to help with your IT issue.")

    # Ask questions and get answers from the user
    for question, possible_answers in questions.items():
        answer = input(question + " ")
        while answer not in possible_answers:
            print("Sorry, I didn't understand your answer. Please try again.")
            answer = input(question + " ")
        print("Great, thanks for letting me know!")

    # Generate a random response to the user's issue
    responses = [
        "I think I know what's going on. Try restarting your computer and see if that fixes the issue.",
        "I'm not sure what the issue is, but I'll create a ticket and have someone from IT contact you soon.",
        "I need more information to help you with this issue. Can you provide any more details?"
    ]
    print(random.choice(responses))

# Call the chatbot function to start the conversation
chatbot()
