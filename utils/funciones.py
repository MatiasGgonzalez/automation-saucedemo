from selenium.webdriver.common.by import By

## Función para realizar el login 

def login(driver, usuario="standard_user", password="secret_sauce"):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def obtener_productos(driver):
    ##Devuelve la lista de todos los productos del inventario##
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


def obtener_producto_por_indice(driver, indice):
    ## Devuelve una tupla (nombre, precio) del producto en la posición indicada.
    productos = obtener_productos(driver)
    producto = productos[indice]
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio