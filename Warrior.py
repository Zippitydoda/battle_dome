import random


class Warrior:
    """Represents a warrior in the game, with a specific type and a randomly assigned weapon."""

    # Weapons bonuses for respective warrior types
    WEAPONS_BONUS = {
        "knight": "sword",
        "ranger": "bow",
        "wizard": "magic wand",
        "bard": "lute",
        "rogue": "dagger",
        "psychic": "crystal Ball",
    }
    # Weapons list
    ALL_WEAPONS = list(WEAPONS_BONUS.values())

    def __init__(self, type):
        """
        Initializes a Warrior instance.

        Args:
            type (str): The type of the warrior (e.g., 'knight', 'ranger', 'wizard').
                        Will be converted to lowercase.
        """
        self.type = type.lower()
        self.weapon = random.choice(self.ALL_WEAPONS)
        # Users win loss record
        self.player_record = {"win": 0, "draw": 0, "lose": 0}
        # Bool if Warrior has a weapons bonus
        self.has_weapon_bonus = False

        if self.WEAPONS_BONUS.get(self.type) == self.weapon:
            self.has_weapon_bonus = True

    def match_up(self, opponent: object) -> str:
        # Raise a TypeError if the opponent object is not of the Warrior class
        if not isinstance(opponent, Warrior):

            raise TypeError("Opponent must be a Warrior instance.")

        TYPE_LIST = list(self.WEAPONS_BONUS.keys())

        user_victory_status = ""
        # If the users battle number is > 3 then divide the number by 2
        user_battlenumb = int(
            TYPE_LIST.index(self.type) - 3
            if TYPE_LIST.index(self.type) > 2
            else TYPE_LIST.index(self.type)
        )
        # If the opponents battle number is > 2 then subtract the number by 2
        opponent_battlenumb = int(
            TYPE_LIST.index(opponent.type) - 3
            if TYPE_LIST.index(opponent.type) > 2
            else TYPE_LIST.index(opponent.type)
        )

        wining_list = [
            user_battlenumb,
            (TYPE_LIST.index(self.type) + 1) % len(TYPE_LIST),
        ]

        if opponent_battlenumb == wining_list[1]:

            user_victory_status = "win"
        elif opponent_battlenumb == user_battlenumb:

            user_victory_status = "draw"
        else:

            user_victory_status = "lose"

        match user_victory_status:

            case "win":
                # If opponent does not have a weapons bonus
                if opponent.has_weapon_bonus == False:
                    print("You Win!")
                    return "win"
                # If user and opponent both have weapons bonuses
                elif self.has_weapon_bonus == True:
                    print("You Win!")
                    return "win"
                # If your opponent has a weapons bonus but user does not
                else:
                    print("You Lose!")
                    return "lose"

            case "lose":
                # If user dose not have weapon bonus
                if self.has_weapon_bonus == False:
                    print("You Lose!")
                    return "lose"
                # If user hase a weapons bonus and the opponent does not.
                elif opponent.has_weapon_bonus == False:
                    print("You Win!")
                    return "win"
                # If both user and opponent have weapons bonuses
                else:
                    print("You Lose!")
                    return "lose"
            case "draw":
                # If user has a weapons bonus but opponent does not
                if self.has_weapon_bonus == True and opponent.has_weapon_bonus == False:
                    print("You Win!")
                    return "win"
                # If user and opponent both have weapons bonuses
                if self.has_weapon_bonus == True and opponent.has_weapon_bonus == True:
                    print("Draw")
                    return "draw"
                # If user dose not have weapons bonus but opponent does
                if self.has_weapon_bonus == False and opponent.has_weapon_bonus == True:
                    print("You Lose!")
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

    # Update the players record with win, lose, or draw.
    def update_record(self, outcome: str):
        self.player_record[outcome] += 1
