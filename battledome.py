from random import randint


class Warrior:
    def __init__(self, type):

        self.TYPE_LIST = ["knight", "ranger", "wizard"]
        weapon = ["sword", "magic wand", "bow", "nothing"]

        self.type = type.lower()
        self.weapon = weapon[randint(0, len(weapon) - 1)]


# Dictionary of warrior classes and respective bonus weapons.
BATTLE_POOL = {"knight": "sword", "ranger": "bow", "wizard": "magic wand"}
# List of warrior types
TYPE_LIST = list(BATTLE_POOL.keys())


def main():

    # Prompt the user to type in a valid Warrior Knight , Ranger , or a Wizard.
    while True:

        try:
            Warrior_type = input("\nChoose either a Knight , Ranger , or a Wizard: ")
            if Warrior_type.strip().lower() in TYPE_LIST:
                user = Warrior(Warrior_type.strip().lower())
                break
            else:
                raise ValueError
        except ValueError:
            print("Please choose a valid Warrior")

    # Create a randomly generated Warrior
    opponent = Warrior(TYPE_LIST[randint(0, len(TYPE_LIST) - 1)])
    # Have the user and opponent battle
    battle(user.type, user.weapon, opponent.type, opponent.weapon)


def battle(user_char: str, user_weapon: str, opponent_char: str, opponent_weapon: str):

    # user_char = user current warrior
    # user_weapon = user current weapon
    # opponent_char = opponent current warrior
    # opponent_weapon = opponent current weapon

    print(
        f"\nYour warrior is a {user_char} and is equiped with {user_weapon}.\n\nYou will be fighting a {opponent_char} with {opponent_weapon}."
    )

    # Check to see who wins with no bonuses attached

    # win_loss(user_char, opponent_char)
    print(f"you get a {weapons_bonus(user_char,user_weapon)} bonus")
    print(f"opponent gets a {weapons_bonus(opponent_char,opponent_weapon)} bonus")
    print(f"you won: {win_loss(user_char, opponent_char)}")

    # print(list(BATTLE_POOL.keys())[0])


def win_loss(user_char: str, opponent_char: str) -> bool:
    # Create the winning scenario for the users current Warrior
    user_victory_status = False
    user_battlenumb = TYPE_LIST.index(user_char)
    opponent_battlenumb = TYPE_LIST.index(opponent_char)

    wining_list = [user_battlenumb, (TYPE_LIST.index(user_char) + 1) % len(TYPE_LIST)]

    if opponent_battlenumb == wining_list[1]:
        print("You Win!")
        user_victory_status = True
    elif opponent_battlenumb == user_battlenumb:
        print("Stalemate")
        user_victory_status = False
    else:
        print("You Lose")
        user_victory_status = False

    return user_victory_status


def weapons_bonus(warrior: str, weapon: str) -> bool:
    # Check if user has appropriate weapon for bonus
    # key = {"knight": "sword", "ranger": "bow", "wizard": "magic wand"}
    if BATTLE_POOL.get(warrior) == weapon:
        return True
    else:
        return False


main()
