# Yatzy Game

This program is a simple simulation of the dice game called Yatzy. The player rolls five dice and tries to achieve different combinations to score points.

## Instructions

1. Run the program by executing the code in the file `main.py`.
2. Enter the player's name when prompted by the program.
3. During each round, the program will roll the dice and display the results.
4. You can choose to keep some of the dice and roll the rest again.
5. Select the category where you want to mark your points.
6. At the end of the game, you will receive the final score.

## Program Structure

- `from random import randint`: Imports the `randint` function for generating random numbers.
- `from collections import Counter`: Imports the `Counter` class for counting occurrences of dice values.
- `from os import environ`: Imports the `environ` function from the `os` module for retrieving the username.
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
- Main program: Creates a player using the username from the environment variables and plays rounds until all categories are filled.

Please note that the program uses the `USERNAME` environment variable to retrieve the player's name.
