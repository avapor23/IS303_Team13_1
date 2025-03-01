'''
Michelle Johanson
Section 004: P2
02 / 28 / 2025

This program plays the womens soccer season as defined in Assignment 4, using at least 5 functions.
'''

from function1 import * # displayIntro()
from function2 import * # displayMenu()
from function3 import * # selectTeams(sHomeTeam)
from function4 import * # generateScores()
from function5 import * # finalRecord(iTotalGames, dScores)

# Initialize Dictionary
dictGameResults = {}

# Introduces the game and sets the player name
playerName = displayIntro()
print("\nFirst, let's pick your home team!")
homeTeam = selectTeams()
totalGameCount = 0

# Displays options for player to pick from
#  1. Play a game.
#  2. View final record.
#  3. Quit.
nextAction = displayMenu()

# Runs through options until user decides to quit the game
while nextAction != 3 :
    if nextAction == 1 :
        print("Who are you playing against?")
        awayTeam = selectTeams(homeTeam)
        dictGameResults[homeTeam] = generateScores(homeTeam, awayTeam)
        totalGameCount += 1
    if nextAction == 2 :
        finalRecord(totalGameCount, dictGameResults)
    nextAction = displayMenu()

print(f"Goodbye, {playerName}!")