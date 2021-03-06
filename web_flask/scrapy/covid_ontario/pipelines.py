# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from urllib.parse import quote_plus
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
from covid_ontario.items import CovidOntarioItem


class MongoDBPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        uri = "mongodb://%s:%s@%s:%s" % (quote_plus(settings['MONGODB_USER']), quote_plus(
            settings['MONGODB_PASS']), settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        connection = pymongo.MongoClient('mongodb://juniha:Rodyroem@cluster0-shard-00-00-naqor.mongodb.net:27017,cluster0-shard-00-01-naqor.mongodb.net:27017,cluster0-shard-00-02-naqor.mongodb.net:27017/covid_ontario?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
        db = connection[settings['MONGODB_DB']]
        self.status_collection = db[settings['MONGODB_STATUS_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if isinstance(item, CovidOntarioItem):
                self.status_collection.update(
                    {'date': item['date']}, dict(item), True)
        return item
