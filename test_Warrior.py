# test_warrior.py
import pytest
from Warrior import (
    Warrior,
    Outcome,
    Bonus,
    WEAPONS_BONUS,
    ARMOR_BONUS,
    ALL_WEAPONS,
    ALL_ARMORS,
)
from character_map import WARRIOR_LOGIC


@pytest.fixture
def create_test_warrior():
    """
    A factory fixture to create Warrior instances for testing.
    It allows specifying the warrior type and influencing the
    internal _weapon_bonus and _armor_bonus for deterministic battle tests
    by setting _has_weapon_bonus and _has_armor_bonus directly, and ensuring
    the _weapon and _armor attributes align for the property calculations.
    """

    def _create_warrior(
        warrior_type: str,
        has_weapon_bonus: bool | None = None,
        has_armor_bonus: bool | None = None,
    ) -> Warrior:
        warrior = Warrior(warrior_type)

        # Control _has_weapon_bonus and _has_armor_bonus flags
        # These flags are directly used by the weapon_bonus and armor_bonus properties.
        if has_weapon_bonus is not None:
            warrior._has_weapon_bonus = has_weapon_bonus
            if has_weapon_bonus:
                # Set weapon to the type's bonus weapon to ensure HIGH_BONUS
                warrior._weapon = WEAPONS_BONUS.get(warrior_type)
            else:
                # Set weapon to something that is NOT the type's bonus weapon
                # and NOT the "naked man" weapon to ensure MEDIUM_BONUS.
                # If we want LOW_BONUS specifically, we'd need another parameter to force "naked man" weapon.
                non_bonus_weapons = [
                    w
                    for w in ALL_WEAPONS
                    if w != WEAPONS_BONUS.get(warrior_type)
                    and w != WEAPONS_BONUS["naked man"]
                ]
                if non_bonus_weapons:
                    # Pick the first available non-bonus and non-naked man weapon
                    warrior._weapon = non_bonus_weapons[0]
                else:
                    # Fallback if no suitable non-bonus weapon is found (unlikely with current setup)
                    warrior._weapon = "some_other_weapon"

        if has_armor_bonus is not None:
            warrior._has_armor_bonus = has_armor_bonus
            if has_armor_bonus:
                # Set armor to the type's bonus armor to ensure HIGH_BONUS
                warrior._armor = ARMOR_BONUS.get(warrior_type)
            else:
                # Set armor to something that is NOT the type's bonus armor
                # and NOT the "naked man" armor to ensure MEDIUM_BONUS.
                # If we want LOW_BONUS specifically, we'd need another parameter to force "Nudity" armor.
                non_bonus_armors = [
                    a
                    for a in ALL_ARMORS
                    if a != ARMOR_BONUS.get(warrior_type)
                    and a != ARMOR_BONUS["naked man"]
                ]
                if non_bonus_armors:
                    # Pick the first available non-bonus and non-naked man armor
                    warrior._armor = non_bonus_armors[0]
                else:
                    # Fallback if no suitable non-bonus armor is found
                    warrior._armor = "some_other_armor"

        # The _weapon_bonus and _armor_bonus attributes are re-calculated by their properties
        # when accessed. To ensure the battle function uses the intended values based on
        # the setup above, we can assert on the property directly within the test.
        # This part below is for internal consistency but the main control is via _has_bonus flags.
        warrior._weapon_bonus = warrior.weapon_bonus  # This calls the property getter
        warrior._armor_bonus = warrior.armor_bonus  # This calls the property getter

        return warrior

    return _create_warrior


# --- Test cases for stare_down function ---


def test_stare_down_user_wins(create_test_warrior):
    """
    Tests stare_down when the user's warrior has a type advantage over the opponent.
    Example: Knight has advantage over Bard.
    """
    knight = create_test_warrior("knight")
    bard = create_test_warrior("bard")
    expected_outcome = Outcome.WIN
    assert knight.stare_down(bard) == expected_outcome


def test_stare_down_opponent_wins(create_test_warrior):
    """
    Tests stare_down when the opponent's warrior has a type advantage over the user.
    Example: Bard loses to Knight (because Knight has advantage over Bard).
    """
    bard = create_test_warrior("bard")
    knight = create_test_warrior("knight")
    expected_outcome = Outcome.LOSE
    assert bard.stare_down(knight) == expected_outcome


