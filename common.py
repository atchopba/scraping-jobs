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

import json

# pour exploiter les requêtes
from requests import post

# pour le contrôle des requêtes
from time import sleep, time
from random import randint


from warnings import warn

### nombre de requêtes
NB_REQUETE = 10

### nombre maxi de page
NB_PAGE = 2

def convert_arr_2_string(arr, sep):
    """ Convert array to string with separator """
    return sep.join(arr)

def get_term(path):
    """ get term in a path. Otherwise, return 'Non renseigné' """
    if path is not None:
        return path.text.strip()
    return ''

def jprint(obj):
    """ convert array to json """
    # create a formatted string of the Python JSON object
    return json.dumps(obj, sort_keys=True) #, indent=4 

def post_data(root_path, payload, requests, start_time):
    """ post data and get the result  """
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
    if requests > NB_REQUETE:
        warn('Nombre de requêtes trop important')
        return
    
    try:
        json_data = json.loads(content)
    except:
        json_data = ""
    
    return json_data
