import random

def number_guessing_game():
    number = random.randint(1, 100)
    tries = 0

    print("🎲 Guess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {tries} tries.")
            break

if __name__ == "__main__":
    number_guessing_game()
