from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from .locators import PatientCardLocators, WorkJournalLocators, ArvLogLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random
from .values import *

class ArvLogs(BasePage):

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
        self.make(f"{ArvLogLocators.CONTRACT_NUM}.val('{numbers3}');")
        self.make(f"{ArvLogLocators.INVOICE_NUM}.val('{numbers5}');")
        self.make(f"{ArvLogLocators.MED_RECEIPT_DATE}.val('{twenty_days_ago}');")
        # p18 = random.choice(['1', '2', '3', '4'])
        self.make(f"{ArvLogLocators.PROGRAMM}.dropdown('set selected', '2');")
        self.make(f"{ArvLogLocators.RECIPIENT_NAME}.val('{surname}');")
        procurement_choice = random.choice(['1', '2', '3'])
        self.make(f"{ArvLogLocators.PROCUREMENT_TYPE}.dropdown('set selected', '{procurement_choice}');")
        self.make(f"{ArvLogLocators.CONTRACT_DATE}.val('{thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_ADD}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('2500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('4500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{thirty_days_ago}');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('9500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvLogLocators.RECEIPT_SAVE}.click()")
        self.browser.close()
        self.browser.switch_to.window(first_window)
