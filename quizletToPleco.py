#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:56:47 2019

@author: Michael Bögli

converts flashcards from quizlet to pleco format 

1) on quizlet.com click on export, select "separate by tab", and "new line" then copy text.
2) run this script
3) everything is saved in the output variable
"""

#%% Imports
import pyperclip
import re

#%% read from clipboard and split by new line
data = pyperclip.paste() 
a = data.split("\n")

#%% extract content for each line
# regexp replace each line 
# format: characters<tab>english<space>(pinyin)
#exp = r'([^\t]*)\t([^\(（]*)[\(（]([^\)）]*)[\)）]'
exp = r'([^\t]*)\t(.*)[\(（]([^\)）]*)[\)）]'          # use this one for hanzi[tab]english(pinyin), use with sub1
#exp = r'([^\(（]*)[\(（]([^\)）]*)[\)）]\t([^\t]*)'    # use this one for hanzi(pinyin)[tab]english, use with sub2
#exp = r'([^\t]*)\t([^-]*)-(.*)'                        # use this one for hanzi[tab]pinyin-english, use with sub2
sub1 = r'\1\t\3\t\2'
sub2 = r'\1\t\2\t\3'
# format: characters<space>(pinyin)<tab>english
# exp = r'([^\s]*)\s[\(（]([^\)）]*)[\)）]\t(.*)'
# sub = r'\1\t\2\t\3'
replace_st = lambda x : re.sub(exp, sub1, x)

b = list( map(replace_st, a))

#%% save output
output = "\n".join(b)
