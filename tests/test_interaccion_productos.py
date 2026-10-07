import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.funciones import login, obtener_productos, agregar_producto_al_carrito, obtener_contador_carrito, ir_al_carrito, obtener_productos_carrito




def test_interaccion_productos():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        # Login
        login(driver)

        # Verificar que se cargaron los productos
        productos = obtener_productos(driver)
        print(len(productos))
        assert len(productos) > 0

        # Agregar el PRIMER producto al carrito (índice 0)
        nombre_agregado = agregar_producto_al_carrito(driver, 0)

        # Verificar el contador del carrito
        contador_carrito = obtener_contador_carrito(driver)
        print(f"Cantidad de productos en el carrito: {contador_carrito}")
        assert contador_carrito > 0

        # Navegar al carrito
        ir_al_carrito(driver)
        assert "https://www.saucedemo.com/cart.html" in driver.current_url

        # Verificar que el producto agregado esté en el carrito
        productos_carrito = obtener_productos_carrito(driver)
        nombre_producto_carrito = productos_carrito[0].find_element(By.CLASS_NAME, "inventory_item_name").text

        print(f"Nombre del producto en el carrito: {nombre_producto_carrito}")

        assert nombre_producto_carrito == "Sauce Labs Backpack"

    finally:
        driver.quit()      
