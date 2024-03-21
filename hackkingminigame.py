import random

def display_hint(secret_word, guess):
    """Display a hint based on the correctness of the guessed word."""
    hint = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i]
        else:
            hint += '_'
    return hint

def hack_the_computer():
    words = ["MONITOR", "COMPUTER", "SECURITY", "PROGRAM", "HACKING", "PASSWORD", "NETWORK"]

    secret_password = random.choice(words)

    print("Welcome to Hack the Computer!")
    print("Try to guess the seven-letter secret password.")

    attempts = 0
    max_attempts = 10


    while attempts < max_attempts:
        guess = input("Enter your guess: ").upper()

        if len(guess) != 7 or not guess.isalpha():
            print("Invalid input. Please enter a seven-letter word.")
            continue

        attempts += 1

        if guess == secret_password:
            print("A C C E S S  G R A N T E D")
            break
        else:
            hint = display_hint(secret_password, guess)
            print("I N C O R R E C T E D  P A S S W O R D ")
            print(f"A C C E S S  D E N I E D . Hint: {hint}")
    
    else:
        print(f"Sorry, you've run out of attempts. The secret password was {secret_password}.")

hack_the_computer()
