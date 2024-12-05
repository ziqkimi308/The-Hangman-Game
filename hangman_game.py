"""
********************************************************************************
* Project Name:  Hangman Game
* Description:   The Hangman Game is a classic word-guessing game where the player tries to guess a randomly chosen word, one letter at a time
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

import random

from art import logo, stages
from word import word_list

# Opening
print(logo)
print("Welcome to the Hangman Game!")
chosen_word = random.choice(word_list)
display_word = []
chosen_word_len = len(chosen_word)
for i in range(0, chosen_word_len):
    display_word += "_"
print("Guess the word: " + " ".join(display_word))

# The game
lives = 6
game_end = False
while not game_end:
    user_guess = input("Enter a letter: ").lower()

    # Find hay in stack
    for i in range(chosen_word_len):
        if user_guess == chosen_word[i]:
            display_word[i] = user_guess
    print(" ".join(display_word))

    # If wrong guess...
    if user_guess not in chosen_word:
        print(f"\nWrong...{user_guess} is not in the word.")
        lives -= 1
        if lives == 0:
            game_end = True
            print("You lose...")

    # Check if finish guessing or not
    if "_" not in display_word:
        game_end = True
        print("You win!")

    print(stages[lives])
