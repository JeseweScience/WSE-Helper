import requests, os, time, folium, socket
from colorama import Fore, init
init()

banner="""
_ ___     _ _  _ ____ ____ ____ _  _ ____ ___ _ ____ _  _  
| |__]    | |\ | |___ |  | |__/ |\/| |__|  |  | |  | |\ | 
| |       | | \| |    |__| |  \ |  | |  |  |  | |__| | \|
"""

def get_info_by_ip(ip=''):
    if not os.path.isdir("ip-list"):
        os.mkdir("ip-list")
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        print('')
        for k, v in data.items():
            print(Fore.CYAN + f'{k} : {v}')
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'ip-list/{response.get("query")}_{response.get("city")}.html')
    except:
        input(Fore.RED + "Failed to get response to request, press Enter to continue... ")
    else:
        input(Fore.GREEN + "\nDone, press Enter to continue... ")

def ip_check():
    os.system("cls")
    print(Fore.GREEN + banner)
    print(Fore.YELLOW + '\nYour ip address: ' + socket.gethostbyname(socket.gethostname()))
    ip = input(Fore.RED + "\nEnter target ip: " + Fore.CYAN)
    get_info_by_ip(ip=ip)