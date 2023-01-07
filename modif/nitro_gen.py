import os, time, string, numpy, ctypes, requests
from colorama import Fore, init
init()

class NitroGen():
    def main(self):
        os.system('cls')
        try:
            num = int(input(Fore.GREEN + 'Input how many codes to generate and check: ' + Fore.CYAN))
        except ValueError:
            input(Fore.RED + "\nError: Invalid Value, press Enter to continue... ")
            os.abort()

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"
                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                input(Fore.RED + "Error: Interrupted by user, press Enter to continue..")
                pass

            except Exception as e:
                print(Fore.CYAN + f" Generated | {url} ")
                print('')

        input(Fore.GREEN + "\nDone, press Enter to continue... ")