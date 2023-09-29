import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if choice == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
GUESS = random.randint(1, 100)
user_guess = int(input("Make a guess: "))


def game():
    global user_guess
    global attempts
    while user_guess != GUESS:
        if user_guess > GUESS and attempts != 0:
            print('Too high.')
            attempts -= 1
            print(
                f"You have {attempts} attempts remaining to guess the number.")
        elif user_guess < GUESS and attempts != 0:
            print('Too low.')
            attempts -= 1
            print(
                f"You have {attempts} attempts remaining to guess the number.")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return 0
        user_guess = int(input("Make a guess: "))
    if user_guess == GUESS:
        print(f"You got it! The answer was {GUESS}.")
        return 0


game()