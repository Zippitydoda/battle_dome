# --- Test Cases for Warrior.base_battle_outcome ---

# Fixtures for common Warrior types with and without bonuses

import pytest
from Warrior import Warrior


# Knight
@pytest.fixture
def knight_no_bonus():
    war = Warrior("knight")
    war.weapon = "bow"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def knight_with_bonus():
    war = Warrior("knight")
    war.weapon = "sword"
    war.has_weapon_bonus = True
    return war


# Ranger
@pytest.fixture
def ranger_no_bonus():
    war = Warrior("ranger")
    war.weapon = "magic wand"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def ranger_with_bonus():
    war = Warrior("ranger")
    war.weapon = "bow"
    war.has_weapon_bonus = True
    return war


# Wizard
@pytest.fixture
def wizard_no_bonus():
    war = Warrior("wizard")
    war.weapon = "sword"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def wizard_with_bonus():
    war = Warrior("wizard")
    war.weapon = "magic wand"
    war.has_weapon_bonus = True
    return war


# Bard
@pytest.fixture
def bard_no_bonus():
    war = Warrior("bard")
    war.weapon = "sword"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def bard_with_bonus():
    war = Warrior("bard")
    war.weapon = "lute"
    war.has_weapon_bonus = True
    return war


# Rogue
@pytest.fixture
def rogue_no_bonus():
    war = Warrior("rogue")
    war.weapon = "sword"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def rogue_with_bonus():
    war = Warrior("rogue")
    war.weapon = "dagger"
    war.has_weapon_bonus = True
    return war


# Psychic
@pytest.fixture
def psychic_no_bonus():
    war = Warrior("psychic")
    war.weapon = "sword"
    war.has_weapon_bonus = False
    return war


@pytest.fixture
def psychic_with_bonus():
    war = Warrior("psychic")
    war.weapon = "crystal ball"
    war.has_weapon_bonus = True
    return war


'''# temp test
def test_basic_type_win1(knight_no_bonus, bard_no_bonus):
    # Knight (self) vs Bard (opponent) -> Knight wins
    assert knight_no_bonus.base_battle_outcome(bard_no_bonus) == "win"

def test_basic_type_lose(knight_no_bonus, bard_no_bonus):
    # Knight (self) vs Bard (opponent) -> Knight wins
    assert knight_no_bonus.base_battle_outcome(bard_no_bonus) == "win"'''


# Test cases for basic type advantages (no weapon bonuses involved initially)
def test_basic_type_win(knight_no_bonus, ranger_no_bonus, bard_no_bonus):
    # Knight (self) vs Ranger (opponent) -> Knight wins
    assert knight_no_bonus.base_battle_outcome(ranger_no_bonus) == "win"
    assert knight_no_bonus.base_battle_outcome(bard_no_bonus) == "win"


def test_basic_type_lose(knight_no_bonus, wizard_no_bonus, psychic_no_bonus):
    # Knight (self) vs Wizard (opponent) -> Knight loses
    assert knight_no_bonus.base_battle_outcome(wizard_no_bonus) == "lose"
    assert knight_no_bonus.base_battle_outcome(psychic_no_bonus) == "lose"


def test_basic_type_draw(knight_no_bonus):
    # Knight (self) vs Knight (opponent) -> Draw
    assert knight_no_bonus.base_battle_outcome(knight_no_bonus) == "draw"


# Test cases for weapon bonus effects
def test_self_bonus_overcomes_lose(knight_with_bonus, wizard_no_bonus):
    # Knight (self, bonus) vs Wizard (opponent, no bonus)
    # Base: Knight loses to Wizard. With self bonus, Knight wins.
    assert knight_with_bonus.base_battle_outcome(wizard_no_bonus) == "win"


def test_self_bonus_overcomes_draw(knight_with_bonus, knight_no_bonus):
    # Knight (self, bonus) vs Knight (opponent, no bonus)
    # Base: Draw. With self bonus, Knight wins.
    assert knight_with_bonus.base_battle_outcome(knight_no_bonus) == "win"


def test_opponent_bonus_overcomes_win(knight_no_bonus, ranger_with_bonus):
    # Knight (self, no bonus) vs Ranger (opponent, bonus)
    # Base: Knight wins against Ranger. With opponent bonus, Knight loses.
    assert knight_no_bonus.base_battle_outcome(ranger_with_bonus) == "lose"


def test_opponent_bonus_overcomes_draw(knight_no_bonus, knight_with_bonus):
    # Knight (self, no bonus) vs Knight (opponent, bonus)
    # Base: Draw. With opponent bonus, Knight loses.
    assert knight_no_bonus.base_battle_outcome(knight_with_bonus) == "lose"


def test_both_have_bonus_win(knight_with_bonus, ranger_with_bonus):
    # Knight (self, bonus) vs Ranger (opponent, bonus)
    # Base: Knight wins. Both have bonus, so base outcome stands.
    assert knight_with_bonus.base_battle_outcome(ranger_with_bonus) == "win"


def test_both_have_bonus_lose(knight_with_bonus, wizard_with_bonus):
    # Knight (self, bonus) vs Wizard (opponent, bonus)
    # Base: Knight loses. Both have bonus, so base outcome stands.
    assert knight_with_bonus.base_battle_outcome(wizard_with_bonus) == "lose"


def test_both_have_bonus_draw(knight_with_bonus):
    # Knight (self, bonus) vs Knight (opponent, bonus)
    # Base: Draw. Both have bonus, so base outcome stands.
    opponent_knight = Warrior("knight")
    opponent_knight.weapon = "sword"
    opponent_knight.has_weapon_bonus = True

    assert knight_with_bonus.base_battle_outcome(opponent_knight) == "draw"


def test_no_bonuses_win(knight_no_bonus, ranger_no_bonus):
    # Knight (self, no bonus) vs Ranger (opponent, no bonus)
    # Base: Knight wins. No bonuses, so base outcome stands.
    assert knight_no_bonus.base_battle_outcome(ranger_no_bonus) == "win"


def test_no_bonuses_lose(knight_no_bonus, wizard_no_bonus):
    # Knight (self, no bonus) vs Wizard (opponent, no bonus)
    # Base: Knight loses. No bonuses, so base outcome stands.
    assert knight_no_bonus.base_battle_outcome(wizard_no_bonus) == "lose"


def test_no_bonuses_draw(knight_no_bonus):
    # Knight (self, no bonus) vs Knight (opponent, no bonus)
    # Base: Draw. No bonuses, so base outcome stands.
    assert knight_no_bonus.base_battle_outcome(knight_no_bonus) == "draw"


# Test case for TypeError
def test_base_battle_outcome_type_error(knight_no_bonus):
    with pytest.raises(TypeError, match="Opponent must be a Warrior instance."):
        knight_no_bonus.base_battle_outcome("not a warrior")


def test_base_battle_outcome_type_error_with_number(knight_no_bonus):
    with pytest.raises(TypeError, match="Opponent must be a Warrior instance."):
        knight_no_bonus.base_battle_outcome(123)
