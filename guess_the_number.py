import random

n = random.randint(1, 100)
a = -1
guesses = 0
max_guesses = 7

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")
print("You have only 7 attempts.")

while a != n and guesses < max_guesses:

    a = int(input("Guess the number: "))
    guesses += 1

    if a > n:
        print("Lower number please")

    elif a < n:
        print("Higher number please")

    else:
        print(f"Correct! You guessed it in {guesses} attempts.")

if a != n:
    print(f"Game Over! The correct number was {n}.")