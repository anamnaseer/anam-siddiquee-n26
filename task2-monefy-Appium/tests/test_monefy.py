import pytest
import allure
from pages.Onboarding_page import OnboardingPage


@pytest.mark.run(order=1)
@allure.title("App Launch via Onboarding Dismissal")
@allure.description("Verify initial onboarding screens are dismissed using the 'Continue' button")
def test_launch_onboarding_dismissal(base_page):
    onboarding = OnboardingPage(base_page)
    with allure.step("Dismiss onboarding screens by tapping 'Continue'"):
        onboarding.click_continue_until_absent()
    with allure.step("Confirm 'Continue' button is no longer visible"):
        assert not onboarding.is_continue_button_present(), "Onboarding 'Continue' button still visible"

@pytest.mark.run(order=2)
@allure.title("Offer Page Dismissal")
@allure.description("Verify that the offer page appears and is correctly dismissed")
def test_offer_page_dismissal(base_page):
    onboarding = OnboardingPage(base_page)
    with allure.step("Assert offer page is displayed"):
        assert onboarding.is_offer_page_displayed(), "Offer page did not appear"
    with allure.step("Dismiss the offer by tapping 'Close'"):
        onboarding.click_offer_close_button()
    with allure.step("Confirm the offer page is no longer visible"):
        assert not onboarding.is_offer_page_displayed(), "Offer page still visible after dismissal"


@pytest.mark.run(order=3)
@allure.title("Default Currency Verification")
@allure.description("Ensure the app sets the default currency based on geo-location")
def test_default_currency_verification(base_page):
    onboarding = OnboardingPage(base_page)
    with allure.step("Confirm displayed currency is 'ES'"):
        assert onboarding.check_currency_value('ES'), "Default currency mismatch: expected 'ES'"
