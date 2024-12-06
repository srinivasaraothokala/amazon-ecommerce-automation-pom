import time
from selenium import webdriver
from pages.home_page import HomePage

def test_search_item():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    home_page = HomePage(driver)
    home_page.search_item("iPhone 16")

    time.sleep(5)
    driver.quit()
