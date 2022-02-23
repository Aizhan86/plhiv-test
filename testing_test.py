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
        register_page.register_new_child_and_edit_card()

    # def test_family_members_modal(self, browser):
        # login_url = "https://plhiv-demo.dec.kz/"
        # login_page = LoginPage(browser, login_url)
        # login_page.open()
        # login_page.should_fill_login_form()
        # work_page = WorkPage(browser, browser.current_url)
        # work_page.should_add_kz_patient()
        # register_page = RegisterPage(browser, browser.current_url)
        # register_page.register_new_child()
        # register_page.edit_card()

    # def test_registration_of_bomj(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.register_new_bomj_and_edit_card()
    #
    # def test_registration_of_new_citizen(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.register_new_citizen_and_edit_card()
    #
    # def test_registration_of_new_foreigner(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_add_kz_patient()
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.register_new_foreigner_and_edit_card()

    # def test_work_journal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_generate_sample_work_log()

    # def test_epi_info(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_fill_epi_detected_in_current_region()
    #     work_page.should_fill_epi_d_accounted_in_current_region()

    # def test_visit_journal(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_visits_page()
    #     visits_page = VisitsPage(browser, browser.current_url)
    #     visits_page.should_generate_sample_report()

    # def test_analysis_logs(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_analysis_page()
    #     analysis_page = AnalysisPage(browser, browser.current_url)
    #     analysis_page.should_generate_detected_cases_log()
    #     analysis_page.should_generate_d_accounting_log()
    #     analysis_page.should_generate_art_log()
    #     analysis_page.should_generate_dead_log()
    #     analysis_page.should_generate_child_d_accounting_log()
    #     analysis_page.should_generate_pregnancy_log()
    #     analysis_page.should_generate_hiv_log()
    #     analysis_page.should_generate_dropout_log()

    # def test_arv_logs(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_arv_logs_page()
    #     arv_page = ArvPage(browser, browser.current_url)
    #     arv_page.should_generate_contract_log()
    #     arv_page.should_generate_debit_log()
    #     arv_page.should_generate_arrival_log()
    #     arv_page.should_generate_expense_log()

    # def test_population(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_population_in_book_page()
    #     book_page = BookPage(browser, browser.current_url)
    #     book_page.should_add_population()

    # def test_form4_monthly(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_form4_in_book_page()
    #     book_page = BookPage(browser, browser.current_url)
    #     book_page.should_generate_form4_monthly()

    # def test_form4_cumulative(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_form4_in_book_page()
    #     book_page = BookPage(browser, browser.current_url)
    #     book_page.should_generate_form4_cumulative()

    # def test_reports_log(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_reports_log_in_book_page()
    #     book_page = BookPage(browser, browser.current_url)
    #     book_page.should_generate_reports_log()

    # def test_tariffication(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_tariffication_in_book_page()
    #     book_page = BookPage(browser, browser.current_url)
    #     book_page.should_generate_tariffications()

    # def test_addition_of_aidc_center(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_organizations_in_settings_page()
    #     settings_page = SettingsPage(browser, browser.current_url)
    #     settings_page.should_add_aidc_center()
    #
    # def test_addition_of_new_user(self, browser):
    #     login_url = "https://plhiv-demo.dec.kz/login?next=%2F"
    #     login_page = LoginPage(browser, login_url)
    #     login_page.open()
    #     login_page.should_fill_login_form()
    #     work_page = WorkPage(browser, browser.current_url)
    #     work_page.should_switch_to_users_in_settings_page()
    #     settings_page = SettingsPage(browser, browser.current_url)
    #     settings_page.should_add_new_user()
