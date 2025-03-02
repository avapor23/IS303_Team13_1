'''
Rebekah Lingen
Section 004: P2
02 / 27 / 2025

TASK 4:
Play the game receiving both team names. Generate random scores without ties. Return W or L.
'''

#prep for randomly generated scores
import random

def generateScores(sTeam, sOpponent) :
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
        print(f"\nYou Lost!")
    else :
        sResult = "W"
        print(f"\nYou Win!")

    print(f"{sTeam}'s score : {iHomeTeamScore} | {sOpponent}'s score : {iOpponentTeamScore}")
    #return all of the data in the form of a list
    return [sTeam,iHomeTeamScore,sOpponent,iOpponentTeamScore,sResult]
