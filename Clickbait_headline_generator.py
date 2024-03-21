import random

object_pronouns = ['His' , 'Her' , 'Them']
Posessive_pronouns = ['Her' , 'His' , 'Their']
personal_pronouns = ['He' , 'She' , 'They']
states = [  'California' , 'Texas' , 'Florida' , 'New York' , 'Pensalvania' , 'Illinois' , 'Ohio' , 'Georgia' , 'North Carolina' , 'Michigan']
Nouns = ['Athalet' , 'Clown' , 'Shovel' , 'Paleo Diet' , 'Doctor' , 'Parent' , 'Cat' , 'Dog' , 'Chicken' , 'Robot' , 'Video Game' , 'Avacado' , 'Plastic straw' , 'Serial Killer' , 'Telephonic Psychic']
places = ['Houses' , 'attic' , 'Bank Deposit Box' , 'School' , 'Basement' , 'Workplace' , 'Donut shop' , 'Apocalypse Bunker']
When = ['Soon' , 'THis year' , 'Later today' , 'RIGHT NOW' , 'Next week']


def generatoAreMillenialsKillingHeadline():
    noun = random.choice(Nouns)
    return 'Are milliennials killng the {} Industry?'.format(noun)

def generateWhatyoudontknowheadline():
    noun = random.choice(Nouns)
    pluralNoun = random.choice(Nouns) + 's'
    when = random.choice(When)
    return 'Without this {} , {} could kill you {}'.format(noun, pluralNoun,when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(object_pronouns)
    state = random.choice(states)
    noun1 = random.choice(Nouns)
    noun2 = random.choice(Nouns)
    return 'Bigg companies hate {}! See how this {} {} invented a cheaper {}.'.format(pronoun,state,noun1,noun2)

def generateYouWontBelieveHeadline():
    noun = random.choice(Nouns)
    state = random.choice(states)
    pronoun = random.choice(Posessive_pronouns)
    place = random.choice(places)
    return 'You won\'t believe this {} {} found in  {} {}'.format(state,noun,pronoun,place)

def generatedontwantyoutoknowHeadline():
    pluralNoun1 = random.choice(Nouns) + 's'
    pluralNoun2 = random.choice(Nouns) + 's'
    return 'What {} don\'t want you to know about {}.'.format(pluralNoun1,pluralNoun2)

def generategiftideaHeadline():
    number = random.randint(7,15)
    noun = random.choice(Nouns)
    state = random.choice(states)
    return '{} Gift ideas to give your {} from {}'.format(number,noun,state)

def generatereasonwhyheadline():
    number1=random.randint(3,19)
    pluralnoun = random.choice(Nouns)+'s'
    number2 = random.randint(1,number1)
    return '{}Reasons why {} are more interesting than you think(Number {} will surprise you!)'.format(number1,pluralnoun,number2)

def genereatejobautomatedheadline():
    state = random.choice(states)
    noun = random.choice(Nouns)
    i = 2
    pronoun1 = Posessive_pronouns[i]
    pronoun2 = personal_pronouns[i]
    if pronoun1 == 'Their':
        return 'THis {} {} didn\'t think robots would take {} job. {} were wrong.'.format(state,noun,pronoun1,pronoun2)
    else:
        return 'This {} {} didn\'t think robots would take {} job. {} were wrong.'.format(state,noun,pronoun1,pronoun2)
def main():
    print('Welcome to clickbait generator:)')
    print('Our website needs to trick into looking  at ads')
    
    print("Enter how many ad headlines do you need?")
    response = int(input(">"))
    numberofHeadlines = int(response)
    headlines_list = [generatoAreMillenialsKillingHeadline() , generateWhatyoudontknowheadline() , generateBigCompaniesHateHerHeadline() , generateYouWontBelieveHeadline() , generatedontwantyoutoknowHeadline() , generategiftideaHeadline() , generatereasonwhyheadline() , genereatejobautomatedheadline()]
    #print(random.choices(headlines_list,k=numberofHeadlines))
    
    
    necessary_headlines = headlines_list[:response]

    for headlines_list in necessary_headlines:
        print(headlines_list)

        
    print("headline")
    print()
    website = random.choice(['wobsite' , 'Blag' , 'Facebuuk' , 'Googles' , 'Twidee' , 'Faacesbook' , 'Pastagram'])
    when = random.choice(When).lower()
    print('Post these to our' , website , when , 'or you\'re fired!!')
    
main()