# Web Scraping con Selenium - MercadoLibre

Script en Python que automatiza la búsqueda de un producto en MercadoLibre 
y toma capturas de pantalla de los resultados, usando Selenium.

**Autor:** Diego Valle Cuevas  
**Grupo:** 952  
**Actividad:** Meta 1.3 - Web Scraping

## ¿Qué hace?

El script abre un navegador Chrome controlado por Selenium, busca el producto 
que el usuario indique en MercadoLibre, y va guardando una captura de pantalla 
por cada página de resultados que visite (el número de páginas también lo 
decide el usuario).

## Requisitos

- Python 3.10 o superior
- Google Chrome instalado
- Selenium 4.1 o superior

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/diegovc20/<Web-Scraping-con-Selenium---MercadoLibre>.git
cd <Web-Scraping-con-Selenium---MercadoLibre>
```

2. (Opcional pero recomendado) Crea un entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instala Selenium:
```bash
pip install selenium
```

No es necesario descargar el ChromeDriver por separado — desde Selenium 4.6+ 
se gestiona automáticamente.

## Cómo correrlo

Desde la terminal, dentro de la carpeta del proyecto:
```bash
python webscrapping_meli.py
```

El script te va a preguntar dos cosas directamente en la terminal:

¿Qué producto quieres buscar?
¿Cuántas páginas quieres visitar?
