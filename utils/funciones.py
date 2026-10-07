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


def agregar_producto_al_carrito(driver, indice):
    ## Agrega al carrito el producto en la posición indicada.
    ## Devuelve el nombre del producto agregado.
    producto = obtener_productos(driver)[indice]
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    producto.find_element(By.CLASS_NAME, "btn_inventory").click()
    return nombre

def obtener_contador_carrito(driver):
    ## Devuelve el contador del carrito como entero.
    return int(driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)

def ir_al_carrito(driver):
    ## Ir al carrito.
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


def obtener_productos_carrito(driver):
    ## Devuelve la lista de productos que están en el carrito.
    return driver.find_elements(By.CLASS_NAME, "cart_item")