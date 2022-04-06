from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from .locators import RegisterPageLocators, PatientCardLocators, WorkJournalLocators, ArvLogLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random

class ArvLogs(BasePage):

    eighty_days_ago = datetime.strftime(datetime.now() - timedelta(days=80), '%d.%m.%Y')
    sixty_days_ago = datetime.strftime(datetime.now() - timedelta(days=60), '%d.%m.%Y')
    fifty_days_ago = datetime.strftime(datetime.now() - timedelta(days=50), '%d.%m.%Y')
    thirty_days_ago = datetime.strftime(datetime.now() - timedelta(days=30), '%d.%m.%Y')
    twenty_days_ago = datetime.strftime(datetime.now() - timedelta(days=20), '%d.%m.%Y')
    regis_date = datetime.strftime(datetime.now() - timedelta(days=50), '%d.%m.%Y')
    deregis_date = datetime.strftime(datetime.now() - timedelta(days=5), '%d.%m.%Y')
    ib_date = datetime.strftime(datetime.now() - timedelta(days=180), '%d.%m.%Y')
    diagnosis_date = datetime.strftime(datetime.now() - timedelta(days=190), '%d.%m.%Y')
    thirty_days_forward = datetime.strftime(datetime.now() + timedelta(days=30), '%d.%m.%Y')
    fifty_days_forward = datetime.strftime(datetime.now() + timedelta(days=50), '%d.%m.%Y')
    expiration_date = datetime.strftime(datetime.now() + timedelta(days=365), '%d.%m.%Y')
    numbers3 = ''.join(random.choices(string.digits, k=3))
    numbers4 = ''.join(random.choices(string.digits, k=4))
    numbers5 = ''.join(random.choices(string.digits, k=5))
    surname = ''.join(random.choices(string.ascii_uppercase, k=10))

    def should_test_receipt_log(self):
        self.fill_receipt_log()
        # self.check_receipt_log()

    def fill_receipt_log(self):
        self.make(f"{ArvLogLocators.ARV_LOGS_MENU}.click()")
        self.make(f"{ArvLogLocators.RECEIPT_LOG}.click()")
        self.make(f"{ArvLogLocators.RECEIPT_ADD}.click()")
        new_window = self.browser.window_handles[1]
        first_window = self.browser.window_handles[0]
        self.browser.switch_to.window(new_window)
        budget_choice = random.choice(['1', '2', '3', '4'])
        self.make(f"{ArvLogLocators.BUDGET_TYPE}.dropdown('set selected', '{budget_choice}');")
        p18 = random.choice(['1', '2', '3'])
        self.make(f"{ArvLogLocators.SUPPLIER}.dropdown('set selected', 'p18');")
        self.make(f"{ArvLogLocators.CONTRACT_NUM}.val('{self.numbers3}');")
        self.make(f"{ArvLogLocators.INVOICE_NUM}.val('{self.numbers5}');")
        self.make(f"{ArvLogLocators.MED_RECEIPT_DATE}.val('{self.twenty_days_ago}');")
        # p18 = random.choice(['1', '2', '3', '4'])
        self.make(f"{ArvLogLocators.PROGRAMM}.dropdown('set selected', '2');")
        self.make(f"{ArvLogLocators.RECIPIENT_NAME}.val('{self.surname}');")
        procurement_choice = random.choice(['1', '2', '3'])
        self.make(f"{ArvLogLocators.PROCUREMENT_TYPE}.dropdown('set selected', '{procurement_choice}');")
        self.make(f"{ArvLogLocators.CONTRACT_DATE}.val('{self.thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_ADD}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{self.thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{self.expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('2500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{self.numbers4}');")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{self.thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{self.expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('4500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{self.numbers4}');")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{self.thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{self.expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('9500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{self.numbers4}');")
        self.make(f"{ArvLogLocators.RECEIPT_SAVE}.click()")
        self.browser.close()
        self.browser.switch_to.window(first_window)
