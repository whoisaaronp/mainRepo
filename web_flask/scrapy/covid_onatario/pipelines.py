# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from urllib.parse import quote_plus
from scrapy.utis.project import get_project_settings
from scrapy.exceptions import Dropitem
from covid_ontario.items import CovidOntarioStatusItem

class MongoDBPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        uri = "mongodb://%s:%s@%s:%s" % (quote_plus(settings['MONGODB_USER']), quote_plus(
            settings['MONGODB_PASS']), settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        connection = pymongo.MongoClient(uri)
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if isinstance(item, CovidOntarioStatusItem)
            self.collection.update(dict(item))

        return item
