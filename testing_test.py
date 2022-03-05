from pages.register_page import RegisterPage
# from pages.config import LinkData
# from .pages.settings_page import SettingsPage
from pages.work_page import WorkPage
from pages.login_page import LoginPage
# from .pages.visits_page import VisitsPage

class TestPlhiv():
    def test_registration_of_child(self, browser):
        login_url = "https://plhiv-demo.dec.kz/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.should_fill_login_form()
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_child()

    # def test_registration_of_homeless(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.register_new_homeless()
    #
    def test_registration_of_adult(self, browser):
        login_url = "https://plhiv-demo.dec.kz/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.should_fill_login_form()
        work_page = WorkPage(browser, browser.current_url)
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_adult()
    #
    # def test_registration_of_foreigner(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_foreign_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.register_new_foreigner()

    def test_editing_general_information_in_patient_card(self, browser):
        login_url = "https://plhiv-demo.dec.kz/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.should_fill_login_form()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.open_card_of_child()
        register_page.edit_card()

    def test_HIV_antibody_testing_OGC_modal(self, browser):
        login_url = "https://plhiv-demo.dec.kz/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        login_page.should_fill_login_form()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.open_card_of_adult()
        register_page.fill_HIV_antibody_testing_OGC_modal()
        # register_page.check_HIV_antibody_testing_OGC_modal()

    # def test_HIV_antibody_testing_KNCDIZ_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_HIV_antibody_testing_KNCDIZ_modal()
    #     register_page.check_HIV_antibody_testing_KNCDIZ_modal()
    #
    # def test_IB_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_IB_modal()
    #     register_page.check_IB_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_family_members_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_family_members_modal()
    #     register_page.check_family_members_modal()
    #
    # def test_luin_modal(self, browser):
    #     config.open_luin_modal()
    #     register_page.fill_and_check_luin_modal()
    #
    # def test_luin_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_luin_modal()
    #     register_page.check_luin_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()
    #
    # def test_PCR_modal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fil_PCR_modal()
    #     register_page.check_PCR_modal()



