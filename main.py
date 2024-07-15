import random

def get_player1_number(number):
    """Return a valid number from Player 1."""
    if 1 <= number <= 100:
        return number
    else:
        raise ValueError("Number must be between 1 and 100.")

def provide_feedback(guess, target_number):
    """Provide feedback on the guess."""
    if guess < target_number:
        return "Too low!"
    elif guess > target_number:
        return "Too high!"
    else:
        return "Correct!"

def play_game(player1_number, player2_guesses):
    """Main game logic."""
    attempts = 0
    for guess in player2_guesses:
        attempts += 1
        feedback = provide_feedback(guess, player1_number)
        if feedback == "Correct!":
            return attempts
    return attempts  # Return attempts even if the number wasn't guessed

if __name__ == "__main__":
    print("Welcome to 'Guess the Number'!")
    player1_number = int(input("Player 1, please think of a number between 1 and 100 (inclusive): "))
    player1_number = get_player1_number(player1_number)
    
    print("\n" + "="*30 + "\n")
    
    player2_guesses = []
    while True:
        guess = int(input("Player 2, make your guess: "))
        player2_guesses.append(guess)
        feedback = provide_feedback(guess, player1_number)
        print(feedback)
        if feedback == "Correct!":
            break
    
    print(f"Congratulations, Player 2! You've guessed the number {player1_number} in {len(player2_guesses)} attempts.")
