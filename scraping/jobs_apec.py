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

# pour le contrôle des requêtes
from time import time

from scraping.jobs import scraping_jobs

# pour transformer les données obtenues
import common as jc


class scraping_jobs_apec(scraping_jobs):
    
    #
    def set_code_dpt(self, code_dpt):
        self.code_dpt = code_dpt
    
    #
    def scrap_job(self):
        ### paramètres pris
        # les termes doivent être séparés par ' ' ou '%20'
        param_search_words = self.s_job #'developpeur aws'
        # le numéro du département
        param_search_location = self.code_dpt
        # type de contrat du job
        param_type_contract = self.type_contract #''
        
        ### type de job
        arr_type_contract = {
            'perm' : '101888',
            'full' : '101888',
            'ints' : '20053',
            'free' : '101887'
            }
        str_type_contract = '' # TODO use this
        if param_type_contract != '' and arr_type_contract[param_type_contract] is not None: 
            str_type_contract = 597171
        
        ### pages à parcourir
        pages = [str(i) for i in range(0, jc.NB_PAGE)]
        requests = 0
        start_time = time()
        
        dict_jobs = []
        
        ### parcours des pages
        for page in pages:
            #
            root_path = 'https://www.apec.fr/cms/webservices/rechercheOffre'
            payload = {
                'lieux': [param_search_location],
                'typeClient': 'CADRE',
                'sorts' : [{
                    'type': 'SCORE',
                    'direction': 'DESCENDING'
                }],
                'pagination': {
                    'range': 20,
                    'startIndex': page
                },
                'activeFiltre': True,
                'pointGeolocDeReference': {
                    'distance': 0
                },
                'motsCles': param_search_words
            }
            
            json_data = jc.post_data(root_path, payload, requests, start_time)
            
            ### vérifier l'existence de l'index 'resultats'
            if 'resultats' in json_data:
                result_containers = json_data['resultats']
            
                ### extraction des données du JSON renvoyé
                for result in result_containers:
                    #
                    dict_jobs.append({
                        'title' : result['intitule'],
                        'link' : 'https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/'+result['numeroOffre'],
                        'location' : result['lieuTexte'],
                        'description' : result['texteOffre'],
                        'company' : result['nomCommercial'],
                        'note' : result['score'],
                        'salary' : result['salaireTexte'],
                        'publication_date' : result['datePublication'],
                        'publication_time' : ''
                    })
            
        ### retourne array
        return dict_jobs
