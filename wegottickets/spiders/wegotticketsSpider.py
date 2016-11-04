# -*- coding: utf-8 -*-

from wegottickets.items import WegotticketsItem
from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

class wegottickets(CrawlSpider):
    #Spider name
    name = "wegottickets"
    #Spider only in this domain
    allowed_domains = ["www.wegottickets.com"]
    #Start from here
    start_urls = ["http://www.wegottickets.com/searchresults/page/1/all#paginate",]
    #Set rule using regex in scrapy
    rules = (
        Rule(LinkExtractor(allow=r"searchresults/page/\d+/all#paginate"),
         callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        sel = response.selector
        #Got all div class named "content block-group chatterbox-margin"
        events = sel.xpath('//div[@class="content block-group chatterbox-margin"]')
        items = []
        for event in events:   
            item = WegotticketsItem()
            #There is no artists in most of events
            item['artists'] =  event.xpath('div[@class="block diptych chatterbox-margin"]/div[@class="venue-details"]/h4[3]/i/text()').extract_first() 
            #Actually we can only get the city's name, anyway, we can deal with the data later
            item['city'] =  event.xpath('div[@class="block diptych chatterbox-margin"]/div[@class="venue-details"]/h4[1]/text()').extract_first() 
            item['venue'] =  event.xpath('h2/a/text()').extract_first() 
            item['date'] = event.xpath('div[@class="block diptych chatterbox-margin"]/div[@class="venue-details"]/h4[2]/text()').extract_first() 
            #\u00a3 is £
            item['price'] = event.xpath('div[@class="block diptych text-right"]/div[@class="searchResultsPrice"]/strong/text()').extract_first() 
            items.append(item)
        return items