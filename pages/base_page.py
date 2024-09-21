from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import configs.config as config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def maximize_window(self):
        self.driver.maximize_window()
