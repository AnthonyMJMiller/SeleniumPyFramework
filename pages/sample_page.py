from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.RETURN)
