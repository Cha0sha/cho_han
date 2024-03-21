import sys
#Colatz sequence

#we have to take an input named "n"
print(" Please enter the number from which you want to start the collatz sequence")
response = input('>')
n = int(response)

#if n is 1 or 0, stop.
if n == 0 or n ==1:
    print("PLease enter a valid number which is not 0 or 1")
    sys.exit("Try again")


#if n is even next number of n is quotient0 n/2
#if n is odd next nummber of n  is n*3+1

while n!=1:
    if n%2 == 0:
        n = n//2
    else:
        n=3*n+1 
    print('-> ' + str(n) , flush=True)
