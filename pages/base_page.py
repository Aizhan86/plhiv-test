from time import sleep
from .values import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

from pages.locators import PatientCardLocators, WorkJournalLocators


class BasePage(object):

    # Мы создаем конструктор, в котором передаются тело браузера и ссылка для дальнейшего использования

    def __init__(self, browser, url, timeout=10):
        super(BasePage, self).__init__()
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # def get_environ(name, *args):
    #     environ = os.environ.get(name, "https://plhiv-demo.dec.kz/")
    #
    #     if str(environ).startswith('/run/secrets/'):
    #         if os.path.exists(environ):
    #             with open(environ, 'r') as secrets_file:
    #                 environ = secrets_file.read()
    #                 secrets_file.close()
    #
    #     return environ

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=10):
        try:
            self.browser.find_element(how, what)
            self.browser.implicitly_wait(timeout)
        except NoSuchElementException:
            return False
        return True

    def make(self, action, timeout=10):
        try:
            self.browser.execute_script(action)
            self.browser.implicitly_wait(timeout)
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    # def take_screenshot(self):
    #     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     namefile = f"screenshot-{now}.png"
    #     self.browser.get_screenshot_as_file(namefile)
    #     self.browser.save_screenshot('C:\Work\plhiv-test\screenshots')
    #     print(f"Taked screenshot: {namefile}")

    def choose_user_organization(self, user_org):
        self.make(f"{PatientCardLocators.USER_NAME}.click()")
        self.make(f"$('div[data-name=account-settings] div.menu').children()[0].click()")
        self.make(f"document.querySelector('[id=account-edit]').click()")
        self.make(f"{PatientCardLocators.MED_ORG_REMOVE}.click()")
        self.make(f"{PatientCardLocators.MED_ORG}.dropdown('set selected', '{user_org}');")
        self.make(f"{PatientCardLocators.WORKING_SCHEDULE}.dropdown('set selected', '1')")
        self.make(f"{PatientCardLocators.USER_DATA_SAVE}.click()")
        self.make(f"{WorkJournalLocators.HOME_ICON}.click()")

    def get_patient_id(self):
        enc = 0
        patient_id = self.browser.current_url.split('/')[-1].split('?')[0]
        while patient_id == "0000000000":
            patient_id = self.browser.current_url.split('/')[-1].split('?')[0]
            enc += 1
            sleep(1)
            if enc == 10:
                break
        return patient_id

    def get_referral(self, ref_type, ref_name):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.REFFERALS}.click();")  # Выбрали Направления
        self.make(f"{PatientCardLocators.REFERRAL_ADD}.click();")
        self.make(f"{PatientCardLocators.REFERRAL_TYPE}.dropdown('set selected', '{ref_type}');")
        self.make(f"{PatientCardLocators.REFERRAL_DATE}.calendar('set date', '{today}');")
        # referral_name_choice = random.choice(['178', '35', '36', '37', '38', '40', '46']) {referral_name_choice}
        self.make(f"{PatientCardLocators.REFERRAL_NAME}.dropdown('set selected', '{ref_name}');")
        self.make(f"{PatientCardLocators.REFERRAL_NUM}.val('{numbers4}');")
        # self.make(f"{PatientCardLocators.SENDER_ORG}.dropdown('set selected', '{mo_choice2}');")
        # self.make(f"{PatientCardLocators.RECIPIENT_ORG}.dropdown('set selected', '{mo_choice2}');")
        # category_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])
        # self.make(f"{PatientCardLocators.CATEGORY}.dropdown('set selected', '{category_choice}');")
        # self.make(f"{PatientCardLocators.NOSOLOGY}.click();")
        # self.make(f"{PatientCardLocators.NOSOLOGY_CHOICE}.click();")
        # self.make(f"{PatientCardLocators.SURVEY_ELEMENTS}.val('Не знаю');")
        # self.make(f"{PatientCardLocators.SCREENING_RESULT}.val('Положительный');")
        self.make(f"{PatientCardLocators.REFERRAL_SAVE}.click();")







