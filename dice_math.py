import random 
numbers = [1,2,3,4,5,6,0]

Dice1= random.choice(numbers)
dice2= random.choice(numbers)
dice3= random.choice(numbers)
dice4= random.choice(numbers)
dice5= random.choice(numbers)
dice6= random.choice(numbers)

sam = Dice1 + dice2 + dice3 + dice4 + dice5 + dice6
print("You rolled dice-1 is ", Dice1,", dice-2 is ",dice2,", dice-3 is ",dice3,", dice-4 is ",dice4,", dice-5 is ",dice5,"and dice-6 is ",dice6)
print("Enter the sum")
q = input(">")
h = int(q)
if h == sam:
    print("Woe that's right. THe total sum of the of the number from the rolled dice is {}".format(sam))
else:
    print("The sum of your roll is: ", sam)