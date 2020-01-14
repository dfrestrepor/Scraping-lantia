# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from noticia.items import NoticiaItem
from newspaper import Article

class web_spider(CrawlSpider):
	name = 'noticias'
	item_count = 0
	allowed_domain = ['www.sciencenews.org']
	start_urls = ['https://www.sciencenews.org/topics']
	"""
	rules = {
		# Para cada item
		#Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="merlotCollection"]/div[2]/div[2]/div[4]/div/nav/ul/li[10]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h3/a/@href')),
							callback = 'parse_item', follow = False)
	}
	"""
	def parse(self, response):
		noticia = response.xpath('//*[@id="content"]/section/div/article/div/h3/a')
		print(noticia)
		for value in noticia:
			url = value.xpath('@href').extract()
			article = Article(url[0])
			article.download()
			article.parse()
			ws_item = NoticiaItem()
			ws_item['titulo'] = article.title
			ws_item['descrip'] = article.text
			ws_item['link'] = article.url
			ws_item['pubdate'] = article.publish_date
			yield ws_item

	#def parse_item(self, response):
		#ws_item = NoticiaItem()
		#print(response)
		#article = Article(response)
		#print(article.title)
		#informacion elementos
		#ws_item['titulo'] = response.xpath('normalize-space(/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/h2/text())').extract()

		#ws_item['url'] = 'https://www.merlot.org/merlot/viewMaterial.htm?id=' +\
						# str(response.xpath('normalize-space(//div[@class="col detail-title"]/input/@value)').extract()[0])

		#ws_item['autor'] = str(response.xpath('normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/span/text())').extract()[0])# +\
			#str(response.xpath('normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/a[1]/span[2])').extract()[0])

		#if len(ws_item['autor']) == 0:
		#	ws_item['autor'] = str(response.xpath(
		#		'normalize-space(/html/body/div[2]/div[2]/div[3]/div[1]/dl/dd[4]/span/a[1]/span[1])').extract()[0])

		#ws_item['contenido'] = str(response.xpath('normalize-space(//*[@id="material_description"]/p/text())').extract()[0])
		#if len(ws_item['contenido']) == 0:
		#	ws_item['contenido'] = str(response.xpath(
		#		'normalize-space(// *[@id="material_description"]/text()[1])').extract()[0])


		#self.item_count += 1
		#if self.item_count > 35:
		#	raise CloseSpider('item_exceeded')
		#yield ws_item
