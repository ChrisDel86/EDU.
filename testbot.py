import random
import string


def generate_ticket():
    ticket = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return ticket

def chatbot(user_input):
    if 'password' in user_input.lower():
        response = "To reset your password, please contact your IT administrator."
    elif 'network' in user_input.lower():
        response = "To report a network issue, please contact your IT administrator."
    elif 'software' in user_input.lower():
        response = "To report a software issue, please contact your IT administrator."
    elif 'hardware' in user_input.lower():
        response = "To report a hardware issue, please contact your IT administrator."
    else:
        response = " . Please try again."
    return response


print("Welcome to the IT chatbot. How can I assist you?")
while True:
    user_input = input()
    if user_input.lower() == 'exit':
        break
    else:
        response = chatbot(user_input)
        print(response)
