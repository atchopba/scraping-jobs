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

from abc import ABCMeta, abstractmethod

class scraping_jobs(metaclass=ABCMeta):
    
    def __init__(self, s_job, type_contract):
        self.s_job = s_job
        self.type_contract = type_contract
    
    @abstractmethod
    def scrap_job(self, dict_jobs, s_job, type_contract):
        pass
    