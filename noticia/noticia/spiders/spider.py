# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from noticia.items import NoticiaItem
from newspaper import Article
from datetime import date
from datetime import datetime



class web_spider(CrawlSpider):
	name = 'noticias'
	allowed_domain = ['www.sciencenews.org']#, 'https://www.screenskills.com/', 'http://designpackagingnews.com']
	start_urls = ['https://www.sciencenews.org/topics']#, 'https://www.screenskills.com/', 'http://designpackagingnews.com/en/']



	def __init__(self, history=False, *args, **kwargs):
		super(web_spider, self).__init__(*args, **kwargs)
		self.history = history


	def parse(self, response):
		noticia1 = response.xpath('//div/article/div/h3/a')
		noticia2 = response.xpath('//*[@id="scroll-anchor"]/main/section/div/div/div/article/a')
		noticia3 = response.xpath('/html/body/div/div/div/div/div/div/div/article/h2/a')
		noticia= noticia1+noticia2+noticia3
		#print(noticia)
		for value in noticia:
			try:
				url = value.xpath('@href').extract()
				article = Article(url[0])
				article.download()
				article.parse()
				ws_item = NoticiaItem()
				if self.history:
					ws_item['link'] = article.url
					ws_item['titulo']=article.title
					ws_item['autor']=article.authors
					ws_item['pubdate'] = article.publish_date
					ws_item['descrip']=article.text
					ws_item['imagen']=article.top_image
					ws_item['video']=article.movies
					yield ws_item
				else:
					hoy = date.today()
					fecha = article.publish_date
					if (fecha.year, fecha.month, fecha.day) == (hoy.year, hoy.month, hoy.day):
						ws_item['link'] = article.url
						ws_item['titulo'] = article.title
						ws_item['autor'] = article.authors
						ws_item['pubdate'] = article.publish_date
						ws_item['descrip'] = article.text
						ws_item['imagen'] = article.top_image
						ws_item['video'] = article.movies
						yield ws_item
			except:
				print('La noticia {} no puedo ser leida'.format(url))
				pass







