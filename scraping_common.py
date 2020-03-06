#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:05:19 2020

@author: 7h3 d34d
"""

import json

### nombre de requêtes
NB_REQUETE = 10

### nombre maxi de page
NB_PAGE = 2

### non renseigné
NON_RENSEIGNE = 'Non renseigné'

def convert_arr_2_string(arr, sep):
    """ Convert array to string with separator """
    return sep.join(arr)

def get_term(path):
    """ get term in a path. Otherwise, return 'Non renseigné' """
    if path is not None:
        return path.text.strip()
    return 'Non renseigné'

def jprint(obj):
    """ convert array to json """
    # create a formatted string of the Python JSON object
    return repr(json.dumps(obj, sort_keys=True)) #, indent=4

