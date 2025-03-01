'''
Narissa (Ungrangsee) Broderick
Section 004: P2
02 / 27 / 2025

TASK 2:
This function displays a menu and return choice. Stores in variable and uses this value to determine which function to call next.
'''

def displayMenu():
    while True:
        # Displays menu options
        print('\nMenu:')
        print(f"1. Play a game.")
        print(f"2. View final record.")
        print(f"3. Quit.")

        # Takes user input w/ error handling
        try:
            choice = int(input(f"\nEnter your choice (1-3): "))
            if choice in [1,2,3]:
                return choice
            else:
                print('\nInvalid choice. Pleases enter 1, 2, or 3.')
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 3.")