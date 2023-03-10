from gtts import gTTS
import os, time, ctypes
from colorama import Fore, init
init()

banner="""
___ ____ _  _ ___    ___ ____    ____ ___  ____ ____ ____ _  _   
 |  |___  \/   |      |  |  |    [__  |__] |___ |___ |    |__|   
 |  |___ _/\_  |      |  |__|    ___] |    |___ |___ |___ |  |   

"""

def text_to_speech():
    os.system('cls')
    print(Fore.GREEN + banner)
    if not os.path.isdir("text-to-speech"):
        os.mkdir("text-to-speech")
    s = input(Fore.GREEN + "Enter the File name (For example sample.txt): " + Fore.CYAN)
    f = open('text-to-speech/' + s, 'w+')
    lang = input(Fore.GREEN + "\nEnter the language code (Fore example: en; ru; de): " + Fore.CYAN)
    text_to = input(Fore.GREEN + "\nEnter the text to be spoken: " + Fore.YELLOW)
    f.write(text_to)
    text = f.read()
    try:
        obj = gTTS(text=text_to, lang=lang, slow=False)
        f1 = input(Fore.GREEN + "\nEnter the Audio name to be saved (For example sample.mp3): " + Fore.YELLOW)
        obj.save('text-to-speech/' + f1)
    except Exception:
        input(Fore.RED + '\nError: Invalid Value, press Enter to continue... ')
    else:
        print(Fore.YELLOW + f"\nDone the '{f1}' file has been saved in the 'text-to-speech' folder.")
        input(Fore.GREEN + "\nDone, press Enter to continue... ")