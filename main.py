from modif.youtube_view import *
from modif.ip_checker import *
from modif.qrcode import *
from modif.updater import *
from modif.cleaner import *
from modif.check_connection import *
from modif.text_to_speech import *
from modif.speedtest import *
from modif.nickname_gen import *
from games.number_guessing import *
from games.dice_simulation import *
from games.hangman import *

import os, webbrowser, time, version, ctypes, logging
import urllib.request
from colorama import Fore, init
init()

# logging
logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# name
name = "WSE Helper 0.4 "
# version
version = "0.4"
# pyfiglet --font=cybermedium TEXT
banner="""
_ _ _ ____ ____    _  _ ____ _    ___  ____ ____    
| | | [__  |___    |__| |___ |    |__] |___ |__/    
|_|_| ___] |___    |  | |___ |___ |    |___ |  \ 
"""
about = f"""\nWSE Helper is a versatile and user-friendly software program 
that provides a range of useful tools for internet users.

=========================================================
===               GitHub: @JeseweScience              ===
=========================================================

                      Version : {version}
                    
            Made By Jesewe Science Technologies

              Authors: Jesewe, f0rk1l, Smirvv
"""


def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(name + '| Menu')
    print(Fore.GREEN + banner)
    print(Fore.YELLOW + """
        Functions:

[1] YouTube Viewer                [6] NickName Generator
[2] IP Information                
[3] QR Code Generator             
[4] Text to Speech                
[5] Speedtest Internet            

        Games:

[50] Number Guessing              [52] Hangman 
[51] Dice Simulation              

        Program:

[0] Exiting the program     [23] Check For Updates
[22] About The Program      [24] Cache Cleaner            """)
    try:
        choose = input(Fore.GREEN + f"\nPC > " + Fore.YELLOW)
    except Exception:
        input(Fore.RED + "\nError: Invalid value, press Enter to continue... ")
        main()
    finally:
        # program
        if choose=="0":
            logging.debug('Exiting the program...')
            os.abort()
        # functions
        elif choose=="1":
            logging.debug('The function has been run: YouTube Viewer Bot')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| YouTube Viewer Bot')
            youtube_view()
            main()
        elif choose=="2":
            logging.debug('The function has been run: IP Information')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| IP Information')
            ip_check()
            main()
        elif choose=="3":
            logging.debug('The function has been run: QR Code Generator')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| QR Code Generator')
            qrcode()
            main()
        elif choose=="4":
            logging.debug('The function has been run: Text to Speech')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Text to Speech')
            text_to_speech()
            main()
        elif choose=="5":
            logging.debug('The function has been run: Speedtest Internet')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Speedtest Internet')
            speedtest()
            main()
        elif choose=="6":
            logging.debug('The function has been run: NickName Generator')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| NickName Generator')
            nickname_gen()
            main()
        # program
        elif choose=="22":
            logging.debug('Switching to system functions of the program: About The Program')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| About The Program')
            os.system('cls')
            print(Fore.YELLOW + about)
            input(Fore.GREEN + '\nDone, press Enter to continue... ')
            main()
        elif choose=="23":
            logging.debug('Switching to system functions of the program: Check For Updates')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Check For Updates')
            check_update()
            input(Fore.GREEN + '\nDone, press Enter to continue... ')
            main()
        elif choose=="24":
            logging.debug('Switching to system functions of the program: Cache Cleaner')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Cache Cleaner')
            temp_cleaner()
            dump_cleaner()
            main()
        # games
        elif choose=="50":
            logging.debug('Game function launched: Number Guessing Game')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Number Guessing Game')
            number_guessing()
            main()
        elif choose=="51":
            logging.debug('Game function launched: Dice Simulation')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Dice Simulation Game')
            dice_sim()
            main()
        elif choose=="52":
            logging.debug('Game function launched: Hangman')
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Hangman Game')
            hangman()
            main()
        else:
            logging.error(f'Error: Invalid value: {choose}')
            input(Fore.RED + "\nError: Invalid value, press Enter to continue... ")
            main()

if __name__ == '__main__':
    if connect():
        print(Fore.GREEN + "connected")
        logging.debug('An internet test has been replayed, status: successful!')
    else:
        print(Fore.RED + "Unable to start the program, error: No internet!")
        logging.debug('An internet check was played, status: unable to connect to the internet!')
        input('Press Enter to exit')
        os.abort()

    check_update()
    main()