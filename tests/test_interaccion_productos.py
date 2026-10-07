import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.funciones import login


def test_interaccion_productos():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos
    try:
        #login
        login(driver)

        #Añadir producto al carrito
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(len(productos))
        buzo_swag = productos[3]
        boton_agregar = buzo_swag.find_element(By.CLASS_NAME, "btn_inventory")
        boton_agregar.click()

        #Verificar que el producto se haya agregado al carrito
        contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        contador_carrito = int(contador_carrito)
        print(f"Cantidad de productos en el carrito: {contador_carrito}")
        assert contador_carrito > 0

        #Navegar al carrito de compras. 

        carrito_buttom = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        carrito_buttom.click()
        assert "https://www.saucedemo.com/cart.html" in driver.current_url 

        #Verificar que el producto este agregado correctamente en el carrito
        productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
        buzo_carrito = productos_carrito[0]
        nombre_producto_carrito = buzo_carrito.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"Nombre del producto en el carrito: {nombre_producto_carrito}")
        assert nombre_producto_carrito == "Sauce Labs Fleece Jacket"

    finally:
        driver.quit()          
