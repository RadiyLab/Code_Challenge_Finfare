import pytest
from configs.config import *
from pages.google_finance_page import GoogleFinancePage
from logs.logger import logger


def test_open_page_and_verify_title(driver):
    logger.info("Test started: Open page and verify title")
    driver.get(URL)
    assert "Google Finance" in driver.title, "Page title does not match"
    logger.info("Page title verified successfully.")


def test_compare_stock_symbols(driver):
    logger.info("Test started: Compare stock symbols")

    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")

    assert GIVEN_TEST_DATA == stock_symbols_ui


@pytest.mark.smoke
def test_symbols_in_ui_but_not_in_given_data(driver):
    logger.info("Test started: Print symbols in UI, but not in given data.")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")
    difference = [
        symbol for symbol in stock_symbols_ui if symbol not in GIVEN_TEST_DATA]
    logger.info(
        f"List of symbols in UI that are not in given test data {difference}")
    assert len(difference) == 0


@pytest.mark.smoke
def test_symbols_in_test_data_but_not_in_ui(driver):
    logger.info("Test started: Print symbols in test data that are not in UI")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")
    difference = [
        symbol for symbol in GIVEN_TEST_DATA if symbol not in stock_symbols_ui]
    logger.info(
        f"List of symbols in test data that are not in UI {difference}")
    assert len(difference) == 0
