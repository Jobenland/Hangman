#!/usr/bin/env python

'''
Simple hangman game with highscore feature for INST 126 Final Project
'''

__author__ = "Jonathan Obenland and Andrew Knox"
__copyright__ = None
__credits__ = ["Jonathan Obenland","Andrew Knox"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Jonathan Obenland and Andrew Knox"
__email__ = "jobenland1@gmail.com, amknox5@gmail.com"
__status__ = "Production"

#imports
import time
import json
from random import randint


#main menu for the program
def welcome():

    print("Welcome to Hangman")
    print("--------------")
    print("|    Menu    |")
    print("--------------\n")
    print("1 >>>> Start Game")
    print("2 >>>> High Score\n")

    #makes call to the option menu
    menu()

#main selection portion for the main menu
#keeps on running in case someone selected a wrong option
def menu():

    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            gameStart()
            break
        if choice == "2":
            findHighScores()
            break
        else:
            print(choice, "was not a valid option! try agian...")

def gameStart():
    
    score = {}

    attempt = 0

    f = open('wordlist.txt','r')
    data_list = f.readlines()
    f.close()

    data_list = [word.strip() for word in data_list]

    wordLoc = randint(0,49)

    word = data_list[wordLoc]

    blanks = []
    guesses = []

    for letter in word:
        blanks.append('_ ')

    name = input("Enter your Name: ")
    print('')
    print("".join(blanks))
    print('\n')
    print("Game starts in 3")
    time.sleep(1)
    print("Game starts in 2")
    time.sleep(1)
    print("Game starts in 1")
    time.sleep(1)
    print("GO! The timer has started! start guessing!")

    start_time = time.time()

    while True:
        if attempt == 20:
            finalTime = round(time.time()-start_time,5)
            print("GAME OVER! you attempted 10 times")
            print("The correct word was", word)
            print("your total time was", finalTime,"seconds")
            break
        
        print("This is attempt number",attempt+1)
        print("You have guessed",guesses)
        guess = input("Guess a letter: ")
        print('')
        guesses.append(guess)
        attempt+=1
        
        if len(guess)==1:
            for letter in range(len(word)):
                if guess == word[letter]:
                    blanks[letter] = guess + " "
            print(''.join(blanks))
            print('')

        elif len(guess)>1:
            if guess == word:
                finalTime = round(time.time()-start_time,5)
                print("YOU WIN!")
                print("your total time was", finalTime,"seconds")
                passRound = True
                score = {'name': name,'time' : finalTime, 'attempts' : attempt, 'word' : word, 'pass' : passRound}
                highScores(score)
                break
                
        checkwin = (''.join(blanks).replace(' ',''))
        if checkwin == word:
            finalTime = round(time.time()-start_time,5)
            print("YOU WIN!")
            print("your total time was", finalTime,"seconds")
            passRound = True
            score = {'name' : name, 'time' : finalTime, 'attempts' : attempt, 'word' : word, 'pass' : passRound}
            highScores(score)
            break

#this function will add the user high score to the JSON file 
def highScores(score):
    
    #this will open the file and read the dictionary in as list to add the score
    #this is necessary otherwise data coming in would overwrite existing data
    try:
        with open ("highscores.json") as f:
            data = json.load(f)

        if type(data) is dict:
            data = [data]
            data.append(score)

        with open ("highscores.json","w") as f:
            json.dump(data, f)

    #if the file isnt found and it is the first time playing, it will create a new file and add the player to it
    except FileNotFoundError:
        print("Since this is your first time playing, a high score file has been created for you")

        with open ("highscores.json",'w') as f:
            json.dump(score, f)

#this function will find the highscore of the already existing highscore JSON list
def findHighScores():
    try:

        #reads the json object into memory
        highscorestime = []
        highplayer = []
        with open('highscores.json',"r",encoding="utf8") as json_file:
            data = json_file.read() 
        obj = json.loads(data)

        #adds the time to an array and finds the MIN
        #as that would be the "highest score"
        for player in range(len(obj)):
            time = obj[player]['time']
            highscorestime.append(time)
            player = obj[player]['name']
            highplayer.append(player)

        #print(highplayer[(highscorestime.index(min(highscorestime)))])
        print((highplayer[(highscorestime.index(min(highscorestime)))]),"------",min(highscorestime),"seconds")

    #if user has no games yet, it will print this placeholder
    except FileNotFoundError:
        print("You have no highscore games yet, Start the game to autogenerate the high score file")

#>>start the program
welcome()
