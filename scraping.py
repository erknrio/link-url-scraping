#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from bs4 import BeautifulSoup
import requests
import re
reload(sys)
sys.setdefaultencoding('UTF8')

try:
    def valid_url(url_string):
        patron = re.compile('((?:https?:)?\/\/(?:[\w]+[.][\w]+)+\/?)')
        result = patron.match(url_string)
        if result == None:
            return False
        else:
            return True
    
    def scrapingURL(url, num=-1, recursive = False):
        # Realizamos la peticion
        req = requests.get(url)
        statusCode = req.status_code
        
        # Peticion es correcta
        if statusCode == 200:
            # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
            html = BeautifulSoup(req.text, "html.parser")
            # Obtenemos todos los enlaces
            enlaces = html.find_all('a',{'href' : True})
            # Recorremos todos los enlaces para extraer al atributo href
            for i,enlace in enumerate(enlaces):
                if valid_url(enlace["href"]):
                    print "---", enlace["href"]
        else:
            print "Status Code: ", statusCode

    def main():
        num_params = len(sys.argv)
        param3 = ''

        if num_params < 2:
            raise IndexError("Debe introducir una URL")
        elif num_params > 3:
            raise IndexError("Exceso de parámetros")
        elif num_params == 3:
            param3 = int(sys.argv[2])
            if not isinstance(param3, (int) ):
                raise TypeError("El último argumento debe ser númerico")
            else:
                if callable(scrapingURL) and callable(valid_url):
                    if valid_url(sys.argv[1]):
                        scrapingURL(sys.argv[1], param3)
                    else:
                        raise Exception("URL no válida")
                else:
                    print "El método no existe"
        else:
            if callable(scrapingURL) and callable(valid_url):
                valid_url(sys.argv[1])
                scrapingURL(sys.argv[1])
            else:
                print "El método no existe"
        
    if __name__=="__main__":
        main()
            
except Exception as err:
        print "Ha ocurrido un error: ", err