import os, sys, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, init
init()

def youtube_view():
	os.system("cls")
	print(Fore.YELLOW + 'WARNING: Perhaps YouTube will remove cheated views after a while!')
	print(Fore.GREEN + 'INFO: The more views you put, the more the program will work, 1 view is wound up in 20 seconds.\nTo end the program press CTRL + C.')
	try:
		link=input(Fore.GREEN + "\nEnter the link to the youtube video: " + Fore.CYAN)
		views=int(input(Fore.GREEN + "How many views do you want: " + Fore.RED))
	except Exception as e:
		input(Fore.RED + '\nError: Invalid Value, press Enter to continue... ')
		pass
	else:
		options = Options()
		options.add_argument('--disable-extensions')
		options.add_argument('--disable-logging')
		options.add_argument('--disable-gpu')
		options.add_argument('--headless')
		driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
		try:
			driver.get(link)
		except Exception:
			input(Fore.RED + '\nError: Invalid Argument, press Enter to continue... ')
			pass
		else:
			for i in range(views):
				time.sleep(20)
				driver.refresh()
		finally:
			print(Fore.GREEN + '\nDone, press Enter to continue... ')
			pass