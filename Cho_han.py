import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 , dice2

def play(guess, dice_sum):
    is_even = dice_sum%2==0
    if (guess.lower() == 'cho' and is_even ) or (guess.lower() == 'han' and not is_even):
        return True
    else:
        return False
    
while True:
    player_guess = input("Do you want to bet cho or han : ")

    dice_result = roll_dice()
    total_sum = sum(dice_result)
    print(f"Dice result is : {dice_result}")
    print(f"Total sum : {total_sum}")

    if play(player_guess,total_sum):
        print("Congratulations  you have guessed correctly.")
    else:
        print("Sorry , you guessed inncorrectly")

    play_again = input("Do you want to play again?")
    if play_again.lower() != 'yes':
        print("THanks for playing")
        break   


