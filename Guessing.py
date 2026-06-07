# Python program to create a guessing game where the user has to guess a number between 1 and 75. The program will give hints if the guess is too low or too high, and will keep track of the number of attempts.
import random

lowest_num = 1
highest_num = 75
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:


    guess = input("Enter your guess: ")