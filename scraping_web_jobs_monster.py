#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:37:06 2020

@author: 7h3d d34d
"""

# pour exploiter les requêtes
from requests import get
from bs4 import BeautifulSoup

# pour transformer les données obtenues
import scraping_common as shc


def scrap_job(arr_jobs, s_job, city, type_contract):
    
    ### paramètres pris
    # les termes doivent être séparés par '-'
    param_search_words = shc.convert_arr_2_string(s_job.split(' '), '-') #'developpeur-aws'
    # le/la ville/département
    param_search_location = city #'Nantes'
    # type de contrat du job
    param_type_contract = type_contract #''
     
    ### type de job
    arr_type_contract = {
        'perm' : 'CDI_8',
        'full' : 'Temps-Plein_8',
        'ints' : 'Stage-Apprentissage-Alternance_8',
        'free' : 'Indépendant-Freelance-Saisonnier_8'
        }
    str_type_contract = ''
    if param_type_contract != '' and arr_type_contract[param_type_contract] is not None: 
        str_type_contract = arr_type_contract[param_type_contract]
    
    ### pages à parcourir
    pages = str(shc.NB_PAGE)
    
    # 
    root_path = 'https://www.monster.fr/emploi/recherche/'+ str_type_contract +'?q='+ param_search_words +'&where='+ param_search_location +'&cy=fr&stpage=1&page='+pages
    response = get(root_path)
    
    ### extraction du HTML de la page
    content = response.text
    html_soup = BeautifulSoup(content, 'html.parser')
    
    ### resultats de la recherche
    tmp_result_container = html_soup.find('div', id='ResultsContainer')
    result_containers = tmp_result_container.find_all('section', class_='card-content')
    
    ### parcours des containers
    for result in result_containers:
    
        # s'il y a un titre    
        if result.find('h2', class_='title') is not None:
            
            ### ajout des resultats dans les tableaux
            # titre
            tmp_title = result.find('h2', class_='title')
            # print(tmp_title)
            title = tmp_title.a.text.strip()
            # lien
            link = tmp_title.a['href'].strip()
            # entreprise
            company = ''
            if result.find('div', class_='company').a is not None:
                company = result.find('div', class_='company').a.text.strip()
            # localisation 
            location = ''
            if result.find('div', class_='location').span is not None:
                location = result.find('div', class_='location').span.text.strip()
            elif result.find('div', class_='location').a is not None:
                location = result.find('div', class_='location').a.text.strip()
            # date de publication
            tmp_time = result.find('time')
            publication_date = tmp_time.text.strip()
            publication_time = tmp_time['datetime'].strip()
            
            arr_jobs.append({
                'title' : title,
                'link' : link,
                'location' : location,
                'description' : '',
                'company' : company,
                'note' : '',
                'salary' : '',
                'publication_date' : publication_date,
                'publication_time': publication_time
            })
    
    ### retourne array
    return arr_jobs
