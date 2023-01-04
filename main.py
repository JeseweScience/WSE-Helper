from modif.youtube_view import *
from modif.ip_checker import *
from modif.qrcode import *
from modif.qrcode_decode import *
from modif.shortener import *
from modif.updater import *

# CODE BY JESEWE HACK

import os, sys, webbrowser, time, pymem, version, ctypes
from colorama import Fore, init
init()

def main():
	os.system('cls')
	print(Fore.RED + "Welcome to WSE Helper")
	print("Made by Jesewe Hack Company © 2023")
	print(Fore.YELLOW + """
[0] Exit
[1] YouTube Viewer Bot (ALPHA)
[2] IP CHECKER
[3] QR CODE GENERATOR
[4] QR CODE DECODER
[5] Link shortener
[20] Check for Updates""")

	try:
		choose = input(Fore.GREEN + "\nConsole -> " + Fore.YELLOW)
	except Exception:
		input(Fore.RED + "\nError: Invalid value ")
		main()
	finally:
		if choose=="0":
			print(Fore.RED + "\nI'm leaving...")
			os.abort()
		elif choose=="1":
			youtube_view()
			main()
		elif choose=="2":
			ip_check()
			main()
		elif choose=="3":
			qrcode()
			main()
		elif choose=="4":
			qr_decoder()
			main()
		elif choose=="5":
			shortener()
			main()
		elif choose=="20":
			check_update()
			main()
		else:
			input(Fore.RED + "\nError: Invalid value ")
			main()

if __name__ == '__main__':
	check_update()
	main()
