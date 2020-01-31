Documentación para el segundo algoritmo que realiza el scraping de noticias.

Para la realización del algoritmo se usan dos librerías que son el eje central de este:

La primera es la librería "scrapy" (https://docs.scrapy.org/en/latest/index.html), para la cual, se recomienda usar
en un entorno virtual.
La segunda es la librería "newspaper3k" (https://newspaper.readthedocs.io/en/latest/).

En este scraping se trabajan las fuentes de noticias para las cuales no fue posible extraer su 
fecha de publicación (pubdate), por lo tanto, se extraeran las últimas noticias publicadas de cada página. 

A continuación se especificará el archivo "spider.py" en el cual se desarrollan las arañas que son usadas para la
extracción de los datos requeridos. 

  spider.py: En este archivo se empieza por definir la araña con un tipo "CrawlSpider", se le asigna un 
nombre, los dominios y páginas que se desean analizar. Posteriormente se define la función "parse" la cual es la 
encargada de extraer y almacenar lo datos requeridos. Dentro de esta función se define la variable "lista_caminos"
en la cual se almacena a modo de lista todos los xpath necesarios para la extracción de las url de las noticias en
cada página; estas url se almacenan en la variable "noticia".
El segundo "for" ingresa de manera individual a las url obtenidas, para condicionar las noticias en cuyo link
está contenido su respectivo dominio; para el caso afirmativo, con el uso de la librería "newspaper3k" se extraen
los datos requeridos (url de la noticia, titulo, autor, fecha de publicación, descripción, url de imagen y url video);
caso contrario se realiza una concatenación para completar el link y proceder de forma análoga con el uso de la
librería "newspaper3k". 

NOTA: para correr el scraping se usa el comando "scrapy crawl noticias -t formato"