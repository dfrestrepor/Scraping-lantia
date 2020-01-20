from newspaper import Article

article = Article('https://www.redalyc.org/articulo.oa?id=287123554018')
article.download()
article.parse()
link = article.url
titulo = article.title
print(link)
print(titulo)