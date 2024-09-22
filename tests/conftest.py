import os
import pytest
from selenium import webdriver
from datetime import datetime
from logs.logger import logger
import configs.config as config


@pytest.fixture()
def driver(request):
    test_name = os.environ.get(
        'PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    logger.info(f'########## Test Case: {test_name} ##########')

    driver = webdriver.Firefox()
    logger.info('Opened Firefox Browser')
    # driver = webdriver.Chrome()
    # logger.info('Opened Chrome Browser')

    driver.get(config.URL)
    logger.info(f'Navigated to {config.URL}')
    driver.implicitly_wait(config.TIMEOUT)
    driver.maximize_window()

    yield driver

    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    screenshot_name = f".\\evidence\\{test_name}_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    logger.info(f'Screenshot saved: {screenshot_name}')

    driver.quit()
    logger.info('Browser was closed successfully')
