import pytest

from Warrior import Warrior

from battle_dome import battle, Outcome


# Helper function to create a Warrior with specific bonuses for testing
def create_test_warrior(
    warrior_type: str, weapon_bonus: int, armor_bonus: int
) -> Warrior:
    """
    Creates a Warrior object and sets its weapon_bonus and armor_bonus
    attributes directly for testing purposes.
    """
    # Instantiate a Warrior. Its initial weapon/armor will be random,
    # but we'll immediately override the bonus attributes.
    # Choose a valid type from your WARRIOR_LOGIC (e.g., 'knight')
    test_warrior = Warrior(warrior_type)
    test_warrior.weapon_bonus = weapon_bonus
    test_warrior.armor_bonus = armor_bonus
    return test_warrior


# Test cases for the battle function


# --- Initial Outcome: WIN ---
def test_battle_initial_win_user_wins():
    """
    Test case: Initial outcome is WIN, and user's weapon bonus is greater
    than opponent's armor bonus, leading to a user WIN.
    """
    user = create_test_warrior("knight", 5, 2)  # User has high weapon bonus
    opponent = create_test_warrior("ranger", 3, 1)  # Opponent has low armor bonus
    result = battle(user, opponent, Outcome.WIN)
    assert result == Outcome.WIN


def test_battle_initial_win_user_loses():
    """
    Test case: Initial outcome is WIN, but user's weapon bonus is less
    than opponent's armor bonus, leading to a user LOSE.
    """
    user = create_test_warrior("knight", 1, 2)  # User has low weapon bonus
    opponent = create_test_warrior("ranger", 3, 5)  # Opponent has high armor bonus
    result = battle(user, opponent, Outcome.WIN)
    assert result == Outcome.LOSE


def test_battle_initial_win_draw():
    """
    Test case: Initial outcome is WIN, and user's weapon bonus is equal
    to opponent's armor bonus, leading to a DRAW.
    """
    user = create_test_warrior("knight", 3, 2)  # User weapon bonus 3
    opponent = create_test_warrior("ranger", 2, 3)  # Opponent armor bonus 3
    result = battle(user, opponent, Outcome.WIN)
    assert result == Outcome.DRAW


# --- Initial Outcome: LOSE ---
def test_battle_initial_lose_user_loses():
    """
    Test case: Initial outcome is LOSE, and opponent's weapon bonus is greater
    than user's armor bonus, leading to a user LOSE.
    """
    user = create_test_warrior("knight", 2, 1)  # User armor bonus 1
    opponent = create_test_warrior("ranger", 5, 3)  # Opponent weapon bonus 5
    result = battle(user, opponent, Outcome.LOSE)
    assert result == Outcome.LOSE


def test_battle_initial_lose_user_wins():
    """
    Test case: Initial outcome is LOSE, but opponent's weapon bonus is less
    than user's armor bonus, leading to a user WIN.
    """
    user = create_test_warrior("knight", 5, 3)  # User armor bonus 3
    opponent = create_test_warrior("ranger", 1, 2)  # Opponent weapon bonus 1
    result = battle(user, opponent, Outcome.LOSE)
    assert result == Outcome.WIN


def test_battle_initial_lose_draw():
    """
    Test case: Initial outcome is LOSE, and opponent's weapon bonus is equal
    to user's armor bonus, leading to a DRAW.
    """
    user = create_test_warrior("knight", 2, 3)  # User armor bonus 3
    opponent = create_test_warrior("ranger", 3, 2)  # Opponent weapon bonus 3
    result = battle(user, opponent, Outcome.LOSE)
    assert result == Outcome.DRAW


# --- Initial Outcome: DRAW ---
def test_battle_initial_draw_user_loses():
    """
    Test case: Initial outcome is DRAW, and opponent's total bonus is greater
    than user's total bonus, leading to a user LOSE.
    """
    user = create_test_warrior("knight", 2, 2)  # Total 4
    opponent = create_test_warrior("ranger", 3, 2)  # Total 5
    result = battle(user, opponent, Outcome.DRAW)
    assert result == Outcome.LOSE


def test_battle_initial_draw_user_wins():
    """
    Test case: Initial outcome is DRAW, and opponent's total bonus is less
    than user's total bonus, leading to a user WIN.
    """
    user = create_test_warrior("knight", 3, 2)  # Total 5
    opponent = create_test_warrior("ranger", 2, 2)  # Total 4
    result = battle(user, opponent, Outcome.DRAW)
    assert result == Outcome.WIN


def test_battle_initial_draw_draw():
    """
    Test case: Initial outcome is DRAW, and both warriors' total bonuses are equal,
    leading to a DRAW.
    """
    user = create_test_warrior("knight", 3, 2)  # Total 5
    opponent = create_test_warrior("ranger", 3, 2)  # Total 5
    result = battle(user, opponent, Outcome.DRAW)
    assert result == Outcome.DRAW
