# Cora Longhurst
#Section 004
# P2


def display_intro():
    """
    Displays an introduction to the game, explains the rules,
    prompts the user for their name, and returns it.
    """
    print("Welcome to the Women's Soccer Season Simulator!")
    print("In this game, you will play through a season of women's soccer matches.")
    print("Your choices and strategies will impact the outcomes of the games!")
    print("Let's get started!\n")
    
    # Prompt for player's name
    player_name = input("Enter your name: ")
    print(f"\nWelcome, {player_name}! Get ready for an exciting season!\n")
    
    return player_name

if __name__ == "__main__":
    player_name = display_intro()
