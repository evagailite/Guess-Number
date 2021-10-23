import art, random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)


# print(f"Pssst, the correct answer is {secret_number}")

def level_message(level_attempts):
    print(f"You have {level_attempts} attempts remaining to guess the number.")


def remaining_guesses(remaining_attempts):
    print(f"You have {remaining_attempts} attempts remaining to guess the number.")


def check_number(number, attempts):
    if number == secret_number:
        print(f"You got it! The answer was {secret_number}.")
    elif number > secret_number:
        print("Too high.")
        attempts -= 1
        check_left_attempts(attempts)
    elif number < secret_number:
        print("Too low.")
        attempts -= 1
        check_left_attempts(attempts)


def check_left_attempts(attempts):
    if attempts > 0:
        print("Guess again.")
        remaining_guesses(attempts)
        user_guess = int(input("Make a guess: "))
        check_number(user_guess, attempts)
    else:
        print("You've run out of guesses, you lose.")


level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "hard":
    attempts = 5
    level_message(attempts)
    user_guess = int(input("Make a guess: "))
    check_number(user_guess, attempts)

elif level == "easy":
    attempts = 10
    level_message(attempts)
    user_guess = int(input("Make a guess: "))
    check_number(user_guess, attempts)

else:
    print("Invalid input!")