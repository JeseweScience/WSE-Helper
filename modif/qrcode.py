import pyqrcode
import png
import time, os
from colorama import Fore, init
init()

def qrcode():
	os.system("cls")
	if not os.path.isdir("qrcodes"):
		os.mkdir("qrcodes")
	qrcode=input(Fore.GREEN + 'Enter qrcode name: ' + Fore.CYAN)
	mt=input(Fore.GREEN + 'Enter link or text: ' + Fore.CYAN)
	try:
		url = pyqrcode.create(mt)
		url.png(f'qrcodes/{qrcode}.png', scale=8)
	except Exception as e:
		input(Fore.RED + '\nFailed to find qrcodes folder, press Enter to continue... ')
	else:
		url.show()
		print(Fore.YELLOW + f'\nA {qrcode}.png file has been created in the qrcodes folder.')
		main = input(Fore.GREEN + "\nDone, press Enter to continue... ")