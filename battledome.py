from random import randint


class Character:
    def __init__(self, type):

        self.base_class_type = ["knight", "ranger", "wizard"]
        weapon = ["sword", "magic wand", "bow", "nothing"]

        self.type = type.lower()
        self.weapon = weapon[randint(0, len(weapon) - 1)]


battle_pool = {"knight": "sword", "ranger": "bow", "wizard": "magic wand"}
type_list = list(battle_pool.keys())


def main():
    base_class_type = list(battle_pool.keys())

    # Prompt the user to type in a valid character Knight , Ranger , or a Wizard.
    while True:

        try:
            character_type = input("\nChoose either a Knight , Ranger , or a Wizard: ")
            if character_type.strip().lower() in base_class_type:
                user = Character(character_type.strip().lower())
                break
            else:
                raise ValueError
        except ValueError:
            print("Please choose a valid Character")

    # Create a randomly generated character
    opponent = Character(base_class_type[randint(0, len(base_class_type) - 1)])
    # Have the user and opponent battle
    battle(user, opponent)


def battle(user: object, opponent: object):

    user_char = user.type
    user_weapon = user.weapon
    opponent_char = opponent.type
    opponent_weapon = opponent.weapon

    print(
        f"\nYour warrior is a {user.type} and is equiped with {user.weapon}\n\nYou will be fighting a {opponent.type} with {opponent.weapon}"
    )

    # Check to see who wins with no bonuses attached
    win_loss(user_char, opponent_char)
    print(win_loss(user_char, opponent_char))

    # print(list(battle_pool.keys())[0])


def win_loss(user_char: str, opponent_char: str) -> bool:
    # Create the winning scenario for the users current character
    user_victory_status = False
    user_battlenumb = type_list.index(user_char)
    opponent_battlenumb = type_list.index(opponent_char)

    wining_list = [user_battlenumb, (type_list.index(user_char) + 1) % len(type_list)]

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


def weapons_bonus(
    user_type: str, user_weapon: str, opponent_type: str, opponent_weapon: str
):
    # Check if user has appropriate weapon for bonus
    pass


main()
