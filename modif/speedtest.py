import speedtest
import time, os, logging
from colorama import Fore, init
init()

banner="""
____ ___  ____ ____ ___  ___ ____ ____ ___   
[__  |__] |___ |___ |  \  |  |___ [__   |  
___] |    |___ |___ |__/  |  |___ ___]  |   
"""

st = speedtest.Speedtest() 

def size(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

def speedtest():
	os.system('cls')
	print(Fore.GREEN + banner)
	print(Fore.YELLOW + '\nThis procedure takes about 1 minute...')
	try:
		download = st.download()
		upload = st.upload()
		print(Fore.GREEN + '\nDownload Speed: ' + size(download))
		print('Upload Speed: ' + size(upload))
		logging.debug(f'A speed test has been played, Download Speed : ' + size(download) + ', Upload Speed : ' + size(upload))
	except Exception:
		logging.error('Failed to recognize internet speed')
		input(Fore.RED + '\nFailed to recognize internet speed, press Enter to continue... ')
	finally:
		input(Fore.GREEN + "\nDone, press Enter to continue... ")