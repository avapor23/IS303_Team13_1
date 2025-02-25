# Narissa (Ungrangsee) Broderick
# This function displays a menu and return choice. Stores in variable and uses this value to determine which function to call next.

def displayMenu():
    while True:
        print('\nMenu:')
        print(f"1. Play a game.")
        print(f"2. View final record.")
        print(f"3. Quit.")

        try:
            choice = int(input(f"\nEnter your choice (1-3): "))
            if choice in [1,2,3]:
                return choice
            else:
                print('\nInvalid choice. Pleases enter 1, 2, or 3.')
        except ValueError:
            print("\nInvalid input. Please enter a number (1, 2, or 3).")

displayMenu()