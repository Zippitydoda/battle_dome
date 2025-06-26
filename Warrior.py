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

# Warrior list
ALL_TYPES = tuple(WARRIOR_LOGIC.keys())
# Weapons list
ALL_WEAPONS = tuple(details["weapon_bonus"] for details in WARRIOR_LOGIC.values())
# Armor list
ALL_ARMORS = tuple(details["armor_bonus"] for details in WARRIOR_LOGIC.values())
# Skills list
ALL_SKILLS = tuple(details["skill_bonus"] for details in WARRIOR_LOGIC.values())


# Bonus Constants for Weapons and Armors
class Bonus(Enum):
    HIGH_BONUS = 3
    MEDIUM_BONUS = 2
    LOW_BONUS = 1


# Enum of outcome options
class Outcome(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"


class Warrior:
    def __init__(self, type) -> None:
        self._type = str(type)
        self._weapon = random.choice(ALL_WEAPONS)
        self._armor = random.choice(ALL_ARMORS)
        self._skill = str(SKILL_BONUS.get(type))
        self._has_weapon_bonus = (
            # If the skill bonus lines up with the appropriate class set value to true
            True
            if self._weapon == WEAPONS_BONUS.get(type)
            else False
        )
        self._has_armor_bonus = (
            # If the armor bonus lines up with the appropriate class set value to true
            True
            if self._armor == ARMOR_BONUS.get(type)
            else False
        )
        self._weapon_bonus = self.weapon_bonus
        self._armor_bonus = self.armor_bonus

    def __str__(self) -> str:

        return (
            f"Your warrior is a {self.type} with {self.skill} bonus and is equiped with {self.weapon} and {self.armor}."
            f"Also weapons bonus is {self.weapon_bonus} and armor bonus is {self.armor_bonus}."
        )

    @property
    def armor_bonus(self) -> int:
        if self.has_armor_bonus:
            self._armor_bonus = Bonus.HIGH_BONUS.value
        elif self._armor == ARMOR_BONUS["naked man"]:
            self._armor_bonus = Bonus.LOW_BONUS.value
        else:
            self._armor_bonus = Bonus.MEDIUM_BONUS.value
        return self._armor_bonus

    @property
    def weapon_bonus(self) -> int:
        if self.has_weapon_bonus:
            self._weapon_bonus = Bonus.HIGH_BONUS.value
        elif self.weapon == WEAPONS_BONUS["naked man"]:
            self._weapon_bonus = Bonus.LOW_BONUS.value
        else:
            self._weapon_bonus = Bonus.MEDIUM_BONUS.value
        return self._weapon_bonus

    @property
    def type(self) -> str:
        return self._type

    @property
    def weapon(self) -> str:
        return self._weapon

    @property
    def armor(self) -> str:
        return self._armor

    @property
    def skill(self) -> str:
        return self._skill

    @property
    def has_weapon_bonus(self) -> bool:
        return self._has_weapon_bonus

    @property
    def has_armor_bonus(self) -> bool:
        return self._has_armor_bonus

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

    # Compare warriors to see what the type advantage is.
    def stare_down(self, opponent_warrior: "Warrior") -> Outcome:
        """
        Compares the type advantage between the user's warrior and the opponent's warrior.

        This function determines the initial outcome of a battle phase based on
        which warrior type has an inherent advantage over the other.

        Args:
            user_warrior (Warrior): The user's warrior object.
            opponent_warrior (Warrior): The opponent's warrior object.

        Returns:
            Outcome:
                - Outcome.WIN if the user's warrior has a type advantage.
                - Outcome.LOSE if the opponent's warrior has a type advantage.
                - Outcome.DRAW if neither warrior has a type advantage over the other.
        """

        # Check if the opponent's warrior type is in the user's warrior's advantage list.
        if opponent_warrior.type in TYPE_ADVANTAGE.get(self.type):  # type: ignore
            return Outcome.WIN
        # Check if the user's warrior type is in the opponent's warrior's advantage list.
        elif self.type in TYPE_ADVANTAGE.get(opponent_warrior.type):  # type: ignore
            return Outcome.LOSE
        # If neither has a direct type advantage, it's a draw.
        else:
            return Outcome.DRAW

    def battle(self, opponent_warrior: "Warrior", outcome: Outcome) -> Outcome:
        """
        Determines the final outcome of a battle phase based on the initial outcome
        (from stare_down) and the warriors' weapon and armor bonuses.

        Args:
            user_warrior (Warrior): The user's warrior object.
            opponent_warrior (Warrior): The opponent's warrior object.
            outcome (Outcome): The outcome of the previous phase (e.g., stare_down).

        Returns:
            Outcome: The final outcome of the battle (WIN, LOSE, or DRAW).
        """

        # Compare bonuses based on the outcome of the previous phase
        match outcome:
            case Outcome.WIN:
                # If user won the previous phase, compare user's weapon bonus against opponent's armor bonus.
                if self.weapon_bonus > opponent_warrior.armor_bonus:
                    return Outcome.WIN
                else:
                    return Outcome.LOSE
            case Outcome.LOSE:
                # If user lost the previous phase, compare opponent's weapon bonus against user's armor bonus.
                if opponent_warrior.weapon_bonus > self.armor_bonus:
                    return Outcome.LOSE
                else:
                    return Outcome.WIN
            case Outcome.DRAW:
                # If it was a draw, compare both warriors' bonuses.
                if self.weapon_bonus == opponent_warrior.armor_bonus:
                    return Outcome.DRAW
                elif self.weapon_bonus > opponent_warrior.armor_bonus:
                    return Outcome.WIN
                else:
                    return Outcome.LOSE


war = Warrior.random_warrior()
war2 = Warrior.random_warrior()

print(war)
print(war2)

print(war.stare_down(war2))
print(war.battle(war2, war.stare_down(war2)))
