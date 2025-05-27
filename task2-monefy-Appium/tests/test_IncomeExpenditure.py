import pytest
import allure
from pages.base_page import BasePage
from pages.IncomeExpenditure_page import IncomeExpenditurePage


@pytest.mark.run(order=4)
@allure.title("Test onboarding handling and basic income addition")
@allure.description("Verify onboarding is handled and basic income can be added")
@pytest.mark.usefixtures("wait_after_test")
def test_04_add_income(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Go to Income field and input income by addition"):
        # Simple addition: 14 + 3 = 17
        assert incExp.add_income(['1', '4', '+', '3', '=']), "Error in adding Incomes"
    with allure.step("Add notes for the Income earned"):
        assert incExp.verify_note("Hourly Income")
    with allure.step("Select category for Incomes"):
        incExp.get_category(), "Error in selecting category"
    with allure.step("Compare result in Balance field"):
        assert incExp.get_balance("17.00"), "Error in adding income to Balance field"


@pytest.mark.run(order=5)
@allure.title("Test complex income calculations")
@allure.description("Verify more complex income calculations work correctly")
@pytest.mark.usefixtures("wait_after_test")
def test_05_complex_income(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Add complex income calculation"):
        # Complex addition: 12 + 34 = 46
        assert incExp.add_income(['1', '2', '+', '3', '4', '=']), "Error in complex income addition"
    with allure.step("Add detailed note"):
        assert incExp.verify_note("Complex Income Test")
    with allure.step("Select category"):
        incExp.get_category()
    with allure.step("Verify balance"):
        #17 from previous step
        assert incExp.get_balance("63.00"), "Error in complex income balance"


@pytest.mark.run(order=6)
@allure.title("Test basic expense addition")
@allure.description("Verify basic expense can be added")
@pytest.mark.usefixtures("wait_after_test")
def test_06_add_expense(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Add basic expense"):
        # Simple addition: 12 + 4 = 16
        assert incExp.add_expense(['1', '2', '+', '4', '=']), "Error in adding Expenses"
    with allure.step("Add expense note"):
        assert incExp.verify_note("Basic Expense")
    with allure.step("Select expense category"):
        incExp.get_category()
    with allure.step("Verify updated balance"):
        # previous balance 63 - 16 = 47
        assert incExp.get_balance("47.00"), "Error in balance after expense"


@pytest.mark.run(order=7)
@allure.title("Test complex expense calculations")
@allure.description("Verify more complex expense calculations work correctly")
@pytest.mark.usefixtures("wait_after_test")
def test_07_complex_expense(base_page):
    incExp = IncomeExpenditurePage(base_page)
    with allure.step("Add complex expense calculation"):
        # Complex addition: 33 + 15 = 48
        assert incExp.add_expense(['3', '3', '+', '1', '5', '=']), "Error in complex expense addition"
    with allure.step("Add detailed expense note"):
        assert incExp.verify_note("Complex Expense Test")
    with allure.step("Select category"):
        incExp.get_category()
    with allure.step("Verify final balance"):
        # Previous balance 47.00 - 48.00 = -1.00
        assert incExp.get_balance("-1.00"), "Error in final balance calculation"
