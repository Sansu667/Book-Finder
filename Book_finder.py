import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/page-{}.html"

libros_mejores = []

# Iterar páginas
for n in range(1, 51):
    
    # Crear sopa en cada página
    url = url_base.format(n)
    resultado = requests.get(url)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")
    
    # Seleccionar datos de los libros
    libros = sopa.select(".product_pod")
    
    # Iterar libros
    for libro in libros:
        if len(libro.select(".star-rating.Five")) != 0 or len(libro.select(".star-rating.Four")) != 0:
            titulo_libro = libro.select("a")[1]["title"]
            libros_mejores.append(titulo_libro)
            
for t in libros_mejores:
    print(t)
            
            