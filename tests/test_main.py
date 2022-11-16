#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:13:24 2022

@author: CAPEL Louna
"""

import sys
sys.path.append("../")
from scrapper import *

import requests
from bs4 import BeautifulSoup 
  
video_url = "https://www.youtube.com/watch?v=fmsoym8I-3o&t=2s"  
page = requests.get(video_url) 
soup = BeautifulSoup(page.content, "html.parser")  

def test_Titre():
    assert TrouverTitre(soup) == "Pierre Niney : L’interview face cachée par HugoDécrypte"
    
def test_Auteur():
    assert TrouverAuteur(soup) == "HugoDécrypte"
    
def test_NbrLike():
    assert int(TrouverNbrLike(soup)) >= 30400
    
def test_Description():
    assert (("Chaleureux remerciements" in TrouverDescription(soup)) and ("Manon Montoriol" in TrouverDescription(soup)))
    
def test_Description():
    assert ("Carrément j'ai quitté la vidéo de Squeezie" in TrouverCommentaire(soup))
