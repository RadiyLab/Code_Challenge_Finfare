from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# class GoogleFinancePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.interested_section_xpath = "//div[text()='You may be interested in']/following-sibling::div//span"

#     def get_stock_symbols(self):
#         stock_elements = self.driver.find_elements(
#             By.XPATH, self.interested_section_xpath)
#         return [element.text for element in stock_elements]


class GoogleFinancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.interested_section_xpath = "//div[contains(@class, 'COaKTb')]//span"

    def get_stock_symbols(self):
        stock_elements = self.driver.find_elements(
            By.XPATH, self.interested_section_xpath)
        return [element.text for element in stock_elements if element.text.strip()]
