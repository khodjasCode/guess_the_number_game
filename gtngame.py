# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:34:55 2024

author: Asrorkhodja
"""

'''
The program generates a random number, the user makes a guess as to what the number is, and the program responds with clues (e.g., “too high”, “too low”) until the user guesses correctly.
'''
name = str(input(f"Welcome to our game! What is your name?\n>>> "))
print(f"Well, {name}, I am thinking of a number between 1 and 50, you have 3 attempts and you should guess the number. If you guess the number, you win, if you don't, you lose. GOOD LUCK, LET'S GO!")

import random as r
def main():
  number = r.randint(1, 50)
  tries = 1
  while tries <= 3:
    guess = int(input("Take a guess\n>>> "))
    if guess == number:
      print('You win,', name, '!')
      break
    elif guess > number:
      print('Too high!')
      tries += 1
    elif guess < number:
      print('Too low!')
      tries += 1
    if tries == 4:
      print("Unfortunately, you didn't guess the number. The number was", number, "\n Please try again!")

main()
