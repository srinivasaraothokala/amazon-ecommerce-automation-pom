from selenium.webdriver.common.by import By

class AmazonHomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.sign_in_button = (By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
        self.search_box = (By.XPATH, '//*[@id="twotabsearchtextbox"]')
        self.search_button = (By.XPATH, '//*[@id="nav-search-submit-button"]')

    def hover_over_sign_in(self, action):
        sign_in = self.wait.until(lambda d: d.find_element(*self.sign_in_button))
        action.move_to_element(sign_in).perform()

    def search_item(self, item_name):
        search_box = self.wait.until(lambda d: d.find_element(*self.search_box))
        search_box.clear()
        search_box.send_keys(item_name)
        self.driver.find_element(*self.search_button).click()
