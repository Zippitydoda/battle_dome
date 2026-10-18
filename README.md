# Battle Dome

Battle Dome is a text-based, terminal-run RPG battler written in Python. Players choose from a variety of warrior classes, equip randomly rolled gear, and face off against CPU-controlled opponents in the ultimate arena.

Combat resolution relies on a strategic mix of inherent type advantages (rock-paper-scissors style) and gear-based stat bonuses.

## Features

* **7 Unique Warrior Classes:** Each with specific type advantages over other classes.

* **Randomized Gear System:** Warriors are assigned a random weapon and armor upon creation. If the gear matches the warrior's class (e.g., a Knight wielding a Sword), they receive a high stat bonus. Mismatched gear results in medium bonuses, and "Naked Man" gear yields the lowest bonuses.

* **Multi-Phase Combat:**

  * **Stare Down:** Determines initial advantage based on class matchups.

  * **Battle:** Compares the advantaged player's attack stats against the disadvantaged player's defense stats.

* **Holy Grail Mechanic:** A "last-chance victory" mini-game that triggers on losses or draws, allowing players to guess a randomly generated number to overturn their fate.

* **Stat Tracking:** Keeps a running record of your Wins, Draws, and Losses throughout the session.

## Character Classes

The game features a rich `character_map` dictating who beats who:

* **Knight:** Beats Bard, Ranger (Weapon: Sword, Armor: Suit of Armor)

* **Ranger:** Beats Rogue, Wizard (Weapon: Bow, Armor: Leather Tunic)

* **Wizard:** Beats Psychic, Knight (Weapon: Magic Wand, Armor: Magic Robes)

* **Bard:** Beats Rogue, Ranger (Weapon: Lute, Armor: Fine Clothes)

* **Rogue:** Beats Psychic, Wizard (Weapon: Dagger, Armor: Hooded Cloak)

* **Psychic:** Beats Bard, Knight (Weapon: Crystal Ball, Armor: Clairvoyant Shawl)

* **Naked Man:** Beats Bard, Knight (Weapon: Empty Handed, Armor: Nudity)

## Project Structure

* `battle_dome.py`: The main executable file containing the game loop, battle logic, and the Holy Grail mini-game.

* `Warrior.py`: Contains the `Warrior` class, which handles character instantiation, random gear assignment, and bonus calculations.

* `character_map.py`: A configuration file containing the `WARRIOR_LOGIC` dictionary that maps type advantages and optimal gear for each class.

* `test_Warrior.py`: A Pytest suite containing unit tests to verify the integrity of the battle calculation logic.

## Requirements

* Python 3.10 or higher (The codebase utilizes Python's `match/case` syntax).

* `pytest` (Optional: only required if you want to run the test suite).

## How to Play

1. Clone or download the repository to your local machine.

2. Open your terminal and navigate to the project directory.

3. Run the main script:

   ```
   python battle_dome.py
   
   ```

4. Follow the on-screen prompts to select your warrior. The game will randomly generate your gear and your opponent, calculate the battle outcome, and ask if you'd like to play again.

## Running Tests

To run the automated tests and verify the combat logic, ensure you have `pytest` installed:

```
pip install pytest
pytest test_Warrior.py

```