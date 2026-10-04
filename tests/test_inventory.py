import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_inventory():
    driver = webdriver.Chrome()
    try:
        #login
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        password.send_keys("secret_sauce")
        usuario.send_keys("standard_user")
        login_button.click()      

        #Verificar titulo de la pagina
        assert driver.title == "Swag Labs"

        #Verificar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(len(productos))
        assert len(productos) > 0

        buzo_swag = productos[3]
        nombre_producto = buzo_swag.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = buzo_swag.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Buzo Swag: {nombre_producto} - Precio: {precio_producto}")

        assert nombre_producto == "Sauce Labs Fleece Jacket"  
        assert precio_producto ==  "$49.99"

        #Verificar menu 
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu_button.is_displayed()

        #Verificar filtro
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

    finally:
        driver.quit()
