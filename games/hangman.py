import random, os, logging
from colorama import Fore, init
init()

banner="""
_  _ ____ _  _ ____ _  _ ____ _  _
|__| |__| |\ | | __ |\/| |__| |\ |
|  | |  | | \| |__] |  | |  | | \|

"""

def hangman():
    os.system('cls')
    print(Fore.GREEN + banner)
    word_list = ['python', 'java', 'kotlin', 'javascript', 'ruby']
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letter_guessed = set()
    tries = 6
    while len(word_letters) > 0 and tries > 0:
        print(Fore.GREEN + "\nYou have", tries, "tries left.")
        missing_letters = word_letters - letter_guessed
        print("Available letters:", ''.join(sorted(alphabet - letter_guessed)))
        guess = input("Guess a letter: ").lower()
        if guess in alphabet - letter_guessed:
            letter_guessed.add(guess)
            if guess in word_letters:
                print(Fore.GREEN + "Good job! The letter", guess, "is in the word.")
                word_letters.remove(guess)
            else:
                print(Fore.RED + "Oops! The letter", guess, "is not in the word.")
                tries -= 1
        else:
            print(Fore.YELLOW + "You have already guessed that letter. Try again.")
        print("The word:", end=" ")
        for letter in word:
            os.system('cls')
            if letter in letter_guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
    if len(word_letters) == 0:
        logging.debug(f'[GAME LOG] The user guessed the word: {word}')
        print(Fore.GREEN + "\nCongratulations! You won!")
        input(Fore.GREEN + "\nDone, press Enter to continue... ")
        logging.debug('[GAME LOG] Exiting the Hangman')
    else:
        logging.debug(f'[GAME LOG] The user did not guess the word: {word}')
        print(Fore.RED + "\nYou lost! The word was", word, ".")
        input(Fore.GREEN + "\nDone, press Enter to continue... ")
        logging.debug('[GAME LOG] Exiting the Hangman')