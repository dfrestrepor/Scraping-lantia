import urllib
from bs4 import BeautifulSoup
import json
import urllib.request as libreq
import re
from categorias import lista
import funciones


data_arxiv = {}
data_arxiv['arxiv'] = []
titulos = []
autores = []
abstract = []
links = []
fechas = []
lis= lista()

for codigo in lis:
    link = 'http://export.arxiv.org/api/query?search_query=all:'+codigo
    with libreq.urlopen(link) as url:
        r = url.read().decode("utf-8")

    titulos += fun_titulo(r)
    autores += fun_autor(r)
    abstract += fun_resumen(r)
    links += fun_links(r)[1:]
    fechas += fun_fechas(r)[1:]




for i in range(len(titulos)):
    data_arxiv['arxiv'].append({
    'Autor': autores[i] ,
    'Resumen': abstract[i],
    'Url': links[i],
    'Fecha': fechas[i],
    'Titulo': titulos[i]})

with open('data_arxiv.json', 'w') as file:
    json.dump(data_arxiv, file, indent=4)


