# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tutorial.items import web_item


class web_spider(CrawlSpider):
    name = 'web_scraping'
    item_count = 0
    allowed_domain = ['www.merlot.org/merlot']
    start_urls = ['https://www.merlot.org/merlot/materials.htm?sort.property=overallRating']

    rules = {
        # Para cada item
        Rule(LinkExtractor(allow=(),
                           restrict_xpaths=('//*[@id="merlotCollection"]/div[2]/div[2]/div[4]/div/nav/ul/li[10]/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="card-header"]/div/h4')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        ws_item = web_item()
        # informacion elementos
        ws_item['titulo'] = response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/h2/text())').extract()

        ws_item['url'] = 'https://www.merlot.org/merlot/viewMaterial.htm?id=' + \
                         str(response.xpath('normalize-space(//div[@class="col detail-title"]/input/@value)').extract()[
                                 0])

        ws_item['autor'] = str(response.xpath(
            'normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/span/text())').extract()[0])  # +\
        # str(response.xpath('normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/a[1]/span[2])').extract()[0])

        if len(ws_item['autor']) == 0:
            ws_item['autor'] = str(response.xpath(
                'normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/a[1]/span[1])').extract()[0])

        ws_item['contenido'] = str(
            response.xpath('normalize-space(//*[@id="material_description"]/p/text())').extract()[0])
        if len(ws_item['contenido']) == 0:
            ws_item['contenido'] = str(response.xpath(
                'normalize-space(// *[@id="material_description"]/text()[1])').extract()[0])

        self.item_count += 1
        if self.item_count > 35:
            raise CloseSpider('item_exceeded')
        yield ws_ite
