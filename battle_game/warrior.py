from character_map import WARRIOR_LOGIC
from enum import Enum
import random

""" These attribute dicts are what the whole logic system is based off of """
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

    def __repr__(self) -> str:
        war = f"Warrior(\n Type={self.type},\n Skill={self.skill},\n Weapon type={self.weapon},\n Has Weapon bonus={self.has_weapon_bonus},\n Weapon bonuse={self.weapon_bonus},\n Armor type={self.armor},\n Has Armor bonus={self.has_armor_bonus},\n Armor bonus={self.armor_bonus}"
        return war

    def __str__(self) -> str:

        return (
            f"Your warrior is a {self.type} with {self.skill} bonus and is equiped with a {self.weapon} and {self.armor}."
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

    def attack(self, opponent_warrior: "Warrior") -> Outcome:
        """
        Simulates an attack between this warrior and an opponent.

        The outcome of the attack is determined by comparing the attacker's
        weapon bonus to the opponent's armor bonus.

        Args:
            opponent_warrior: The Warrior instance that is being attacked.

        Returns:
            An Outcome enum value indicating the result of the attack:
            - Outcome.WIN: If the attacker's weapon bonus is greater.
            - Outcome.LOSE: If the opponent's armor bonus is greater.
            - Outcome.DRAW: If their bonuses are equal.
        """
        # If users weapon bonus is greater than opponents armor bonus.
        if self.weapon_bonus > opponent_warrior.armor_bonus:
            return Outcome.WIN
        # If users weeapon bonus in not greater than opponent armor bonus.
        elif self.weapon_bonus < opponent_warrior.armor_bonus:
            return Outcome.LOSE
        else:
            return Outcome.DRAW

    def clash(self, opponent_warrior: "Warrior") -> Outcome:
        """Simulates a clash between this warrior and an opponent.

        The outcome is determined by comparing the sum of each warrior's
        armor and weapon bonuses.

        Args:
            opponent_warrior: The Warrior instance to clash with.

        Returns:
            An Outcome enum value indicating the result of the clash:
            - Outcome.WIN: If the current warrior's total bonus is greater.
            - Outcome.LOSE: If the opponent's total bonus is greater.
            - Outcome.DRAW: If their total bonuses are equal.
        """
        # Add the armor and weapon bonuses together then compare the values
        self_point_bonus = self.armor_bonus + self.weapon_bonus
        opponent_warrior_point_bonus = (
            opponent_warrior.armor_bonus + opponent_warrior.weapon_bonus
        )

        if self_point_bonus > opponent_warrior_point_bonus:
            return Outcome.WIN
        elif self_point_bonus < opponent_warrior_point_bonus:
            return Outcome.LOSE
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

    def full_battle(self, opponent_warrior: "Warrior") -> Outcome:
        phase_victor = None
        # Phase 1: Pick whether user or opponent gets to attack first based off of base type advantage
        phase_1_outcome = self.stare_down(opponent_warrior)
        # Phase 2: winner of phase 1 gets to attack the opposing player
        match phase_1_outcome:
            case Outcome.WIN:
                # User attacks opponent
                phase_victor = self
                phase_2_outcome = self.attack(opponent_warrior)
            case Outcome.LOSE:
                # Opponent attacks user
                phase_victor = opponent_warrior
                phase_2_outcome = opponent_warrior.attack(self)
            case Outcome.DRAW:
                # User clashes with opponent
                phase_2_outcome = self.clash(opponent_warrior)
                if phase_2_outcome == Outcome.WIN:
                    return Outcome.WIN
                elif phase_2_outcome == Outcome.LOSE:
                    return Outcome.LOSE
                else:
                    return Outcome.DRAW
        # Phase 3
        match phase_2_outcome:
            # If user wins the previous phase they win the battle
            case Outcome.WIN:
                if phase_victor == self:
                    return Outcome.WIN
                else:
                    return Outcome.LOSE
            # If user loses the previous phase they are attacked by their opponent
            case Outcome.LOSE:
                phase_victor = opponent_warrior
                phase_3_outcome = opponent_warrior.attack(self)

            case Outcome.DRAW:
                # TODO
                pass


war = Warrior.get_warrior()
war2 = Warrior.random_warrior()


print(repr(war))
print(repr(war2))
print(war.clash(war2))
print(war.attack(war2))
print(war2.attack(war))
# print(war.stare_down(war2))
# print(war.battle(war2, war.stare_down(war2)))
