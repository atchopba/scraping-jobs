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
code_dpt = sys.argv[3]
type_contract = ''
if len(sys.argv) == 5:
	type_contract = sys.argv[4]

import common as jc
from scraping.jobs_apec import scraping_jobs_apec
from scraping.jobs_indeed import scraping_jobs_indeed
from scraping.jobs_monster import scraping_jobs_monster

# array of jobs
arr_jobs = []

print('please wait, search in progress...')

## apec.fr
sjapec = scraping_jobs_apec(s_job, type_contract)
sjapec.set_code_dpt(code_dpt)
dict_tmp = sjapec.scrap_job()
if len(dict_tmp) > 0:
    arr_jobs += dict_tmp

## indeed.fr
sjindeed = scraping_jobs_indeed(s_job, type_contract)
sjindeed.set_city(city)
sjindeed.set_code_dpt(code_dpt)
dict_tmp = sjindeed.scrap_job()
if len(dict_tmp) > 0:
    arr_jobs += dict_tmp

## monster.fr
sjmonster = scraping_jobs_monster(s_job, type_contract)
sjmonster.set_city(city)
dict_tmp = sjmonster.scrap_job()
if len(dict_tmp) > 0:
    arr_jobs += dict_tmp

### 

### impression des jobs en json
print(jc.jprint(arr_jobs))
