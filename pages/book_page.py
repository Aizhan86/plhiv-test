import random
import string
from time import sleep
from .base_page import BasePage
from .locators import BookPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date



class BookPage(BasePage):
    def should_add_population(self):
        # проверка объектов на странице Численность населения
        sleep(2)
        assert self.is_element_present(*BookPageLocators.POPULATION_ADD_BTN), "Add object is not presented"
        assert self.is_element_present(*BookPageLocators.POPULATION_YEAR), "Calendar is not presented"
        assert self.is_element_present(*BookPageLocators.MAN_LESS_5), "Field for men less 5 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.MAN_5_14), "Field for men 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.MAN_0_14), "Field for men 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.MAN_15_49), "Field for men 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.MAN_50_MORE), "Field for men 50 y/o and more is not presented"
        assert self.is_element_present(*BookPageLocators.WOMAN_LESS_5), "Field for women less 5 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.WOMAN_5_14), "Field for women 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.WOMAN_0_14), "Field for women 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.WOMAN_15_49), "Field for women 5-14 y/o is not presented"
        assert self.is_element_present(*BookPageLocators.WOMAN_50_MORE), "Field for women 50 y/o and more is not presented"
        assert self.is_element_present(*BookPageLocators.POPULATION_YES_BTN), "Yes object is not presented"

        self.browser.find_element(*BookPageLocators.POPULATION_ADD_BTN).click()
        filter_choice = random.choice(['5', '2', '4'])
        self.browser.execute_script(f"{BookPageLocators.FORM4_PARAM_FILTER}.dropdown('set selected', '{filter_choice}');")
        men_group_5 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.MAN_LESS_5).send_keys(men_group_5)
        men_group_5_14 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.MAN_5_14).send_keys(men_group_5_14)
        men_group_0_14 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.MAN_0_14).send_keys(men_group_0_14)
        men_group_15_49 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.MAN_15_49).send_keys(men_group_15_49)
        men_group_50 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.MAN_50_MORE).send_keys(men_group_50)
        women_group_5 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.WOMAN_LESS_5).send_keys(women_group_5)
        women_group_5_14 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.WOMAN_5_14).send_keys(women_group_5_14)
        women_group_0_14 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.WOMAN_0_14).send_keys(women_group_0_14)
        women_group_15_49 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.WOMAN_15_49).send_keys(women_group_15_49)
        women_group_50 = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*BookPageLocators.WOMAN_50_MORE).send_keys(women_group_50)
        self.browser.find_element(*BookPageLocators.POPULATION_YES_BTN).click()

    def should_generate_form4_monthly(self):
          # проверка объектов на странице Формы 4
          sleep(2)
        assert self.is_element_present(*BookPageLocators.MONTHLY_BTN), "Data range start object is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_PARAM_FILTER), "Filter for parametrizing is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_CALCULATE), "Calculate object is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*BookPageLocators.MONTHLY_BTN).click()
        filter_choice = random.choice(['5', '2', '4'])
        self.browser.execute_script(f"{BookPageLocators.FORM4_PARAM_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*BookPageLocators.FORM4_YEAR_CALENDAR).click()
        self.browser.find_element(*BookPageLocators.FORM4_MONTH_CALENDAR).click()
        self.browser.find_element(*BookPageLocators.FORM4_CALCULATE).click()
        self.browser.find_element(*BookPageLocators.FORM4_EXPORT).click()

    def should_generate_form4_cumulative(self):
        # проверка объектов на странице Формы 4
        sleep(2)
        assert self.is_element_present(*BookPageLocators.MONTHLY_BTN), "Data range start object is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_PARAM_FILTER), "Filter for parametrizing is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_MONTH_FILTER), "Filter for choosing month is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_CALCULATE), "Calculate object is not presented"
        assert self.is_element_present(*BookPageLocators.FORM4_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*BookPageLocators.MONTHLY_BTN).click()
        filter_choice = random.choice(['5', '2', '4'])
        self.browser.execute_script(f"{BookPageLocators.FORM4_PARAM_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*BookPageLocators.FORM4_YEAR_CALENDAR).click()
        filter2_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
        self.browser.execute_script(f"{BookPageLocators.FORM4_MONTH_FILTER}.dropdown('set selected', '{filter2_choice}');")
        self.browser.find_element(*BookPageLocators.FORM4_CALCULATE).click()
        self.browser.find_element(*BookPageLocators.FORM4_EXPORT).click()

    def should_generate_reports_log(self):
        # проверка объектов на странице Журнала отчетов
        sleep(2)
        assert self.is_element_present(*BookPageLocators.REPORTS_LOG_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*BookPageLocators.REPORTS_LOG_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(*BookPageLocators.REPORTS_LOG_APPLY_BTN), "Date range button object is not presented"
        assert self.is_element_present(*BookPageLocators.REPORTS_LOG_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*BookPageLocators.REPORTS_LOG_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*BookPageLocators.REPORTS_LOG_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        self.browser.find_element(*BookPageLocators.REPORTS_LOG_APPLY_BTN).click()
        self.browser.find_element(*BookPageLocators.REPORTS_LOG_EXPORT).click()


    def should_generate_tariffications(self):
        # проверка объектов на странице Тарификаторы
        sleep(2)
        assert self.is_element_present(*BookPageLocators.TARIFFICATION_DATE_START), "Data range start object is not presented"
        assert self.is_element_present(*BookPageLocators.TARIFFICATION_DATE_END), "Date range end object is not presented"
        assert self.is_element_present(*BookPageLocators.TARIFFICATION_FILTER), "Filter for parametrizing is not presented"
        assert self.is_element_present(*BookPageLocators.TARIFFICATION_APPLY_BTN), "Apply object is not presented"
        assert self.is_element_present(*BookPageLocators.TARIFFICATION_EXPORT), "Object for export of report is not presented"

        self.browser.find_element(*BookPageLocators.TARIFFICATION_DATE_START).send_keys("01.01.2019")
        today = date.today()
        self.browser.find_element(*BookPageLocators.TARIFFICATION_DATE_END).send_keys(today.strftime("%d.%m.%y"))
        filter_choice = random.choice(['10', '20'])
        self.browser.execute_script(f"{BookPageLocators.TARIFFICATION_FILTER}.dropdown('set selected', '{filter_choice}');")
        self.browser.find_element(*BookPageLocators.TARIFFICATION_APPLY_BTN).click()
        self.browser.find_element(*BookPageLocators.TARIFFICATION_EXPORT).click()






