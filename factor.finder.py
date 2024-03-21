#This program is about finding the factorial.

import math,sys

while True:
    print('PLease enter te number that you want factors.')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit
    
    if not (response.isdecimal()and int(response)>0):
        continue
    number = int(response)

    factors = []

    for i in range(1,int(math.sqrt(number))+1):
        if number % i== 0:  
            factors.append(i)
            factors.append(number//i)

    factors = list(set(factors))
    #factors.sort()

    for i,factors in enumerate(factors):
        print(factors)