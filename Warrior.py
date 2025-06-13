from character_map import WARRIOR_LOGIC
from enum import Enum
import random

# Type addvantages for warriors
TYPE_ADVANTAGE = {
    warrior_type: details["type_advantage"]
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


# Bonus Constants for Weapons and Armors
class Bonus(Enum):
    HIGH_BONUS = 3
    MEDIUM_BONUS = 2
    LOW_BONUS = 1


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
        # Set bonus weapon number
        if self.has_weapon_bonus:
            self.weapon_bonus = Bonus.HIGH_BONUS.value
        elif self.weapon == WEAPONS_BONUS["naked man"]:
            self.weapon_bonus = Bonus.LOW_BONUS.value
        else:
            self.weapon_bonus = Bonus.MEDIUM_BONUS.value

        # Set bonus armor number
        if self.has_armor_bonus:
            self.armor_bonus = Bonus.HIGH_BONUS.value
        elif self.armor == ARMOR_BONUS["naked man"]:
            self.armor_bonus = Bonus.LOW_BONUS.value
        else:
            self.armor_bonus = Bonus.MEDIUM_BONUS.value

    def __str__(self) -> str:

        return (
            f"Your warrior is a {self.type} with {self.skill} bonus and is equiped with {self.weapon} and {self.armor}."
            f"Also weapons bonus is {self.weapon_bonus} and armor bonus is {self.armor_bonus}."
        )

    @classmethod
    def get_warrior(cls):
        while True:
            # Prompt the user to type in a valid Warrior Knight, Ranger, or a Wizard looping until a valid input has been selected.

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


# print(type(WEAPONS_BONUS["naked man"]))
"""war = Warrior.get_warrior()
# war2 = Warrior.random_warrior()

print(war)
war.has_weapon_bonus = False
war.weapon = "Empty Handed"


print(war)"""
