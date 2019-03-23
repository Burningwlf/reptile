# -*- coding: utf-8 -*-
import scrapy

from books.items import BooksItem


class JinyongSpider(scrapy.Spider):
    name = 'jinyong'
    allowed_domains = ['jinyongwang.com']
    start_urls = ['http://www.jinyongwang.com/book/']

    def parse(self, response):

        links = response.xpath("//div[@class='booklist']/ul[@class='list'][1]/li")
        for link in links:
            url = link.xpath(".//p[@class='title']/a/@href").get()
            yield scrapy.Request(url=response.urljoin(url), callback=self.get_zhangjie)
            # break

    def get_zhangjie(self,response):
        zhangjies = response.xpath("//ul[@class='mlist']/li")
        for zhangjie in zhangjies:
            url = zhangjie.xpath(".//a/@href").get()
            yield scrapy.Request(url=response.urljoin(url), callback=self.get_content)

    def get_content(self,response):
        item = BooksItem()

        name = response.xpath("//span[@id='breadnav']/a[2]/text()").get()
        item["name"] = name

        zhangjie = response.xpath("//h1[@id='title']/text()").get()
        item["zhangjie"] = zhangjie

        zhangjie_content = ""
        contents = response.xpath("//div[@class='vcon']/p/text()").extract()
        for content in contents:
            zhangjie_content = zhangjie_content + content
            item["content"] = zhangjie_content

        yield item



