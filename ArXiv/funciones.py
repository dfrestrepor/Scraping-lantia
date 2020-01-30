import re
def fun_links(contenidoPagina):
    links = re.findall('<link href=\"(.+\n*.+\n*)" rel="', contenidoPagina)
    return links


def fun_titulo(contenidoPagina):
    title = re.findall('<title>(.*\n*.+\n*)</title>', contenidoPagina)
    return title
    
    
def fun_fechas(contenidoPagina):
    update = re.findall('<updated>(.*\n*.+\n*)</updated>', contenidoPagina)
    return update

    
def fun_resumen(contenidoPagina):
    abstract = re.findall('<summary>  (.+\n*.+\n*.+\n*.+\n*.+\n*)</summary>', contenidoPagina)
    return abstract



def fun_autor(contenidoPagina):
    autor = re.findall('<name>(.*\n*.+\n*)</name>', contenidoPagina)
    return autor