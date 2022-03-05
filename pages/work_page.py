import random
from time import sleep
from .base_page import BasePage
from .locators import WorkJournalLocators, RegisterPageLocators, VizitsPageLocators, ArvLogLocators, \
    AnalysisPageLocators, BookPageLocators, SettingsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date


class WorkPage(BasePage):
    def should_add_kz_patient(self):
        # переход на страницу с регистрационной формой для казахстанцев
        assert self.is_element_present(*RegisterPageLocators.ADD_PATIENT), "Incorrect link to KZ Patient registration"
        self.browser.find_element(*RegisterPageLocators.ADD_PATIENT).click()

    def should_add_foreign_patient(self):
        # переход на страницу с регистрационной формой для казахстанцев
        assert self.is_element_present(*RegisterPageLocators.ADD_FOREIGN_PATIENT), "Incorrect link to foreign Patient registration"
        self.browser.find_element(*RegisterPageLocators.ADD_FOREIGN_PATIENT).click()

    def should_generate_sample_work_log(self):
        # проверка объектов на странице рабочего журнала
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        # assert self.is_element_present(*WorkJournalLocators.DATE_RANGE_START), "Data range start object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.DATE_RANGE_END), "Date range end object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.DATA_TYPE), "Object for selection of data type is not presented"
        # assert self.is_element_present(*WorkJournalLocators.DATE_RANGE_BTN), "Date range button object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EXPORT_REPORT), "Object for export of report is not presented"

        self.browser.find_element(*WorkJournalLocators.DATE_RANGE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*WorkJournalLocators.DATE_RANGE_END).send_keys(today.strftime("%d.%m.%y"))
        data_type_choice = random.choice(['1', '2', '3'])
        self.make(f"{WorkJournalLocators.DATA_TYPE}.dropdown('set selected', '{data_type_choice}');")
        self.browser.find_element(*WorkJournalLocators.DATE_RANGE_BTN).click()
        self.browser.find_element(*WorkJournalLocators.EXPORT_REPORT).click()

    def should_fill_epi_detected_in_current_region(self):
        # проверка объектов в окне для выгрузки в Epi info
        sleep(2)
        # assert self.is_element_present(*WorkJournalLocators.EPI_DATE_RANGE_START), "Data range start object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_DATE_RANGE_END), "Date range end object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_DETECTED_IN_CUR_REG), "Object for selection of data type is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_GENERATE), "Object for export of report is not presented"

        self.browser.find_element(*WorkJournalLocators.EPI_DATE_RANGE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*WorkJournalLocators.EPI_DATE_RANGE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*WorkJournalLocators.EPI_DETECTED_IN_CUR_REG).click()
        self.browser.find_element(*WorkJournalLocators.EPI_GENERATE).click()

    def should_fill_epi_d_accounted_in_current_region(self):
        # проверка объектов в окне для выгрузки в Epi info
        sleep(2)
        # assert self.is_element_present(*WorkJournalLocators.EPI_DATE_RANGE_START), "Data range start object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_DATE_RANGE_END), "Date range end object is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_D-ACCOUNTED_IN_CUR_REG), "Object for selection of data type is not presented"
        # assert self.is_element_present(*WorkJournalLocators.EPI_GENERATE), "Object for export of report is not presented"

        self.browser.find_element(*WorkJournalLocators.EPI_DATE_RANGE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*WorkJournalLocators.EPI_DATE_RANGE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*WorkJournalLocators.EPI_D_ACCOUNTED_IN_CUR_REG).click()
        self.browser.find_element(*WorkJournalLocators.EPI_GENERATE).click()

    def should_switch_to_visits_page(self):
        # переход на страницу Журнала визитов
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*VizitsPageLocators.VISITS_LINK).click()

    def should_switch_to_analysis_page(self):
        # переход на страницу Журнала визитов
        self.browser.find_element(*WorkJournalLocators.WORK_JOURNAL_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*AnalysisPageLocators.DETECTED_CASES_LOG).click()

    def should_switch_to_arv_logs_page(self):
        # переход на страницу Журнала АРВ
        self.browser.find_element(*WorkJournalLocators.ARV_LOG_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*ArvLogLocators.CONTRACT_LOG).click()


    def should_switch_to_form4_in_book_page(self):
        # переход на страницу Формы 4
        self.browser.find_element(*WorkJournalLocators.BOOK_ICON_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*BookPageLocators.FORM4).click()

    def should_switch_to_reports_log_in_book_page(self):
        # переход на страницу Отчеты в меню
        self.browser.find_element(*WorkJournalLocators.BOOK_ICON_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*BookPageLocators.FORM4).click()

    def should_switch_to_tariffication_in_book_page(self):
        # переход на страницу Тариффикация в меню
        self.browser.find_element(*WorkJournalLocators.BOOK_ICON_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*BookPageLocators.FORM4).click()

    def should_switch_to_population_in_book_page(self):
        # переход на страницу Население в меню
        self.browser.find_element(*WorkJournalLocators.BOOK_ICON_MENU).click()
        # assert self.is_element_present(*VizitsPageLocators.VISITS_LINK), "Incorrect link to Foreign Patient registration"
        self.browser.find_element(*BookPageLocators.FORM4).click()

    def should_switch_to_organizations_in_settings_page(self):
        # переход на страницу Организации в Настройках прложения
        self.browser.find_element(*WorkJournalLocators.SETTINGS_ICON_MENU).click()
        # assert self.is_element_present(*SettingsPageLocators.ORGANIZATION), "Incorrect link to ORGANIZATION"
        self.browser.find_element(*SettingsPageLocators.ORGANIZATION).click()

    def should_switch_to_users_in_settings_page(self):
        # переход на страницу Пользователи в Настройках прложения
        self.browser.find_element(*WorkJournalLocators.SETTINGS_ICON_MENU).click()
        # assert self.is_element_present(*SettingsPageLocators.USERS), "Incorrect link to USERS"
        self.browser.find_element(*SettingsPageLocators.USERS).click()