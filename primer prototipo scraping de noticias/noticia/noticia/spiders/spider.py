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
	allowed_domain = ['http://www.abc.net.au/news/topic/federal-government?page=',
'http://www.actuary.org/newsreleases?page=',
'http://www.bbc.com/future/tags/sustainability']
	start_urls = ['http://www.abc.net.au/news/topic/federal-government?page=',
'http://www.actuary.org/newsreleases?page=',
'http://www.bbc.com/future/tags/sustainability']


	def parse(self, response):
		lista_caminos = ['//*[@id="article-index"]/ul/li/h3/a',
'//*[@id="block-nt-actuary-content"]/div/div/div/div/div/div[3]/span/a',
'//main/div[1]/div/div/div/div/a',]
		noticia=[]
		for camino in lista_caminos:
			noticia1 = response.xpath(camino)
			noticia += noticia1
		#print(self.allowed_domain)
		#print(noticia)
		for value in noticia:
			try:
				url = value.xpath('@href').extract()[0]
				if 'http' in url:
					article = Article(url)
					article.download()
					article.parse()
					ws_item = NoticiaItem()
					ws_item['link'] = article.url
					ws_item['titulo']=article.title
					ws_item['autor']=article.authors
					ws_item['pubdate'] = article.publish_date
					ws_item['descrip']=article.text
					ws_item['imagen']=article.top_image
					ws_item['video']=article.movies
					yield ws_item
				else:
					for i in range(len(self.allowed_domain)):
						try:
							url = value.xpath('@href').extract()[0]
							url = self.allowed_domain[i] + url
							article = Article(url)
							article.download()
							article.parse()
							ws_item = NoticiaItem()
							ws_item['link'] = article.url
							ws_item['titulo'] = article.title
							ws_item['autor'] = article.authors
							ws_item['pubdate'] = article.publish_date
							ws_item['descrip'] = article.text
							ws_item['imagen'] = article.top_image
							ws_item['video'] = article.movies
							yield ws_item
						except:
							pass
			except:
				pass







