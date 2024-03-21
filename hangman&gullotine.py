#Hangman and gullotine

import random

def choose_random_word():
    words = ["RABBIT", "PIGEON", "ELEPHANT", "TIGER", "GIRAFFE", "KANGAROO", "DOLPHIN", "CHEETAH"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    secret_word = choose_random_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6  # Adjust the number of attempts as needed

    print("Welcome to Hangman - Animal Edition!")

    while incorrect_attempts < max_attempts:
        current_display = display_word(secret_word, guessed_letters)
        print("\nCurrent Word:", current_display)

        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            incorrect_attempts += 1
            print(f"Incorrect! {max_attempts - incorrect_attempts} attempts remaining.")
            # Optionally, you can add code here to draw the hangman

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    else:
        print(f"Sorry, you've run out of attempts. The correct word was: {secret_word}")

# Run the hangman game
hangman()
