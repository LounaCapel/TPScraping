#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:42:24 2022

@author: CAPEL Louna
"""


import requests
from bs4 import BeautifulSoup 
import re

video_url = "https://www.youtube.com/watch?v=fmsoym8I-3o&t=2s"  
page = requests.get(video_url) 
soup = BeautifulSoup(page.content, "html.parser")  
  

#print(soup)

def TrouverTitre():
    title = soup.find("meta", itemprop="name")["content"]
    return(title)

def TrouverAuteur():
    auteur = soup.find("span", itemprop="author").next.next["content"]
    return(auteur)

def TrouverNbrLike():
    results = soup.find_all("script")
    pattern = 0
    for result in results :
        pattern = re.compile(r'([0-9]*.?[0-9]*[0-9]).?clics')
        match = pattern.search(str(result))
        if match:
            nb = (match.group(1))
            break
    return("".join([nb for nb in nb if nb.isdigit()]))

def TrouverDescription():
    results = soup.find_all("script")
    pattern = 0
    for result in results :
        pattern = re.compile(r'descriptionBodyText(.*)showMoreText')
        match = pattern.search(str(result))
        if match:
            pattern2 = re.compile(r'(?:{"text":"((?:[^\\"]|\\"|\\))"[^}]})*')
            match2 = pattern2.search(str(match.group(1)))
            if match2:
                break
    return (match2.group(1))

def TrouverLienDescription():
    results = soup.find_all("script")
    pattern = 0
    for result in results :
        pattern = re.compile(r'descriptionBodyText(.*)showMoreText')
        match = pattern.search(str(result))
        if match:
            pattern2 = re.compile(r'(?:{"text":"((?:[^\\"]|\\"|\\))"[^}]})*')
            match2 = pattern2.search(str(match.group(1)))
            if match2:
                break
    return (match2.group(1))

def GetDescription () :
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    return (pattern.findall(str(soup))[0].replace('\\n','\n'))

def main():
    print(TrouverTitre())

    print(TrouverAuteur())
    
    print(TrouverNbrLike())

    print(GetDescription())
    
    
    
main()
    
    



