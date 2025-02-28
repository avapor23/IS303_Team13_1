# Chloe DePierro
# Function 5
# Receives the home team data, displays results of each game, final season record, and final statement

def FinalRecord(iTotalGames,dScores):
    #print the results for each game
    for iCount in range(iTotalGames) : 
        #display each game's scores
        print(f"{dScores[iCount][0]}'s score : {dScores[iCount][1]} | {dScores[iCount][2]}'s score : {dScores[iCount][3]}")

        #determine the home team's total wins
        if dScores[iCount][4] == "W" :
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
        

