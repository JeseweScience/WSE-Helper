import random, time, os, logging
from colorama import Fore, init
init()

banner="""
___  _ ____ ____    ____ _ _  _ _  _ _    ____ ___ _ ____ _  _ 
|  \ | |    |___    [__  | |\/| |  | |    |__|  |  | |  | |\ | 
|__/ | |___ |___    ___] | |  | |__| |___ |  |  |  | |__| | \|

"""

def dice_sim():
    sides = 6
    roll = random.randint(1, sides)
    os.system('cls')
    print(Fore.GREEN + banner)

    print("You rolled a " + Fore.RED + str(roll))
    logging.debug(f'[GAME LOG] The user gets a number: ' + str(roll))
    input(Fore.GREEN + "\nDone, press Enter to continue... ")