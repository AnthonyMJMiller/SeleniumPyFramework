from selenium import webdriver
import time

from utils.webdriver_setup import get_driver

def test_google_search():
    driver = get_driver()  # or webdriver.Firefox()
    driver.get("https://www.google.com")
    time.sleep(2)  # Wait for the page to load
    assert "Google" in driver.title
    driver.quit()
