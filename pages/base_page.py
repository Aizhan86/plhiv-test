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

    def get_environ(name, *args):
        environ = os.environ.get(name, "https://plhiv-demo.dec.kz/")

        if str(environ).startswith('/run/secrets/'):
            if os.path.exists(environ):
                with open(environ, 'r') as secrets_file:
                    environ = secrets_file.read()
                    secrets_file.close()

        return environ

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
        self.make(f"{PatientCardLocators.USER_DATA_SAVE}.click()")
        self.make(f"{WorkJournalLocators.HOME_ICON}.click()")

    def take_patient_id(self):
        id_url = self.browser.current_url
        url_part = id_url.split('/')[5]
        patient_id = url_part.split('?')[0]
        return patient_id




