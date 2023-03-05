import random, os
from colorama import Fore, init
init()

banner="""
_  _ _ ____ _  _ _  _ ____ _  _ ____ 
|\ | | |    |_/  |\ | |__| |\/| |___ 
| \| | |___ | \_ | \| |  | |  | |___ 

____ ____ _  _ ____ ____ ____ ___ ____ ____ 
| __ |___ |\ | |___ |__/ |__|  |  |  | |__/  
|__] |___ | \| |___ |  \ |  |  |  |__| |  \  

"""

adjectives = ["null","ebola","moe","warlord","pusher","simple","sample","mortis","switch","kill","cromwell", "", "", "", "wizard", "", "tasmanian", "nightmare", "drugstore", "hugh", "neil", "dewclaws", "skoomahead", "tom", "freak", "bailey", "helga", "immortal", "creepy", "dead", "fabulous", "jack", "flakes", "princess", "gene", "sentinel", "error404", "buckshot", "serana", "payton", "guillotine", "greely", "holly", "horny", "twitch", "sam", "tony", "riff", "mercury", "Fester", "IvAnA", "Mighty", "Nick", "OcTaViUs", "ViRUs", "Lars", "Omega", "Vagabond", "ziggy", "obgyn", "Charles", "Hunter", "Candy", "Lover", "Miss", "Deadbolt", "ironbum", "vigilante", "ring", "slow", "faSt", "siRen", "little", "Dan", "baloo", "mad"]
nouns = ["", "", "kotackbas","devil", "mako", "king", "cowboy", "mungous", "evert", "tripp", "baxter", "horton", "calvert", "faustinus", "julian", "tyon", "borislaw", "admon", "urunir", "norville", "gebhard", "roux", "fangar", "lenox", "danto", "sarkin", "emmett", "maugrim", "lucas", "brigham", "hawthorne", "laurent", "hamel", "everhard", "lister", "tyvrik", "jarlath", "lazarus", "ransley", "aurri", "karles", "dodd", "jasper", "armand", "cain", "marcel", "mikal", "lestat", "godwin", "hendrick", "friduwulf", "milo", "cassian", "edsel", "melchior", "straker", "balto", "ernald", "gallien", "lyre", "urien", "draven", "shadwyn"]

def generate_nickname():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    nickname = adjective + " " + noun
    return nickname

def nickname_gen():
    os.system('cls')
    print(Fore.GREEN + banner)
    nickname = generate_nickname()
    try:
        i=int(input(Fore.GREEN + 'How many nicknames do you want to generate? (Min=1 | Max=30) > ' + Fore.CYAN))
    except ValueError:
        input(Fore.RED + '\nError: Invalid Value, press Enter to continue... ')
        pass
    else:
        if 1<=i<=30:
            for i in range(i):
                print(Fore.YELLOW + "Your nickname is: " + Fore.RED + generate_nickname())
            input(Fore.GREEN + "\nDone, press Enter to continue... ")
        elif i<=0:
            input(Fore.RED + '\nError: You entered a lower number, press Enter to continue... ')
        else:
            input(Fore.RED + '\nError: You entered a large number, press Enter to continue... ')