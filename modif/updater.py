import requests
import webbrowser
import version, os, re, ctypes
from colorama import Fore, init
init()

def check_update():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW('Check For Updates')
    print(Fore.GREEN + 'Checking for updates...')
    local_version = version.ver
    try:
        response = requests.get('https://pastebin.com/raw/mpHsjd76').text
    except:
        input(Fore.RED + "Failed to get latest version, press Enter to continue... ")
        response = None
    if response != None:
        github_version = float(re.split('=', response.strip())[1])
        if github_version > local_version:
            print(Fore.GREEN + f'\nFound new version: {github_version}')
            try:
                webbrowser.open('https://github.com/Jesewe-Hack/WSE-Helper/releases')
            except:
                print(Fore.CYAN + "No updates found... ")
        else:
            print(Fore.CYAN + "No updates found... ")