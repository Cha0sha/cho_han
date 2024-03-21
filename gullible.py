while True:
    print("Do you want to keep a gullible person busy? Y/N")
    response = input('> ')
    if response.lower() == 'no' or response.lower() == 'no':
        break
    if response.lower() == 'yes' or response.lower() =='y':
        continue
    print('"{}" is not a valid for yes/no reponde'.format(response))

print('THank you. have a nice day')