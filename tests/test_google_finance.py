import pytest
from configs.config import *
from pages.google_finance_page import GoogleFinancePage
from logs.logger import logger

# no need to parameterize this test
# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_open_page_and_verify_title(driver, test_data):
def test_open_page_and_verify_title(driver):
    logger.info("Test started: Open page and verify title")
    driver.get(URL)
    # 2. Verifies the page is loaded by asserting the page title
    assert "Google Finance" in driver.title, "Page title does not match"
    logger.info("Page title verified successfully.")

# no need to paramterize this test
# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_compare_stock_symbols(driver, test_data):
def test_compare_stock_symbols(driver):
    logger.info("Test started: Compare stock symbols")

    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    # adding the following
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")

    # 4. Compare the stock symbols retrieved from (3) with given test data
    assert GIVEN_TEST_DATA == stock_symbols_ui

    # ui_not_in_test = [
    #     symbol for symbol in stock_symbols_ui if symbol not in test_data]
    # test_not_in_ui = [
    #     symbol for symbol in test_data if symbol not in stock_symbols_ui]

    # logger.info(f"Symbols in UI but not in test data: {ui_not_in_test}")
    # logger.info(f"Symbols in test data but not in UI: {test_not_in_ui}")

    # assert not test_not_in_ui, f"Symbols missing from UI: {test_not_in_ui}"

    # logger.info("Test completed successfully.")

# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_print_symbols_not_in_ui(driver, test_data):
@pytest.mark.smoke
def test_symbols_in_ui_but_not_in_given_data(driver):
    logger.info("Test started: Print symbols in UI, but not in given data.")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    # not_in_ui = [
    #     symbol for symbol in test_data if symbol not in stock_symbols_ui]
    # logger.info(f"Symbols in test data but not in UI: {not_in_ui}")

    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")
    difference = [symbol for symbol in stock_symbols_ui if symbol not in GIVEN_TEST_DATA]
    # 5. Print all stock symbols that are in (3) but not in given test data
    logger.info(f"List of symbols in UI that are not in given test data {difference}")
    assert len(difference) == 0

# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_print_symbols_in_ui(driver, test_data):
@pytest.mark.smoke
def test_symbols_in_test_data_but_not_in_ui(driver):
    logger.info("Test started: Print symbols in test data that are not in UI")
    page = GoogleFinancePage(driver)
    stock_symbols_ui = page.get_stock_symbols()

    # logger.info(f"Symbols in UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols retrieved from UI: {stock_symbols_ui}")
    logger.info(f"Stock symbols in given test data: {GIVEN_TEST_DATA}")
    difference = [symbol for symbol in GIVEN_TEST_DATA if symbol not in stock_symbols_ui]
    # 6. Print all stock symbols that are in given test data but not in (3)
    logger.info(f"List of symbols in test data that are not in UI {difference}")
    assert len(difference) == 0



# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_ui_symbol_count(driver, test_data):
#     logger.info("Test started: Verify count of symbols in UI")
#     page = GoogleFinancePage(driver)
#     stock_symbols_ui = page.get_stock_symbols()

#     logger.info(f"Number of symbols in UI: {len(stock_symbols_ui)}")


# @pytest.mark.parametrize("test_data", [GIVEN_TEST_DATA])
# def test_compare_ui_count_with_test_data(driver, test_data):
#     logger.info("Test started: Compare count of symbols in UI with test data")
#     page = GoogleFinancePage(driver)
#     stock_symbols_ui = page.get_stock_symbols()

#     assert len(stock_symbols_ui) == len(
#         test_data), "Count of symbols in UI does not match test data"
#     logger.info("Count of symbols matches successfully.")
