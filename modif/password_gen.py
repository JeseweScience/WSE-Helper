import random, os, ctypes, time
from colorama import Fore, init
init()

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def gen_pass():
    os.system('cls')
    try:
        length = input(Fore.GREEN + 'Enter password length (max=16): ' + Fore.YELLOW)
        length = int(length)
        print('')
        if length>16:
            input(Fore.RED + "\nError: Maximum password length is 16, press Enter to continue... ")
        else:
            for n in range(0,5):
                password =''
                for i in range(length):
                    password += random.choice(chars)
                print(Fore.YELLOW + 'Result: ' + Fore.CYAN + password)
            input(Fore.GREEN + '\nDone, press Enter to continue... ')
    except Exception:
        input(Fore.RED + 'Error: Invalid Value, press Enter to continue... ')