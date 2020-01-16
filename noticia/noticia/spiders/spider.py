# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from noticia.items import NoticiaItem
from newspaper import Article
import csv


class web_spider(CrawlSpider):
	name = 'noticias'
	item_count = 0
	allowed_domain = ['www.sciencenews.org', 'https://www.screenskills.com/', 'http://designpackagingnews.com']
	start_urls = ['https://www.sciencenews.org/topics', 'https://www.screenskills.com/', 'http://designpackagingnews.com/en/']


	def parse(self, response):
		noticia1 = response.xpath('//h3/a')
		noticia2 = response.xpath('//article/a')
		noticia3 = response.xpath('//h2/a')
		noticia= noticia1+noticia2+noticia3
		print(noticia)
		for value in noticia:
			url = value.xpath('@href').extract()
			article = Article(url[0])
			article.download()
			article.parse()
			ws_item = NoticiaItem()
			ws_item['link'] = article.url
			ws_item['pubdate'] = article.publish_date
			yield ws_item






