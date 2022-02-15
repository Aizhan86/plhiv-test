from random import random
from time import sleep
from .base_page import BasePage
from .locators import ArvLogLocators, WorkJournalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date



class ArvPage(BasePage):
    def should_generate_contract_log(self):
        #     проверка объектов на странице Журнала договоров
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(*ArvLogLocators.CONTRACT_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*ArvLogLocators.CONTRACT_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(*ArvLogLocators.CONTRACT_LOG_APPLY_BTN), "Date range button object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.CONTRACT_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*ArvLogLocators.CONTRACT_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*ArvLogLocators.CONTRACT_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*ArvLogLocators.CONTRACT_LOG_APPLY_BTN).click()
        self.browser.find_element(*ArvLogLocators.CONTRACT_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.ARV_LOG_MENU).click()
        self.browser.find_element(*ArvLogLocators.DEBIT_LOG).click()


    def should_generate_debit_log(self):
        #     проверка объектов на странице Журнала списания
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(
            *ArvLogLocators.DEBIT_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*ArvLogLocators.DEBIT_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.DEBIT_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.DEBIT_LOG_APPLY_BTN), "Apply button object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.DEBIT_LOG_ADD_BTN), "Add button is not presented"
        assert self.is_element_present(
            *ArvLogLocators.DEBIT_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*ArvLogLocators.DEBIT_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*ArvLogLocators.DEBIT_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2'])
        self.browser.execute_script(
            f"{ArvLogLocators.DEBIT_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*ArvLogLocators.DEBIT_LOG_APPLY_BTN).click()
        self.browser.find_element(*ArvLogLocators.DEBIT_LOG_ADD_BTN).click()
        self.browser.find_element(*ArvLogLocators.DEBIT_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.ARV_LOG_MENU).click()
        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG).click()


    def should_generate_arrival_log(self):
        #     проверка объектов на странице Журнала прихода
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*ArvLogLocators.ARRIVAL_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_APPLY_BTN), "Apply button object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_FILTER1), "Filter 1 dropdown object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_FILTER2), "Filter 2 dropdown object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_ADD_BTN), "Add button is not presented"
        assert self.is_element_present(
            *ArvLogLocators.ARRIVAL_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        filter1_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{ArvLogLocators.ARRIVAL_LOG_FILTER1}.dropdown('set selected', '{filter1_choice}');")
        filter2_choice = random.choice(['1', '2'])
        self.browser.execute_script(
            f"{ArvLogLocators.ARRIVAL_LOG_FILTER2}.dropdown('set selected', '{filter2_choice}');")
        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG_APPLY_BTN).click()
        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG_ADD_BTN).click()
        self.browser.find_element(*ArvLogLocators.ARRIVAL_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.ARV_LOG_MENU).click()
        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG).click()


    def should_generate_expense_log(self):
        #     проверка объектов на странице Журнала расхода
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(
            *ArvLogLocators.EXPENSE_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*ArvLogLocators.EXPENSE_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.EXPENSE_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.EXPENSE_LOG_APPLY_BTN), "Apply button object is not presented"
        assert self.is_element_present(
            *ArvLogLocators.EXPENSE_LOG_ADD_BTN), "Add button is not presented"
        assert self.is_element_present(
            *ArvLogLocators.EXPENSE_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        filter3_choice = random.choice(['1', '2', '3', '4'])
        self.browser.execute_script(
            f"{ArvLogLocators.EXPENSE_LOG_FILTER}.dropdown('set selected', '{filter3_choice}');")
        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG_APPLY_BTN).click()
        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG_ADD_BTN).click()
        self.browser.find_element(*ArvLogLocators.EXPENSE_LOG_EXPORT).click()

