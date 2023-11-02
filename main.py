"""
Scraping in the Band: A quick Python scraper
Created by Lilbud (November 2023)

Purpose: Used to get the raw MP3 files from the Dead.net "Playing in the Band" site.

See readme for more info

Below, enter the name of the album you'd like to get the links for. Then run this file and the links will be acquired.
"""

import json, requests
from bs4 import BeautifulSoup as bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
main_url = "https://www.dead.net/"

album = "Veneta"

if album == "Veneta":
    dropDown = "songSelect desktop songs-two"
    date = "2022-08"
    saveFile = ".\\Veneta_Links.txt"
elif album == "WOTF":
    dropDown = "songSelect desktop songs-one"
    date = "2023-09"
    saveFile = ".\\WOTF_Links.txt"

f = open(saveFile, "w")
files_url = f"https://www.dead.net/sites/g/files/g2000007851/files/{date}/"

r = requests.get("https://www.dead.net/playingintheband", headers)
soup = bs4(r.text, 'lxml')
songs = soup.find_all("div", {'class': dropDown})
for s in songs:
    for o in s.find_all('option'):
        if o.get('value'):
            r = requests.get(f"{files_url}{o.get('value')}.json")
            soup = bs4(r.text, 'lxml')
            data = json.loads(soup.find("p").text)
            jsonSave = open(f"json\\{o.get('value')}.json", 'w')
            jsonSave.write(json.dumps(data, indent=4))

            for d in data['tracks']:
                f.write(f"{main_url}{d['path']}\n")

f.close()
jsonSave.close()