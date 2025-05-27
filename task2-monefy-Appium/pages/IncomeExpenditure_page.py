from appium.webdriver.common.appiumby import AppiumBy
import time
import logging
from pages.base_page import BasePage
from pages.Onboarding_page import OnboardingPage

class IncomeExpenditurePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.handle_onboarding()

    def handle_onboarding(self):
        """Check and handle onboarding pages if they appear"""
        try:
            onboarding = OnboardingPage(self.driver)
            
            # Handle continue buttons if present
            if onboarding.is_continue_button_present():
                onboarding.click_continue_until_absent()
            
            # Handle offer page if present
            if onboarding.is_offer_page_displayed():
                onboarding.click_offer_close_button()
                
            time.sleep(2)  # Small wait to ensure UI is stable
        except Exception as e:
            raise Exception(f"Failed to handle onboarding: {str(e)}")

    # Locators
    BUTTON_1 = "com.monefy.app.lite:id/buttonKeyboard1"
    BUTTON_2 = "com.monefy.app.lite:id/buttonKeyboard2"
    BUTTON_3 = "com.monefy.app.lite:id/buttonKeyboard3"
    BUTTON_4 = "com.monefy.app.lite:id/buttonKeyboard4"
    BUTTON_5 = "com.monefy.app.lite:id/buttonKeyboard5"
    BUTTON_ADD = "com.monefy.app.lite:id/buttonKeyboardPlus"
    BUTTON_EQUAL = "com.monefy.app.lite:id/buttonKeyboardEquals"
    RESULT_FIELD = "com.monefy.app.lite:id/amount_text"
    INCOME_BUTTON = "com.monefy.app.lite:id/income_button"
    EXPENSE_BUTTON = "com.monefy.app.lite:id/expense_button"
    CHOOSE_CATEGORY = "com.monefy.app.lite:id/keyboard_action_button"
    SALARY_CATEGORY = '(//android.widget.ImageView[@resource-id="com.monefy.app.lite:id/imageView"])[2]'
    NOTE_FIELD = "com.monefy.app.lite:id/textViewNote"
    BALANCE_FIELD = "com.monefy.app.lite:id/balance_amount"

    def enter_amount(self, amount_sequence):
        """
        Enter amount using number pad
        :param amount_sequence: List of button actions to perform (e.g. ['1', '4', '+', '3'])
        """
        button_map = {
            '1': self.BUTTON_1,
            '2': self.BUTTON_2,
            '3': self.BUTTON_3,
            '4': self.BUTTON_4,
            '5': self.BUTTON_5,
            '+': self.BUTTON_ADD,
            '=': self.BUTTON_EQUAL
        }
        
        for action in amount_sequence:
            if action in button_map:
                self.click_element("id", button_map[action])

        result = self.get_element_text("id", self.RESULT_FIELD)
        return result

    def add_income(self, amount_sequence=['1', '4', '+', '3', '=']):
        """
        Add income with specified amount sequence
        :param amount_sequence: List of button actions to perform
        :return: True if amount matches expected, False otherwise
        """
        self.click_element("id", self.INCOME_BUTTON)
        result = self.enter_amount(amount_sequence)
        expected = str(eval(''.join(amount_sequence).replace('=', '')))  # Calculate expected result
        return result == expected

    def add_expense(self, amount_sequence=['1', '2', '+', '4', '=']):
        """
        Add expense with specified amount sequence
        :param amount_sequence: List of button actions to perform
        :return: True if amount matches expected, False otherwise
        """
        self.click_element("id", self.EXPENSE_BUTTON)
        result = self.enter_amount(amount_sequence)
        expected = str(eval(''.join(amount_sequence).replace('=', '')))  # Calculate expected result
        return result == expected

    def get_category(self):
        """Select category for transaction"""
        self.click_element("id", self.CHOOSE_CATEGORY)
        self.click_element("xpath", self.SALARY_CATEGORY)

    def get_balance(self, expected_balance):
        """
        Check if balance matches expected amount
        :param expected_balance: Expected balance amount as string
        :return: True if balance matches, False otherwise
        """
        balance = self.get_element_text("id", self.BALANCE_FIELD)
        print(f"Current Balance: ${balance} (Expected: ${expected_balance})")
        balance = balance.split('Balance $')[1]
        return balance == expected_balance

    def verify_note(self, note_text):
        """
        Add and verify note text
        :param note_text: Text to add as note
        :return: True if note matches input, False otherwise
        """
        self.input_text("id", self.NOTE_FIELD, note_text)
        note = self.get_element_text("id", self.NOTE_FIELD)
        return note == note_text
