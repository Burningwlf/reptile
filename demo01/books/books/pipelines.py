# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class BooksMySQLPipeline(object):
    def open_spider(self,spider):

        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',db='novel', password='1234', charset='utf8')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        sql = 'insert into jinyong(name,zhangjie,content) VALUES (%s,%s,%s);'
        self.cursor.execute(sql,(item['name'],item['zhangjie'],item['content']))
        self.conn.commit()
        return item

    def close_spider(self, spider):

        self.cursor.close()
        self.conn.close()

