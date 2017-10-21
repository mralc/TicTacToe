#
import os
won = "Flase"
grid=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
tictactoe=["-","-","-","-","-","-","-","-","-"]
Player="X"
os.system('clear')
while won == "Flase":
    os.system('clear')
    print ("   1   2   3 ")
    print ("A ",tictactoe[0],"|",tictactoe[1],"|",tictactoe[2])
    print ("   ----------")
    print ("B ",tictactoe[3],"|",tictactoe[4],"|",tictactoe[5])
    print ("   ----------")
    print ("C ",tictactoe[6],"|",tictactoe[7],"|",tictactoe[8])
    print ("")
    row = input("Player " + Player + " chose row:")
    column= input("Player " + Player + " chose column:")
    row = row.capitalize()
    choice = row + column
    Gridlocation = grid.index(choice)
    choicevaule = (tictactoe[Gridlocation])
    if choicevaule == "-":
            tictactoe[Gridlocation]=Player
    else:
            print ("This Postion is already taken chose again")
            input("Press Enter to chose anoter Postion continue...")
            continue

    if tictactoe[0] == Player and tictactoe[1] == Player and tictactoe[2] == Player:

            won = "Ture"

    if tictactoe[3] == Player and tictactoe[4] == Player and tictactoe[5] == Player:

            won = "Ture"
    if tictactoe[6] == Player and tictactoe[7] == Player and tictactoe[8] == Player:

            won = "Ture"
    if tictactoe[0] == Player and tictactoe[3] == Player and tictactoe[6] == Player:

            won = "Ture"

    if tictactoe[1] == Player and tictactoe[4] == Player and tictactoe[7] == Player:

            won = "Ture"

    if tictactoe[2] == Player and tictactoe[5] == Player and tictactoe[8] == Player:

            won = "Ture"

    if tictactoe[0] == Player and tictactoe[4] == Player and tictactoe[8] == Player:

            won = "Ture"

    if tictactoe[2] == Player and tictactoe[4] == Player and tictactoe[6] == Player:
            won = "Ture"
    if not "-" in tictactoe:
            stale = "yes"
            won = "Ture"
    else:
            stale = "not"
            if Player == "O":
                    Player="X"
            else:
                    Player="O"
    os.system('clear')

if Player == "O":
        Player="X"
else:
        Player="O"

print ("   1   2   3 ")
print ("A ",tictactoe[0],"|",tictactoe[1],"|",tictactoe[2])
print ("   ----------")
print ("B ",tictactoe[3],"|",tictactoe[4],"|",tictactoe[5])
print ("   ----------")
print ("C ",tictactoe[6],"|",tictactoe[7],"|",tictactoe[8])
print ("")
if not stale == "yes":
    print ("Player",Player,"Has Won")
else:
    print ("No one won!")
