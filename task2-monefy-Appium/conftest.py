from base.common import get_resource_config
import os
from collections import namedtuple
import pytest
import allure
from base.web_drivers import WebDriver
from pages.base_page import BasePage
import logging
import time

logging.basicConfig(  format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
) 

def pytest_addoption(parser):
    parser.addoption(
        "--device_name", action="store", default="emulator-5556", help="device name for appium driver"
    )

@allure.feature("Launch App")
@allure.story("Verify app launches and click on get started works")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture(scope='session')
def set_driver(request):
    device_name = request.config.getoption("--device_name")
    driver = WebDriver.get_appiumdriver(device_name=device_name)

    yield driver
    try:
        driver.driver.close()
    except (Exception, ValueError):
        pass

@pytest.fixture()
def base_page(set_driver):
    return BasePage(set_driver)

@pytest.fixture()
def wait_after_test():
    """Adds a hard wait after each test."""
    yield  # Run the test first
    wait_time = 20
    if wait_time:
        logging.info(f"Waiting for {wait_time} seconds before proceeding...")
        time.sleep(wait_time)
