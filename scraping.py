#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from bs4 import BeautifulSoup
import requests

try:
    def valid_url(url_string):
        patron = re.compile('((?:https?:)?\/\/(?:[\w]+[.][\w]+)+\/?)')
        result = patron.match(url_string)
        if result == None:
            return False
        else:
            return True
    
    def scrapingURL(url, iteraciones = 0, saltos = 0):
        i = 0
        j = 0
        whitespaces = '    '
        # Realizamos la peticion
        req = requests.get(url)
        status_code = req.status_code
        if status_code == 200:
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "html.parser")
            # Obtenemos todos los enlaces
            enlaces = html.find_all('a',{'href' : True})
            # Recorremos todos los enlaces para extraer los atributos href
            for i,enlace in enumerate(enlaces):
                # url absolutas
                if valid_url(enlace["href"]):
                    print u"" + (whitespaces * saltos) + "---" +  enlace["href"]
                    iteraciones -= 1
                    if iteraciones > 0:
                        scrapingURL(enlace["href"], iteraciones, saltos + 1)
        elif status_code == 404:
            print u"Url inalcanzable"

    def main():
        iteraciones = 0
        num_params = len(sys.argv)

        if num_params < 2:
            raise IndexError("Debe introducir una URL")
        elif num_params > 3:
            raise IndexError("Exceso de parámetros")
        else:
            if num_params == 3:
                iteraciones = int(sys.argv[2])
            if not isinstance(iteraciones, (int) ):
                raise TypeError("El último argumento debe ser númerico")
            else:
                if callable(valid_url) and callable(scrapingURL):
                    if valid_url(sys.argv[1]):
                        scrapingURL(sys.argv[1], iteraciones)
                    else:
                        raise Exception("URL no válida")
                else:
                    raise Exception("No se puede ejecutar")
        
    if __name__=="__main__":
        main()
            
except Exception as err:
        print u"Ha ocurrido un error: ", err
