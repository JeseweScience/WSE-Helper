from modif.ip_checker import *
from modif.qrcode import *
from modif.updater import *
from modif.cleaner import *
from modif.check_connection import *
from modif.text_to_speech import *
from modif.speedtest import *
from modif.nickname_gen import *
from modif.dns_rec import *
from modif.image_parsing import *

import os, webbrowser, time, version, ctypes
import urllib.request
from colorama import Fore, init
init()

name = "WSE Helper 0.5 "
version = "0.5"
# pyfiglet --font=cybermedium TEXT
banner="""
    _ _ _ ____ ____    _  _ ____ _    ___  ____ ____    
    | | | [__  |___    |__| |___ |    |__] |___ |__/    
    |_|_| ___] |___    |  | |___ |___ |    |___ |  \ 
"""
about = f"""WSE Helper is a powerful tool that brings together many 
useful features and mini-games. WSE Helper is the ideal 
solution for those who value efficiency and convenience.

=========================================================
===               GitHub: @JeseweScience              ===
=========================================================

                      Version : {version}
                    
       MIT License | Copyright (c) 2023 Jesewe Science
            Developers: Jesewe, f0rk1l, Smirvv"""


def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(name + '| Menu')
    print(Fore.GREEN + banner)
    print(Fore.YELLOW + """
        Functions:
         
[1] IP Information                [6] Get DNS-Records               
[2] QR Code Generator             [7] Image Parsing                 
[3] Text to Speech                
[4] Speedtest Internet            
[5] NickName Generator            

        Program:

[0] Exiting the program            [23] Check For Updates
[22] About The Program             [24] Cache Cleaner            """)
    try:
        choose = input(Fore.GREEN + f"\nDevice > " + Fore.YELLOW)
    except Exception:
        input(Fore.RED + "\nMistake: Invalid value, press Enter to continue... ")
        main()
    finally:
        if choose=="0":
            logging.debug('Exiting the program...')
            os.abort()
        elif choose=="1":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| IP Information')
            ip_check()
            main()
        elif choose=="2":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| QR Code Generator')
            qrcode()
            main()
        elif choose=="3":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Text to Speech')
            text_to_speech()
            main()
        elif choose=="4":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Speedtest Internet')
            speedtest()
            main()
        elif choose=="5":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| NickName Generator')
            nickname_gen()
            main()
        elif choose=="6":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Get DNS-Records')
            dns_rec()
            main()
        elif choose=="7":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Image Parsing')
            img_parsing()
            main()
        elif choose=="22":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| About The Program')
            os.system('cls')
            print(Fore.YELLOW + about)
            input(Fore.GREEN + '\nDone, press Enter to continue... ')
            main()
        elif choose=="23":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Check For Updates')
            check_update()
            input(Fore.GREEN + '\nDone, press Enter to continue... ')
            main()
        elif choose=="24":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Cache Cleaner')
            temp_cleaner()
            dump_cleaner()
            main()
        else:
            input(Fore.RED + "\nMistake: Invalid value, press Enter to continue... ")
            main()

if __name__ == '__main__':
    if connect():
        print(Fore.GREEN + "connected")
    else:
        print(Fore.RED + "I can't start the program, error: there is no Internet!")
        input('Press Enter to exit')
        os.abort()

    main()