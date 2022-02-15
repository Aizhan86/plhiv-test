from datetime import datetime, timedelta

from .base_page import BasePage
from .locators import SettingsPageLocators
from time import sleep
import string
import random

class SettingsPage(BasePage):
    def should_add_aidc_center(self):
        full_center_ru = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*SettingsPageLocators.FULL_CENTER_NAME_RU).send_keys(full_center_ru)
        dropped_center_ru = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*SettingsPageLocators.DROPPED_CENTER_NAME_RU).send_keys(dropped_center_ru)
        full_center_kz = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*SettingsPageLocators.FULL_CENTER_NAME_KZ).send_keys(full_center_kz)
        dropped_center_kz = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*SettingsPageLocators.DROPPED_CENTER_NAME_KZ).send_keys(dropped_center_kz)
        area_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.browser.execute_script(f"{SettingsPageLocators.CENTER_AREA}.dropdown('set selected', '{area_choice}');")
        city = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*SettingsPageLocators.CENTER_CITY).send_keys(city)
        street_choice = random.choice(['Назарбаев', 'Абай', 'Конаев', 'Кабанбай батыр', ])
        self.browser.find_element(*SettingsPageLocators.CENTER_STREET).send_keys(street_choice)
        self.browser.find_element(*SettingsPageLocators.CENTER_HOUSE).send_keys(25)
        self.browser.find_element(*SettingsPageLocators.CENTER_APT).send_keys(45)
        level_choice = random.choice(['1', '2', '3'])
        self.browser.execute_script(f"{SettingsPageLocators.LEVEL}.dropdown('set selected', '{level_choice}');")
        okpo = ''.join(random.choices(string.digits, k=5))
        self.browser.find_element(*SettingsPageLocators.OKPO).send_keys(okpo)
        director = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*SettingsPageLocators.DIRECTOR_NAME).send_keys(director)
        main_org_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.browser.execute_script(f"{SettingsPageLocators.MAIN_ORG}.dropdown('set selected', '{main_org_choice}');")
        self.browser.find_element(*SettingsPageLocators.REPUB_SIGNIFICANCE).click()
        self.browser.find_element(*SettingsPageLocators.CSM).click()
        self.browser.find_element(*SettingsPageLocators.SMS_EMAIL).click()
        repres_org_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.browser.execute_script(f"{SettingsPageLocators.REPRESENT_ORG}.dropdown('set selected', '{repres_org_choice}');")
        self.browser.find_element(*SettingsPageLocators.CENTER_ACCESS1).click()
        self.browser.find_element(*SettingsPageLocators.CENTER_SAVE).click()

    def should_add_new_user(self):
        role_choice = random.choice(['20', '30'])
        self.browser.execute_script(f"{SettingsPageLocators.ROLE}.dropdown('set selected', '{role_choice}');")
        surname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*SettingsPageLocators.USER_SURNAME).send_keys(surname)
        name = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*SettingsPageLocators.USER_NAME).send_keys(name)
        middle_name = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*SettingsPageLocators.USER_MIDDLE_NAME).send_keys(middle_name)
        d1 = datetime.strptime('01.01.1960', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2005', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(random.randrange(int_delta))
        first_numbers = random_date.strftime('%y%m%d')
        birthday = random_date.strftime('%d.%m.%Y')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*SettingsPageLocators.USER_IIN).send_keys(iin)
        devision_choice = random.choice(['10000000003', '60000000007', '60000000005', '70000000008'])
        self.browser.execute_script(f"{SettingsPageLocators.DEVISION}.dropdown('set selected', '{devision_choice}');")
        occupation = ''.join(random.choices(string.ascii_uppercase, k=5))
        self.browser.find_element(*SettingsPageLocators.USER_OCCUPATION).send_keys(occupation)
        others = random.randrange(1000000, 999999)
        phone = f'{8700}{others}'
        self.browser.find_element(*SettingsPageLocators.USER_PHONE).send_keys(phone)
        self.browser.find_element(*SettingsPageLocators.LABORATORY).click()
        self.browser.find_element(*SettingsPageLocators.EPID_DEVISION).click()
        self.browser.find_element(*SettingsPageLocators.DISP_DEVISION).click()
        self.browser.find_element(*SettingsPageLocators.REVIEW).click()
        self.browser.find_element(*SettingsPageLocators.ARV_ACCOUNTING).click()
        self.browser.find_element(*SettingsPageLocators.LEGEND_REVISE).click()
        org_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.browser.execute_script(f"{SettingsPageLocators.USER_ORGANIZATION}.dropdown('set selected', '{org_choice}');")
        self.browser.find_element(*SettingsPageLocators.USER_ADD).click()

