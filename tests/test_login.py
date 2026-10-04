import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        password.send_keys("secret_sauce")
        usuario.send_keys("standard_user")
        login_button.click()

        assert "https://www.saucedemo.com/inventory.html" in driver.current_url

        texto_swag_labs = driver.find_element(By.CLASS_NAME, "app_logo").text
        texto_products = driver.find_element(By.CSS_SELECTOR, "[data-test='title']").text
        assert texto_swag_labs == "Swag Labs"
        assert texto_products == "Products"
    finally:
        driver.quit()