import pytest
import allure
from sentry_sdk import capture_exception
from pages.arv_logs import ArvLogs
from pages.register_page import RegisterPage
from pages.work_page import WorkPage
from pages.login_page import LoginPage


def login(browser):
    login_url = "https://plhiv-demo.dec.kz/"
    login_page = LoginPage(browser, login_url)
    login_page.open()
    login_page.should_fill_login_form()

def kncdiz_user_opens_card_of_child(browser):
    work_page = WorkPage(browser, browser.current_url)
    work_page.choose_KNCDIZ_as_user_org()
    work_page.open_card_of_child()

def zhetysai_user_opens_card_of_foreigner(browser):
    work_page = WorkPage(browser, browser.current_url)
    work_page.choose_Zhetysai_as_user_org()
    work_page.open_card_of_foreigner()

def zhetysai_user_opens_card_of_child(browser):
    work_page = WorkPage(browser, browser.current_url)
    work_page.choose_Zhetysai_as_user_org()
    work_page.open_card_of_child()





class TestGeneralData():
    def test_registration_of_child(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_child()

    def test_patient_id(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_id_child()

    def test_patient_iin(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_iin()

    def test_patient_surname(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_surname()

    def test_patient_birth_date(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_birth_date()

    def test_patient_gender(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_gender()

    def test_emergence_area(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_emergence_area()

    def test_patient_midname(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_midname()

    def test_patient_name(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_name()

    def test_patient_citizenship(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_citizenship()

    def test_child_status(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_child_status()

    def test_social_status(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_social_status()

    def test_edit_button_registration_address_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_registration_address_modal()

    def test_registration_area(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_area()

    def test_registration_unit_area(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_unit_area()

    def test_registration_locality(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_locality()

    def test_registration_place(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_place()

    def test_registration_street(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_street()

    def test_registration_house(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_house()

    def test_registration_apartment(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_apartment()

    def test_registration_phone_number(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_phone_number()

    def test_cancel_button_registration_address_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_registration_address_modal()

    def test_edit_button_residence_address_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_residence_address_modal()

    def test_residence_area(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_area()

    def test_residence_unit_area(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_unit_area()

    def test_residence_locality(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_locality()

    def test_residence_place(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_place()

    def test_residence_street(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_street()

    def test_residence_house(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_house()

    def test_residence_apartment(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_apartment()

    def test_residence_phone_number(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_residence_locality()

    def test_cancel_button_residence_address_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_residence_address_modal()

    # def test_residence_medical_organization(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_residence_medical_organization()
    #
    # def test_retrospective_child_checkbox(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_retrospective_child_checkbox()
    #
    # def test_surname_of_mother(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_surname_of_mother()
    #
    # def test_name_of_mother(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_name_of_mother()
    #
    # def test_midname_of_mother(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_midname_of_mother()
    #
    # def test_ib_number_of_mother(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_ib_number_of_mother()
    #
    # def test_ib_number_date_of_mother(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_ib_number_date_of_mother()

@allure.severity(allure.severity_level.NORMAL)
class TestChildCase():
    @pytest.mark.smoke
    def test_fill_HIV_antibody_testing_ogc_modal(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_child()
        register_page.fill_hiv_antibody_testing_ogc_modal()

    @pytest.mark.skipif(test_fill_HIV_antibody_testing_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_medical_organization_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_medical_organization_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_surname_of_person_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_surname_of_person_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_referral_number_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_referral_number_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_blood_sampling_date_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_blood_sampling_date_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_receipt_date_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_receipt_date_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_production_date_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_production_date_hiv_ogc_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # def test_serum_number_hiv_ogc_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_serum_number_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_serum_number2_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_serum_number2_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_testing_system_type_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_test_system_type_hiv_ogc_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # def test_expiration_date_hiv_ogc_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_expiration_date_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_series_number_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_series_number_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_testing_category_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_test_category_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_op_critical_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_op_critical_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_op_serum_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_op_serum_hiv_ogc_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # def test_result_hiv_ogc_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_result_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_responsible_person_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_responsible_person_hiv_ogc_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # def test_services_hiv_ogc_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_services_hiv_ogc_modal()

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_hiv_ogc_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_hiv_ogc_modal()

    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_fill_HIV_antibody_testing_KNCDIZ_modal(self, browser):
    #     kncdiz_user_opens_card_of_child(browser)
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_HIV_antibody_testing_KNCDIZ_modal()
    #
    # @pytest.mark.skipif(test_fill_HIV_antibody_testing_KNCDIZ_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_screening_number_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_screening_number_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_serum_number_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_serum_number_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_referral_number_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_referral_number_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_production_date_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_production_date_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_testing_system_type_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_test_system_type_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_expiration_date_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_expiration_date_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_series_number_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_series_number_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_op_critical_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_op_critical_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_op_serum_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_op_serum_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_result_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_result_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_hiv_kncdiz_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_hiv_kncdiz_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_fill_IB_modal(self, browser):
    #     zhetysai_user_opens_card_of_child(browser)
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.get_refferal_for_ib()
    #     register_page.get_refferal_for_pcr()
    #     kncdiz_user_opens_card_of_child(browser)
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_IB_modal()
    #
    # @pytest.mark.skipif(test_fill_IB_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_ib_number_in_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_ib_number_in_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_serum_number_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_serum_number_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_sample_number_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_sample_number_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_receipt_date_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_receipt_date_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_register_date_ib_modal(self, browser):
    #     kncdiz_user_opens_card_of_child(browser)
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_register_date_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_register_date_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_register_date_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_result_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_result_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_test_system_name_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_test_system_name_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_expiration_date_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_expiration_date_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_series_number_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_series_number_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_responsible_person_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_responsible_person_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_gp160_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_gp160_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_gp110_120_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_gp110_120_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p68_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p68_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p55_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p55_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p52_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p52_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_gp41_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_gp41_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p40_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p40_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p34_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p34_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p25_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p25_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_p18_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_p18_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_services_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_services_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_ib_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_ib_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_fill_PCR_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_PCR_modal()
    #
    # @pytest.mark.skipif(test_fill_PCR_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_pcr_number_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_pcr_number_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_serum_number_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_serum_number_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_sample_number_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_sample_number_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_pcr_type_in_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_pcr_type_in_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_receipt_date_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_receipt_date_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_register_date_pcr_modal(self, browser):
    #     kncdiz_user_opens_card_of_child(browser)
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_register_date_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_test_system_name_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_test_system_name_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_expiration_date_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_expiration_date_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_series_number_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_series_number_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_result_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_result_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_responsible_person_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_responsible_person_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_services_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_services_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_pcr_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_pcr_modal()
    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # @pytest.mark.smoke
    # def test_result_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_result_modal()
    #     print(f"test_result_modal passed")
#
# @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_receipt_log(self, browser):
#         login(browser)
#         arv_page = ArvLogs(browser, browser.current_url)
#         arv_page.should_test_receipt_log()
#         print(f"test_receipt_log passed")

    @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    def test_perinatal_registration_modal(self, browser):
        zhetysai_user_opens_card_of_child(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_dispensary_observation_modal()
        register_page.fill_perinatal_registration_modal()

    #
    # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
    # def test_arv_prophylaxis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_arv_prophylaxis_modal()
    #     print(f"test_arv_prophylaxis_modal passed")


@allure.severity(allure.severity_level.NORMAL)
class TestHomelessCase():
    @pytest.mark.smoke
    def test_registration_of_homeless(self, browser):
        try:
            login(browser)
            work_page = WorkPage(browser, browser.current_url)
            work_page.choose_Zhetysai_as_user_org()
            work_page.should_add_kz_patient()
            register_page = RegisterPage(browser, browser.current_url)
            register_page.register_new_homeless()
            print(f"test_registration_of_homeless passed")
        except Exception as e:
            capture_exception(e)

    def test_patient_id_homeless(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_id_homeless()
    #
    # @pytest.mark.smoke
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_family_members_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_family_members_modal()
    #     print(f"test_family_members_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_luin_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_luin_modal()
    #     print(f"test_luin_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_sexual_contacts_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_sexual_contacts_modal()
    #     print(f"test_sexual_contacts_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_mls_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_mls_modal()
    #     print(f"test_mls_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_blood_donor_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_blood_donor_modal()
    #     print(f"test_blood_donor_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_organ_donor_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_organ_donor_modal()
    #     print(f"test_organ_donor_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_ippp_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_ippp_modal()
    #     print(f"test_ippp_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_manipulations_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_manipulations_modal()
    #     print(f"test_manipulations_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_emergencies_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_emergencies_modal()
    #     print(f"test_emergencies_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_departure_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_departure_modal()
    #     print(f"test_departure_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_source_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_source_modal()
    #     print(f"test_source_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_contact_person_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_contact_person_modal()
    #     print(f"test_contact_person_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    # def test_dispensary_observation_modal_when_patient_deregistered(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_dispensary_observation_modal_when_patient_deregistered()
    #     print(f"test_dispensary_observation_modal_when_patient_deregistered passed")


@allure.severity(allure.severity_level.NORMAL)
class TestForeignerCase():
    @pytest.mark.smoke
    def test_registration_of_foreigner(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_foreign_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_foreigner()

    def test_patient_id_foreigner(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_id_foreigner()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_organ_recipient_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_organ_recipient_modal()
        print(f"test_organ_recipient_modal passed")

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_blood_recipient_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_blood_recipient_modal()
        print(f"test_blood_recipient_modal passed")

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_dispensary_observation_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_hiv_antibody_testing_ogc_modal()
        register_page.check_save_button_hiv_ogc_modal()
        register_page.fill_dispensary_observation_modal()

    def test_save_button_of_dispensary_observation_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_of_dispensary_observation_modal()

    def test_edit_button_of_dispensary_observation_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_of_dispensary_observation_modal()

    def test_dispensary_registration_date(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_dispensary_registration_date()

    def cancel_button_of_dispensary_observation_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_of_dispensary_observation_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_at_risk_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_at_risk_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_drug_injection(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_drug_injection()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_drug_consumption_year(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_drug_consumption_year()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_dispensary_registration_date(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_dispensary_registration_date()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_registration_date_at_narcology(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registration_date_at_narcology()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_alcohol_consumption(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_alcohol_consumption()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_outpatient_card_num(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_outpatient_card_num()

    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_initial_registration_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_initial_registration_date()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_doctor_name(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_doctor_name()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_save_button_in_at_risk_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_in_at_risk_modal()

    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_result_modal_in_additional_analysis_tab(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_result_modal_in_additional_analysis_tab()
    #     print(f"test_result_modal passed")

    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_referral_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_referral_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_registration_num(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_registration_num()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_blood_donor_medical_org(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_blood_donor_medical_org()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_material_receipt_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_material_receipt_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_sample_receipt_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_sample_receipt_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_registering_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_registering_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd3(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd3()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd8(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd8()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_cd8(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_cd8()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_rate(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_rate()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_medical_org_provided_analysis(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_medical_org_provided_analysis()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_note(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_note()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_services(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_services()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_cd4_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_cd4_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_viral_load_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_viral_load_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_cd4_vl_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_cd4_vl_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_cd4_vl_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_cd4_vl_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_cd4_vl_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_cd4_vl_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vl_analysis_num(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vl_analysis_num()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_blood_donor_medical_org(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_donor_medical_org()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_material_receipt_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_material_receipt_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_material_sampling_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_material_sampling_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_registering_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_registering_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_result(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_result()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_result_ml(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_result_ml()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_log(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_log()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_medical_org_provided_analysis(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_medical_org_provided_analysis()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_note(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_note()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cd4_vl_services(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cd4_vl_services()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_cd4_vl_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_cd4_vl_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_vgv_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_vgv_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_vgv_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_vgv_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_vgv_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_vgv_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_vgv_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_registration_num(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_registration_num()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_blood_donor_medical_org(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_donor_medical_org()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_material_receipt_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_material_receipt_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_registering_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_registering_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_marker(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_marker()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_result(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_result()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_medical_org_provided_analysis(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_medical_org_provided_analysis()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_note(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgv_note()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_vgv_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_vgv_modal()
    #
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_vgs_modal()
    #     print(f"test_vgs_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_vgs_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_vgs_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_vgs_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_vgs_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_vgs_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_vgs_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_registration_num(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_registration_num()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_donor_medical_org(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_donor_medical_org()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_material_receipt_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_material_receipt_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgv_registering_date(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_registering_date()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_analysis_type(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_analysis_type()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_result(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_result()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_medical_org_provided_analysis(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_medical_org_provided_analysis()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_note(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_vgs_note()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_vgs_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_vgs_modal()
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_vac_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_vgv_vac_modal()
    #     print(f"test_vgv_vac_modal passed")
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_preventive_therapy_and_ost_modals(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_preventive_therapy_and_ost_modals()
    #     print(f"test_preventive_therapy_and_ost_modals passed")
    #
    # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    # def test_vgs_treatment_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.should_test_vgs_treatment_modal()
    #     print(f"test_vgs_treatment_modal passed")

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_save_button_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_add_button_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_date_of_eligibility_for_treatment_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_date_of_eligibility_for_treatment_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_treatment_type_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_treatment_type_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_mpi_profile_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_mpi_profile_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_hosp_date_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_hosp_date_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_date_of_discharge_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_date_of_discharge_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_treatment_result_d_screening_hospitalization(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_treatment_result_d_screening_hospitalization()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_d_screening_hospitalization_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_d_screening_hospitalization_modal()

    @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
    def test_visits_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_visits_modal()
        print(f"test_visits_modal passed")

@allure.severity(allure.severity_level.NORMAL)
class TestWomanCase():
    @pytest.mark.smoke
    def test_registration_of_woman(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_woman()

    def test_patient_id(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_patient_id_woman()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_hiv_diagnosis_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_dispensary_observation_modal()
        register_page.check_save_button_of_dispensary_observation_modal()
        # register_page.fill_hiv_diagnosis_modal()

    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_formulating_change_date_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_formulating_change_date_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_hiv_stage_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_hiv_stage_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_hiv_diagnosis_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_hiv_diagnosis_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_hiv_diagnosis_modal_and_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_hiv_related_disease_modal()
    #
    # # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # # def test_hiv_stage_hiv_related_disease_modal(self, browser):
    # #     register_page = RegisterPage(browser, browser.current_url)
    # #     register_page.check_hiv_stage_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_disease_start_date_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_disease_start_date_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_disease_end_date_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_disease_end_date_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_hiv_related_disease_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_hiv_related_disease_modal()
    #
    # @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    # def test_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_date_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_date_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_type_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_type_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_description_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_description_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_recommended_consultation_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_recommended_consultation_modal()
    #
    # @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    # def test_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.fill_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_save_button_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_save_button_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_add_button_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_add_button_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_edit_button_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_edit_button_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_date_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_date_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_type_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_type_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_consultation_description_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_consultation_description_recommended_screening_modal()
    #
    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_cancel_button_recommended_screening_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_cancel_button_recommended_screening_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_fluoroscopy_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_fluoroscopy_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_fluoroscopy_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_fluoroscopy_modal()

    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_registering_date_fluoroscopy_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_registering_date_fluoroscopy_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_fluoroscopy_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_fluoroscopy_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_fluoroscopy_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_radiography_modals(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_radiography_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_radiography_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_radiography_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_radiography_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_registering_date_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registering_date_radiography_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_radiography_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_radiography_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_radiography_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_sputum_smear_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_sputum_smear_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_sputum_smear_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_sputum_smear_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_registering_date_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registering_date_sputum_smear_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_sputum_smear_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_sputum_smear_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_sputum_smear_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_tb_symphtoms_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_tb_symphtoms_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_tb_symphtoms_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_tb_symphtoms_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_registering_date_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registering_date_tb_symphtoms_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_tb_symphtoms_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_tb_symphtoms_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_tb_symphtoms_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_xpert_mtb_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_xpert_mtb_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_xpert_mtb_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_xpert_mtb_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_registering_date_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registering_date_xpert_mtb_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_xpert_mtb_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_xpert_mtb_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_xpert_mtb_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_kt_mrt_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_kt_mrt_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_kt_mrt_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_kt_mrt_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_registering_date_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_registering_date_kt_mrt_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_result_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_result_kt_mrt_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_kt_mrt_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_kt_mrt_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.fill_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_save_button_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_add_button_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_edit_button_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_edit_button_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_lab_name_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_lab_name_tb_treatment_modal()

    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_diagnosis_registering_date_tb_treatment_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_diagnosis_registering_date_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_sick_type_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_sick_type_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_diagnosis_mkb10_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_diagnosis_mkb10_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_location_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_location_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_bac_secretion_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_bac_secretion_tb_treatment_modal()

    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_treatment_start_date_tb_treatment_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_treatment_start_date_tb_treatment_modal()

    # @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    # def test_treatment_end_date_tb_treatment_modal(self, browser):
    #     register_page = RegisterPage(browser, browser.current_url)
    #     register_page.check_treatment_end_date_tb_treatment_modal()

    @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
    def test_outcome_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_outcome_tb_treatment_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_tb_treatment_modal(self, browser):
        register_page = RegisterPage(browser, browser.current_url)
        register_page.check_cancel_button_tb_treatment_modal()

#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_art_information_modal(self, browser):
#         register_page = RegisterPage(browser, browser.current_url)
#         register_page.should_test_art_information_modal()
#         print(f"test_art_information_modal passed")
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_art_adherence_level_modal(self, browser):
#         register_page = RegisterPage(browser, browser.current_url)
#         register_page.should_test_art_adherence_level_modal()
#         print(f"test_art_adherence_level_modal passed")
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_recipe_modal(self, browser):
#         register_page = RegisterPage(browser, browser.current_url)
#         register_page.should_test_recipe_modal()
#         print(f"test_recipe_modal passed")
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_pregnancy_modal(self, browser):
#         register_page = RegisterPage(browser, browser.current_url)
#         register_page.should_test_pregnancy_modal()
#         print(f"test_pregnancy_modal passed")
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", test_pregnancy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_children_modal(self, browser):
#         register_page = RegisterPage(browser, browser.current_url)
#         register_page.should_test_children_modal()
#         print(f"test_children_modal passed")
