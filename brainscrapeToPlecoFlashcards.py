#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:38:17 2019

@author: Michael Bögli 

Download from brainscape.com, extract flashcards and convert to pleco flashcards 
parsed falshcards are saved in variable 'output'
"""

#imports
import requests
import re
from bs4 import BeautifulSoup 

#settings
base_url = 'https://www.brainscape.com'
index_url = base_url + '/packs/contemporary-chinese-for-beginners-3542394'
#url = 'https://www.brainscape.com/flashcards/lesson-1-what-s-your-surname-1910172/packs/3542394'
download = False

#download index
if download:
    req_all = {}
    req_all["index"] = requests.get(index_url) 
soup = BeautifulSoup(req_all["index"].text, 'html.parser') 
all_decks_tags = soup.find_all('a', class_ = 'deck-bar-link')

all_decks = [{ 'name': deck_tag.text.strip(), 'url': deck_tag["href"]} for deck_tag in all_decks_tags ]

output = ""

# download each deck of flashcards 
for deck in all_decks: 
    print ("downloading " + deck["name"])
    if download: 
        req_all[deck["name"]] = requests.get(base_url + deck["url"])
    soup = BeautifulSoup(req_all[deck["name"]].text, 'html.parser') 
    table = soup.find('div', class_ = 'card-table')
    cards = table.find_all('section', class_ = 'card')
    
    b = []
    for card in cards :       
        english = card.find('h2', class_="card-question-text").text.strip()
        answer_raw = card.find('h3', class_="card-answer-text").text.strip()
        #answer = unicodedata.normalize("NFKD", answer_raw)
        answer = answer_raw.replace(u'\xa0', u' ')
        # check for chinese character in answer
        character_start = re.search(u'[\u4e00-\u9fff]', answer)
        if character_start:
            pinyin = answer[:character_start.start()].strip()
            character = answer[character_start.start():].strip()           
            b.append(character + "\t"+ pinyin + "\t"+ english)
    
    output += "\n//Contemporary Chinese For Beginers/"+deck["name"]+"\n"
    output +=  "\n".join(b)