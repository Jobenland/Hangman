# Hangman Game

This is a cli recreation of the popular game `hangman` with slight modifications to make it more user friendly. This game also stores user highscores in a seperate file that can be used to look up past high scores

## Getting Started

Simply running `python main.py` or `python3 main.py` in the directory will start the game

### Prerequisites

Programs and other things needed to run this program
```
Python 3.x
Pip
```

### Installing

Because this game is fairly simple the only libraries that are used are already installed with python
```
random
time
json
math
```
If you are having problems related to libraries, you can try to reinstall the other ones
`pip install <package name>`
or
`conda forge <package name>`
## Running the tests

To ensure that all modules are loaded and everything is working. Launch the program, If it launches with no errors, it is working properly 

## Running the program

Simply start `main.py` and youll be greeted with the menu. Pressing 1 will prompt a new game to start where the user will enter their name and have 3 seconds until the timer starts and they can start guessing. If the User wins, their highscore will be added to the JSON file. Furthermore, Pressing option 2 will allow the user to see the name and time of the current record 

Highscores can be reset by deleting the `highscores.json` file

Words can be added or removed in the `wordlist.txt` file as this is where the program generates the words from

## Built With

* [JSON](https://docs.python.org/3/library/json.html) - Used to open and edit JSON files
* [Random](https://docs.python.org/3/library/random.html) - Used to generate random files
* [Time](https://docs.python.org/3/library/time.html) - Used to compute program time
## Contributing

If any Enhancements, Features or Problems arrise, Please submit a request on github

## Versioning

If another version is set to release, We will add better version control

## Authors

* **Jonathan Obenland** - *Highscoring functions* - [Jonathan Obenland](https://github.com/jobenland)
* **Andrew Knox** - *Game mechanics* - [Andrew Knox]

## License

This project is licensed under the GPL License
