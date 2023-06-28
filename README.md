# Yatzy Game

This program is a simple simulation of the dice game called Yatzy. The player rolls five dice and tries to achieve different combinations to score points. The player's score can be saved to a SQLite database.

## Instructions
1. Go to the yatzy folder.
1. Run the program by executing the code in the file `yatzy.py`.
2. During each round, the program will roll the dice and display the results.
3. You can choose to keep some of the dice and roll the rest again.
4. Select the category where you want to mark your points.
5. At the end of the game, you will receive the final score, and it will be saved to the database.

## Program Structure

- `from random import randint`: Imports the `randint` function for generating random numbers.
- `from collections import Counter`: Imports the `Counter` class for counting occurrences of dice values.
- `from os import environ`: Imports the `environ` function from the `os` module for retrieving the username.
- `import sqlite3`: Imports the `sqlite3` module for working with the SQLite database.
- `dice = lambda: randint(1, 6)`: Defines a lambda function `dice` that returns a random dice roll between 1 and 6.
- `int_input = lambda x: int(input(x))`: Defines a lambda function `int_input` that converts user input to an integer.
- `choose = lambda: input("Which point in minutes do you want to fill in? You can only select those whose value is None.: ")`: Defines a lambda function `choose` that prompts the user to choose a point to fill in.
- `class Player`: Defines the player class.
  - `__init__(self, name)`: Initializes the player's name and score for different categories.
  - `roll(self)`: Rolls five dice and calculates the potential scores.
  - `potential(self)`: Calculates the potential score options based on the dice rolls.
  - `mark(self, choice)`: Marks the player's selected score option.
  - `change(self, l)`: Changes the selected dice to new rolls.
  - `final(self)`: Calculates the player's final score.
  - `save_score(self)`: Saves the player's score to the SQLite database.
- Main program: Creates a player using the username from the environment variables and plays rounds until all categories are filled. The final score is printed, and the score is saved to the database.

Please note that the program uses the `USERNAME` environment variable to retrieve the player's name. The score is saved to a SQLite database named `yatzy.db`.

Make sure to have the `sqlite3` module installed before running the program.
