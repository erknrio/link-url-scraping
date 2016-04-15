# Descontinuado

# URL Scraping
Scraping de una URL para obtener todos los enlaces de la página introducida por parámetro y un parámetro opcional para seguir buscando enlaces dentro de la página en forma de árbol.

## Uso
Una vez desplazado a la ruta del fichero scraping.py lo ejecutamos con una URL (cambiar la de ejemplo por la deseada):
python scraping.py http://adriangarrido.com.es/prueba-enlaces 3

El parámetro numérico, "3" en el ejemplo, es opcional. Por defecto el programa solamente busca las URL de la página suministrada.

## Dependencias
* [python 27.7.11](https://www.python.org/downloads/)
* pip install beautifulsoup4.
* pip install requests

## Screenshot

![scraping](https://github.com/erknrio/link-url-scraping/blob/master/screenshot/scraping.jpg)

## TODO
* Permitir el uso de URL relativas
* Permitir devolver los datos en otro formato

## Changelog

[Changelog](https://github.com/erknrio/link-url-scraping/releases)

## License
Programa baho la linecia MIT [`LICENSE`](LICENSE)
