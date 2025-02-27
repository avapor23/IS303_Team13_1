#Play the game receiving both team names. Generate random scores without ties. Return W or L.
#Rebekah Lingen


def task4() :
    #prep for randomly generated scores
    import random

    #create dictionary
    dScores = {}

    #initialize variables
    iTotalWins = 0

    #ask the team name and total games they played
    sTeam = input("\nWhat is the name of your home team? ")
    iTotalGames = int(input("\nHow many games did " + sTeam + " play? "))
    
    #loop for each game the home team plays
    for iCount in range(iTotalGames) :
        sOpponent = input(f"Enter the name of away team for game {iCount+1}: ")

        #initialize the scores and set them equal to each other temporarily
        iHomeTeamScore = 0
        iOpponentTeamScore = 0

        #randomly generate score, using a loop to make sure there is NO tie
        while iHomeTeamScore == iOpponentTeamScore :
            #randomly generate scores between 0 and 12
            iHomeTeamScore = random.randrange(0,12)
            iOpponentTeamScore = random.randrange(0,12)

        #determine if the home team won or loss the game
        if iOpponentTeamScore > iHomeTeamScore :
            sResult = "L"
        else :
            sResult = "W"

        #store all of the data in the dictionary
        dScores[iCount] = [sTeam,iHomeTeamScore,sOpponent,iOpponentTeamScore,sResult]
    return dScores
