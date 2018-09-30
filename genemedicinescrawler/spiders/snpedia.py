# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from scrapy.loader import ItemLoader
from genemedicinescrawler.items import GenemedicinescrawlerItem
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose, Join
class SnpediaSpider(scrapy.Spider):
    name = 'snpedia'
    allowed_domains = ['snpedia.com']
    start_urls = ['https://bots.snpedia.com/api.php?action=query&list=categorymembers&cmtitle=Category:Is_a_medicine&format=json&cmlimit=500']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ["name", "description"]
    }
    def parse_page(self, response):
        js = json.loads(response.body)
        wikitext = Selector(text=js['parse']['text']['*'])
        l = ItemLoader(item=GenemedicinescrawlerItem(), selector=wikitext, response=response)
        l.add_xpath('description', '//div',MapCompose(unicode.strip), Join())
        l.add_value('name', js['parse']['title'])
        return l.load_item()

    def parse(self, response):
        js = json.loads(response.body)
        if hasattr(js,'continue'):
            yield Request(response.url + '&' + urllib.urlencode(getattr(js,'continue')))
        
        for pages in js['query']['categorymembers']:
            yield Request('https://bots.snpedia.com/api.php?action=parse&prop=text&format=json&pageid=' + str(pages['pageid']), callback=self.parse_page)

        pass
