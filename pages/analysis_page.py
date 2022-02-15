from random import random
from time import sleep
from .base_page import BasePage
from .locators import WorkJournalLocators, AnalysisPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class AnalysisPage(BasePage):
    def should_generate_detected_cases_log(self):
        # проверка объектов на странице Журнала выявленных случаев
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(
            *AnalysisPageLocators.DETECTED_CASES_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*AnalysisPageLocators.DETECTED_CASES_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DETECTED_CASES_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DETECTED_CASES_LOG_APPLY_BTN), "Date range button object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DETECTED_CASES_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.DETECTED_CASES_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.DETECTED_CASES_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.DETECTED_CASES_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.DETECTED_CASES_LOG_APPLY_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.DETECTED_CASES_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.D_ACCOUNTING_LOG).click()

    def should_generate_d_accounting_log(self):
        # проверка объектов на странице Журнала Д-учета
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.D_ACCOUNTING_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*AnalysisPageLocators.D_ACCOUNTING_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.D_ACCOUNTING_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.D_ACCOUNTING_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.D_ACCOUNTING_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.D_ACCOUNTING_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*AnalysisPageLocators.D_ACCOUNTING_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.D_ACCOUNTING_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.ART_LOG).click()

    def should_generate_art_log(self):
        # проверка объектов на странице Журнала ЛЖВ на АРТ
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.ART_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.ART_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.ART_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.ART_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.ART_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.ART_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.ART_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.ART_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.ART_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.ART_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.DEAD_LOG).click()

    def should_generate_dead_log(self):
        # проверка объектов на странице Журнала умерших
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.DEAD_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DEAD_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DEAD_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DEAD_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DEAD_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.DEAD_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.DEAD_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.DEAD_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.DEAD_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.DEAD_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG).click()

    def should_generate_child_d_accounting_log(self):
        # проверка объектов на странице Журнала умерших
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.CHILD_D_ACCOUNTING_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.PREGNANCY_LOG).click()

    def should_generate_pregnancy_log(self):
        # проверка объектов на странице Журнала беременностей
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.PREGNANCY_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.PREGNANCY_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.PREGNANCY_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.PREGNANCY_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.PREGNANCY_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.PREGNANCY_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.PREGNANCY_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.PREGNANCY_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.PREGNANCY_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.PREGNANCY_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.HIV_LOG).click()

    def should_generate_hiv_log(self):
        # проверка объектов на странице Журнала ВИЧ/ТБ
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.HIV_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.HIV_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.HIV_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.HIV_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.HIV_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.HIV_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.HIV_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.HIV_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.HIV_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.HIV_LOG_EXPORT).click()

        self.browser.find_element(*WorkJournalLocators.HOME_ICON).click()
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        self.browser.find_element(*AnalysisPageLocators.DROPOUT_LOG).click()

    def should_generate_dropout_log(self):
        # проверка объектов на странице Журнала выбывших
        sleep(2)
        assert self.is_element_present(
            *AnalysisPageLocators.DROPOUT_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DROPOUT_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DROPOUT_LOG_FILTER), "Filter dropdown object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DROPOUT_LOG_GENERATE_BTN), "Generate object is not presented"
        assert self.is_element_present(
            *AnalysisPageLocators.DROPOUT_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*AnalysisPageLocators.DROPOUT_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*AnalysisPageLocators.DROPOUT_LOG_DATE_END).send_keys(
            today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(
            f"{AnalysisPageLocators.DROPOUT_LOG_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*AnalysisPageLocators.DROPOUT_LOG_GENERATE_BTN).click()
        self.browser.find_element(*AnalysisPageLocators.DROPOUT_LOG_EXPORT).click()

