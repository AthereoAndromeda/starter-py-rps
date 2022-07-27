from enum import Enum
from scoreboard import Scoreboard
from input import convert_input_to_word, get_random_input, validate_input

class GameResult(Enum):
    WIN = 0
    LOSS = 1
    DRAW = 2

def calculate_game(scoreboard, user_input, comp_input):
    match (user_input, comp_input):
        # Win Conditions
        case ("R", "S") | ("P", "R") | ("S", "P"):
            scoreboard.wins += 1
            return GameResult.WIN

        # Lose Conditions
        case ("S", "R") | ("R", "P") | ("P", "S"):
            scoreboard.losses += 1
            return GameResult.LOSS

        # Draw Conditions
        case ("R", "R") | ("P", "P") | ("S", "S"):
            scoreboard.draws += 1
            return GameResult.DRAW
        
def start_game():
    # Instantiated outside the while loop so it does not
    # get reset every iteration
    scoreboard = Scoreboard()

    # We loop the game forever
    while True:
        # Prompt the user for input. Then we `strip` away the whitespace, then use
        # `upper` to transform all the characters to uppercase
        user_input = input("Input R, P, or S! Input N to exit\n").strip().upper()

        # Exit if `N` is the input
        if user_input == "N":
            scoreboard.display()
            exit()
        
        is_input_valid = validate_input(user_input)

        # If is_input_valid is not True, loop again
        if not is_input_valid:
            print("Invalid Input! try again")
            print("\n--------------------------------------\n")
            continue

        comp_choice = get_random_input()

        # Convert the single character to a full word, then display
        print("\nYou chose: " + convert_input_to_word(user_input))
        print("Computer chose: " + convert_input_to_word(comp_choice))

        result = calculate_game(scoreboard, user_input, comp_choice)

        if result == GameResult.WIN:
            print("==| You Won! :> |==")
        elif result == GameResult.LOSS:
            print("==| You Lost :< |==")
        else:
            print("==| You Tied :| |==")

        # Just for formatting
        print("\n--------------------------------------\n")

start_game()