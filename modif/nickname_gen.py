import random, os, logging
from colorama import Fore, init
init()

banner="""
_  _ _ ____ _  _ _  _ ____ _  _ ____ 
|\ | | |    |_/  |\ | |__| |\/| |___ 
| \| | |___ | \_ | \| |  | |  | |___ 

____ ____ _  _ ____ ____ ____ ___ ____ ____ 
| __ |___ |\ | |___ |__/ |__|  |  |  | |__/  
|__] |___ | \| |___ |  \ |  |  |  |__| |  \  

"""

adjectives = ["Clumsy", "Bored", "Dizzy", "Repulsive", "Scary", "Amusedly", "Worried", "Calm", "Friendly", "Exuberant", "Empty", "Gentle", "Dangerous", "Cool", "Funny", "Crazy", "Awesome", "Weird", "Silly", "Quirky", "Unusual", "Alert", "Beautiful", "Expensive", "Famous", "Sleepy", "Shy", "Innocent", "Inquisitive", "Vast", "Tender", "Tame", "Good", "Shaky", "Sharp", "Breezy", "Broken", "Cold", "Dry", "Hot"]
nouns = ["Person", "Penguin", "Kangaroo", "Unicorn", "Dragon", "Gorilla", "Squirrel", "Worker", "Doctor", "Scientist", "Engineer", "Astronaut", "Explorer", "Butterfly", "Cat", "Crocodile", "Deer", "Dolphin", "Dragon", "Elephant", "Fish", "Fox", "Giraffe", "Horse", "Kangaroo", "Lion", "Monkey", "Owl", "Panda", "Parrot", "Penguin", "Pig", "Rabbit", "Rat", "Shark", "Squirrel", "Tiger", "Turtle", "Wolf", "Zebra", "Ant", "Bee", "Caterpillar", "Centipede", "Spider", "Camel", "Cheetah", "Chicken", "Crab", "Deer", "Duck", "Eagle", "Elephant", "Flamingo", "Gorilla", "Hippopotamus", "Jaguar", "Kangaroo", "Lion", "Moose", "Ostrich", "Panther", "Quail", "Raccoon", "Snail", "Turkey", "Uakari", "Vulture", "Wombat", "Xerus", "Yak", "Zebra", "Aardvark", "Bison", "Cheetah", "Deer", "Elk", "Fox", "Giraffe", "Hawk", "Iguana", "Jaguar", "Kangaroo", "Llama", "Mule", "Newt", "Otter", "Puma", "Quokka", "Raccoon", "Squirrel", "Toad", "Uakari", "Vole", "Walrus", "Xerus", "Yak", "Zebra"]

def generate_nickname():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = adjective + " " + noun
    return nickname

def nickname_gen():
    os.system('cls')
    print(Fore.GREEN + banner)
    nickname = generate_nickname()
    try:
        i=int(input(Fore.GREEN + 'How many nicknames do you want to generate? (Min=1 | Max=30) > ' + Fore.CYAN))
    except ValueError:
        logging.error(f'Error: Invalid value')
        input(Fore.RED + '\nError: Invalid Value, press Enter to continue... ')
        pass
    else:
        if 1<=i<=30:
            for i in range(i):
                print(Fore.YELLOW + "Your nickname is: " + Fore.RED + generate_nickname())
            
            logging.debug(f'User generated {i} nicknames')
            input(Fore.GREEN + "\nDone, press Enter to continue... ")
        elif i<=0:
            logging.error('The user entered too lower a number to generate a nickname.')
            input(Fore.RED + '\nError: You entered a lower number, press Enter to continue... ')
        else:
            logging.error('The user entered too large a number to generate a nickname.')
            input(Fore.RED + '\nError: You entered a large number, press Enter to continue... ')