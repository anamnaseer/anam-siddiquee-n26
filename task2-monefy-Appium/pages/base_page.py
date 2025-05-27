from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator, timeout=10):
        """
        Wait for and return a web element identified by the given locator tuple.
        Raises an exception if the element is not found within the timeout period.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            raise Exception(f"Element with locator {locator} not found within {timeout} seconds.") from e

    def find_elements(self, *locator, timeout=10):
        """
        Wait for and return a list of web elements identified by the given locator tuple.
        Raises an exception if no elements are found within the timeout period.
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except Exception as e:
            raise Exception(f"Elements with locator {locator} not found within {timeout} seconds.") from e

    def click_element(self, *locator, timeout=10):
        """
        Find an element using the given locator tuple and click on it.
        """
        element = self.find_element(*locator, timeout=timeout)
        element.click()

    def get_element_text(self, locator_type, locator_value, timeout=10):
        """
        Find an element using locator_type and locator_value and return its text.
        """
        element = self.find_element(locator_type, locator_value, timeout=timeout)
        return element.text

    def input_text(self, locator_type, locator_value, text, timeout=10):
        """
        Find an element using locator_type and locator_value, clear it, and input the provided text.
        """
        element = self.find_element(locator_type, locator_value, timeout=timeout)
        element.clear()
        element.send_keys(text)
