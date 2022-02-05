import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class deneme(CrawlSpider):
    name = 'scraper'
    #allowed_domains = ['hepsiburada.com']
    start_urls = ['https://www.youtube.com/watch?v=Gw2jWWJbduI']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    print(rules)
    def parse_item(self, response):


        print(response)
        print(response.xpath('//p[@class="review-text"]/text()').extract())