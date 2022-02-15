from time import sleep
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_fill_login_form(self):
        # проверка, что есть форма логина и объекты на ней
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not accessible"
        assert self.is_element_present(*LoginPageLocators.USER_NAME), "No field for the User's IIN"
        assert self.is_element_present(*LoginPageLocators.USER_PASS), "No field for the User's password"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "No Login button"


        self.browser.find_element(*LoginPageLocators.USER_NAME).send_keys("aizha.o")
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys("Sunshine86!")
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

        sleep(2)
        #  проверка, что есть форма модального соглашения и кликнуть на кнопку согласия
        if self.is_element_present(*LoginPageLocators.MODAL_AGR):
            self.browser.find_element(*LoginPageLocators.AGR_BTN).click()
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", agr_btn)


