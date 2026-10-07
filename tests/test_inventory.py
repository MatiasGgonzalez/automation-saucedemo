import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.funciones import login, obtener_producto_por_indice, obtener_productos
 


def test_inventory():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos
    
    try:
        
        login(driver) 

        #Verificar que se hayan cargado los productos del inventario
        productos = obtener_productos(driver)
        print(len(productos))
        assert len(productos) > 0

        nombre, precio = obtener_producto_por_indice(driver, 0)
        print(f"Producto: {nombre} - Precio: {precio}")

        #Verificar que el nombre y precio del producto sean correctos
        assert nombre == "Sauce Labs Backpack"
        assert precio == "$29.99"


        #Verificar menu 
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_button.is_displayed()

        #Verificar filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

    finally:
        driver.quit()
