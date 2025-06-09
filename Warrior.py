from character_map import WARRIOR_LOGIC
import random

# Type advantages for warriors
TYPE_ADDVANTAGE = {
    warrior_type: details["type_addvatange"]
    for warrior_type, details in WARRIOR_LOGIC.items()
}
# Weapons bonuses for respective warrior types
WEAPONS_BONUS = {
    warrior_type: details["weapon_bonus"]
    for warrior_type, details in WARRIOR_LOGIC.items()
}

# Armor bonuses for respective warrior types
ARMOR_BONUS = {
    warrior_type: details["armor_bonus"]
    for warrior_type, details in WARRIOR_LOGIC.items()
}
# Skill bonus no use fot this yet
SKILL_BONUS = {
    warrior_type: details["skill_bonus"]
    for warrior_type, details in WARRIOR_LOGIC.items()
}

# Warrior list
ALL_TYPES = tuple(WARRIOR_LOGIC.keys())
# Weapons list
ALL_WEAPONS = tuple(details["weapon_bonus"] for details in WARRIOR_LOGIC.values())
# Armor list
ALL_ARMORS = tuple(details["armor_bonus"] for details in WARRIOR_LOGIC.values())
# Skills list
ALL_SKILLS = tuple(details["skill_bonus"] for details in WARRIOR_LOGIC.values())


class Warrior:

    def __init__(self, type) -> None:
        self.type = type
        self.weapon = random.choice(ALL_WEAPONS)
        self.armor = random.choice(ALL_ARMORS)
        self.skill = SKILL_BONUS.get(type)
        self.has_weapon_bonus = (
            # If the skill bonus lines up with the appropriate class set value to true
            True
            if self.weapon == WEAPONS_BONUS.get(type)
            else False
        )
        self.has_armor_bonus = (
            # If the armor bonus lines up with the appropriate class set value to true
            True
            if self.armor == ARMOR_BONUS.get(type)
            else False
        )

    def __str__(self) -> str:

        return (
            f"Your warrior is a {self.type} with {self.skill} bonus and is equiped with {self.weapon} and {self.armor}."
            f"Also weapons bonus is {self.has_weapon_bonus} and armor bonus is {self.has_armor_bonus}."
        )

    @classmethod
    def get_warrior(cls):
        while True:
            # Prompt the user to type in a valid Warrior Knight, Ranger, or a Wizard looping until a valid input has been selected.
            warrior = ""
            try:

                prompt_message = f"\nChoose from: {', '.join(name.capitalize() for name in ALL_TYPES)}: "
                warrior = input(prompt_message).strip().lower()

                if warrior in ALL_TYPES:
                    # If warrior enterd is in the list then break the loop and instantiate the object
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nPlease choose a valid Warrior")
        return cls(warrior)

    @classmethod
    # Create a random warrior
    def random_warrior(cls):
        return cls(random.choices(ALL_TYPES)[0])

    def base_battle_outcome(self, opponent: object) -> str:
        # Current outcome status
        outcome = ""
        # Raise a TypeError if the opponent object is not of the Warrior class
        if not isinstance(opponent, Warrior):

            raise TypeError("Opponent must be a Warrior instance.")
        if opponent.type in TYPE_ADDVANTAGE.get(self.type):
            outcome = "win"

        elif self.type in TYPE_ADDVANTAGE.get(opponent.type):

            outcome = "lose"
        else:
            outcome = "draw"
        # Check for overturn weapons bonus scenario

        match outcome:
            case "win":
                if not self.has_weapon_bonus and opponent.has_weapon_bonus:
                    return "lose"
                else:
                    return "win"

            case "lose":
                if not self.has_weapon_bonus:
                    return "lose"
                elif self.has_weapon_bonus and not opponent.has_weapon_bonus:
                    return "win"
                else:
                    return "lose"

            case "draw":
                if not self.has_weapon_bonus and opponent.has_weapon_bonus:
                    return "lose"
                elif self.has_weapon_bonus and not opponent.has_weapon_bonus:
                    return "win"
                else:
                    return "draw"

            # Catch all if something other than win, draw or lose is sent through the function
            case _:
                raise ValueError(
                    "Error: Unexpected outcome from victory function. Defaulting to draw."
                )
                return "draw"


"""
war = Warrior.get_warrior()
war2 = Warrior.random_warrior()
print(f"opponent has a weapon bonuse {war2.has_weapon_bonus}")
print(f"{war.type} vs {war2.type}")
print(f"Weapons bonus outcome is {war.type} {war.base_battle_outcome(war2)}")
print(war)"""
