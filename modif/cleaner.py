import os
import shutil
import psutil
from colorama import Fore, init
init()

banner="""
____ _    ____ ____ _  _ ____ ____  
|    |    |___ |__| |\ | |___ |__/  
|___ |___ |___ |  | | \| |___ |  \  
"""

def temp_cleaner():
    os.system('cls')
    print(Fore.GREEN + banner)
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'
    deleteFileCount = 0
    deleteFolderCount = 0
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                deleteFolderCount = deleteFolderCount + 1

        except Exception as e:
            pass
    print(Fore.GREEN + '\nTemp folder cleared successfully... ')

def dump_cleaner():
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/CrashDumps'
    if not os.path.isdir(folder):
        os.mkdir(folder)
    deleteFileCount = 0
    deleteFolderCount = 0
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                deleteFolderCount = deleteFolderCount + 1

        except Exception as e:
            pass
    input(Fore.GREEN + 'CrashDumps folder cleared successfully, press Enter to continue... ')