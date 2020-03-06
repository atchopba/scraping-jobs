# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

Scrap jobs on apec.fr, indeed.fr, monster.fr

To do : google.fr, pole-emploi.fr

### How do I get set up? ###

* Install python 3.7 : https://www.python.org/downloads/release/python-376/

Install modules 

* python -m pip install --upgrade pip

* pip install BeautifulSoup4

* pip install ipython 

### How test? ###

* python scraping_web_jobs_index.py "job search" City NumDpt TypeContract

TypeContract value : perm (permanent), full (fulltime), ints (intership), free (freelance)

* Example: python scraping_web_jobs_index.py "developpeur aws" Nantes 44 free

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines