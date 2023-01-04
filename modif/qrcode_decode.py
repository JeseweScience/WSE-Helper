import os
from PIL import Image
from pyzbar.pyzbar import decode
from colorama import Fore, init
init()

def qr_decoder():
	os.system('cls')
	message=input(Fore.GREEN + 'Drag QR CODE here: ' + Fore.CYAN)
	try:
		data = decode(Image.open(message))
	except Exception as e:
		input(Fore.RED + '\nFailed to decode QR CODE, press Enter to continue... ')
	else:
		print(Fore.YELLOW + '\nResult:\n', data)
		main = input(Fore.GREEN + "\nDone, press Enter to continue... ")