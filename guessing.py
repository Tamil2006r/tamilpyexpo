import random

def guessing_game():
    # The computer picks a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        try:
            # Ask the player for their guess
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the player's guess is correct
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Please enter a valid integer.")
            
if __name__ == "__main__":
    guessing_game()