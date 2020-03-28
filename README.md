# Overview

Scraping jobs allow to extract job offers from majors job boards (currently, indeed.fr, apec.fr, monster.fr), store them locally in JSON format. More importantly, it provides on top of the collected data an simple and unified job search.

You can easily search for jobs using only key parameters, including: 
- the title of the job you are looking for,
- the name of city (in France),
- the code of the department in which the city is located and
- the type of contract you want.

## Benefits 

* Make it easier to find a job

* Gather information from several sites.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Windows 7+ or Linux kernel version 3.10 or higher
* 2.00 GB of RAM
* 3.00 GB of available disk space

Use with Docker http://www.docker.io

### Installation

To build an image with docker is pretty simple:
```
docker build -t jobs-cli .
```

## Using the tool

Then to run that image and attach to it at the same time:
```
docker run jobs-cli "job search" City codeDpt TypeContract
```
TypeContract value : perm (permanent), full (fulltime), ints (intership), free (freelance)
Example: 
```
docker run jobs-cli "developpeur aws" Nantes 44 free
```

## License & copyright

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details
