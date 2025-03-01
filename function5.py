'''
Chloe DePierro
Section 004: P2
02 / 28 / 2025

TASK 5:
Receives the home team data, displays results of each game, final season record, and final statement
'''

def finalRecord(iTotalGames,dScores):
    #print the results for each game
    for game in dScores : 
        #display each game's scores
        print(f"{dScores[game][0]}'s score : {dScores[game][1]} | {dScores[game][2]}'s score : {dScores[game][3]}")

        # initialize variable
        iTotalWins = 0

        #determine the home team's total wins
        if dScores[game][4] == "W" :
            iTotalWins = iTotalWins + 1

    #print the team final season record
    print(f"\nFinal season record: {iTotalWins}-{iTotalGames - iTotalWins}\n")

    #determine final season statement based on team total wins
    iPercentWins = (iTotalWins/iTotalGames) * 100

    if iPercentWins >= 75 :
        print("Qualified for the NCAA Women's Soccer Tournament.")
    elif iPercentWins >= 50 :
        print("You had a good season.")
    else:
        print("Your team needs to practice!")


