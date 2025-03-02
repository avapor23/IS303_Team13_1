'''
Ava Porter
Section 004: P2
02 / 27 / 2025

TASK 3:
Function that:
    1. Determines if a team has already been selected or not
    2. Creates a list of available teams the user can select from
    3. Determines what team the user has selected and return it

NOTE: in order to get the function to NOT include a previously selected team, you must pass the variable that contains that team name THROUGH the function
    Example: selectTeams("Brigham Young University")
    ^ the list generated from that line of code above WILL NOT INCLUDE Brigham Young University
'''

# Initialize List of Available Teams
allSeasonTeams = ["Brigham Young University", "Utah State University", "Utah Valley University", "University of Utah"]

def selectTeams(availableTeams=allSeasonTeams) :
    # ^^In the case no perameter is passed through the fuction, no team has been selected previously and all options are available
    teamOptions = availableTeams

    # Display Available Teams in List
    print("\n\nAvailable Teams to Select: ")
    for count in range(0, len(teamOptions)):
        print(f"{count + 1}. {teamOptions[count]}")

    # Gets user selection for team w/ error handling
    while True:
        try:
            teamSelection = int(input("\nPlease select a team by inputting an integer from the available options: ")) - 1
            if teamSelection <= -1 :
                print("Invalid input. Please input a number from the available options.")
            else :
                pickedTeam = teamOptions.pop(teamSelection)
                return [pickedTeam, teamOptions]
        except:
            print("Invalid input. Please input a number from the available options.")