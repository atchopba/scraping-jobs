#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

# pour exploiter les requêtes
from requests import get
from bs4 import BeautifulSoup

# pour le contrôle des requêtes
from time import sleep
from random import randint
from time import time
from IPython.display import clear_output
from warnings import warn

# pour transformer les données obtenues
import jobs_common as jc


def scrap_job(arr_jobs, s_job, city, num_dpt, type_contract):
    
    ### paramètres pris
    # les termes doivent être séparés par '+'
    param_search_words = jc.convert_arr_2_string(s_job.split(' '), '+') #'developpeur+aws'
    # le/la ville/département + (le numéro du département) => sans espace
    param_search_location = city + '+' + num_dpt #'Nantes+(44)'
    # type de contrat du job
    param_type_contract = type_contract #'free'
    
    ### type de job
    arr_type_contract = {
        'all' : '',
        'perm' : 'permanent',
        'full' : 'fulltime',
        'ints' : 'internship',
        'free' : 'subcontract'
        }
    str_type_contract = ''
    if param_type_contract != '' and arr_type_contract[param_type_contract] is not None: 
        str_type_contract = 'jt='+arr_type_contract[param_type_contract]
    
    ### pages à parcourir
    pages = [str(i*10) for i in range(0, jc.NB_PAGE)]
    requests = 0
    start_time = time()
    
    ### parcours des pages
    for page in pages:
        # 
        root_path = 'https://www.indeed.fr/jobs?q='+ param_search_words +'&l='+ param_search_location +'&start='+page+'&'+str_type_contract
        #print(root_path)
        #break
        response = get(root_path)
        
        ### pause de 8 à 15s
        sleep(randint(8, 15))
        
        ### afficher les informations sur les requêtes
        requests += 1 # incrémentation du nombre de requête
        elapsed_time = time() - start_time
        print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait=True)
        
        ### avertir si le code status est différent de 200
        if response.status_code != 200:
            warn('Request: {}; Status code:{}'.format(requests, requests/elapsed_time))
        
        ### stopper quand les requêtes atteignent le quota
        if requests > jc.NB_REQUETE:
            warn('Nombre de requêtes trop important')
            break
        
        ### extraction du HTML de la page
        content = response.text
        html_soup = BeautifulSoup(content, 'html.parser')
        
        ### resultats de la recherche
        result_containers = html_soup.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')
        
        ### parcours des containers
        for result in result_containers:
            
            try:
                ### ajout des resultats dans les tableaux
                # titre
                tmp_title = result.find('h2', class_='title')
                #
                title = tmp_title.a['title'].strip()
                # lien
                link = tmp_title.a['href'].strip()
                # localisation 
                location = ''
                if result.find('div', class_='location') is not None:
                    location = result.find('div', class_='location').text.strip()
                elif result.find('span', class_='location') is not None:
                    location = result.find('span', class_='location').text
                # description
                description = result.ul.text.strip()
                # entreprise
                company = ''
                if result.find('span', class_='company').a is not None:
                    company = result.find('span', class_='company').a.text.strip()
                elif result.find('span', class_='company') is not None:
                    company = result.find('span', class_='company').text.strip()
                # note
                note = jc.get_term(result.find('span', class_='ratingsContent'))
                # salaire
                salary = jc.get_term(result.find('span', class_='salaryText'))
                
                # date de publication
                publication_date = result.find('span', class_='date').text.strip()
                
                arr_jobs.append({
                    'title' : title,
                    'link' : 'https://www.indeed.fr'+link,
                    'location' : location,
                    'description' : description,
                    'company' : company,
                    'note' : note,
                    'salary' : salary,
                    'publication_date' : publication_date,
                    'publication_time' : ''
                })
            except AttributeError as ae:
                warn("Error : ", ae)

    ### retourne array
    return arr_jobs
