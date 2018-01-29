# -*- coding: utf-8 -*-
import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OlxPipeline(object):

    def process_item(self, item, spider):
        self.conn.execute(
            'insert into cars (title, ports, year) values (:title, :ports, :year)',
            item            
        )
        self.conn.commit()
        return item
        
    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "cars"'
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table cars(id integer primary key, title text, ports text, year text)'
            )
    
    def open_spider (self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider (self, spider):
        self.conn.close()