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
import random


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
    
    #Andrew
    #needs to store...
    #   attempts
    #   time
    #   num Incorrect
    #   prompt for name
    #   word
    #   print letters already guessed

    attempts = 0
    num_incorrect = 0
    limit = 10
    wordlist = []
    display = []
    letters_guessed = []

    with open('wordlist.txt') as fh:
        for line in fh:
            wordlist.append(line.rstrip('\n'))
        fh.close()

    word = random.choice(wordlist)

    for i in range(0,len(word)):
        display.append('_ ')
    
    name = input('Enter you name: ')
    print('The game starts now! Start guessing!')
    start_time = time.time()
            

    while num_incorrect < limit:
        
        if '_ ' not in display:
            final_time = time.time() - start_time
            print('Correct! You finished with ' + str(attempts) + ' attempts with ' + str(num_incorrect) + ' of them being incorrect in ' + str(final_time) + ' seconds.')
            score = {'name' : name, 'time' : final_time, 'attempts' : attempts, 'word' : word, 'pass' : True}
            highScores(score)
            break

        print('This is attempt number ' + str(attempts))
        print('The letters you have guessed are ', letters_guessed)
        print(''.join(display))

        guess = input('Guess the word or a letter: ')

        if len(guess) == 0:
            print('You did not make a guess! Try again!')

        elif len(guess) > 1:
            if guess == word:
                attempts += 1
                final_time = time.time() - start_time
                print("Correct! You finished with " + str(attempts) + " attempts with " + str(num_incorrect) + " of them being incorrect in " + str(time.time() - start_time) + " seconds.")
                score = {'name' : name, 'time' : final_time, 'attempts' : attempts, 'word' : word, 'pass' : True}
                highScores(score)
                break
            else:
                num_incorrect += 1
                attempts += 1
                print("Incorrect! You have " + str(limit - num_incorrect) + " attempts left.")
        elif len(guess) == 1:
            if guess.lower() in letters_guessed:
                    print('You already guessed ' + str(guess) + '! Try again!')
            elif guess.lower() in word:
                attempts += 1
                letters_guessed.append(guess)
                for letter in range(0,len(word)):
                    if guess == word[letter]:
                        display[letter] = guess + ' '
                print(''.join(display))
            else:
                attempts += 1
                letters_guessed.append(guess)
                num_incorrect += 1

    if num_incorrect >= limit:
        print('GAME OVER! You got too many wrong!')
        print('The correct word was ' + word + '.')
        print('Your total time was ' + str(time.time() - start_time) + ' seconds.')

#this function will add the user high score to the JSON file 
def highScores(score):
    
    #this will open the file and read the dictionary in as list to add the score
    #this is necessary otherwise data coming in would overwrite existing data
    try:
        with open ("highscores.json") as f:
            data = json.load(f)

        if type(score) is dict:
            data.append(score)

        with open ("highscores.json","w") as f:
            json.dump(data, f)

    #if the file isnt found and it is the first time playing, it will create a new file and add the player to it
    except FileNotFoundError:
        print("Since this is your first time playing, a high score file has been created for you")

        if type(score) is dict:
            data = [score]

        with open ("highscores.json",'w') as f:
            json.dump(data, f)
    
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
