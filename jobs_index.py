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

# pour la gestion des paramètres
import sys

from warnings import warn

#####
# Pour lancer le programme dans le shell:
# python jobs_index.py "libellé du job recherché" Ville NuméroDépartement TypeDeContrat
# 
# Pour par exemple lancer
# python jobs_index.py "developpeur aws" Nantes 44 free
#####

# vérification du nb de paramètres
if len(sys.argv) not in (4, 5):
    warn('le programme a besoin de 4 paramètres')
    exit()

s_job = sys.argv[1]
city = sys.argv[2]
num_dpt = sys.argv[3]
type_contract = ''
if len(sys.argv) == 5:
	type_contract = sys.argv[4]

import jobs_common as jc
import jobs_apec as japec
import jobs_indeed as jindeed
import jobs_monster as jmonster

# array of jobs
arr_jobs = []

print('please wait, search in progress...')

## apec.fr
arr_jobs = japec.scrap_job(arr_jobs, s_job, num_dpt, type_contract)

## indeed.fr
arr_jobs = jindeed.scrap_job(arr_jobs, s_job, city, num_dpt, type_contract)

## monster.fr
arr_jobs = jmonster.scrap_job(arr_jobs, s_job, city, type_contract)

### 

### impression des jobs en json
print(jc.jprint(arr_jobs))
