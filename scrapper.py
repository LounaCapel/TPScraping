#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:42:24 2022

@author: CAPEL Louna
"""


import requests
from bs4 import BeautifulSoup 
import re
import json
 


def TrouverTitre(soup):
    title : str = soup.find("meta", itemprop="name")["content"]
    return(title)


def TrouverAuteur(soup):
    auteur :str = soup.find("span", itemprop="author").next.next["content"]
    return(auteur)


def TrouverNbrLike(soup):
    results = soup.find_all("script")
    pattern : int = 0
    for result in results :
        pattern = re.compile(r'([0-9]*.?[0-9]*[0-9]).?clics')
        match = pattern.search(str(result))
        if match:
            nb = (match.group(1))
            break
    return("".join([nb for nb in nb if nb.isdigit()]))


def TrouverDescription(soup):
    results = soup.find_all("script")
    pattern : int = 0
    for result in results :
        pattern = re.compile(r'descriptionBodyText(.*)showMoreText')
        match = pattern.search(str(result))
        if match:
            pattern2 = re.compile(r'(?:{"text":"((?:[^\\"]|\\"|\\))"[^}]})*')
            match2 = pattern2.search(str(match.group(1)))
            if match2:
                break
    return (match2.group(1))


def TrouverDescription (soup) :
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    return (pattern.findall(str(soup))[0].replace('\\n','\n'))


def TrouverLienDescription():
    results = soup.find_all("script")
    pattern :int = 0
    for result in results :
        pattern = re.compile(r'descriptionBodyText(.*)showMoreText')
        match = pattern.search(str(result))
        if match:
            pattern2 = re.compile(r'(?:{"text":"((?:[^\\"]|\\"|\\))"[^}]})*')
            match2 = pattern2.search(str(match.group(1)))
            if match2:
                break
    return (match2.group(1))


def main():
    
    #print(soup2)
    
    with open('input.json') as mon_fichier:
        data : dict = json.load(mon_fichier)
        
    IdVideos : list = data['videos_id']
    NbrVideos : int = len(IdVideos)
    
    for i in range (NbrVideos):
        lien : str = "https://www.youtube.com/watch?v="+IdVideos[i]
        page = requests.get(lien) 
        soup = BeautifulSoup(page.content, "html.parser")
        donnees : dict = {"Titre": TrouverTitre(soup),"Auteur": TrouverAuteur(soup),"Nombre de like": TrouverNbrLike(soup),
                   "Description":TrouverDescription(soup)}
        with open("output.json", "a") as file:
            json.dump(donnees, file)
            file.write("\n")
        
    
    
main()
    
    



