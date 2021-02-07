import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scraper.items import NewsArticle

class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = ['https://cnn.com/africa']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1/text()').get()
        article['description'] = response.xpath('//meta[@name="description"]/@content').get()
        article['date'] = response.xpath('//meta[')