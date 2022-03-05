from time import sleep
from .base_page import BasePage
from .config import UserData
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_fill_login_form(self):
        # проверка, что есть форма логина и объекты на ней
        self.is_element_present(*LoginPageLocators.USER_NAME)
        self.browser.find_element(*LoginPageLocators.USER_NAME).send_keys(*UserData.NAME)

        self.is_element_present(*LoginPageLocators.USER_PASS)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(*UserData.PASSWORD)

        self.is_element_clickable(*LoginPageLocators.LOGIN_BTN)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

        #  проверка, что есть форма модального соглашения и кликнуть на кнопку согласия
        # if self.is_element_present(*LoginPageLocators.MODAL_AGR):
        #     self.browser.find_element(*LoginPageLocators.AGR_BTN).click()
        # self.make("return arguments[0].scrollIntoView(true);", agr_btn)

class OpenPage(BasePage):
    def open_luin_modal(self):
        login_url = "https://plhiv-demo.dec.kz/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.should_fill_login_form()
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_find_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_open_luin_modal


