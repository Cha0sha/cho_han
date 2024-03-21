import random
user = input('>')

print(user)
index_of_d = user.find('d')
def game_play():
    if index_of_d != -1:
        number_before_d = int(user[:index_of_d])#i want 3 dies to roll
    
        number_after_d = int(user[index_of_d + 1:]) #here is hte number of faces for the dies
        faces = range(0,number_after_d)
        fuck = random.choices(faces)
        number_variables = {}
        for i in range(0, number_before_d):
            variable_name = f"Dice_{i}"
            variable_value = i
            number_variables[variable_name] = variable_value
            #print("the value got for {} is {}.".format(variable_name,fuck))
            
            
        for idx, variable in enumerate(number_variables):
            random_choice = random.choice(faces)
            print(f"Random choice for variable{idx}: {random_choice}")
        
    else:
        print("The character 'd' was not found. Please try again.")
game_play()
    
    
    


#print("the choice for {} is {}".format(variable_name,fuck))
