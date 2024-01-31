import random
from replit import clear


# Magic 8 Ball Introduction
def magic8():
    response = input("(Press any enter for an answer and type 'quit' to leave)\nWhat do you want to ask?\n> ")

  # Magic 8 Ball List of Responses
    responses = [
        "It is certain",
        "Without a doubt",
        "You may rely on it",
        "Yes definitely",
        "It is decidedly so",
        "As I see it, yes",
        "Most likely",
        "Yes",
        "Outlook good",
        "Signs point to yes",
        "Reply hazy try again",
        "Better not tell you now",
        "Ask again later",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don’t count on it",
        "Outlook not so good",
        "My sources say no",
        "Very doubtful",
        "My reply is no",
        ]
    # User leaving
    if response == "quit":
        print("Bye bye! See you again!")
        input("(Press enter to continue)\n")
        clear()
    # Magic 8 Ball reply
    else:
        print(random.choice(responses), "\n")
        input("(Press enter to continue)\n")
        clear()
    # Return to introduction
        magic8()
magic8()