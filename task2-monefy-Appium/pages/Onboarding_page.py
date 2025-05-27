from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time


class OnboardingPage:
    # Locators for page elements
    CONTINUE_BUTTON_LOCATOR = ("id", "com.monefy.app.lite:id/buttonContinue")
    OFFER_PURCHASE_LOCATOR = ("id", "com.monefy.app.lite:id/buttonPurchase")
    OFFER_CLOSE_LOCATOR = ("id", "com.monefy.app.lite:id/buttonClose")
    CURRENCY_LABEL_LOCATOR = ("id", "com.monefy.app.lite:id/currencyLabel")  # Adjust if needed

    def __init__(self, base_page):
        self.base_page = base_page

    def click_continue_until_absent(self):
        """
        Repeatedly clicks the 'Continue' button until it is no longer present.
        """
        while self.is_continue_button_present():
            try:
                btn = self.base_page.find_element(*self.CONTINUE_BUTTON_LOCATOR)
                btn.click()
            except StaleElementReferenceException:
                continue

    def is_continue_button_present(self):
        """
        Checks if the 'Continue' button is present.
        Returns True if present, False otherwise.
        """
        try:
            btn = self.base_page.find_element(*self.CONTINUE_BUTTON_LOCATOR)
            return btn is not None
        except NoSuchElementException:
            return False
        except Exception:
            return False

    def is_offer_page_displayed(self):
        """
        Verifies if the offer page is displayed by checking the presence of the Purchase button.
        Returns True if displayed, False otherwise.
        """
        try:
            elem = self.base_page.find_element(*self.OFFER_PURCHASE_LOCATOR)
            return elem is not None
        except NoSuchElementException:
            return False
        except Exception:
            return False

    def click_offer_close_button(self):
        """
        Clicks the 'Close' button on the offer page to dismiss it.
        Raises an exception if the offer page is still visible after multiple attempts.
        """
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                btn = self.base_page.find_element(*self.OFFER_CLOSE_LOCATOR)
                btn.click()
                time.sleep(1)
                if not self.is_offer_page_displayed():
                    return
            except Exception:
                pass
        raise Exception("Offer page still visible after dismissal")

    def check_currency_value(self, expected_currency):
        """
        Checks if the displayed currency matches the expected value.
        Returns True if the currency matches, otherwise False.
        """
        try:
            elem = self.base_page.find_element(*self.CURRENCY_LABEL_LOCATOR)
            return elem.text.strip() == expected_currency
        except Exception:
            return False