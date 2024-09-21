import pytest
from configs.config import *
from pages.google_finance_page import GoogleFinancePage
from logs.logger import logger


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_open_page_and_verify_title(driver, test_data):
    logger.info("Test started: Open page and verify title")
    driver.get(URL)
    assert "Google Finance" in driver.title, "Page title does not match"
    logger.info("Page title verified successfully.")


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_compare_stock_symbols(driver, test_data):
    logger.info("Test started: Compare stock symbols")

    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")

    ui_not_in_test = [
        symbol for symbol in stock_symbols_ui if symbol not in test_data]
    test_not_in_ui = [
        symbol for symbol in test_data if symbol not in stock_symbols_ui]

    logger.info(f"Symbols in UI but not in test data: {ui_not_in_test}")
    logger.info(f"Symbols in test data but not in UI: {test_not_in_ui}")

    assert not test_not_in_ui, f"Symbols missing from UI: {test_not_in_ui}"

    logger.info("Test completed successfully.")


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_print_symbols_not_in_ui(driver, test_data):
    logger.info("Test started: Print symbols in test data but not in UI")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    not_in_ui = [
        symbol for symbol in test_data if symbol not in stock_symbols_ui]
    logger.info(f"Symbols in test data but not in UI: {not_in_ui}")


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_print_symbols_in_ui(driver, test_data):
    logger.info("Test started: Print symbols in UI")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Symbols in UI: {stock_symbols_ui}")


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_ui_symbol_count(driver, test_data):
    logger.info("Test started: Verify count of symbols in UI")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Number of symbols in UI: {len(stock_symbols_ui)}")


@pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
def test_compare_ui_count_with_test_data(driver, test_data):
    logger.info("Test started: Compare count of symbols in UI with test data")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    assert len(stock_symbols_ui) == len(
        test_data), "Count of symbols in UI does not match test data"
    logger.info("Count of symbols matches successfully.")
