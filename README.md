# Scraping in the Band: A quick Python scraper
## Created by Lilbud (November 2023)

Note: run "pip install -r requirements.txt" in this folder to get the required dependencies.

### Info
This is a little thing I threw together quite quickly. Pretty much this is used to get the raw MP3 files from the Dead.net "Playing in the Band" site.
Which is where users can mess around with the multitracks from (as of now) 2 albums. Select tracks from Veneta 72 and Wake of the Flood are currently available.
I imagine Mars Hotel stuff might happen next year.

This program will grab the song list from the site, use those to get the .json files (which are used to store links and the default panning/fader values). 
Those .json files are parsed, and the .mp3 links are saved into a txt file. I could figure out how to download the files, maybe later.

But at least all the links are saved, then downloading those is fairly easy. You can use an extension like "DownThemAll", which allows txt file import.