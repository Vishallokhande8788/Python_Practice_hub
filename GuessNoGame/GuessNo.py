import random

def welcome_message():
    print("===================================")
    print("   Welcome to the Guess the Number Game!  ")
    print("===================================")
    print("I have picked a number between 1 and 100.")
    print("Can you guess it in the fewest tries possible?\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.\n")
        elif guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
            break

def main():
    welcome_message()
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()