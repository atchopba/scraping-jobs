#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Albin TCHOPBA"
__copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
__credits__ = ["Albin TCHOPBA and contributors"]
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Albin TCHOPBA"
__email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
__status__ = "Production"

import json

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
    # return repr(json.dumps(obj, sort_keys=True)) #, indent=4

