import time
from selenium import webdriver
from pages.login_page import LoginPage

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("79*******", "Te*****@123")

    time.sleep(5)
    driver.quit()
