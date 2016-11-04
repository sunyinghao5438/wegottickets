# -*- coding: utf-8 -*-

import scrapy


class WegotticketsItem(scrapy.Item):
    artists = scrapy.Field() 	#the artists playing
    city = scrapy.Field()     	#the city
    venue = scrapy.Field()   	#the name of the venue
    date = scrapy.Field()   	#the date
    price = scrapy.Field()   	#the price