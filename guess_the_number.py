import random


def guess_number():
    compguess = random.randint(1,100)
    for _ in range(10):
        print("PLease enter your guess")
        guess = int(input('> '))
        if guess == compguess:
            print('YAY thats right')
            break
        elif guess > compguess:
            print('Too high')
        elif guess < compguess:
            print('Too low')

    else:
        print("Ouch You're running out of guesses. Please try again")

guess_number()