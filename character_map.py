# Type advantages for warriors
WARRIOR_LOGIC = {
    "knight": {
        "type_advantage": ("bard", "ranger"),
        "weapon_bonus": "sword",
        "armor_bonus": "Suit of Armor",
        "skill_bonus": "Hand to hand",
    },
    "ranger": {
        "type_advantage": ("rogue", "wizard"),
        "weapon_bonus": "bow",
        "armor_bonus": "Leather Tunic",
        "skill_bonus": "Long range Combat",
    },
    "wizard": {
        "type_advantage": ("psychic", "knight"),
        "weapon_bonus": "magic wand",
        "armor_bonus": "Magic Robes",
        "skill_bonus": "Magic",
    },
    "bard": {
        "type_advantage": ("rogue", "ranger"),
        "weapon_bonus": "lute",
        "armor_bonus": "Fine Clothes",
        "skill_bonus": "Persuasion",
    },
    "rogue": {
        "type_advantage": ("psychic", "wizard"),
        "weapon_bonus": "dagger",
        "armor_bonus": "Hooded Cloak",
        "skill_bonus": "Stealth",
    },
    "psychic": {
        "type_advantage": ("bard", "knight"),
        "weapon_bonus": "crystal Ball",
        "armor_bonus": "Clairvoyant Shawl",
        "skill_bonus": "Clairvoyance",
    },
    "naked man": {
        #TODO finish this char map
        "type_advantage": ("bard", "knight"),
        "weapon_bonus": "Empty Handed",
        "armor_bonus": "Nudity",
        "skill_bonus": "The naked man",
    },
}
