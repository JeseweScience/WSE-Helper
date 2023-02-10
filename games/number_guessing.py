import random, os, time, logging
from colorama import Fore, init
init()

number = random.randint(1, 100)

banner="""
_  _ _  _ _  _ ___  ____ ____    ____ _  _ ____ ____ ____ _ _  _ ____ 
|\ | |  | |\/| |__] |___ |__/    | __ |  | |___ [__  [__  | |\ | | __ 
| \| |__| |  | |__] |___ |  \    |__] |__| |___ ___] ___] | | \| |__] 

"""
def number_guessing():
    while True:
        os.system('cls')
        print(Fore.GREEN + banner)
        try:
            guess = int(input(Fore.GREEN + "Guess the number between 1 and 100: " + Fore.CYAN))
        except ValueError:
            logging.error(f'[GAME LOG] Error: Invalid value: {guess}')
            input(Fore.RED + '\nError: Invalid Value, press Enter to continue... ')
        else:
            if guess == number:
                print(Fore.GREEN + "\nYou guessed it! The number was " + Fore.RED + str(number))
                logging.debug('[GAME LOG] The user guessed the number: ' + str(number))
                input(Fore.GREEN + "\nDone, press Enter to continue... ")
                logging.debug('[GAME LOG] Exiting the Number Guessing')
                break
            elif guess < number:
                print(Fore.YELLOW + "\nToo low!")
                time.sleep(2)
            else:
                print(Fore.YELLOW + "\nToo high!")
                time.sleep(2)