def test_stare_down_draw(create_test_warrior):
    """
    Tests stare_down when neither warrior has a type advantage over the other.
    Example: Knight vs Rogue (no direct advantage for either).
    """
    knight = create_test_warrior("knight")
    rogue = create_test_warrior("rogue")
    expected_outcome = Outcome.DRAW
    assert knight.stare_down(rogue) == expected_outcome


# --- Test cases for battle function ---

# Scenario 1: Initial outcome from stare_down is WIN (user has type advantage)


def test_battle_initial_win_user_weapon_stronger_than_opponent_armor(
    create_test_warrior,
):
    """
    Tests battle when initial_outcome is WIN, and user's weapon bonus
    is higher than opponent's armor bonus, leading to a user WIN.
    User: HIGH_BONUS weapon. Opponent: LOW_BONUS armor.
    """
    user_warrior = create_test_warrior(
        "knight", has_weapon_bonus=True
    )  # Knight with bonus weapon -> HIGH_BONUS
    # To get LOW_BONUS for opponent armor, we need to ensure their armor is "Nudity"
    # For a deterministic LOW_BONUS, we need to directly set the armor to "Nudity"
    # and set has_armor_bonus=False (as it's not their specific bonus armor).
    opponent_warrior = create_test_warrior("bard", has_armor_bonus=False)
    opponent_warrior._armor = ARMOR_BONUS[
        "naked man"
    ]  # Force naked man armor for LOW_BONUS
    opponent_warrior._armor_bonus = (
        opponent_warrior.armor_bonus
    )  # Recalculate property's internal value

    initial_outcome = Outcome.WIN
    expected_outcome = Outcome.WIN
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_win_user_weapon_weaker_than_opponent_armor(create_test_warrior):
    """
    Tests battle when initial_outcome is WIN, but user's weapon bonus
    is lower than opponent's armor bonus, leading to a user LOSE.
    User: MEDIUM_BONUS weapon. Opponent: HIGH_BONUS armor.
    """
    user_warrior = create_test_warrior(
        "knight", has_weapon_bonus=False
    )  # Knight without bonus weapon -> MEDIUM_BONUS
    opponent_warrior = create_test_warrior(
        "bard", has_armor_bonus=True
    )  # Bard with bonus armor -> HIGH_BONUS

    initial_outcome = Outcome.WIN
    expected_outcome = Outcome.LOSE
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_win_user_weapon_equal_to_opponent_armor(create_test_warrior):
    """
    Tests battle when initial_outcome is WIN, and user's weapon bonus
    is equal to opponent's armor bonus, leading to a user LOSE (as per current logic).
    User: MEDIUM_BONUS weapon. Opponent: MEDIUM_BONUS armor.
    """
    user_warrior = create_test_warrior(
        "knight", has_weapon_bonus=False
    )  # MEDIUM_BONUS weapon
    opponent_warrior = create_test_warrior(
        "bard", has_armor_bonus=False
    )  # MEDIUM_BONUS armor

    initial_outcome = Outcome.WIN
    expected_outcome = Outcome.LOSE
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


# Scenario 2: Initial outcome from stare_down is LOSE (opponent has type advantage)


