Este repositorio utiliza las técnicas de web crawler y web scraping  bajo la arquitectura de la libreria scrapy para
python 3.

Para inicializar su funcionamiento, primera se realiza una copia del respositorio git, se accede a la carpeta spiders desde
la consola y se ejecuta el siguiente comando


scrapy runspider get_patente.py  -a query='12/12/2019-13/12/2019'

El valor para el parametro query corresponde al rango de fechas de las tentes que se desea explorar
