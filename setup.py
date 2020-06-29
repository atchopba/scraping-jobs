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

from io import open
from os import path

from setuptools import setup

path_ = path.abspath(path.dirname(__file__))

long_description = ""

with open(path.join(path_, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="scraping_jobs",
    version="0.0.1",
    description="Scraping jobs on the web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atchopba/scraping-jobs",
    author="atchopba",
    author_email="atchopba@gmail.com",
    classifiers=[
        "Development Status :: 0.0.1",
        "Intended Audience :: web API",
        "License :: GPL-3.0 License ",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="python scraping jobs apec indeed monster",
    install_requires=["pytest>=5.4.3"],
    license="GPL-3.0 License",
    
)
