import random

def play_guessing_game(difficulty):
    if difficulty == 'easy':
        random_number = random.randint(1, 100)
        max_attempts = 10
        print("Guess the number between 1 and 100.")
    elif difficulty == 'medium':
        random_number = random.randint(1, 500)
        max_attempts = 15
        print("Guess the number between 1 and 500.")
    elif difficulty == 'hard':
        random_number = random.randint(1, 1000)
        max_attempts = 20
        print("Guess the number between 1 and 1000.")
    else:
        print("Invalid difficulty level.")
        return

    attempts = 0
    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < random_number:
                print("Higher")
            elif user_guess > random_number:
                print("Lower")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return

        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You ran out of attempts. The number was {random_number}.")

ready = input("Are you ready to play? (y/n) ").lower()

if ready == 'y':
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    play_guessing_game(difficulty)
else:
    print("Okay, maybe next time!")

