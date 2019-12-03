import time
import json
from random import randint



def welcome():

    print("Welcome to Hangman")
    print("--------------")
    print("|    Menu    |")
    print("--------------\n")
    print("1 >>>> Start Game")
    print("2 >>>> High Score\n")
    menu()

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
    print("".join(blanks))

    name = input("Enter your Name: ")
    print("The timer has started! start guessing!")

    start_time = time.time()

    while True:
        if attempt == 10:
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


        



    #score={}
    #time = 57
    #attempts = 77
    #scoreName = input("Congrats!, Enter your name: ")
    #score[scoreName] = {'time' : time, 'attempts' : attempts}
    #highScores(score)
def highScores(score):
    #Jonathan
    try:
        with open ("highscores.json") as f:
            data = json.load(f)

        if type(data) is dict:
            data = [data]
            data.append(score)

        with open ("highscores.json","w") as f:
            json.dump(data, f)

    except FileNotFoundError:
        print("Since this is your first time playing, a high score file has been created for you")

        with open ("highscores.json",'w') as f:
            json.dump(score, f)

def findHighScores():
    try:
        highscorestime = []
        highplayer = []
        with open('highscores.json',"r",encoding="utf8") as json_file:
            data = json_file.read() 
        obj = json.loads(data)1

        for player in range(len(obj)):
            time = obj[player]['time']
            highscorestime.append(time)
            player = obj[player]['name']
            highplayer.append(player)

        #print(highplayer[(highscorestime.index(min(highscorestime)))])
        print((highplayer[(highscorestime.index(min(highscorestime)))]),"won with a time of",min(highscorestime))
    except FileNotFoundError:
        print("You have no highscore games yet, Start the game to autogenerate the high score file")





welcome()
