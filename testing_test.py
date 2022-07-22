from time import sleep

from pages import values
import pytest
import allure
from sentry_sdk import capture_exception
from sentry_sdk import capture_message
from pages.main_page import ArvLogs
from pages.patient_card import PatientCard
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


# class TestMainPage():
#
#     def test_receipt_log(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.choose_KNCDIZ_as_user_org()
#         main_page = ArvLogs(browser, browser.current_url)
#         main_page.fill_receipt_log()


#
# class TestGeneralData():
#     def test_registration_of_child(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.choose_Zhetysai_as_user_org()
#         work_page.should_add_kz_patient()
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.register_new_child()
#         capture_message('Passed')
#
#     def test_patient_id_child(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_id_child()
#         capture_message('Passed')
#
#     def test_search_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_mothers_data()
#         capture_message('Passed')
#
#     def test_patient_iin(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_iin()
#         capture_message('Passed')
#
#     def test_patient_surname(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_surname()
#         capture_message('Passed')
#
#     def test_patient_birth_date(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_birth_date()
#         capture_message('Passed')
#
#     def test_patient_gender(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_gender()
#         capture_message('Passed')
#
#     def test_emergence_area(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_emergence_area()
#         capture_message('Passed')
#
#     def test_patient_midname(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_midname()
#         capture_message('Passed')
#
#     def test_patient_name(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_name()
#         capture_message('Passed')
#
#     def test_patient_citizenship(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_citizenship()
#         capture_message('Passed')
#
#     def test_child_status(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_child_status()
#         capture_message('Passed')
#
#     def test_social_status(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_social_status()
#         capture_message('Passed')
#
#     def test_edit_button_registration_address_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_registration_address_modal()
#         capture_message('Passed')
#
#     def test_registration_area(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_area()
#         capture_message('Passed')
#
#     def test_registration_unit_area(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_unit_area()
#         capture_message('Passed')
#
#     def test_registration_locality(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_locality()
#
#     def test_registration_place(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_place()
#
#     def test_registration_street(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_street()
#
#     def test_registration_house(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_house()
#
#     def test_registration_apartment(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_apartment()
#
#     def test_registration_phone_number(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_phone_number()
#
#     def test_cancel_button_registration_address_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_registration_address_modal()
#
#     def test_edit_button_residence_address_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_residence_address_modal()
#
#     def test_residence_area(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_area()
#
#     def test_residence_unit_area(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_unit_area()
#
#     def test_residence_locality(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_locality()
#
#     def test_residence_place(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_place()
#
#     def test_residence_street(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_street()
#
#     def test_residence_house(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_house()
#
#     def test_residence_apartment(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_apartment()
#
#     def test_residence_phone_number(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_residence_locality()
#
#     def test_cancel_button_residence_address_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_residence_address_modal()
#
#     # @pytest.mark.xfail(reason="не понятно")
#     # def test_residence_medical_organization(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_residence_medical_organization()
#
#     def test_retrospective_child_checkbox(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_retrospective_child_checkbox()
#
#     def test_surname_of_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_surname_of_mother()
#
#     def test_name_of_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_name_of_mother()
#
#     def test_midname_of_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_midname_of_mother()
#
#     def test_ib_number_of_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ib_number_of_mother()
#
#     def test_ib_number_date_of_mother(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ib_number_date_of_mother()
#
#     @pytest.mark.skipif(test_patient_id_child == "FAILED", reason="patient id wasn't taken")
#     def test_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_hiv_antibody_testing_ogc_modal()
#         patient_card.check_save_button_hiv_ogc_modal()
#         patient_card.fill_dispensary_observation_modal()
#         patient_card.check_save_button_dispensary_observation_modal()
#         patient_card.fill_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_patient_id_child == "FAILED", reason="patient id wasn't taken")
#     def test_save_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registration_date_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_date_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_deregistration_date_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_deregistration_date_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_deregistration_reason_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_deregistration_reason_perinatal_registration_modal()
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_patient_death_case_perinatal_registration_modal(self, browser):
#         if values.reason_perinatal_deregis_choice == 2:
#             patient_card = PatientCard(browser, browser.current_url)
#             patient_card.check_country_perinatal_registration_modal()
#         if values.reason_perinatal_deregis_choice == 3:
#             patient_card = PatientCard(browser, browser.current_url)
#             patient_card.check_area_perinatal_registration_modal()
#             patient_card.check_unit_area_perinatal_registration_modal()
#         if values.reason_perinatal_deregis_choice == 4:
#             patient_card = PatientCard(browser, browser.current_url)
#             patient_card.check_date_of_death_perinatal_registration_modal()
#             patient_card.check_death_reason_perinatal_registration_modal()
#             patient_card.check_death_place_perinatal_registration_modal()
#         else: pass
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_perinatal_registration_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_perinatal_registration_modal()
#
#
#     @pytest.mark.skipif(test_save_perinatal_registration_modal == "FAILED", reason="patient id wasn't taken")
#     def test_arv_prophylaxis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_perinatal_registration_tab()
#
# @allure.severity(allure.severity_level.NORMAL)
# class TestChildCase():
#     @pytest.mark.smoke
#     def test_fill_HIV_antibody_testing_ogc_modal(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.choose_Zhetysai_as_user_org()
#         work_page.should_add_kz_patient()
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.register_new_child()
#         patient_card.fill_hiv_antibody_testing_ogc_modal()
#         capture_message('Passed')
#
#     @pytest.mark.skipif(test_fill_HIV_antibody_testing_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_hiv_ogc_modal()
#         capture_message('Passed')
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_hiv_ogc_modal()
#         capture_message('Passed')
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_surname_of_person_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_surname_of_person_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_referral_number_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_referral_number_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_sampling_date_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_sampling_date_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_receipt_date_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_receipt_date_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_production_date_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_production_date_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_serum_number_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_serum_number_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_serum_number2_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_serum_number2_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_testing_system_type_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_test_system_type_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_expiration_date_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_expiration_date_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_series_number_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_series_number_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_testing_category_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_test_category_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_op_critical_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_op_critical_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_op_serum_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_op_serum_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_responsible_person_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_responsible_person_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_services_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_services_hiv_ogc_modal()
#
#     @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_hiv_ogc_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_hiv_ogc_modal()
#
#     # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     # @pytest.mark.smoke
#     # def test_fill_HIV_antibody_testing_KNCDIZ_modal(self, browser):
#     #     kncdiz_user_opens_card_of_child(browser)
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_HIV_antibody_testing_KNCDIZ_modal()
#     #
#     # @pytest.mark.skipif(test_fill_HIV_antibody_testing_KNCDIZ_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_screening_number_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_screening_number_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_serum_number_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_serum_number_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_referral_number_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_referral_number_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_production_date_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_production_date_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_testing_system_type_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_test_system_type_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_expiration_date_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_expiration_date_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_series_number_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_series_number_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_op_critical_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_op_critical_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_op_serum_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_op_serum_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_kncdiz_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_hiv_kncdiz_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_hiv_kncdiz_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     # @pytest.mark.smoke
#     # def test_fill_IB_modal(self, browser):
#     #     zhetysai_user_opens_card_of_child(browser)
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.get_refferal_for_ib()
#     #     patient_card.get_refferal_for_pcr()
#     #     kncdiz_user_opens_card_of_child(browser)
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_IB_modal()
#     #
#     # @pytest.mark.skipif(test_fill_IB_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_ib_number_in_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_ib_number_in_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_serum_number_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_serum_number_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_sample_number_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_sample_number_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_receipt_date_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_receipt_date_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # @pytest.mark.smoke
#     # def test_register_date_ib_modal(self, browser):
#     #     kncdiz_user_opens_card_of_child(browser)
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_register_date_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_register_date_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_register_date_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_test_system_name_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_test_system_name_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_expiration_date_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_expiration_date_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_series_number_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_series_number_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_responsible_person_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_responsible_person_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_gp160_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_gp160_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_gp110_120_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_gp110_120_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p68_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p68_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p55_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p55_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p52_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p52_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_gp41_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_gp41_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p40_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p40_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p34_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p34_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p25_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p25_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_p18_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_p18_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_services_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_services_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_ib_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_ib_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_ib_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     # @pytest.mark.smoke
#     # def test_fill_PCR_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_PCR_modal()
#     #
#     # @pytest.mark.skipif(test_fill_PCR_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_pcr_number_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_pcr_number_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_serum_number_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_serum_number_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_sample_number_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_sample_number_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_pcr_type_in_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_pcr_type_in_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_receipt_date_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_receipt_date_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # @pytest.mark.smoke
#     # def test_register_date_pcr_modal(self, browser):
#     #     kncdiz_user_opens_card_of_child(browser)
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_register_date_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_test_system_name_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_test_system_name_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_expiration_date_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_expiration_date_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_series_number_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_series_number_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_responsible_person_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_responsible_person_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_services_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_services_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_pcr_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_pcr_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_pcr_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_hiv_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_result_modal()
#     #
#     # @pytest.mark.skipif(test_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_number_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_number_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_result_date_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_date_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_responsible_person_in_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_responsible_person_in_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_labaratory_superviser_in_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_labaratory_superviser_in_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_analysis_result_in_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_analysis_result_in_result_modal()
#     #
#     # @pytest.mark.skipif(test_save_button_result_modal == "FAILED", reason="patient id wasn't taken")
#     # def test_cansel_button_result_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cansel_button_result_modal()
#
#     @pytest.mark.skipif(test_fill_HIV_antibody_testing_ogc_modal == "FAILED", reason="patient id wasn't taken")
#     def test_patient_left_region_case_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_dispensary_observation_modal_when_patient_left_region()
#         capture_message('Passed')
#
#     @pytest.mark.skipif(test_patient_left_region_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_area_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_area_dispensary_observation_modal()
#         capture_message('Passed')
#
#     @pytest.mark.xfail(reason="it's bag, unit_area object doesn't save value")
#     @pytest.mark.skipif(test_patient_left_region_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_unit_area_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_unit_area_dispensary_observation_modal()
#         patient_card.check_cancel_button_dispensary_observation_modal()
#         capture_message('Passed')
#
# @allure.severity(allure.severity_level.NORMAL)
# class TestHomelessCase():
#     @pytest.mark.smoke
#     def test_registration_of_homeless(self, browser):
#         try:
#             login(browser)
#             work_page = WorkPage(browser, browser.current_url)
#             work_page.choose_Zhetysai_as_user_org()
#             work_page.should_add_kz_patient()
#             patient_card = PatientCard(browser, browser.current_url)
#             patient_card.register_new_homeless()
#         except Exception as e:
#             capture_exception(e)
#
#     def test_patient_id_homeless(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_id_homeless()
#
#     @pytest.mark.smoke
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_family_members_modal()
#
#     @pytest.mark.skipif(test_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_surname_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_surname_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_name_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_name_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_middle_name_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_middle_name_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_gender_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_gender_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_birthday_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_birthday_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def check_hiv_status_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_family_connection_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_family_connection_family_members_modal()
#
#     @pytest.mark.skipif(test_save_button_family_members_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_family_members_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_family_members_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_luin_tab()
#
#     @pytest.mark.skipif(test_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_experience_injection_drug_use_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_experience_injection_drug_use_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_drug_usage_in_twelve_month_with_police_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_drug_usage_in_twelve_month_with_police_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_drug_use_years_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_drug_use_years_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_drug_use_month_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_drug_use_month_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sharing_drug_injection_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sharing_drug_injection_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sharing_drug_injection_with_hiv_positiv_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sharing_drug_injection_with_hiv_positiv_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sharing_drug_injection_with_sexual_partner_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sharing_drug_injection_with_sexual_partner_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sharing_drug_injection_with_permanent_group_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sharing_drug_injection_with_permanent_group_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sharing_drug_injection_with_random_group_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sharing_drug_injection_with_random_group_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_heroin_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heroin_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_hanka_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hanka_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_mak_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_mak_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_amphetamin_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_amphetamin_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_sintethics_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sintethics_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_other_drugs_checkbox_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_other_drugs_checkbox_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_registered_in_narcological_dispensary_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registered_in_narcological_dispensary_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_registered_with_police_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registered_with_police_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_sex_experience_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_sex_experience_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_sex_experience_year_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_sex_experience_year_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_sex_experience_month_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_sex_experience_month_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_number_of_sex_partners_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_number_of_sex_partners_luin_tab()
#
#     @pytest.mark.skipif(test_save_button_luin_tab == "FAILED", reason="patient id wasn't taken")
#     def test_condom_usage_luin_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_condom_use_luin_tab()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_sexual_contacts_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_experience_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_experience_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_contacts_existence_last_12month_dispensary_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_contacts_existence_last_12month_dispensary_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_partners_number_during_life_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_partners_number_during_life_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_partners_number_last_12month_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_partners_number_last_12month_sexual_contacts_tab()
#
#     @pytest.mark.xfail(reason="it's bag of test, tired ti look for")
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_homosexual_contacts_last_12month_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_homosexual_contacts_last_12month_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_contact_with_hiv_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_contact_with_hiv_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_homosexual_contact_with_luin_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_homosexual_contact_with_luin_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_permanent_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_permanent_homosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_random_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_random_homosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_homosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_permanent_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_permanent_homosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_random_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_random_homosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_homosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_heterosexual_experience_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heterosexual_experience_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_heterosexual_contacts_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_heterosexual_contacts_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_heterosexual_contact_with_hiv_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heterosexual_contact_with_hiv_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_heterosexual_contact_with_luin_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heterosexual_contact_with_luin_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_heterosexual_experience_last_12month_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heterosexual_experience_last_12month_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_heterosexual_partners_number_last_12month_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_heterosexual_partners_number_last_12month_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_permanent_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_permanent_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_random_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_random_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_permanent_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_permanent_heterosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_random_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_random_heterosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.skipif(test_sexual_contacts_modal == "FAILED", reason="patient id wasn't taken")
#     def test_commercial_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_commercial_heterosexual_partners_during_life_checkbox_sexual_contacts_tab()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_mls_modal()
#
#     @pytest.mark.skipif(test_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_mls_modal()
#
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_mls_experience_checkbox_mls_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_mls_experience_checkbox_mls_tab()
#
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_mls_modal()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_mls_modal()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_mls_name_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_mls_name_mls_modal()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_start_date_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_start_date_mls_modal()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_end_date_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_end_date_mls_modal()
#
#     @pytest.mark.xfail(reason="can't catch a bag")
#     @pytest.mark.skipif(test_save_button_mls_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_mls_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_mls_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_blood_donor_modal()
#
#     @pytest.mark.skipif(test_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_donor_last_5years_checkbox_donor_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_donor_last_5years_checkbox_donor_tab()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_existence_checkbox_donor_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_existence_checkbox_donor_tab()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_place_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_place_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_existence_checkbox_donor_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_existence_checkbox_donor_tab()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_area_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_area_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_unit_area_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_unit_area_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_locality_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_locality_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_date_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_date_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_donor_category_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_donor_category_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_type_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_type_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_code_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_code_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_code_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_code_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_analysis_date_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_analysis_date_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_blood_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_blood_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_blood_donor_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_organ_donor_modal()
#
#     @pytest.mark.skipif(test_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_material_donor_last_5years_checkbox_donor_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_material_donor_last_5years_checkbox_donor_tab()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_place_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_place_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_area_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_area_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_unit_area_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_unit_area_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_locality_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_locality_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donation_date_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donation_date_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_donor_category_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_donor_category_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_type_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_type_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_material_type_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_material_type_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_material_number_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_material_number_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_analysis_date_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_analysis_date_organ_donor_modal()
#
#     @pytest.mark.xfail(reason="it's bag, object doesn't save a value")
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_recipient_medical_organization_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_recipient_medical_organization_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_organ_donor_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_donor_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_organ_donor_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_organ_donor_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_ippp_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_ippp_modal()
#
#     @pytest.mark.skipif(test_ippp_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_ippp_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_ippp_symptoms_modal()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_ippp_symptoms_existence_checkbox_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ippp_symptoms_existence_checkbox_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_dispencary_registered_in_kvd_area_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_dispencary_registered_in_kvd_area_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_dk_contacting_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_dk_contacting_ippp_tab()
#
#     @pytest.mark.xfail(reason="object doesn't save a value")
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_dk_contacting_number_last_12month_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_dk_contacting_number_last_12month_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_private_clinics_contacting_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_private_clinics_contacting_ippp_tab()
#
#     @pytest.mark.xfail(reason="object doesn't save a value")
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_private_clinics_contacting_number_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_private_clinics_contacting_number_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_born_by_caesarean_section_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_born_by_caesarean_section_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_chemoprophylaxis_of_mother_during_pregnancy_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_chemoprophylaxis_of_mother_during_pregnancy_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_child_had_artificial_feeding_ippp_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_child_had_artificial_feeding_ippp_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_chemoprophylaxis_of_child_during_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_chemoprophylaxis_of_child_during_tab()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_ippp_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_ippp_symptoms_modal()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_ippp_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_ippp_symptoms_modal()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_diagnosis_date_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_diagnosis_date_symptoms_modal()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_diagnosis_ippp_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_diagnosis_ippp_symptoms_modal()
#
#     @pytest.mark.skipif(test_save_button_ippp_symptoms_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_ippp_symptoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_ippp_symptoms_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_manipulations_modal()
#
#     @pytest.mark.skipif(test_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_manipulations_existence_checkbox_manipulations_emergencies_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_manipulations_existence_checkbox_manipulations_emergencies_tab()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_manipulations_modal()
#
#     @pytest.mark.xfail(reason="after saving form the date object doesn't save it's value")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_date_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_date_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_sort_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sort_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_type_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_type_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_manipulations_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_manipulations_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_manipulations_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_emergencies_modal()
#
#     @pytest.mark.skipif(test_emergencies_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_emergencies_modal()
#
#     @pytest.mark.skipif(test_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_emergencies_existence_checkbox_manipulations_emergencies_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_emergencies_existence_checkbox_manipulations_emergencies_tab()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_date_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_date_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_sort_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sort_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_trauma_type_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_trauma_type_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_72hours_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_72hours_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_emergencies_modal()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_emergencies_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_emergencies_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_emergencies_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_departure_modal()
#
#     @pytest.mark.skipif(test_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_departure_existence_checkbox_departure_source_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_departure_existence_checkbox_departure_source_tab()
#
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_departure_start_date_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_departure_start_date_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_departure_end_date_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_departure_end_date_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_departure_country_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_departure_country_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_departure_purpose_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_departure_purpose_departure_modal()
#
#     # @pytest.mark.xfail(reason="clicking edit button form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_departure_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_departure_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_emergencies_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_infection_source_existence_checkbox_departure_source_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_infection_source_existence_checkbox_departure_source_tab()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_source_modal()
#
#     @pytest.mark.xfail(reason="gets true value with spaces")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_ib_number_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ib_number_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_ib_date_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ib_date_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_surname_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_surname_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_name_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_name_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_save_button_manipulations_modal == "FAILED", reason="patient id wasn't taken")
#     def test_midname_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_midname_source_modal()
#
#     # @pytest.mark.xfail(reason="after saving form it shows 500 error")
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_source_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_source_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_contact_person_modal()
#
#     @pytest.mark.skipif(test_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contact_person_existence_contact_person_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contact_person_existence_contact_person_tab()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_surname_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_surname_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_name_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_name_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_midname_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_midname_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_bithday_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_bithday_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contacting_start_date_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contacting_start_date_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contact_type_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contact_type_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contact_ib_number_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contact_ib_number_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contact_ib_number_date_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contact_ib_number_date_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.xfail(reason="diagnostics_date doesn't save its value")
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_diagnostics_date_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_diagnostics_date_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_contact_survey_modal_in_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_contact_survey_modal_in_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_reason_not_surveying_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_reason_not_surveying_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contacting_finished_checkbox_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contacting_finished_checkbox_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_contacting_end_date_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_contacting_end_date_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_area_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_area_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_unit_area_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_unit_area_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_locality_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_locality_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_street_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_street_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_house_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_house_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_apartment_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_apartment_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_phone_number_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_phone_number_contact_person_modal()
#
#     @pytest.mark.skipif(test_save_button_contact_person_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_contact_person_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_contact_person_modal()
#
#     @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
#     def test_patient_death_case_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_dispensary_observation_modal_when_patient_died()
#
#     @pytest.mark.skipif(test_patient_death_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_aidc_related_death_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_aidc_related_death_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_patient_death_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_death_reason_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_death_reason_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_patient_death_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_death_place_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_death_place_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_patient_death_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_autopsy_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_autopsy_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_patient_death_case_dispensary_observation_modal == "FAILED", reason="patient id wasn't taken")
#     def test_pathologoanatomic_diagnosis_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_pathologoanatomic_diagnosis_dispensary_observation_modal()
#
# @allure.severity(allure.severity_level.NORMAL)
# class TestForeignerCase():
#     @pytest.mark.smoke
#     def test_registration_of_foreigner(self, browser):
#         login(browser)
#         work_page = WorkPage(browser, browser.current_url)
#         work_page.choose_Zhetysai_as_user_org()
#         work_page.should_add_foreign_patient()
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.register_new_foreigner()
#
#     def test_patient_id_foreigner(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_id_foreigner()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         # patient_card.fill_hiv_antibody_testing_ogc_modal()
#         # patient_card.check_save_button_hiv_ogc_modal()
#         patient_card.fill_dispensary_observation_modal()
#
#     def test_save_button_of_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_dispensary_observation_modal()
#
#     def test_edit_button_of_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_dispensary_observation_modal()
#
#     def test_dispensary_registration_date(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_dispensary_registration_date()
#
#     def cancel_button_of_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_at_risk_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_at_risk_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_in_at_risk_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_in_at_risk_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_drug_injection(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_drug_injection()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_drug_consumption_year(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_drug_consumption_year()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_dispensary_registration_date(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_dispensary_registration_date()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_registration_date_at_narcology(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registration_date_at_narcology()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_alcohol_consumption(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_alcohol_consumption()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_outpatient_card_num(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_outpatient_card_num()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_initial_registration_date(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_initial_registration_date()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_doctor_name(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_doctor_name()
#
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_result_modal_in_additional_analysis_tab(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_result_modal_in_additional_analysis_tab()
#     #     print(f"test_result_modal passed")
#
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_referral_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_referral_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_registration_num(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_registration_num()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_blood_donor_medical_org(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_blood_donor_medical_org()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_material_receipt_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_material_receipt_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_sample_receipt_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_sample_receipt_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_registering_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_registering_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd3(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd3()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd8(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd8()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_cd8(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_cd8()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_rate(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_rate()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_medical_org_provided_analysis(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_medical_org_provided_analysis()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_note(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_note()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_services(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_services()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_cd4_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_cd4_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_viral_load_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_viral_load_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_cd4_vl_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_cd4_vl_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_cd4_vl_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_cd4_vl_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_cd4_vl_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_cd4_vl_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vl_analysis_num(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vl_analysis_num()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_blood_donor_medical_org(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_donor_medical_org()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_material_receipt_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_material_receipt_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_material_sampling_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_material_sampling_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_registering_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_registering_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_result(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_result()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_result_ml(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_result_ml()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_log(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_log()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_medical_org_provided_analysis(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_medical_org_provided_analysis()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_note(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_note()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cd4_vl_services(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cd4_vl_services()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_cd4_vl_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_cd4_vl_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_vgv_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_vgv_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_vgv_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_vgv_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_vgv_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_vgv_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_vgv_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_registration_num(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_registration_num()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_blood_donor_medical_org(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_donor_medical_org()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_material_receipt_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_material_receipt_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_registering_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_registering_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_marker(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_marker()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_result(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_result()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_medical_org_provided_analysis(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_medical_org_provided_analysis()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_note(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgv_note()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_vgv_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_vgv_modal()
#     #
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_vgs_modal()
#     #     print(f"test_vgs_modal passed")
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_save_button_vgs_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_save_button_vgs_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_add_button_vgs_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_add_button_vgs_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_edit_button_vgs_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_edit_button_vgs_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_registration_num(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_registration_num()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_donor_medical_org(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_donor_medical_org()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_material_receipt_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_material_receipt_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgv_registering_date(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_registering_date()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_analysis_type(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_analysis_type()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_result(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_result()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_medical_org_provided_analysis(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_medical_org_provided_analysis()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_note(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_vgs_note()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_cancel_button_vgs_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.check_cancel_button_vgs_modal()
#     #
#     # @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     # def test_vgs_vac_modal(self, browser):
#     #     patient_card = PatientCard(browser, browser.current_url)
#     #     patient_card.fill_vgv_vac_modal()
#     #     print(f"test_vgv_vac_modal passed")
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medication_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medication_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_reason_set_date_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_reason_set_date_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_therapy_start_date_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_therapy_start_date_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_therapy_end_date_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_therapy_end_date_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_save_button_preventive_therapy_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_preventive_therapy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_preventive_therapy_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_ost_modal()
#
#     @pytest.mark.skipif(test_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_ost_modal()
#
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_ost_modal()
#
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_ost_modal()
#
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_ost_start_date_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ost_start_date_ost_modal()
#
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_ost_end_date_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_ost_end_date_ost_modal()
#
#     @pytest.mark.xfail(reason="medication_type object doesn't save it's value")
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medication_type_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medication_type_ost_modal()
#
#     @pytest.mark.skipif(test_save_button_ost_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_ost_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_ost_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_start_date_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_start_date_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_end_date_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_end_date_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_result_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_result_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_save_button_vgs_treatment_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_vgs_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_vgs_treatment_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_date_of_eligibility_for_treatment_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_date_of_eligibility_for_treatment_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_type_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_type_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_mpi_profile_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_mpi_profile_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_hosp_date_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hosp_date_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_date_of_discharge_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_date_of_discharge_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_result_d_screening_hospitalization(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_result_d_screening_hospitalization()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_d_screening_hospitalization_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_d_screening_hospitalization_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_visits_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_visits_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_recipient_last_5years_checkbox_recipient_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_recipient_last_5years_checkbox_recipient_tab()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_place_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_place_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_area_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_area_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_unit_area_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_unit_area_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_locality_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_locality_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_date_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_date_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_medical_organization_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_medical_organization_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_epid_history_number_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_epid_history_number_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_code_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_code_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_blood_component_code_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_blood_component_code_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_blood_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_blood_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_blood_recipient_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_organ_recipient_last_5years_checkbox_recipient_tab(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_organ_recipient_last_5years_checkbox_recipient_tab()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_place_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_place_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_area_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_area_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_unit_area_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_unit_area_organ_recipient_modal()
#
#     # @pytest.mark.xfail(reason="it's bag, locality object doesn't save value")
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_locality_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_locality_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_transfusion_date_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_transfusion_date_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_donor_medical_organization_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_donor_medical_organization_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_recipient_medical_organization_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_recipient_medical_organization_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_organ_material_type_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_organ_material_type_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_organ_material_number_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_organ_material_number_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_organ_material_type_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_organ_material_type_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_organ_donor_name_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_organ_donor_name_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_status_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_status_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_save_button_organ_recipient_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_organ_recipient_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_organ_recipient_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_patient_left_rk_case_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_dispensary_observation_modal_when_patient_left_rk()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_deregistration_date_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_deregistration_date_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_deregistration_reason_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_deregistration_reason_dispensary_observation_modal()
#
#     @pytest.mark.skipif(test_registration_of_foreigner == "FAILED", reason="patient id wasn't taken")
#     def test_country_dispensary_observation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_country_dispensary_observation_modal()
#         patient_card.check_cancel_button_dispensary_observation_modal()
#
@allure.severity(allure.severity_level.NORMAL)
class TestWomanCase():
    @pytest.mark.smoke
    def test_registration_of_woman(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.register_new_woman()

#     def test_patient_id_woman(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_patient_id_woman()
#
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_hiv_diagnosis_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.fill_dispensary_observation_modal()
        patient_card.check_save_button_dispensary_observation_modal()
        sleep(2)
        patient_card.fill_at_risk_modal()
        patient_card.check_save_button_in_at_risk_modal()
        sleep(2)
        patient_card.fill_hiv_diagnosis_modal()
        patient_card.check_save_button_hiv_diagnosis_modal()

#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_formulating_change_date_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_formulating_change_date_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_stage_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_stage_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_hiv_diagnosis_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_hiv_diagnosis_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_diagnosis_modal_and_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_hiv_stage_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_hiv_stage_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_disease_start_date_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_disease_start_date_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_disease_end_date_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_disease_end_date_hiv_related_disease_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_hiv_related_disease_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_hiv_related_disease_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_recommended_consultation_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_recommended_consultation_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="can't extract the value")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_service_within_tarificator_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_service_within_tarificator_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_date_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_date_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_type_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_type_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_description_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_description_recommended_consultation_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_recommended_consultation_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_recommended_consultation_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_recommended_screening_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_recommended_screening_modal(self, browser):
#         sleep(2)
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_recommended_screening_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_recommended_screening_modal(self, browser):
#         sleep(3)
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_recommended_screening_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_recommended_screening_modal(self, browser):
#         sleep(1)
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_recommended_screening_modal()
#
#     @pytest.mark.xfail(reason="can't extract the value")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_service_within_tarificator_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_service_within_tarificator_recommended_screening_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_date_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_date_recommended_screening_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_type_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_type_recommended_screening_modal()
#
#     @pytest.mark.xfail(reason="it's a bag")
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_consultation_description_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_consultation_description_recommended_screening_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_recommended_screening_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_recommended_screening_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_fluoroscopy_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_fluoroscopy_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_radiography_modals(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_radiography_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_radiography_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_radiography_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_radiography_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_radiography_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_radiography_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_radiography_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_radiography_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_sputum_smear_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_sputum_smear_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_tb_symphtoms_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_tb_symphtoms_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_xpert_mtb_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_xpert_mtb_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_registering_date_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_registering_date_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_result_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_result_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_kt_mrt_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_kt_mrt_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.fill_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_save_button_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_save_button_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_add_button_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_add_button_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_edit_button_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_edit_button_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_lab_name_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_lab_name_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_diagnosis_registering_date_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_diagnosis_registering_date_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_sick_type_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_sick_type_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_diagnosis_mkb10_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_diagnosis_mkb10_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_location_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_location_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_bac_secretion_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_bac_secretion_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_start_date_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_start_date_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_treatment_end_date_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_treatment_end_date_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_hiv_diagnosis_modal == "FAILED", reason="patient id wasn't taken")
#     def test_outcome_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_outcome_tb_treatment_modal()
#
#     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
#     def test_cancel_button_tb_treatment_modal(self, browser):
#         patient_card = PatientCard(browser, browser.current_url)
#         patient_card.check_cancel_button_tb_treatment_modal()
#
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_art_information_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.fill_art_information_modal()

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_art_adherence_level_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.fill_art_adherence_level_modal()
        print(f"test_art_adherence_level_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.fill_recipe_modal()

    @pytest.mark.skipif(test_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_save_button_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_save_button_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_add_button_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_add_button_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_recipe_number_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_recipe_number_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_recipe_date_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_recipe_date_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_art_medication_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_art_medication_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_dose_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_dose_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_dose_code_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_dose_code_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_concentration_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_concentration_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_packing_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_packing_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_quatity_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_quatity_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_unpacking_signs_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_unpacking_signs_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_signiture_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_signiture_recipe_modal()

    @pytest.mark.skipif(test_save_button_recipe_modal == "FAILED", reason="patient id wasn't taken")
    def test_cancel_button_recipe_modal(self, browser):
        patient_card = PatientCard(browser, browser.current_url)
        patient_card.check_cancel_button_recipe_modal()

# #
# #     @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
# #     def test_pregnancy_modal(self, browser):
# #         patient_card = PatientCard(browser, browser.current_url)
# #         patient_card.should_test_pregnancy_modal()
# #         print(f"test_pregnancy_modal passed")
# #
# #     @pytest.mark.skipif(test_registration_of_woman == "FAILED", test_pregnancy_modal == "FAILED", reason="patient id wasn't taken")
# #     def test_children_modal(self, browser):
# #         patient_card = PatientCard(browser, browser.current_url)
# #         patient_card.should_test_children_modal()
# #         print(f"test_children_modal passed")
# #
