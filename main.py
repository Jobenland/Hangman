import time
import json



def welcome():

    print("Welcome to Hangman")
    print("--------------")
    print("|    Menu    |")
    print("--------------\n")
    print("1 >>>> Start Game")
    print("2 >>>> High Scores\n")
    menu()

def menu():

    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            gameStart()
            break
        if choice == "2":
            highScores()
            break
        else:
            print(choice, "was not a valid option! try agian...")

def gameStart():
    #Andrew
    #needs to store...
    #   attempts
    #   time
    #   num Incorrect
    print("code here")
    score={}
    time = 57
    attempts = 77
    scoreName = input("Congrats!, Enter your name: ")
    score[scoreName] = {'time' : time, 'attempts' : attempts}
    highScores(score)

def highScores(score):
    #Jonathan
    try:
        with open ("highscores.json") as f:
            data = json.load(f)

        data.update(score)

        with open ("highscores.json","w") as f:
            json.dump(data, f)

    except FileNotFoundError:
        print("Since this is your first time playing, a high score file has been created for you")

        with open ("highscores.json",'w') as f:
            json.dump(score, f)

    print("file")

welcome()
