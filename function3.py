#Ava Porter
#Function 3

#Function that:
# 1. Determines if a team has already been selected or not
# 2. Creates a list of available teams the user can select from
# 3. Determines what team the user has selected and return it

#note: in order to get the function to NOT include a previously selected team, you must pass the variable that contains that team name THROUGH the function
#example: selectTeams("Brigham Young University")
#the list generated from that line of code above WILL NOT INCLUDE Brigham Young University



def selectTeams(parameter=None) : #parameter=None is there in case no parameter is passed through the function, meaning no team has been selected previously

    #determine if a home team has been selected or not and generate the list of available teams
    if parameter is None:
        #no home team has been selected, so we need the full list
        dAvailableTeams = {1: "Brigham Young University", 2: "Utah State University", 3: "Utah Valley University", 4: "University of Utah"}
    else:
        #a home team has been selected, so we need to modify the list
        if parameter == "Brigham Young University" :
            dAvailableTeams = {2: "Utah State University", 3: "Utah Valley University", 4: "University of Utah"}
        elif parameter == "Utah State University" :
            dAvailableTeams = {1: "Brigham Young University", 3: "Utah Valley University", 4: "University of Utah"}
        elif parameter == "Utah Valley University" :
            dAvailableTeams = {1: "Brigham Young University", 2: "Utah State University", 4: "University of Utah"}
        elif parameter == "University of Utah" :
            dAvailableTeams = {1: "Brigham Young University", 2: "Utah State University",3: "Utah Valley University"}
    
    #display the menu
    print("\n\nAvailable Teams to Select: ")
    for key in dAvailableTeams:
        print(f"{key}. {dAvailableTeams[key]}")
    
    #loop until the user gives a valid input
    while True:
        try:
            iSelection = int(input("\nPlease select a team by inputting an integer from the available options: "))
            if iSelection in dAvailableTeams: #the user selected an available team
                return dAvailableTeams[iSelection]
            else: #the user input a number not available in the dictionary
                print("Invalid input. Please input a number from the available options.")
        except: #the user did not put in an integer
            print("Invalid input. Please input an integer.")