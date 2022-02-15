from time import sleep
from .base_page import BasePage
from .locators import VizitsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date



class VisitsPage(BasePage):
      def should_generate_sample_report(self):
        # проверка объектов на странице Журнала визитов
        sleep(2)
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(*WorkJournalLocators.DATE_RANGE_START)
        assert self.is_element_present(*VizitsPageLocators.DATE_RANGE_START), "Data range start object is not presented"
        assert self.is_element_present(*VizitsPageLocators.DATE_RANGE_END), "Date range end object is not presented"
        assert self.is_element_present(*VizitsPageLocators.DATE_RANGE_BTN), "Date range button object is not presented"
        assert self.is_element_present(*VizitsPageLocators.EXPORT_REPORT), "Object for export of report is not presented"

        self.browser.find_element(*VizitsPageLocators.DATE_RANGE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*VizitsPageLocators.DATE_RANGE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*VizitsPageLocators.DATE_RANGE_BTN).click()
        self.browser.find_element(*VizitsPageLocators.EXPORT_REPORT).click()