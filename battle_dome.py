from enum import Enum
import random
from character_map import WARRIOR_LOGIC


# ALL_TYPES is a tuple of all the warrior type options given to the user.
from Warrior import Warrior, ALL_TYPES


# Enum of outcome options
class Outcome(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"


# Users play record
player_record: dict = {"win": 0, "draw": 0, "lose": 0}


def main():

    play_again: bool = True
    while play_again:  # Outer loop for playing multiple rounds

        user = Warrior.get_warrior()
        # Create a randomly generated Warrior
        opponent: Warrior = Warrior(random.choice(ALL_TYPES))

        # Alert the user to what their match up will be
        print(
            f"\nYour warrior is a {user.type} and is equipped with {user.weapon}. Your armor is {user.armor} and total power is {user.weapon_bonus + user.armor_bonus}\n"
            f"You will be fighting a {opponent.type} equipped with {opponent.weapon} Your armor is {opponent.armor} and total power is {opponent.weapon_bonus + opponent.armor_bonus}.\n"
        )

        print(user)
        print(opponent)
        # Phase 1: Type Advantage Stare Down
        stare_down_outcome = stare_down(user, opponent)
        print(f"\nType Advantage Phase: {stare_down_outcome.name}")
        
        # Phase 2: Bonus Battle
        battle_outcome = battle(user, opponent, stare_down_outcome)
        print(f"Battle Phase: {battle_outcome.name}")

        # Phase 3: Last Chance Victory (Only if you didn't win outright)
        if battle_outcome in (Outcome.LOSE, Outcome.DRAW):
            # Pass the enum directly, and reassign the enum directly
            battle_outcome = last_chance_victory(battle_outcome)
            print(f"\nFinal Outcome after the Holy Grail: {battle_outcome.name}")

        # Record update (outside of any battle loops)
        player_record[battle_outcome.value] += 1
        print(
            f"\nYour record is Wins: {player_record['win']} Draws: {player_record['draw']} Losses: {player_record['lose']}"
        )

        # Ask player if they want to play again
        while True:  # Loop for play again prompt
            try:
                answer = input("Would you like to play again? (y/n) ").strip().lower()
                if answer == "y":
                    break  # Break inner loop, main loop continues
                elif answer == "n":
                    print("Thanks for playing!")
                    play_again = False  # Set flag to exit main loop
                    break  # Break inner loop
                else:
                    raise ValueError
            except ValueError:
                print("Please enter only 'y' or 'n'")


def last_chance_victory(outcome: Outcome) -> Outcome:
    # Generate a randomly selected number 1-10
    holy_grail = random.randint(1, 10)
    
    print(
        r"""
  .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.    .--.
 (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )  (    )
  \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /    \  /
   \/      \/      \/      \/      \/      \/      \/      \/      \/      \/
  _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_    _||_
 (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)  (____)
   1       2       3       4       5       6       7       8       9       10
          """
    )
    
    print("\nThe Holy Grail has chosen a number between 1 and 10!")

    match outcome:
        case Outcome.WIN:
            print("Your opponent gets a chance to steal the victory!")
            # Corrected to match the 1-10 range of the holy_grail
            opponent_guess = random.randint(1, 10)
            print(f"Opponent guessed: {opponent_guess}")
            
            if opponent_guess == holy_grail:
                print("The opponent guessed correctly and stole the win!")
                return Outcome.LOSE
            else:
                print(f"The opponent guessed incorrectly (Grail was {holy_grail}). Your victory stands!")
                return Outcome.WIN
                
        case Outcome.LOSE:
            print("You have one last chance to steal the victory!")
            while True:
                try:
                    user_guess = int(input("Pick a number between 1 and 10: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    
            if user_guess == holy_grail:
                print("You guessed correctly and stole the win!")
                return Outcome.WIN
            else:
                print(f"You guessed incorrectly (Grail was {holy_grail}). You lose!")
                return Outcome.LOSE
                
        case Outcome.DRAW:
            print("It's a draw! Whoever guesses closest to the Holy Grail wins.")
            opponent_guess = random.randint(1, 10)
            
            while True:
                try:
                    user_guess = int(input("Pick a number between 1 and 10: "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
                    
            print(f"Opponent guessed: {opponent_guess}")
            print(f"The Holy Grail number was: {holy_grail}")
            
            # Calculate who is closer using absolute difference
            user_diff = abs(user_guess - holy_grail)
            opponent_diff = abs(opponent_guess - holy_grail)
            
            if user_diff < opponent_diff:
                print("You were closer! You win!")
                return Outcome.WIN
            elif opponent_diff < user_diff:
                print("The opponent was closer! You lose!")
                return Outcome.LOSE
            else:
                print("You both guessed equally close! It remains a true draw!")
                return Outcome.DRAW


# Compare warriors to see what the type advantage is.
def stare_down(user_warrior: Warrior, opponent_warrior: Warrior) -> Outcome:
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
    # Create a dictionary mapping each warrior type to the types it has an advantage over.
    # This is derived from the global WARRIOR_LOGIC.
    TYPE_ADVANTAGE = {
        warrior_type: details["type_advantage"]
        for warrior_type, details in WARRIOR_LOGIC.items()
    }
    # Check if the opponent's warrior type is in the user's warrior's advantage list.
    if opponent_warrior.type in TYPE_ADVANTAGE.get(user_warrior.type, ()):
        return Outcome.WIN
    # Check if the user's warrior type is in the opponent's warrior's advantage list.
    elif user_warrior.type in TYPE_ADVANTAGE.get(opponent_warrior.type, ()):
        return Outcome.LOSE
    # If neither has a direct type advantage, it's a draw.
    else:
        return Outcome.DRAW


# Check for weapons vs armor bonus of the previous phases victor.
def battle(
    user_warrior: Warrior, opponent_warrior: Warrior, outcome: Outcome
) -> Outcome:
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
            if user_warrior.weapon_bonus > opponent_warrior.armor_bonus:
                return Outcome.WIN
            elif user_warrior.weapon_bonus < opponent_warrior.armor_bonus:
                return Outcome.LOSE
            else:
                return Outcome.DRAW

        case Outcome.LOSE:
            # If user lost the previous phase, compare opponent's weapon bonus against user's armor bonus.
            if opponent_warrior.weapon_bonus > user_warrior.armor_bonus:
                return Outcome.LOSE
            elif opponent_warrior.weapon_bonus < user_warrior.armor_bonus:
                return Outcome.WIN
            else:
                return Outcome.DRAW

        case Outcome.DRAW:
            # If the previous phase was a draw, compare the total combined bonuses (weapon + armor) of both warriors.
            if (
                opponent_warrior.weapon_bonus + opponent_warrior.armor_bonus
                > user_warrior.weapon_bonus + user_warrior.armor_bonus
            ):
                return Outcome.LOSE
            elif (
                opponent_warrior.weapon_bonus + opponent_warrior.armor_bonus
                < user_warrior.weapon_bonus + user_warrior.armor_bonus
            ):
                return Outcome.WIN
            else:
                return Outcome.DRAW



if __name__ == "__main__":
    main()
