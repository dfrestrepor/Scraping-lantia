# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tutorial.items import web_item
from bs4 import BeautifulSoup
import re


class web_spider(CrawlSpider):
    name = 'web_scraping'
    item_count = 0
    base_url = 'https://www.youtube.com'
    start_urls = ['https://www.youtube.com/channel/UCiMg06DjcUk5FRiM3g5sqoQ']

    rules = {
        Rule(LinkExtractor(allow=(r'/watch?')),
             # , restrict_text = (base_url + str(response.xpath("//ytd-grid-video-renderer/div[1]/div[@id='details']/div/h3[1]/a/@href").get))),
             callback='parse_item', follow=False)
    }

    # Rule(LinkExtractor(allow =(), restrict_xpaths = ("//*[@id='bottom-pager']/div/div/div[2]/div/a/@href")))
    # }

    def find_urls(response):
        urls = re.findall(
            'https://www.youtube.com/watch?(.)', response)
        return urls

    def parse_item(self, response):
        ws_item = web_item()
        soup = BeautifulSoup(response.body, "html.parser")
        # informacion elementos
        ws_item['titulo'] = response.xpath("normalize-space(//*[@id='description']/yt-formatted-string/text()[1])").extract()
        #ws_item['titulo'] = soup.find_all('h1', {'class': 'style-scope ytd-video-primary-info-renderer'})

        # ws_item['url'] = 'https://www.merlot.org/merlot/viewMaterial.htm?id=' +\
        # str(response.xpath('normalize-space()').extract()[0])

        # ws_item['autor'] = str(response.xpath('normalize-space()').extract()[0])

        # ws_item['contenido'] = str(response.xpath('normalize-space(//*[@id="material_description"]/p/text())').extract()[0])

        self.item_count += 1
        if self.item_count > 5:
            raise CloseSpider('item_exceeded')
        yield ws_item
