# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy
import sqlite3
class QuotesPipeline:
        # def open_spider(self, spider):
        #     self.file = open('quoteresult.jl', 'w')
        #
        # def close_spider(self, spider):
        #     self.file.close()

        def process_item(self, item, spider):

            return item
    # def insert(self,item):
    #     self.curr.execute("""insert into quotes_tb values (?,?)""",(
    #         item['title'],
    #         item['price'],
    #         # item['image'][0],
    #         ))
    #         # item['tag'][0]))
    #     self.conn.commit()