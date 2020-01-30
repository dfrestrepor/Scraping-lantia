Este proyecto tiene como finalidad obtener los datos almacenados en el sitio de publicaciones cient�ficas ArXiv, haciendo uso de la Api del sitio web (explore.arxiv). Para hacer funcionar el algoritmo, es suficiente con ejecutar el archivo "ArXiv-Api.py" desde un int�rprete de python.



Las librer�as requridas son:
- bs4
- urllib
- json
- re

todas presentes por defecto en la version 3.7 de python.

Es necesario, tener los archivos "categorias.py" y "funciones.py" en el directorio de trabajo, pues estos contienen las categor�as tem�ticas y las funciones, respectivamente, requeridas para el funcionamiento del algoritmo principal.

La salida del algoritmo es un archivo "data_arxiv.json" el cual contiene el titulo, el resumen, autor, fecha de publicaci�n y url de los articulos disponibles en cada categor�a de temas del sitio web (las cuales est�n contenidas en el archivo "categorias.py").