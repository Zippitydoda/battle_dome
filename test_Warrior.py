import pytest
from battle_game.warrior import Warrior, ALL_ARMORS, ALL_SKILLS, ALL_TYPES, ALL_WEAPONS
from battle_game.character_map import WARRIOR_LOGIC, char_type


@pytest.fixture
def create_knight_no_bonus():
    war = Warrior.random_warrior()
    war._type = char_type.CHAR_1.value
    war._weapon = ALL_WEAPONS
    war._armor = "Leather Tunic"
    war._has_weapon_bonus = False
    war._has_armor_bonus = False


@pytest.fixture
def create_ranger_no_bonus():
    war = Warrior.random_warrior()
    war._type = char_type.CHAR_2.value
    war._weapon = ALL_WEAPONS
    war._armor = "Leather Tunic"
    war._has_weapon_bonus = False
    war._has_armor_bonus = False
