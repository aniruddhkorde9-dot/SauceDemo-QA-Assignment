import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    assert "inventory.html" in driver.current_url
    
    driver.quit()

def test_add_to_cart_and_checkout():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    driver.find_element(By.ID, "checkout").click()
    
    driver.find_element(By.ID, "first-name").send_keys("Aniruddh")
    driver.find_element(By.ID, "last-name").send_keys("Korde")
    driver.find_element(By.ID, "postal-code").send_keys("422103")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    
    msg = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert msg == "Thank you for your order!"
    
    driver.quit()

def test_locked_out_user():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    err = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    
    assert "locked out" in err
    
    driver.quit()