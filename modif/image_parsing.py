import requests, os
from bs4 import BeautifulSoup
from colorama import Fore, init
init()

def img_parsing():
    os.system('cls')
    url = input(Fore.GREEN + 'Enter a link to the site: ' + Fore.CYAN)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")
    if not os.path.exists("images"):
        os.makedirs("images")
    for img in img_tags:
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        img_response = requests.get(img_url)
        filename = os.path.join("images", img_url.split("/")[-1])
        with open(filename, "wb") as f:
            f.write(img_response.content)
    input(Fore.GREEN + "\nDone the files are saved in the folder 'images', press Enter to continue... ")