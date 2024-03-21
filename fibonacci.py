import sys

while True:
    print('Enter the Nth fibonascii number you want to stop at')
    print('calculate (such as 5,50,1000,9999) or quit ')
    response = input('> ')
    if response.upper() == 'QUIT':
        print("THank yoou!!!")
        sys.exit()

    if response.isdecimal() and int(response) !=0:
        nth = int(response)
        break
print()
fibnumbercalculated = []
if nth==1:
    print('0')
    print()
    print('THe #1 Fibonacci number is 0')
elif nth == 2:
    print('0,1')
    print()
    print('THe #2 fibonacci number is 1')
else:  
    if nth >=10000:
        print('Warning: This will take a while to display on the ')
        print('console! Please enter a smaller value for faster results or wait for it')
        input('Please enter to bein ')


        
    secondtolastnumber = 0
    lastnumber = 1
    fibnumbercalculated +=[0,1]
    print('0,1',end='')

    for _ in range(2,nth):
        next_num = secondtolastnumber + lastnumber
        fibnumbercalculated.append(next_num)
        print(',',next_num,end='')

        if len(fibnumbercalculated)==nth:
            print()
            print()
            print(f'The #(nth)fibonacci number is {next_num}')
            break

        secondtolastnumber,lastnumber = lastnumber , next_num