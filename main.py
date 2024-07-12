import random


def get_player2_guess():
    """Get a guess from Player 2."""
    while True:
        try:
            guess = int(input("Player 2, make your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")


def provide_feedback(guess, target_number):
    """Provide feedback on the guess."""
    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")



def play_game():
    """Main game logic."""
    print("Welcome to 'Guess the Number'!")
    
    # Player 1 thinks of a number
    player1_number = get_player1_number()
    
    print("\n" + "="*30 + "\n")
    
    # Player 2 tries to guess the number
    attempts = 0
    player2_guess = None
    
    while player2_guess != player1_number:
        player2_guess = get_player2_guess()
        attempts += 1
        provide_feedback(player2_guess, player1_number)
    
    print(f"Congratulations, Player 2! You've guessed the number {player1_number} in {attempts} attempts.")

if __name__ == "__main__":
    play_game()
