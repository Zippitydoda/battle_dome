from enum import Enum


class char_type(Enum):
    CHAR_1 = "knight"
    CHAR_2 = "ranger"
    CHAR_3 = "wizard"
    CHAR_4 = "bard"
    CHAR_5 = "rouge"
    CHAR_6 = "psychic"


# Type advantages for warriors
WARRIOR_LOGIC = {
    char_type.CHAR_1.value: {
        "type_advantage": (char_type.CHAR_4.value, char_type.CHAR_2.value),
        "weapon_bonus": "sword",
        "armor_bonus": "Suit of Armor",
        "skill_bonus": "Hand to hand",
    },
    char_type.CHAR_2.value: {
        "type_advantage": (char_type.CHAR_5.value, char_type.CHAR_3.value),
        "weapon_bonus": "bow",
        "armor_bonus": "Leather Tunic",
        "skill_bonus": "Long range Combat",
    },
    char_type.CHAR_3.value: {
        "type_advantage": (char_type.CHAR_6.value, char_type.CHAR_1.value),
        "weapon_bonus": "magic wand",
        "armor_bonus": "Magic Robes",
        "skill_bonus": "Magic",
    },
    char_type.CHAR_4.value: {
        "type_advantage": (char_type.CHAR_5.value, char_type.CHAR_2.value),
        "weapon_bonus": "lute",
        "armor_bonus": "Fine Clothes",
        "skill_bonus": "Persuasion",
    },
    char_type.CHAR_5.value: {
        "type_advantage": (char_type.CHAR_6.value, char_type.CHAR_3.value),
        "weapon_bonus": "dagger",
        "armor_bonus": "Hooded Cloak",
        "skill_bonus": "Stealth",
    },
    char_type.CHAR_6.value: {
        "type_advantage": (char_type.CHAR_4.value, char_type.CHAR_1.value),
        "weapon_bonus": "crystal Ball",
        "armor_bonus": "Clairvoyant Shawl",
        "skill_bonus": "Clairvoyance",
    },
    "naked man": {
        # TODO finish this char map
        "type_advantage": ("bard", "knight"),
        "weapon_bonus": "Empty Handed",
        "armor_bonus": "Nudity",
        "skill_bonus": "The naked man",
    },
}
