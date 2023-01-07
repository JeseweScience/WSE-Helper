from modif.youtube_view import *
from modif.ip_checker import *
from modif.qrcode import *
from modif.updater import *
from modif.cleaner import *
from modif.nitro_gen import *
from modif.check_connection import *
from modif.password_gen import *
from modif.text_to_speech import *

import os, webbrowser, time, version, ctypes
import urllib.request
from colorama import Fore, init
init()

name = "WSE Helper 0.2 "
about = """WSE Helper is a versatile and user-friendly software program 
that provides a range of useful tools for internet users.

=========================================================
===               GitHub: @JeseweScience              ===
===              Twitter: @jesewe_offical             ===
=========================================================
"""


def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(name)
    print(Fore.RED + "Welcome to " + name)
    print("Made By Jesewe Science Technologies")
    print(Fore.YELLOW + """
[0] Exit
[1] YouTube Viewer Bot (ALPHA)
[2] IP Information
[3] QR CODE Generator
[4] Discord Nitro Generator (ALPHA)
[5] Password Generator
[6] Text to Speech

[22] About The Program
[23] Check For Updates
[24] Found an error?
[25] Clear Temp Folder""")

    try:
        choose = input(Fore.GREEN + "\nbash -> " + Fore.YELLOW)
    except Exception:
        input(Fore.RED + "\nError: Invalid value, press Enter to continue... ")
        main()
    finally:
        if choose=="0":
            print(Fore.MAGENTA + "\nI'm leaving...")
            os.abort()
        elif choose=="1":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| YouTube Viewer Bot')
            youtube_view()
            main()
        elif choose=="2":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| IP Information')
            ip_check()
            main()
        elif choose=="3":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| QR CODE Generator')
            qrcode()
            main()
        elif choose=="4":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Discord Nitro Generator')
            Gen = NitroGen()
            Gen.main()
            main()
        elif choose=="5":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Password Generator')
            gen_pass()
            main()
        elif choose=="6":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Text to Speech')
            text_to_speech()
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
            webbrowser.open('https://github.com/Jesewe-Hack/WSE-Helper/issues')
            main()
        elif choose=="25":
            ctypes.windll.kernel32.SetConsoleTitleW(name + '| Cleaner')
            temp_cleaner()
            dump_cleaner()
            main()
        else:
            input(Fore.RED + "\nError: Invalid value, press Enter to continue... ")
            main()

if __name__ == '__main__':
    if connect():
        print("connected")
    else:
        print("No internet!")
        os.abort()

    check_update()
    main()