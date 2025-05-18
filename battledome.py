import random


class Warrior:
    """Represents a warrior in the game, with a specific type and a randomly assigned weapon."""

    # Weapons list
    ALL_WEAPONS = ["sword", "magic wand", "bow"]

    def __init__(self, type):
        """
        Initializes a Warrior instance.

        Args:
            type (str): The type of the warrior (e.g., 'knight', 'ranger', 'wizard').
                        Will be converted to lowercase.
        """
        self.type = type.lower()
        self.weapon = self.weapon = random.choice(self.ALL_WEAPONS)


# Dictionary of warrior classes and respective bonus weapons.
BATTLE_POOL = {
    "knight": "sword",
    "ranger": "bow",
    "wizard": "magic wand",
}
# List of warrior types
TYPE_LIST = list(BATTLE_POOL.keys())
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

        # Have the user and opponent battle
        outcome = battle(user.type, user.weapon, opponent.type, opponent.weapon)
        # Update users win loss record
        update_record(outcome)
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


def battle(
    user_char: str, user_weapon: str, opponent_char: str, opponent_weapon: str
) -> str:

    print(
        f"\nYour warrior is a {user_char} and is equiped with {user_weapon}.\n"
        f"You will be fighting a {opponent_char} equiped with {opponent_weapon}.\n"
    )
    match victory(user_char, opponent_char):

        case "win":
            # If opponent does not have a weapons bonus
            if weapons_bonus(opponent_char, opponent_weapon) == False:
                print("You Win!")
                return "win"
            # If user and opponent both have weapons bonuses
            elif weapons_bonus(user_char, user_weapon) == True:
                print("You Win!")
                return "win"
            # If your opponent has a weapons bonus but user does not
            else:
                print("You lose")
                return "lose"

        case "lose":
            # If user dose not have weapon bonus
            if weapons_bonus(user_char, user_weapon) == False:
                print("You Lose")
                return "lose"
            # If user hase a weapons bonus and the opponent does not.
            elif weapons_bonus(opponent_char, opponent_weapon) == False:
                print("You Win!")
                return "win"
            # If both user and opponent have weapons bonuses
            else:
                print("You Lose")
                return "lose"
        case "draw":
            # If user has a weapons bonus but opponent does not
            if (
                weapons_bonus(user_char, user_weapon) == True
                and weapons_bonus(opponent_char, opponent_weapon) == False
            ):
                print("You Win!")
                return "win"
            # If user and opponent both have weapons bonuses
            if (
                weapons_bonus(user_char, user_weapon) == True
                and weapons_bonus(opponent_char, opponent_weapon) == True
            ):
                print("Draw")
                return "draw"
            # If user dose not have weapons bonus but opponent does
            if (
                weapons_bonus(user_char, user_weapon) == False
                and weapons_bonus(opponent_char, opponent_weapon) == True
            ):
                print("You Lose")
                return "lose"

            else:
                print("Draw")
                return "draw"
        # Catch all if something other than win, draw or lose is sent through the function
        case _:
            print(
                "Error: Unexpected outcome from victory function. Defaulting to draw."
            )
            return "draw"


# The battle outcome is first determined by type advantage (victory function).
# Then, weapon bonuses are applied:
# - A bonus can turn a base loss into a win if the opponent has no bonus.
# - A bonus can turn a base draw into a win if the opponent has no bonus.
# - If both or neither have a bonus, a base draw remains a draw.
# - A bonus for the opponent can turn a base win for the user into a loss if the user has no bonus
def victory(user_char: str, opponent_char: str) -> str:
    """
    Determines the base outcome of a battle (win, lose, or draw) based on
    a cyclical type advantage (e.g., Knight > Ranger > Wizard > Knight).

    Args:
        user_char (str): The type of the user's warrior.
        opponent_char (str): The type of the opponent's warrior.

    Returns:
        str: "win" if the user has a type advantage,
             "lose" if the opponent has a type advantage,
             "draw" if both are the same type.
    """
    user_victory_status = ""
    user_battlenumb = TYPE_LIST.index(user_char)
    opponent_battlenumb = TYPE_LIST.index(opponent_char)

    wining_list = [user_battlenumb, (TYPE_LIST.index(user_char) + 1) % len(TYPE_LIST)]

    if opponent_battlenumb == wining_list[1]:

        user_victory_status = "win"
    elif opponent_battlenumb == user_battlenumb:

        user_victory_status = "draw"
    else:

        user_victory_status = "lose"

    return user_victory_status


# Check if user has appropriate weapon for bonus
def weapons_bonus(warrior: str, weapon: str) -> bool:
    # key =
    # "knight": "sword",
    # "ranger": "bow",
    # "wizard": "magic wand"

    # If warrior gets a weapons bonus return true.
    if BATTLE_POOL.get(warrior) == weapon:
        return True
    else:
        return False


# Update the players record with win, lose, or draw.
def update_record(outcome: str):
    player_record[outcome] += 1


if __name__ == "__main__":
    main()