def test_battle_initial_lose_opponent_weapon_weaker_than_user_armor(
    create_test_warrior,
):
    """
    Tests battle when initial_outcome is LOSE, but opponent's weapon bonus
    is lower than user's armor bonus, leading to a user WIN.
    User: HIGH_BONUS armor. Opponent: LOW_BONUS weapon.
    """
    user_warrior = create_test_warrior(
        "bard", has_armor_bonus=True
    )  # Bard with bonus armor -> HIGH_BONUS
    # Force "Empty Handed" weapon for opponent for LOW_BONUS
    opponent_warrior = create_test_warrior("knight", has_weapon_bonus=False)
    opponent_warrior._weapon = WEAPONS_BONUS[
        "naked man"
    ]  # Force naked man weapon for LOW_BONUS
    opponent_warrior._weapon_bonus = (
        opponent_warrior.weapon_bonus
    )  # Recalculate property's internal value

    initial_outcome = Outcome.LOSE
    expected_outcome = Outcome.WIN
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_lose_opponent_weapon_stronger_than_user_armor(
    create_test_warrior,
):
    """
    Tests battle when initial_outcome is LOSE, and opponent's weapon bonus
    is higher than user's armor bonus, leading to a user LOSE.
    User: MEDIUM_BONUS armor. Opponent: HIGH_BONUS weapon.
    """
    user_warrior = create_test_warrior(
        "bard", has_armor_bonus=False
    )  # Bard without bonus armor -> MEDIUM_BONUS
    opponent_warrior = create_test_warrior(
        "knight", has_weapon_bonus=True
    )  # Knight with bonus weapon -> HIGH_BONUS

    initial_outcome = Outcome.LOSE
    expected_outcome = Outcome.LOSE
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_lose_opponent_weapon_equal_to_user_armor(create_test_warrior):
    """
    Tests battle when initial_outcome is LOSE, and opponent's weapon bonus
    is equal to user's armor bonus, leading to a user WIN (as per current logic).
    User: MEDIUM_BONUS armor. Opponent: MEDIUM_BONUS weapon.
    """
    user_warrior = create_test_warrior(
        "bard", has_armor_bonus=False
    )  # MEDIUM_BONUS armor
    opponent_warrior = create_test_warrior(
        "knight", has_weapon_bonus=False
    )  # MEDIUM_BONUS weapon

    initial_outcome = Outcome.LOSE
    expected_outcome = Outcome.WIN
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


# Scenario 3: Initial outcome from stare_down is DRAW


def test_battle_initial_draw_equal_bonuses(create_test_warrior):
    """
    Tests battle when initial_outcome is DRAW, and both warriors have
    equal weapon and armor bonuses, leading to a DRAW.
    User: MEDIUM_BONUS weapon. Opponent: MEDIUM_BONUS armor.
    """
    user_warrior = create_test_warrior(
        "knight", has_weapon_bonus=False
    )  # MEDIUM_BONUS weapon
    opponent_warrior = create_test_warrior(
        "rogue", has_armor_bonus=False
    )  # MEDIUM_BONUS armor

    initial_outcome = Outcome.DRAW
    expected_outcome = Outcome.DRAW
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_draw_user_weapon_stronger_than_opponent_armor(
    create_test_warrior,
):
    """
    Tests battle when initial_outcome is DRAW, and user's weapon bonus
    is higher than opponent's armor bonus, leading to a user WIN.
    User: HIGH_BONUS weapon. Opponent: LOW_BONUS armor.
    """
    user_warrior = create_test_warrior(
        "knight", has_weapon_bonus=True
    )  # HIGH_BONUS weapon
    # Force "Nudity" armor for opponent for LOW_BONUS
    opponent_warrior = create_test_warrior("rogue", has_armor_bonus=False)
    opponent_warrior._armor = ARMOR_BONUS[
        "naked man"
    ]  # Force naked man armor for LOW_BONUS
    opponent_warrior._armor_bonus = (
        opponent_warrior.armor_bonus
    )  # Recalculate property's internal value

    initial_outcome = Outcome.DRAW
    expected_outcome = Outcome.WIN
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome


def test_battle_initial_draw_user_weapon_weaker_than_opponent_armor(
    create_test_warrior,
):
    """
    Tests battle when initial_outcome is DRAW, and user's weapon bonus
    is lower than opponent's armor bonus, leading to a user LOSE.
    User: LOW_BONUS weapon. Opponent: HIGH_BONUS armor.
    """
    # Force "Empty Handed" weapon for user for LOW_BONUS
    user_warrior = create_test_warrior("knight", has_weapon_bonus=False)
    user_warrior._weapon = WEAPONS_BONUS[
        "naked man"
    ]  # Force naked man weapon for LOW_BONUS
    user_warrior._weapon_bonus = (
        user_warrior.weapon_bonus
    )  # Recalculate property's internal value

    opponent_warrior = create_test_warrior(
        "rogue", has_armor_bonus=True
    )  # HIGH_BONUS armor

    initial_outcome = Outcome.DRAW
    expected_outcome = Outcome.LOSE
    assert user_warrior.battle(opponent_warrior, initial_outcome) == expected_outcome
