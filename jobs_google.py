#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 00:46:52 2020

@author: User
"""
# pour exploiter les requêtes
from requests import get
from bs4 import BeautifulSoup

# pour transformer les données obtenues
import json


def scrap_job(s_job, city, type_contract):
    
    ### nombre maxi de page
    NB_PAGE = 2
    
    ### non renseigné
    NON_RENSEIGNE = 'Non renseigné'
    
    ### paramètres pris
    param_type_job = ''
    # les termes doivent être séparés par '+'
    param_search_words = 'developpeur+aws'
    # le/la ville/département
    param_search_location = 'Nantes'
     
    ### type de job
    arr_type_job = {
        'perm' : 'htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME',
        'full' : 'htichips=employment_type:FULLTIME&htischips=employment_type;FULLTIME',
        'ints' : 'htichips=employment_type:INTERN&htischips=employment_type;INTERN',
        'free' : 'htichips=employment_type:CONTRACTOR&htischips=employment_type;CONTRACTOR'
        }
    str_type_job = ''
    if param_type_job != '' and arr_type_job[param_type_job] is not None: 
        str_type_job = '&'+arr_type_job[param_type_job]
    
    ### création des listes
    arr_jobs = [] 
    
    # 
    #root_path = 'https://www.google.com/search?source=hp&q=job+developpeur+aws&oq=job+developpeur+aws&ibp=htl;jobs'
    root_path = 'https://www.google.com/search?source=hp&q=jobs+'+ param_search_location +'+'+ param_search_words +'&oq=jobs+'+ param_search_words +'&ibp=htl;jobs'+str_type_job
    response = get(root_path)
    
    ### extraction du HTML de la page
    content = response.text
    html_soup = BeautifulSoup(content, 'html.parser')
    print(html_soup)
    
    """
    
    ### resultats de la recherche
    result_container = html_soup.find('div', attrs={'jsname':'rymPhb'})
    print(result_container)
    
    ### parcours des containers
    #for result in result_containers:
    """ 
    return arr_jobs