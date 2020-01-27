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
from datetime import timedelta



class web_spider(CrawlSpider):
	name = 'noticias'
	allowed_domain = #aqui va el ambiente de dominios
	start_urls = #aqui va las paginas iniciales



	def __init__(self, history=False, *args, **kwargs):
		super(web_spider, self).__init__(*args, **kwargs)
		self.history = history


	def parse(self, response):
		caminos = #aqui va el ambiente de los caminos
		for camino in caminos:
			noticia1 = response.xpath(camino)
			noticia += noticia1
		#print(noticia)
		hoy = date.today()
		ayer = hoy - timedelta(days=1)
		for value in noticia:
			try:
				url = value.xpath('@href').extract()
				article = Article(url[0])
				article.download()
				article.parse()
				ws_item = NoticiaItem()
				fecha = article.publish_date
				if self.history:
					ws_item['link'] = article.url
					ws_item['titulo']=article.title
					ws_item['autor']=article.authors
					ws_item['pubdate'] = article.publish_date
					ws_item['descrip']=article.text
					ws_item['imagen']=article.top_image
					ws_item['video']=article.movies
					yield ws_item
				elif(fecha.year, fecha.month, fecha.day) == (hoy.year, hoy.month, hoy.day) or \
						(fecha.year, fecha.month, fecha.day) == (ayer.year, ayer.month, ayer.day):
					ws_item['link'] = article.url
					ws_item['titulo'] = article.title
					ws_item['autor'] = article.authors
					ws_item['pubdate'] = article.publish_date
					ws_item['descrip'] = article.text
					ws_item['imagen'] = article.top_image
					ws_item['video'] = article.movies
					yield ws_item
				else:
					pass
			except:
				print('La noticia {} no puedo ser leida'.format(url))
				pass







