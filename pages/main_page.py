from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from .locators import PatientCardLocators, WorkJournalLocators, ArvLogLocators, AnalysisPageLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random
from .values import *

class ArvLogs(BasePage):


    def fill_receipt_log(self):
        self.make(f"{AnalysisPageLocators.LOGS_MENU}.click()")
        self.make(f"window.location = {ArvLogLocators.RECEIPT_LOG}.attr('href')")
        self.make(f"{ArvLogLocators.ORG_FILTER}.dropdown('set selected', '29')")
        self.make(f"window.location = {ArvLogLocators.RECEIPT_ADD}.attr('href')")
        sleep(2)
        self.make(f"{ArvLogLocators.RECEIPT_TYPE}.dropdown('set selected', '0');")
        self.make(f"{ArvLogLocators.BUDGET_TYPE}.dropdown('set selected', '{budget_choice}');")
        self.make(f"{ArvLogLocators.SUPPLIER}.dropdown('set selected', '{three_choice}');")
        self.make(f"{ArvLogLocators.CONSIGNMENT_NUM}.val('{numbers3}');")
        self.make(f"{ArvLogLocators.INVOICE_NUM}.val('{numbers5}');")
        self.make(f"{ArvLogLocators.RECEIPT_DATE}.val('{today}');")
        self.make(f"{ArvLogLocators.PROGRAMM}.dropdown('set selected', '2');")
        self.make(f"{ArvLogLocators.RECIPIENT_NAME}.val('{surname}');")
        self.make(f"{ArvLogLocators.PROCUREMENT_TYPE}.dropdown('set selected', '{three_choice}');")
        self.make(f"{ArvLogLocators.CONTRACT_NUM_DATE}.val('№{numbers4} от {today}');")
        self.make(f"{ArvLogLocators.MEDICATION_ADD}.click()")
        # self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('3TC');")
        self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('1500');")
        self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvLogLocators.MEDICATION_ADD}.click()")
        # self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('DRV/c');")
        # self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        # self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        # self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('30');")
        # self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('2500');")
        # self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        # self.make(f"{ArvLogLocators.MEDICATION_SEARCH}.val('{thirty_days_ago}');")
        # self.make(f"{ArvLogLocators.MEDICATION_CHOICE}.click()")
        # self.make(f"{ArvLogLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        # self.make(f"{ArvLogLocators.MEDICATION_AMOUNT}.val('1');")
        # self.make(f"{ArvLogLocators.MEDICATION_PRICE}.val('9500');")
        # self.make(f"{ArvLogLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvLogLocators.RECEIPT_LOG_SAVE}.click()")
