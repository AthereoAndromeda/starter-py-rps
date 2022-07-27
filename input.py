from random import randint

def convert_input_to_word(input) -> str:
    match input:
        case "R": return "Rock"
        case "P": return "Paper"
        case "S": return "Scissors"

def get_random_input() -> str:
    # This is a tuple of the possible choices
    choices = ("R", "P", "S")
    # Generates a random integer from 0-2, which will be used to index `choices`
    num = randint(0, 2)
    return choices[num]

def validate_input(input) -> bool:
    if input != "R" and input != "P" and input != "S":
        return False
    else:
        return True
