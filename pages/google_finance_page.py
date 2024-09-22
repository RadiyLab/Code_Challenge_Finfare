from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GoogleFinancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_stock_symbols(self):
        stock_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "[aria-labelledby='smart-watchlist-title'] li .COaKTb")
        return [element.text.strip() for element in stock_elements]
