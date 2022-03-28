import pytest
import pages.config
from pages.register_page import RegisterPage
# from .pages.settings_page import SettingsPage
from pages.work_page import WorkPage
from pages.login_page import LoginPage
# from .pages.visits_page import VisitsPage


def login(browser):
    login_url = "https://plhiv-demo.dec.kz/"
    login_page = LoginPage(browser, login_url)
    login_page.open()
    login_page.should_fill_login_form()

def zhetysai_user_opens_card_of_woman(browser):
    work_page = WorkPage(browser, browser.current_url)
    work_page.choose_Zhetysai_as_user_org()
    work_page.open_card_of_woman()
    
def kncdiz_user_opens_card_of_woman(browser):
    work_page = WorkPage(browser, browser.current_url)
    work_page.choose_KNCDIZ_as_user_org()
    work_page.open_card_of_woman()
    
    
class TestPlhiv():
    @pytest.mark.smoke
    def test_registration_of_child(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_child()
        print(f"test_registration_of_child passed")

    @pytest.mark.smoke
    def test_registration_of_homeless(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_homeless()

    @pytest.mark.smoke
    def test_registration_of_woman(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_kz_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_woman()
        print(f"test_registration_of_woman passed")

    @pytest.mark.smoke
    def test_registration_of_foreigner(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.should_add_foreign_patient()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.register_new_foreigner()

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_child == "FAILED", reason="patient id wasn't taken")
    def test_editing_general_information_in_patient_card(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.open_card_of_child()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.edit_card()
        print(f"test_editing_general_information_in_patient_card passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_HIV_antibody_testing_OGC_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_HIV_antibody_testing_OGC_modal()
        print(f"test_HIV_antibody_testing_OGC_modal passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_HIV_antibody_testing_KNCDIZ_modal(self, browser):
        login(browser)
        kncdiz_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_HIV_antibody_testing_KNCDIZ_modal()
        print(f"test_HIV_antibody_testing_KNCDIZ_modal passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_IB_modal(self, browser):
        login(browser)
        kncdiz_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_IB_modal()
        print(f"test_IB_modal passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_PCR_modal(self, browser):
        login(browser)
        kncdiz_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_PCR_modal()
        print(f"test_PCR_modal passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_result_modal(self, browser):
        login(browser)
        kncdiz_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_result_modal()
        print(f"test_result_modal passed")

    @pytest.mark.smoke
    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_family_members_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_family_members_modal()
        print(f"test_family_members_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_luin_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_luin_modal()
        print(f"test_luin_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_sexual_contacts_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_sexual_contacts_modal()
        print(f"test_sexual_contacts_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_mls_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_mls_modal()
        print(f"test_mls_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_blood_donor_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_blood_donor_modal()
        print(f"test_blood_donor_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_organ_donor_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_organ_donor_modal()
        print(f"test_organ_donor_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_blood_recipient_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_blood_recipient_modal()
        print(f"test_blood_recipient_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_organ_recipient_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_organ_recipient_modal()
        print(f"test_organ_recipient_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_ippp_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_ippp_modal()
        print(f"test_ippp_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_manipulations_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_manipulations_modal()
        print(f"test_manipulations_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_emergencies_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_emergencies_modal()
        print(f"test_emergencies_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_departure_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_departure_modal()
        print(f"test_departure_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_source_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_source_modal()
        print(f"test_source_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_contact_person_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_contact_person_modal()
        print(f"test_contact_person_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_dispensary_observation_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_dispensary_observation_modal()
        print(f"test_dispensary_observation_modal passed")

    @pytest.mark.skipif(test_registration_of_homeless == "FAILED", reason="patient id wasn't taken")
    def test_dispensary_observation_modal_when_patient_deregistered(self, browser):
        login(browser)
        work_page = WorkPage(browser, browser.current_url)
        work_page.choose_Zhetysai_as_user_org()
        work_page.open_card_of_homeless()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_dispensary_observation_modal_when_patient_deregistered()
        print(f"test_dispensary_observation_modal_when_patient_deregistered passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_perinatal_registration_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_perinatal_registration_modal()
        print(f"test_perinatal_registration_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_arv_prophylaxis_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_arv_prophylaxis_modal()
        print(f"test_arv_prophylaxis_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_hiv_diagnosis_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_hiv_diagnosis_modal()
        print(f"test_hiv_diagnosis_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_hiv_related_disease_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_hiv_related_disease_modal()
        print(f"test_hiv_related_disease_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_recommended_consultation_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_recommended_consultation_modal()
        print(f"test_recommended_consultation_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_recommended_screening_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_recommended_screening_modal()
        print(f"test_recommended_screening_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_referral_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_referral_modal()
        print(f"test_referral_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_cd4_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_cd4_modal()
        print(f"test_cd4_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_viral_load_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_viral_load_modal()
        print(f"test_viral_load_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_vgv_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_vgv_modal()
        print(f"test_vgv_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_vgs_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_vgs_modal()
        print(f"test_vgs_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_vgv_vac_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_vgv_vac_modal()
        print(f"test_vgv_vac_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_fluoroscopy_and_radiography_modals(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_fluoroscopy_and_radiography_modals()
        print(f"test_fluoroscopy_and_radiography_modals passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_sputum_smear_and_tb_symphtoms_modals(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_sputum_smear_and_tb_symphtoms_modals()
        print(f"test_sputum_smear_and_tb_symphtoms_modals passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_xpert_mtb_and_kt_mrt_modals(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_xpert_mtb_and_kt_mrt_modals()
        print(f"test_xpert_mtb_and_kt_mrt_modals passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_tb_treatment_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_tb_treatment_modal()
        print(f"test_tb_treatment_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_art_information_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_art_information_modal()
        print(f"test_art_information_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_art_adherence_level_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_art_adherence_level_modal()
        print(f"test_art_adherence_level_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_recipe_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_recipe_modal()
        print(f"test_recipe_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_pregnancy_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_pregnancy_modal()
        print(f"test_pregnancy_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", test_pregnancy_modal == "FAILED", reason="patient id wasn't taken")
    def test_children_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_children_modal()
        print(f"test_children_modal passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_preventive_therapy_and_ost_modals(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_preventive_therapy_and_ost_modals()
        print(f"test_preventive_therapy_and_ost_modals passed")

    @pytest.mark.skipif(test_registration_of_woman == "FAILED", reason="patient id wasn't taken")
    def test_vgs_treatment_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_vgs_treatment_modal()
        print(f"test_vgs_treatment_modal passed")

    @pytest.mark.xfail(reason="the test is unfinished")
    def test_d_exam_hospitalization_modal(self, browser):
        login(browser)
        zhetysai_user_opens_card_of_woman(browser)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_test_d_exam_hospitalization_modal()
        print(f"test_d_exam_hospitalization_modal passed")



