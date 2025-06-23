import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty level: easy or hard: ").lower()

    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5
    else:
        print("Invalid difficulty.")
        return

    while guesses > 0:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print(f"You won! The number was {number_to_guess}.")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        guesses -= 1
        print(f"You have {guesses} guesses left.\n")

    print(f"Game over! The number was {number_to_guess}.")

guess_the_number()
