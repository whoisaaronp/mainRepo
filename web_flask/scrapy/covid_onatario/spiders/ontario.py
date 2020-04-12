
import scrapy
from covid_ontario.items import CovidOntarioItem
from scrapy.utils.response import open_in_browser
from datetime import datetime
import time

class OntarioSpider(scrapy.Spider):
    name = 'ontario'
    allowed_domains = ['www.ontario.ca']
    start_urls = ['https://www.ontario.ca/page/2019-novel-coronavirus']

    def parse(self, response):
        status_item = CovidOntarioItem()
        # some debugging here, remove it when you're done
        # self.logger.warning('Table HTML %s', response)
        # open_in_browser(response)
        status_dict = {
            'Number of cases': 'confirmed',
            'Resolved': 'resolved',
            'Deceased': 'deceased',
            'Investigation': 'pending',
            'Total': 'total',
            'Male': 'male',
            'Female': 'female',
            '19': 'youth',
            '20': '20-39',
            '40': '40-59',
            '60': '60-79',
            '80': 'senior',
        }

