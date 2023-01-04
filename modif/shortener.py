import time, os
import pyshorteners as sh
from colorama import Fore, init
init()

s = sh.Shortener()

def shortener():
	os.system("cls")
	link=input(Fore.GREEN + 'Enter the link you want to shorten: ' + Fore.CYAN)
	try:
		output = s.clckru.short(link)
	except Exception as e:
		input(Fore.RED + '\nFailed to shorten link, press Enter to continue... ')
	else:
		print(Fore.YELLOW + 'Result:', Fore.CYAN + output)
		main = input(Fore.GREEN + "\nDone, press Enter to continue... ")