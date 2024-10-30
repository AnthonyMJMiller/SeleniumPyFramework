from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)  # or webdriver.Firefox()
    return driver