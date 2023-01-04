import requests
import webbrowser
import version, os, re
from colorama import Fore, init
init()

def check_update():
    os.system('cls')
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
                input(Fore.CYAN + "No updates found, press Enter to continue... ")
        else:
            input(Fore.CYAN + "No updates found, press Enter to continue... ")