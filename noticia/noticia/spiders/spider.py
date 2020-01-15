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


rutas={'Dominio':['www.sciencenews.org', 'https://www.screenskills.com/'],#, 'http://designpackagingnews.com'],
       'camino':['//h3/a', '//article/a'],#, '//h2/a'],
       'inicial_page':['https://www.sciencenews.org/topics', 'https://www.screenskills.com/']}#, 'http://designpackagingnews.com/en/']}

lista = []
for x in range(2):
	class web_spider(CrawlSpider):
		name = 'noticias'
		item_count = 0
		allowed_domain = [str(rutas['Dominio'][x])]
		start_urls = [str(rutas['inicial_page'][x])]

		def parse(self, response):
			noticia = response.xpath(str(rutas['camino'][x]))
			#print(noticia)
			for value in noticia:
				url = value.xpath('@href').extract()
				article = Article(url[0])
				article.download()
				article.parse()
				ws_item = NoticiaItem()
				lista.append(article.title)
				#lista.append( article.text)
				lista.append('\n\n')
				#print(lista)
				#ws_item['link'] = article.url
				#ws_item['pubdate'] = article.publish_date
				yield ws_item

			print(len(lista))
with open("output.csv", "w") as f:
	w = csv.writer(f)
	w.writerow(lista)





