import random
from Warrior import Warrior
from character_map import WARRIOR_LOGIC

# List of warrior types
TYPE_LIST = tuple(WARRIOR_LOGIC.keys())
# Users play record
player_record = {"win": 0, "draw": 0, "lose": 0}


def main():

    play_again = True
    while play_again:  # Outer loop for playing multiple rounds

        while True:
            # Prompt the user to type in a valid Warrior Knight, Ranger, or a Wizard looping until a valid input has been selected.
            try:

                prompt_message = f"\nChoose from: {', '.join(name.capitalize() for name in TYPE_LIST)}: "
                Warrior_type = input(prompt_message)

                if Warrior_type.strip().lower() in TYPE_LIST:
                    user = Warrior(Warrior_type.strip().lower())
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nPlease choose a valid Warrior")

        # Create a randomly generated Warrior
        opponent = Warrior(random.choice(TYPE_LIST))

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
    # Prompt the losser to guess a number
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


if __name__ == "__main__":
    main()
