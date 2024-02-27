# Market System
import RockPaperScissors
import TextAdventureSACCDS_v2 as t

def Lobby():
    i = input("Do you want to go to the basement or attic or exit?")
    if i == "basement":
        t.WelcomeStatements1()

    elif i =="attic":
        RockPaperScissors.start()

    else:
        exit()

Lobby()
