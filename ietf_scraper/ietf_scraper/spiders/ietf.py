# -*- coding: utf-8 -*-
import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.css('span.title::text').get()
        title = responde.xpath('//span[@class="title"]/text()').get()
        return {"title":title}
        
