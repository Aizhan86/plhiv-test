from time import sleep
from .base_page import BasePage
from .config import UserData
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_fill_login_form(self):
        # проверка, что есть форма логина и объекты на ней
        assert self.is_element_present(*LoginPageLocators.USER_NAME)
        self.browser.find_element(*LoginPageLocators.USER_NAME).send_keys(*UserData.NAME)

        assert self.is_element_present(*LoginPageLocators.USER_PASS)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(*UserData.PASSWORD)

        # assert self.is_element_present(*LoginPageLocators.LOGIN_BTN)
        self.make(f"{LoginPageLocators.LOGIN_BTN}.click()")

         # проверка, что есть форма модального соглашения и кликнуть на кнопку согласия
        if self.is_element_present(*LoginPageLocators.MODAL_AGR):
            agr_btn = self.browser.find_element(*LoginPageLocators.AGR_BTN)
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", agr_btn)
            agr_btn.click()


