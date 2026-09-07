
# Nombre: Diego Valle Cuevas
# Grupo: 952
# Meta 1.3 - Web Scraping con Selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


# Definimos función para establecer el nombre del producto y cantidad de paginas a consultar
def buscar_producto(producto, num_paginas):

    # Colocamos las configuraciones de la visualización del navegador.
    opc = Options()
    opc.add_argument("--window-size=1920,1080")
    navegador = webdriver.Chrome(options=opc)
    # Creamos la carpeta donde guardaremos las capturas
    carpeta_capturas = "capturas"
    os.makedirs(carpeta_capturas, exist_ok=True)

    # Empezamos abrir la web de MELI y esperamos 3 segundos antes de empezar a buscar
    try:
        navegador.get("https://www.mercadolibre.com.mx/")
        time.sleep(3)

        # Buscamos mediante el id la barra de búsqueda
        txtBuscador = navegador.find_element(By.ID, "cb1-edit")

        # Hacemos que en la barra de búsqueda inserte el nombre del producto y espere 2 segundos
        txtBuscador.send_keys(producto)
        time.sleep(2)
        # Hace click en buscar y espera 4 segundos
        txtBuscador.send_keys(Keys.ENTER)
        time.sleep(4)


        # Empezamos a tomar capturas de pantalla y definimos el nombre que deben de tener
        ruta_captura = os.path.join(carpeta_capturas, f"{producto}_pagina_1.png")
        navegador.save_screenshot(ruta_captura)
        print(f"Captura guardada: {ruta_captura}")


    # Empieza a calcular desde que pagina toma capturas, a la primer pagina ya le tomó en la anterior parte
        for pagina in range(2, num_paginas + 1):
            try:
                # Busca el botón con el link para seguir a la siguiente página
                btnSiguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")

                # Hace scroll hasta que el elemento del botón siguiente sea visible y espera
                navegador.execute_script("arguments[0].scrollIntoView();", btnSiguiente)
                time.sleep(1)

                # Después de esperar hace click
                btnSiguiente.click()
                time.sleep(4)

                # Nuevamente establece la ruta y nombre de cada captura de esta función que empieza desde la segunda página.
                ruta_captura = os.path.join(carpeta_capturas, f"{producto}_pagina_{pagina}.png")
                navegador.save_screenshot(ruta_captura)
                print(f"Captura guardada: {ruta_captura}")

            # Si algo llega a fallar o modificaron el html, rompe el ciclo en vez de seguir intentando
            except Exception as e:
                print(f"No se pudo avanzar a la pagina {pagina}: {e}")
                break


            # Establecemos al final, si o si el navegador tiene que cerrar
    finally:
        navegador.quit()

# Ahora si mandamos a llamar la función y los parametros a buscar en la web
if __name__ == "__main__":
    producto_input = input("¿Qué producto quieres buscar? ")
    paginas_input = int(input("¿Cuántas páginas quieres visitar (en números)? "))

    buscar_producto(producto_input, paginas_input)