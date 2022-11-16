#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:42:24 2022

@author: CAPEL Louna
"""

'''
import
'''
import requests
from bs4 import BeautifulSoup 
import re
import json
 

'''
Permet de trouver le titre de la vidéo
Entree : soup
Sortie : Titre de la video
'''
def TrouverTitre(soup):
    title : str = soup.find("meta", itemprop="name")["content"]
    return(title)

'''
Permet de trouver l'auteur de la vidéo
Entree : soup
Sortie : Auteur de la video
'''
def TrouverAuteur(soup):
    auteur :str = soup.find("span", itemprop="author").next.next["content"]
    return(auteur)

'''
Permet de trouver le nombre de like de la vidéo
Entree : soup
Sortie : nombre de like
'''
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

'''
Permet de trouver la description de la vidéo
Entree : soup
Sortie : description de la video
'''
def TrouverDescription (soup) :
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    return (pattern.findall(str(soup))[0].replace('\\n','\n'))

'''
Permet de trouver les liens de la description de la vidéo
Entree : soup
Sortie : liens de la description
'''
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

'''
Permet de trouver les commentaire de la vidéo
Entree : soup
Sortie : commentaires
'''
def TrouverCommentaire (soup) :
    pattern = re.compile(r'Content":{"simpleText":"((?:[^\\"]|\\"|\\)*)"},"trackingParams')
    return (pattern.findall(str(soup))[0].replace('\\n','\n'))

'''
Fonction principale
Entree : 
Sortie : json
'''
def main():

    with open('input.json') as mon_fichier:
        data : dict = json.load(mon_fichier)
        
    IdVideos : list = data['videos_id']
    NbrVideos : int = len(IdVideos)
    
    for i in range (NbrVideos):
        lien : str = "https://www.youtube.com/watch?v="+IdVideos[i]
        page = requests.get(lien) 
        soup = BeautifulSoup(page.content, "html.parser")
        donnees : dict = {"Titre": TrouverTitre(soup),"Auteur": TrouverAuteur(soup),"Nombre de like": TrouverNbrLike(soup),
                   "Description":TrouverDescription(soup),"Id":IdVideos[i],"Commentaire":TrouverCommentaire(soup)}
        with open("output.json", "a") as file:
            json.dump(donnees, file)
            file.write("\n")
    
'''
Appel de la fonction
'''
main()
    
    



