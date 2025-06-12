import random
from character_map import WARRIOR_LOGIC
from enum import Enum
from Warrior import Warrior


#Enum of outcome options
class Outcome(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3
WIN = Outcome.WIN
LOSE = Outcome.LOSE
DRAW = Outcome.DRAW

# List of warrior types
TYPE_LIST = tuple(WARRIOR_LOGIC.keys())
# Users play record
player_record : dict = {"win": 0, "draw": 0, "lose": 0}


def main():

    play_again:bool = True
    while play_again:  # Outer loop for playing multiple rounds

        while True:
            # Prompt the user to type in a valid Warrior Knight, Ranger, or a Wizard looping until a valid input has been selected.
            try:

                prompt_message:str = f"\nChoose from: {', '.join(name.capitalize() for name in TYPE_LIST)}: "
                Warrior_type:str = input(prompt_message)

                if Warrior_type.strip().lower() in TYPE_LIST:
                    user : Warrior = Warrior(Warrior_type.strip().lower())
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nPlease choose a valid Warrior")

        # Create a randomly generated Warrior
        opponent: Warrior = Warrior(random.choice(TYPE_LIST))

        # Alert the user to what their match up will be
        print(
            f"\nYour warrior is a {user.type} and is equiped with {user.weapon}.\n"
            f"You will be fighting a {opponent.type} equiped with {opponent.weapon}.\n"
        )

        # Have the user and opponent battle
        outcome = user.base_battle_outcome(opponent)
        last_chance_victory(outcome)
        # Update the players record with win, lose, or draw.
        player_record[outcome] += 1

        print(
            f"\nYour record is Wins: {player_record['win']} Draws: {player_record['draw']} Losses: {player_record['lose']}"
        )

        # Ask player if they want to play again
        while True:  # Loop for play again prompt
            try:
                answer = input("Would you like to play again? (y/n) ").strip().lower()
                if answer == "y":
                    break  # Break inner loop, main loop continues
                elif answer == "n":
                    print("Thanks for playing!")
                    play_again = False  # Set flag to exit main loop
                    break  # Break inner loop
                else:
                    raise ValueError
            except ValueError:
                print("Please enter only 'y' or 'n'")


def last_chance_victory(outcome):
    # Generate a randomly selected number 1-10
    holy_grail = random.randint(1, 10)
    # Prompt the loser to guess a number
    print(
        r"""
  .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.
 (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )
  \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /
   \/      \/      \/      \/      \/      \/      \/      \/      \/      \/
  _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_
 (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)
   1       2       3       4       5       6       7       8       9       10
          """
    )
    match outcome:
        case "win":
            opponent_guess = random.randint(0, 11)
            if opponent_guess == holy_grail:
                return "lose"
            else:
                return "win"
        case "lose":
            if input("Pick any number between 0-10: ") == holy_grail:
                return "win"
            else:
                return "lose"
        # fix this later
        case "draw":
            opponent_guess = random.randint(0, 11)
            user_guess = input("Pick any number between 0-10: ")

            return "draw"
    # If the loser picks the correct number over turn the loss
    pass
# Compare warriors to see what the type advantage is.
def phase_1(user_warrior: Warrior, opponent_warrior:Warrior)-> Outcome:
    # Type advanta
    TYPE_ADDVANTAGE = {
    warrior_type: details["type_addvatange"]
    for warrior_type, details in WARRIOR_LOGIC.items()
    }
    
    if opponent_warrior.type in TYPE_ADDVANTAGE.get(user_warrior.type):
        outcome = WIN

    elif user_warrior.type in TYPE_ADDVANTAGE.get(opponent_warrior.type):

        outcome = LOSE
    else:
        outcome = DRAW
    
# Check for weapons vs armor bonus of the previous phases victor.
def phase_2(user_warrior: Warrior, opponent_warrior:Warrior)-> Outcome:
    pass
# Check for the initial type advatage warrior weapons vs armor bonus.
def phase_3(user_warrior: Warrior, opponent_warrior:Warrior)-> Outcome:
    pass
# Choose a holy grail to see if you are the chosen.
def phase_4(outcome:Outcome)-> Outcome:
    pass
# Create a recapn of current events.
def narative_generator(outcome: Outcome)-> str:
    pass
if __name__ == "__main__":
    main()
