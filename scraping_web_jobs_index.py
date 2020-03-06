#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:04:03 2020

@author: 7h3 d34d
"""
# pour la gestion des paramètres
import sys

from warnings import warn

#####
# Pour lancer le programme dans le shell:
# python scraping_web_jobs_index.py "libellé du job recherché" Ville NuméroDépartement TypeDeContrat
# 
# Pour par exemple lancer
# python scraping_web_jobs_index.py "developpeur aws" Nantes 44 free
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

import scraping_common as shc
import scraping_web_jobs_apec as japec
#import scraping_web_jobs_google as jgoogle
import scraping_web_jobs_indeed as jindeed
import scraping_web_jobs_monster as jmonster

# array of jobs
arr_jobs = []

## apec.fr
arr_jobs = japec.scrap_job(arr_jobs, s_job, num_dpt, type_contract)

## indeed.fr
arr_jobs = jindeed.scrap_job(arr_jobs, s_job, city, num_dpt, type_contract)

## monster.fr
arr_jobs = jmonster.scrap_job(arr_jobs, s_job, city, type_contract)

### 

### impression des jobs en json
print(shc.jprint(arr_jobs))
