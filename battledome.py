import random
from Warrior import Warrior


# List of warrior types
TYPE_LIST = list(Warrior.WEAPONS_BONUS.keys())
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
        outcome = user.match_up(opponent)
        # Update users win loss record
        user.update_record(outcome)
        print(
            f"\nYour record is Wins: {user.player_record['win']} Draws: {user.player_record['draw']} Losses: {user.player_record['lose']}"
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


if __name__ == "__main__":
    main()
