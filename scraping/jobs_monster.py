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
from requests import post

# pour le contrôle des requêtes
from time import sleep
from random import randint
from time import time
from warnings import warn

# pour gérer json
import json

from scraping.jobs import scraping_jobs

# pour transformer les données obtenues
import common as jc


class scraping_jobs_monster(scraping_jobs):
    #
    def set_city(self, city):
        self.city = city
    
    #
    def scrap_job(self):
                
        # 
        dict_jobs = []
        
        requests = 0
        start_time = time()
        
        dict_jobs = []
        
        ### parcours des pages
        for page in range(0, jc.NB_PAGE):
            #
            root_path = 'https://appsapi.monster.io/jobs-svx-service/v2/monster/search-jobs/samsearch/fr-FR?apikey=ulBrClvGP6BGnOopklreIIPentd101O2'
            payload = {
                "jobQuery": {
                    "query": self.s_job,
                    "locations": [{
                            "country": "fr",
                            "address": self.city,
                            "radius": {
                                "unit": "km",
                                "value": 20
                            }
                        }
                    ]
                },
                "jobAdsRequest": {
                    "position": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    "placement": {
                        "component": "JSR_SPLIT_VIEW",
                        "appName": "monster"
                    }
                },
                "fingerprintId": "4d11b5a4abf5c3062388257b9ee39e93",
                "offset": page * 9,
                "pageSize": 9,
                "includeJobs": []
            }
            response = post(root_path, json=payload)
            
            content = response.content
            
            ### pause de 8 à 15s
            sleep(randint(8, 15))
            
            ### afficher les informations sur les requêtes
            requests += 1 # incrémentation du nombre de requête
            elapsed_time = time() - start_time
            
            ### avertir si le code status est différent de 200
            if response.status_code != 200:
                warn('Request: {}; Status code:{}'.format(requests, requests/elapsed_time))
            
            ### stopper quand les requêtes atteignent le quota
            if requests > jc.NB_REQUETE:
                warn('Nombre de requêtes trop important')
                break
            
            try:
                json_data = json.loads(content)
            except:
                json_data = ""
            
            ### vérifier l'existence de l'index 'resultats'
            if 'jobResults' in json_data:
                result_containers = json_data['jobResults']
            
                ### extraction des données du JSON renvoyé
        
                ### extraction des données du JSON renvoyé
                for result in result_containers:
                    # get salary
                    salary = ''
                    if 'baseSalary' in result['jobPosting']:
                        minValue = result['jobPosting']['baseSalary']['value']['minValue'] if 'minValue' in result['jobPosting']['baseSalary']['value'] else ''
                        maxValue = result['jobPosting']['baseSalary']['value']['maxValue'] if 'maxValue' in result['jobPosting']['baseSalary']['value'] else ''
                        unitText = result['jobPosting']['baseSalary']['value']['unitText'] if 'unitText' in result['jobPosting']['baseSalary']['value'] else ''
                        salary = str(minValue) + ' - ' + str(maxValue) + ' '+ unitText
                    # get location
                    location = result['jobPosting']['jobLocation'][0]['address']['addressLocality'] if len(result['jobPosting']['jobLocation']) > 0 else ''
                    #
                    dict_jobs.append({
                        'title' : result['jobPosting']['title'],
                        'link' : result['jobPosting']['url'],
                        'location' : location,
                        'description' : result['jobPosting']['description'],
                        'company' : result['jobPosting']['hiringOrganization']['name'],
                        'note' : '',
                        'salary' : salary,
                        'publication_date' : result['jobPosting']['datePosted'],
                        'publication_time' : ''
                    })
            
        ### retourne array
        return dict_jobs
