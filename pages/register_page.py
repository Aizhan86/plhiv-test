from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from .locators import RegisterPageLocators, PatientCardLocators, WorkJournalLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random
from .values import *

global patient_id_child
global patient_id_homeless
global patient_id_foreigner
global patient_id_woman

class RegisterPage(BasePage):


    def register_new_child(self):
        # автозаполнение формы регистрации для ребенка
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        res_code_choice = random.choice(['47', '48', '11', '22'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        self.make(f"{RegisterPageLocators.PATIENT_IIN}.val('{iin}')")
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.PATIENT_SURNAME}.val('{p_surname}')")
        self.make(f"{RegisterPageLocators.PATIENT_NAME}.val('{p_name}')")
        self.make(f"{RegisterPageLocators.PATIENT_MIDNAME}.val('{p_midname}')")
        self.make(f"{RegisterPageLocators.BIRTH_DATE}.calendar('set date', '{p_birthday}');")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{gen_choice}');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        if self.browser.find_element(By.CSS_SELECTOR, 'div[data-field=general_data_adm_obl_viyav] input').get_attribute("value") == "33":
            pass
        else:
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        self.make(f"{RegisterPageLocators.CHILD_STATUS}.dropdown('set selected', '{child_status_choice}');")
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        # self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_AREA}.dropdown('set selected', '5');")
        sleep(2)
        self.make(f"$('div[data-field=registration_address_unit_area] input.search').focus();")
        sleep(1)
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.click();")
        sleep(1)
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        sleep(1)
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('hide');")
        # self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_LOCALITY}.dropdown('set selected', '177');")
        self.make(f"{RegisterPageLocators.REGIS_PLACE}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.REGIS_STREET}.val('{street_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_HOUSE}.val('{55}');")
        self.make(f"{RegisterPageLocators.REGIS_APT}.val('{44}');")
        self.make(f"{RegisterPageLocators.REGIS_PHONE_NO}.val('{87273456987}');")
        self.make(f"{RegisterPageLocators.RESID_AREA}.dropdown('set selected', '3');")
        sleep(2)
        self.make(f"$('div[data-field=fact_address_unit_area] input.search').focus();")
        sleep(1)
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.click();")
        sleep(1)
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        sleep(1)
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('hide');")
        self.make(f"{RegisterPageLocators.RESID_LOCALITY}.dropdown('set selected', '170000000008');")
        self.make(f"{RegisterPageLocators.RESID_PLACE}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.RESID_STREET}.val('{street_choice}');")
        self.make(f"{RegisterPageLocators.RESID_HOUSE}.val('25');")
        self.make(f"{RegisterPageLocators.RESID_APT}.val('45');")
        self.make(f"{RegisterPageLocators.RESID_PHONE_NO}.val('87273456789');")
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '170000000558');")
        # self.make(f"{RegisterPageLocators.RETROSPECTIVE_CHILD}.checkbox('set checked');")
        # self.make(f"{RegisterPageLocators.MOTHERS_SURNAME}.val('{surname}');")
        # self.make(f"{RegisterPageLocators.MOTHERS_NAME}.val('{name}');")
        # self.make(f"{RegisterPageLocators.MOTHERS_MIDNAME}.val('{midname}');")
        # self.make(f"{RegisterPageLocators.MOTHERS_IB_NO}.val('{numbers5}');")
        # self.make(f"{RegisterPageLocators.MOTHERS_IB_NO_DATE}.val('{ib_date}');")
        assert self.browser.execute_script(f"return {RegisterPageLocators.REGISTER_SAVE_BTN}.length"), "No Save button for registering patients"
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click()")
        sleep(5)
        global patient_id_child
        patient_id_child = self.get_patient_id()
        print(f"ID of child patient is {patient_id_child}")

    def check_patient_id_child(self):
        assert f"{patient_id_child}" in self.browser.current_url and patient_id_child != "0000000000"

    def check_patient_id_homeless(self):
        assert f"{patient_id_homeless}" in self.browser.current_url and patient_id_homeless != "0000000000"

    def check_patient_id_woman(self):
        assert f"{patient_id_woman}" in self.browser.current_url and patient_id_woman != "0000000000"

    def check_patient_id_foreigner(self):
        assert f"{patient_id_foreigner}" in self.browser.current_url and patient_id_foreigner != "0000000000"

    def check_patient_iin(self):
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_IIN}.length"), "Patient's IIN object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_IIN}.val()") == iin, "Patient's IIN object doesn't take a value"

    def check_patient_surname(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_SURNAME}.length"), "Patient's surname object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_SURNAME}.val()") == p_surname, "Patient's surname object doesn't take a value"

    def check_patient_name(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_NAME}.length"), "Patient's name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_NAME}.val()") == p_name, "Patient's name object doesn't take a value"

    def check_patient_midname(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_MIDNAME}.length"), "Patient's middle name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_MIDNAME}.val()") == p_midname, "Patient's middle name object doesn't take a value"

    def check_patient_birth_date(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.BIRTH_DATE}.length"), "Patient's birth date object is not accessible"
        l = self.browser.execute_script(f"return {RegisterPageLocators.BIRTH_DATE}.find('input').val()")
        assert l == p_birthday, "Patient's birth date object doesn't take a value"

    def check_patient_gender(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_GENDER}.length"), "Patient's gender object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_GENDER}.find('input').val()") == gen_choice, "Patient's gender object doesn't take a value"

    def check_emergence_area(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.EMERGENCE_AREA}.length"), "Patient's emergence area object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.EMERGENCE_AREA}.find('input').val()") == '3', "Patient's emergence area object doesn't take a value"

    def check_patient_citizenship(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.length"), "Patient's citizenship object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.find('input').val()") == '1', "Patient's citizenship object doesn't take a value"

    def check_child_status(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.CHILD_STATUS}.length"), "Child status object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.CHILD_STATUS}.find('input').val()") == child_status_choice, "Child status object doesn't take a value"

    def check_social_status(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.SOCIAL_STATUS}.length"), "Patient's region of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.SOCIAL_STATUS}.find('input').val()") == soc_status_choice, "Patient's region of living object doesn't take a value"

    def check_registration_medical_organization(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.length"), "Social status object is not accessible"
        s = self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.find('input').val()")
        print(s)
        assert s == 'mo_choice', "Social status object doesn't take a value"

    def check_registration_area(self):
        self.make(f"$('#registration_address_edit_button').click();")
        sleep(2)
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_region_name_modal] .ui.dropdown').length"), "Patient's registration area object is not accessible"
        sleep(1)
        a = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_region_name_modal] .ui.dropdown input[type=hidden]').val()")
        print(a)
        assert a == '5', "Patient's registration area object doesn't take a value"

    def check_registration_unit_area(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_unit_area_modal] .ui.dropdown').length"), "Patient's registration unit area object is not accessible"
        m = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_unit_area_modal] .ui.dropdown').find('input[type=hidden]').val()")
        assert m == '180', "Patient's registration unit area object doesn't take a value"

    def check_registration_locality(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_locality_name_modal] .ui.dropdown').length"), "Patient's registration locality object is not accessible"
        n = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_locality_name_modal] .ui.dropdown').find('input[type=hidden]').val()")
        assert n == '177', "Patient's registration locality object doesn't take a value"

    def check_registration_place(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_place_live_modal] .ui.dropdown').length"), "Patient's registration place object is not accessible"
        o = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_place_live_modal] .ui.dropdown').find('input[type=hidden]').val()")
        assert o == '2', "Patient's registration place object doesn't take a value"

    def check_registration_street(self):
        assert self.browser.execute_script(f"return $('#registration_address_street_modal').length"), "Patient's registration street object is not accessible"
        p = self.browser.execute_script(f"return $('#registration_address_street_modal').find('input[type=hidden]').val()")
        assert p == 'street_choice', "Patient's registration street object doesn't take a value"

    def check_registration_house(self):
        assert self.browser.execute_script(f"return $('#registration_address_house_modal').length"), "Patient's registration house object is not accessible"
        q = self.browser.execute_script(f"return $('#registration_address_house_modal').find('input[type=hidden]').val()")
        assert q == '55', "Patient's registration house object doesn't take a value"

    def check_registration_apartment(self):
        assert self.browser.execute_script(f"return $('#registration_address_kvart_modal').length"), "Patient's registration apartment object is not accessible"
        r = self.browser.execute_script(f"return $('#registration_address_kvart_modal').find('input[type=hidden]').val()")
        assert r == '44', "Patient's registration apartment object doesn't take a value"

    def check_registration_phone_number(self):
        assert self.browser.execute_script(f"return $('#registration_address_telephone_modal').length"), "Patient's registration phone number object is not accessible"
        s = self.browser.execute_script(f"return $('#registration_address_telephone_modal').find('input[type=hidden]').val()")
        assert s == '87273456987', "Patient's registration phone number object doesn't take a value"
        self.make(f"$('#duplicate_to_fact_address').siblings().css('ui', 'red', 'deny', 'button').click()")

    def check_residence_area(self):
        sleep(1)
        self.make(f"$('#registration_address_edit_button').click();")
        sleep(2)
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_AREA}.length"), "Patient's residence area object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_AREA}.find('input').val()") == '3', "Patient's residence area object doesn't take a value"

    def check_residence_unit_area(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_UNIT_AREA}.length"), "Patient's residence unit area object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_UNIT_AREA}.find('input').val()") == '33', "Patient's residence unit area object doesn't take a value"

    def check_residence_locality(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_LOCALITY}.length"), "Patient's residence locality object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_LOCALITY}.find('input').val()") == '170000000008', "Patient's residence locality object doesn't take a value"

    def check_residence_place(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_PLACE}.length"), "Patient's residence place object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_PLACE}.find('input').val()") == '2', "Patient's residence place object doesn't take a value"

    def check_residence_street(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_STREET}.length"), "Patient's residence street object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_STREET}.find('input').val()") == 'street_choice', "Patient's residence street object doesn't take a value"

    def check_residence_house(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_HOUSE}.length"), "Patient's residence house object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_HOUSE}.val()") == '25', "Patient's residence house object doesn't take a value"

    def check_residence_apartment(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_APT}.length"), "Patient's residence apartment object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_APT}.val()") == '45', "Patient's residence apartment object doesn't take a value"

    def check_residence_phone_number(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_PHONE_NO}.length"), "Patient's residence phone number object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RESID_PHONE_NO}.val()") == '87273456789', "Patient's residence phone number object doesn't take a value"

    def check_residence_medical_organization(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.length"), "Residence medical organization object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.find('input').val()") == '170000000558', "Residence medical organization object doesn't take a value"
        self.make(f"$('#modal_fact_address .ui.red.deny.button').click();")

    def check_retrospective_child_checkbox(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RETROSPECTIVE_CHILD}.length"), "Retrospective child checkbox object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RETROSPECTIVE_CHILD}.find('input').val()") == surname, "Retrospective child checkbox object doesn't take a value"

    def check_surname_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.length"), "Mother's surname object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.find('input').val()") == surname, "Mother's surname object doesn't take a value"

    def check_name_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_NAME}.length"), "Mother's name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_NAME}.find('input').val()") == name, "Mother's name object doesn't take a value"

    def check_midname_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_MIDNAME}.length"), "Mother's middle name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_MIDNAME}.find('input').val()") == midname, "Mother's middle name object doesn't take a value"

    def check_ib_number_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO}.length"), "Mother's ib number object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO}.find('input').val()") == 'numbers5', "Mother's ib number object doesn't take a value"

    def check_ib_number_date_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO_DATE}.length"), "Mother's ib number date object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO_DATE}.find('input').val()") == 'ib_date', "Mother's ib number date object doesn't take a value"

    def edit_card(self):
        self.make(f"{RegisterPageLocators.EDIT_REGIS_ADDRESS}.click()")
        self.browser.find_element(*RegisterPageLocators.REGIS_APT2).send_keys(77)
        self.make(f"{RegisterPageLocators.ERROR_REGIS_ADDRESS_SAVE}.click()")
        self.make(f"{RegisterPageLocators.REASON_NOT_EPID}.dropdown('set selected', '3');")
        self.make(f"{RegisterPageLocators.REASON_NOT_DISP_REG}.dropdown('set selected', '6');")
        self.make(f"{RegisterPageLocators.PATIENT_CARD_SAVE}.click()")

    def fill_hiv_antibody_testing_ogc_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IFA_OGC_ADD}.click()")
        self.make(f"{PatientCardLocators.IFA_MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.SURNAME_PERSON_MEDORG}.val('{surname}');")
        self.make(f"{PatientCardLocators.REFERRAL_NO}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.BLOOD_SAMPLING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PRODUCTION_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.SERUM_NUM}.dropdown('set selected', '{serum_num_choice}');")
        self.make(f"{PatientCardLocators.SERUM_NUM2}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.TEST_SYSTEM_TYPE}.dropdown('set selected', '{test_sys_choice}');")
        self.make(f"{PatientCardLocators.EXPIRATION_DATE}.val('{expiration_date}');")
        self.make(f"{PatientCardLocators.SERIES_NUM}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.TEST_CATEGORY}.dropdown('set selected', '{test_cat_choice}');")
        self.make(f"{PatientCardLocators.OP_CRITICAL}.val('1');")
        self.make(f"{PatientCardLocators.OP_SERUM}.val('2');")
        self.make(f"{PatientCardLocators.IFA_RESULT}.dropdown('set selected', '{ifa_res_choice}');")
        self.make(f"{PatientCardLocators.RESPONSIBLE_PERSON}.dropdown('set selected', '{ifa_resp_person_choice}');")
        self.make(f"{PatientCardLocators.IFA_SERVICES}.dropdown('set selected', '{ifa_services_choice}');")

    def check_save_button_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_OGC_SAVE}.length"), "Save button in HIV antibody testing OGC modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_OGC_SAVE}.click();")

    def check_add_button_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_OGC_ADD}.length"), "Add button in HIV antibody testing OGC modal is not accessible"

    def check_edit_button_hiv_ogc_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_OGC_EDIT}.length"), "Edit button in HIV antibody testing OGC modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_OGC_EDIT}.click();")

    def check_medical_organization_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_MED_ORG}.length"), "Medical organization in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_MED_ORG}.find('input').val()") == mo_choice, "Medical organization object in HIV antibody testing OGC modal doesn't take a value"

    def check_surname_of_person_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SURNAME_PERSON_MEDORG}.length"), "Surname of person in medical organization in HIV antibody testing OGC modal is not accessible"
        smo = self.browser.execute_script(f"return {PatientCardLocators.SURNAME_PERSON_MEDORG}.val()")
        print(smo)
        assert smo == surname, "Surname of person in medical organization in HIV antibody testing OGC modal doesn't take a value"

    def check_referral_number_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.REFERRAL_NO}.length"), "Referral number in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.REFERRAL_NO}.val()") == numbers5, "Referral number in HIV antibody testing OGC modal doesn't take a value"

    def check_blood_sampling_date_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_SAMPLING_DATE}.length"), "Blood sampling date in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_SAMPLING_DATE}.val()") == today, "Blood sampling date in HIV antibody testing OGC modal doesn't take a value"

    def check_receipt_date_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECEIPT_DATE}.length"), "Receipt date in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RECEIPT_DATE}.val()") == today, "Receipt date in HIV antibody testing OGC modal doesn't take a value"

    def check_production_date_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PRODUCTION_DATE}.length"), "Production date in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PRODUCTION_DATE}.val()") == today, "Production date in HIV antibody testing OGC modal doesn't take a value"

    def check_serum_number_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM}.length"), "Serum number in HIV antibody testing OGC modal is not accessible"
        sn = self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM}.val()")
        print(sn)
        assert sn == serum_num_choice, "Serum number in HIV antibody testing OGC modal doesn't take a value"

    def check_serum_number2_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM2}.length"), "Serum number 2 in HIV antibody testing OGC modal is not accessible"
        sn2 = self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM2}.val()")
        print(sn2)
        assert sn2 == numbers5, "Serum number 2 in HIV antibody testing OGC modal doesn't take a value"

    def check_test_system_type_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_TYPE}.length"), "Test system type in HIV antibody testing OGC modal is not accessible"
        tst = self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_TYPE}.find('input').val()")
        print(tst)
        assert tst == test_sys_choice, "Test system type in HIV antibody testing OGC modal doesn't take a value"

    def check_expiration_date_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE}.length"), "Expiration date in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE}.val()") == today, "Expiration date in HIV antibody testing OGC modal doesn't take a value"

    def check_series_number_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM}.length"), "Series number in HIV antibody testing OGC modal is not accessible"
        sern = self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM}.val()")
        print(sern)
        assert sern == numbers3, "Series number in HIV antibody testing OGC modal doesn't take a value"

    def check_test_category_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_CATEGORY}.length"), "Test category in HIV antibody testing OGC modal is not accessible"
        tc = self.browser.execute_script(f"return {PatientCardLocators.TEST_CATEGORY}.find('input').val()")
        print(tc)
        assert tc == test_cat_choice, "Test category in HIV antibody testing OGC modal doesn't take a value"

    def check_op_critical_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_CRITICAL}.length"), "The OP critical object in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_CRITICAL}.val()") == '1', "The OP critical object in HIV antibody testing OGC modal doesn't take a value"

    def check_op_serum_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_SERUM}.length"), "The OP serum object in HIV antibody testing OGC modal is not accessible"
        ops = self.browser.execute_script(f"return {PatientCardLocators.OP_SERUM}.val()")
        print(ops)
        assert ops == '2', "The OP serum object in HIV antibody testing OGC modal doesn't take a value"

    def check_result_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT}.length"), "Result object in HIV antibody testing OGC modal is not accessible"
        ifares = self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT}.find('input').val()")
        print(ifares)
        assert ifares == ifa_res_choice, "Result object in HIV antibody testing OGC modal doesn't take a value"

    def check_responsible_person_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RESPONSIBLE_PERSON}.length"), "Responsible_person in HIV antibody testing OGC modal is not accessible"
        rp = self.browser.execute_script(f"return {PatientCardLocators.RESPONSIBLE_PERSON}.find('input').val()")
        print(rp)
        assert rp == ifa_resp_person_choice, "Responsible person in HIV antibody testing OGC modal doesn't take a value"

    def check_services_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_SERVICES}.length"), "The Services object in HIV antibody testing OGC modal is not accessible"
        ifaser = self.browser.execute_script(f"return {PatientCardLocators.IFA_SERVICES}.val()")
        print(ifaser)
        assert ifaser == ifa_services_choice, "The Services object in HIV antibody testing OGC modal doesn't take a value"

    def check_cancel_button_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_OGC_CANCEL}.length"), "Cancel button in HIV antibody testing OGC modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_OGC_CANCEL}.click();")

    def fill_HIV_antibody_testing_KNCDIZ_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IFA_KNCDIZ_ADD}.click()")
        self.make(f"{PatientCardLocators.SCREANING_NUM}.val('{numbers5}')")
        self.make(f"{PatientCardLocators.SERUM_NUM_RC}.dropdown('set selected', '{serum_num_choice}');")
        self.make(f"{PatientCardLocators.REFERRAL_NO_RC}.val('{numbers4}')")
        self.make(f"{PatientCardLocators.RECEIPT_DATE_RC}.val('{today}')")
        self.make(f"{PatientCardLocators.PRODUCTION_DATE_RC}.val('{today}')")
        self.make(f"{PatientCardLocators.TEST_SYSTEM_NAME_RC}.dropdown('set selected', '{test_sys_choice}');")
        self.make(f"{PatientCardLocators.EXPIRATION_DATE_RC}.val('{expiration_date}')")
        self.make(f"{PatientCardLocators.SERIES_NUM_RC}.val('{numbers3}')")
        self.make(f"{PatientCardLocators.OP_CRITICAL_RC}.val('{1}')")
        self.make(f"{PatientCardLocators.OP_SERUM_RC}.val('{2}')")
        self.make(f"{PatientCardLocators.IFA_RESULT_RC}.dropdown('set selected', '{two_choice}');")

    def check_save_button_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RC_SAVE}.length"), "Save button in HIV antibody testing KNCDIZ modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_RC_SAVE}.click();")

    def check_add_button_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_KNCDIZ_ADD}.length"), "Add button in HIV antibody testing KNCDIZ modal is not accessible"

    def check_edit_button_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RC_EDIT}.length"), "Edit button in HIV antibody testing KNCDIZ modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_RC_EDIT}.click();")

    def check_screening_number_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREANING_NUM}.length"), "The Screening number object in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREANING_NUM}.find('input').val()") == numbers5, "The Screening number object in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_serum_number_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM_RC}.length"), "Serum number in HIV antibody testing KNCDIZ modal is not accessible"
        snrc = self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM_RC}.val()")
        print(snrc)
        assert snrc == serum_num_choice, "Serum number in HIV antibody testing OGC modal doesn't take a value"

    def check_referral_number_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.REFERRAL_NO_RC}.length"), "Referral number in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.REFERRAL_NO_RC}.val()") == numbers4, "Referral number in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_receipt_date_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECEIPT_DATE_RC}.length"), "Receipt date in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RECEIPT_DATE_RC}.val()") == today, "Receipt date in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_production_date_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PRODUCTION_DATE_RC}.length"), "Production date in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PRODUCTION_DATE_RC}.val()") == today, "Production date in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_test_system_type_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME_RC}.length"), "Test system type in HIV antibody testing KNCDIZ modal is not accessible"
        tstrc = self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME_RC}.find('input').val()")
        print(tstrc)
        assert tstrc == test_sys_choice, "Test system type in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_expiration_date_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE_RC}.length"), "Expiration date in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE_RC}.val()") == expiration_date, "Expiration date in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_series_number_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM_RC}.length"), "Series number in HIV antibody testing KNCDIZ modal is not accessible"
        sernrc = self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM_RC}.val()")
        print(sernrc)
        assert sernrc == numbers3, "Series number in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_op_critical_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_CRITICAL_RC}.length"), "The OP critical object in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_CRITICAL_RC}.val()") == '1', "The OP critical object in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_op_serum_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OP_SERUM_RC}.length"), "The OP serum object in HIV antibody testing KNCDIZ modal is not accessible"
        opsrc = self.browser.execute_script(f"return {PatientCardLocators.OP_SERUM_RC}.val()")
        print(opsrc)
        assert opsrc == '2', "The OP serum object in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_result_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT_RC}.length"), "Result object in HIV antibody testing KNCDIZ modal is not accessible"
        resrc = self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT_RC}.find('input').val()")
        print(resrc)
        assert resrc == two_choice, "Result object in HIV antibody testing OGC modal doesn't take a value"

    def check_cancel_button_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RC_CANCEL}.length"), "Cancel button in HIV antibody testing KNCDIZ modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_RC_CANCEL}.click();")

    def get_refferal_for_ib(self):
        self.get_referral("1", "234")

    def get_refferal_for_pcr(self):
        self.get_referral("1", "262")

    def fill_IB_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IB_PCR}.click()")
        self.make(f"{PatientCardLocators.IB_ADD}.click()")
        self.make(f"{PatientCardLocators.IB_NUMBER}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.IB_SERUM_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.SAMPLE_NUM}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.IB_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.IB_REGISTER_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.IB_RESULT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.TEST_SYSTEM_NAME}.dropdown('set selected', '{test_name_choice}');")
        self.make(f"{PatientCardLocators.IB_EXPIRATION_DATE}.val('{expiration_date}');")
        self.make(f"{PatientCardLocators.IB_SERIES_NUM}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.IB_RESPONSIBLE_PERSON}.dropdown('set selected', '{respon_person_choice}');")
        self.make(f"{PatientCardLocators.GP160}.dropdown('set selected', '{gp160}');")
        self.make(f"{PatientCardLocators.GP110_120}.dropdown('set selected', '{gp110_120}');")
        self.make(f"{PatientCardLocators.P68}.dropdown('set selected', '{p68}');")
        self.make(f"{PatientCardLocators.P55}.dropdown('set selected', '{p55}');")
        self.make(f"{PatientCardLocators.P52}.dropdown('set selected', '{p52}');")
        self.make(f"{PatientCardLocators.GP41}.dropdown('set selected', '{gp41}');")
        self.make(f"{PatientCardLocators.P40}.dropdown('set selected', '{p40}');")
        self.make(f"{PatientCardLocators.P34}.dropdown('set selected', '{p34}');")
        self.make(f"{PatientCardLocators.P25}.dropdown('set selected', '{p25}');")
        self.make(f"{PatientCardLocators.P18}.dropdown('set selected', '{p18}');")
        self.make(f"{PatientCardLocators.IB_SERVICES}.dropdown('set selected', '234');")

    def check_save_button_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SAVE}.length"), "Save button in IB modal is not accessible"
        self.make(f"{PatientCardLocators.IB_SAVE}.click();")

    def check_add_button_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_ADD}.length"), "Add button in IB modal is not accessible"

    def check_edit_button_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_EDIT}.length"), "Edit button in IB modal is not accessible"
        self.make(f"{PatientCardLocators.IB_EDIT}.click();")

    def check_ib_number_in_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_NUMBER}.length"), "The IB number object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_NUMBER}.val()") == numbers5, "The IB number object in IB modal doesn't take a value"

    def check_serum_number_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERUM_NUM}.length"), "The Serum number object in IB modal is not accessible"
        snib = self.browser.execute_script(f"return {PatientCardLocators.IB_SERUM_NUM}.val()")
        print(snib)
        assert snib == numbers4, "The Serum number object in IB modal doesn't take a value"

    def check_sample_number_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SAMPLE_NUM}.length"), "The Sample number object in IB modal is not accessible"
        samn = self.browser.execute_script(f"return {PatientCardLocators.SAMPLE_NUM}.val()")
        print(samn)
        assert samn == numbers3, "The Sample number object in IB modal doesn't take a value"

    def check_receipt_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RECEIPT_DATE}.length"), "The IB Receipt date object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RECEIPT_DATE}.val()") == today, "The IB Receipt date object in IB modal doesn't take a value"

    def check_register_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_REGISTER_DATE}.length"), "The IB Register date object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_REGISTER_DATE}.val()") == today, "The IB Register date object in IB modal doesn't take a value"

    def check_result_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESULT}.length"), "The Result object in IB modal is not accessible"
        ibres = self.browser.execute_script(f"return {PatientCardLocators.IB_RESULT}.find('input').val()")
        print(ibres)
        assert ibres == '1', "The Result object in IB modal doesn't take a value"

    def check_test_system_name_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME}.length"), "The Test system name object in IB modal is not accessible"
        tsn = self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME}.find('input').val()")
        print(tsn)
        assert tsn == test_name_choice, "The Test system name object in IB modal doesn't take a value"

    def check_expiration_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_EXPIRATION_DATE}.length"), "Expiration date in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_EXPIRATION_DATE}.val()") == expiration_date, "Expiration date in IB modal doesn't take a value"

    def check_series_number_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERIES_NUM}.length"), "Series number in IB modal is not accessible"
        sernib = self.browser.execute_script(f"return {PatientCardLocators.IB_SERIES_NUM}.val()")
        print(sernib)
        assert sernib == numbers3, "Series number in IB modal doesn't take a value"

    def check_responsible_person_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESPONSIBLE_PERSON}.length"), "The Responsible_person object in IB modal is not accessible"
        ibrp = self.browser.execute_script(f"return {PatientCardLocators.IB_RESPONSIBLE_PERSON}.find('input').val()")
        print(ibrp)
        assert ibrp == respon_person_choice, "the Responsible person object in IB modal doesn't take a value"

    def check_gp160_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP160}.length"), "The GP160 objectin IB modal is not accessible"
        ib_gp160= self.browser.execute_script(f"return {PatientCardLocators.GP160}.find('input').val()")
        print(ib_gp160)
        assert ib_gp160 == gp160, "The GP160 object in IB modal doesn't take a value"

    def check_gp110_120_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP110_120}.length"), "The GP110_120 objectin IB modal is not accessible"
        ib_gp110_120 = self.browser.execute_script(f"return {PatientCardLocators.GP110_120}.find('input').val()")
        print(ib_gp110_120)
        assert ib_gp110_120 == gp110_120, "The GP110_120 object in IB modal doesn't take a value"

    def check_p68_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P68}.length"), "The P68 objectin IB modal is not accessible"
        ib_p68 = self.browser.execute_script(f"return {PatientCardLocators.P68}.find('input').val()")
        print(ib_p68)
        assert ib_p68 == p68, "The P68 object in IB modal doesn't take a value"

    def check_p55_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P55}.length"), "The P55 objectin IB modal is not accessible"
        ib_p55 = self.browser.execute_script(f"return {PatientCardLocators.P55}.find('input').val()")
        print(ib_p55)
        assert ib_p55 == p55, "The P55 object in IB modal doesn't take a value"

    def check_p52_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P52}.length"), "The P52 objectin IB modal is not accessible"
        ib_p52 = self.browser.execute_script(f"return {PatientCardLocators.P52}.find('input').val()")
        print(ib_p52)
        assert ib_p52 == p52, "The P52 object in IB modal doesn't take a value"

    def check_gp41_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP41}.length"), "The GP41 objectin IB modal is not accessible"
        ib_gp41 = self.browser.execute_script(f"return {PatientCardLocators.GP41}.find('input').val()")
        print(ib_gp41)
        assert ib_gp41 == gp41, "The GP41 object in IB modal doesn't take a value"

    def check_p40_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P40}.length"), "The P40 objectin IB modal is not accessible"
        ib_p40 = self.browser.execute_script(f"return {PatientCardLocators.P40}.find('input').val()")
        print(ib_p40)
        assert ib_p40 == p40, "The P40 object in IB modal doesn't take a value"

    def check_p34_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P34}.length"), "The P34 objectin IB modal is not accessible"
        ib_p34 = self.browser.execute_script(f"return {PatientCardLocators.P34}.find('input').val()")
        print(ib_p34)
        assert ib_p34 == p34, "The P34 object in IB modal doesn't take a value"

    def check_p25_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P25}.length"), "The P25 objectin IB modal is not accessible"
        ib_p25 = self.browser.execute_script(f"return {PatientCardLocators.P25}.find('input').val()")
        print(ib_p25)
        assert ib_p25 == p25, "The P25 object in IB modal doesn't take a value"

    def check_p18_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P18}.length"), "The P18 object in IB modal is not accessible"
        ib_p18 = self.browser.execute_script(f"return {PatientCardLocators.P18}.find('input').val()")
        print(ib_p18)
        assert ib_p18 == p18, "The P18 object in IB modal doesn't take a value"

    def check_services_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERVICES}.length"), "The Services object in IB modal is not accessible"
        ibser = self.browser.execute_script(f"return {PatientCardLocators.IB_SERVICES}.val()")
        print(ibser)
        assert ibser == '234', "The Services object in IB modal doesn't take a value"

    def check_cancel_button_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_CANCEL}.length"), "Cancel button in IB modal is not accessible"
        self.make(f"{PatientCardLocators.IB_CANCEL}.click();")

    def fill_PCR_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IB_PCR}.click()")
        self.make(f"{PatientCardLocators.PCR_ADD}.click()")
        self.make(f"{PatientCardLocators.PCR_NUMBER}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.PCR_SERUM_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.PCR_SAMPLE_NUM}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.PCR_TYPE}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.PCR_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PCR_REGISTER_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PCR_TEST_SYSTEM_NAME}.dropdown('set selected', '{test_name_choice}');")
        self.make(f"{PatientCardLocators.PCR_EXPIRATION_DATE}.val('{expiration_date}');")
        self.make(f"{PatientCardLocators.PCR_SERIES_NUM}.val('{numbers3}');")
        if two_choice == 1:
            self.make(f"{PatientCardLocators.PCR_DNA_RESULT}.dropdown('set selected', '1');")
        else:
            self.make(f"{PatientCardLocators.PCR_RNA_RESULT}.val('положительный');")
        self.make(f"{PatientCardLocators.PCR_RESPONSIBLE_PERSON}.dropdown('set selected', '{respon_person_choice}');")
        if two_choice == 1:
            self.make(f"{PatientCardLocators.PCR_SERVICES}.dropdown('set selected', '262');")
        else:
            self.make(f"{PatientCardLocators.PCR_SERVICES}.dropdown('set selected', 'положительный');")

    def check_save_button_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_SAVE}.length"), "Save button in PCR modal is not accessible"
        self.make(f"{PatientCardLocators.PCR_SAVE}.click();")

    def check_add_button_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_ADD}.length"), "Add button in PCR modal is not accessible"

    def check_edit_button_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_EDIT}.length"), "Edit button in PCR modal is not accessible"
        self.make(f"{PatientCardLocators.PCR_EDIT}.click();")

    def check_pcr_number_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_NUMBER}.length"), "The PCR number object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_NUMBER}.val()") == numbers5, "The PCR number object in IB modal doesn't take a value"

    def check_serum_number_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_SERUM_NUM}.length"), "The Serum number object in PCR modal is not accessible"
        pcrsn = self.browser.execute_script(f"return {PatientCardLocators.PCR_SERUM_NUM}.val()")
        print(pcrsn)
        assert pcrsn == numbers4, "The Serum number object in PCR modal doesn't take a value"

    def check_sample_number_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_SAMPLE_NUM}.length"), "The Sample number object in PCR modal is not accessible"
        pcrsamn = self.browser.execute_script(f"return {PatientCardLocators.PCR_SAMPLE_NUM}.val()")
        print(pcrsamn)
        assert pcrsamn == numbers3, "The Sample number object in PCR modal doesn't take a value"

    def check_pcr_type_in_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_TYPE}.length"), "The PCR type object in PCR modal is not accessible"
        pcrt = self.browser.execute_script(f"return {PatientCardLocators.PCR_TYPE}.find('input').val()")
        print(pcrt)
        assert pcrt == two_choice, "The PCR type object in PCR modal doesn't take a value"

    def check_receipt_date_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_RECEIPT_DATE}.length"), "The PCR Receipt date object in PCR modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_RECEIPT_DATE}.val()") == today, "The PCR Receipt date object in PCR modal doesn't take a value"

    def check_register_date_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_REGISTER_DATE}.length"), "The PCR Register date object in PCR modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_REGISTER_DATE}.val()") == today, "The PCR Register date object in PCR modal doesn't take a value"

    def check_test_system_name_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_TEST_SYSTEM_NAME}.length"), "The Test system name object in PCR modal is not accessible"
        ptst = self.browser.execute_script(f"return {PatientCardLocators.PCR_TEST_SYSTEM_NAME}.find('input').val()")
        print(ptst)
        assert ptst == test_name_choice, "The Test system name object in PCR modal doesn't take a value"

    def check_expiration_date_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_EXPIRATION_DATE}.length"), "Expiration date in PCR modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_EXPIRATION_DATE}.val()") == expiration_date, "Expiration date in PCR modal doesn't take a value"

    def check_series_number_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_SERIES_NUM}.length"), "Series number in PCR modal is not accessible"
        psern = self.browser.execute_script(f"return {PatientCardLocators.PCR_SERIES_NUM}.val()")
        print(psern)
        assert psern == numbers3, "Series number in PCR modal doesn't take a value"

    def check_result_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_DNA_RESULT}.length"), "The DNA Result object in PCR modal is not accessible"
        pcrres = self.browser.execute_script(f"return {PatientCardLocators.PCR_DNA_RESULT}.find('input').val()")
        print(pcrres)
        assert pcrres == '1' or 'положительный', "The DNA Result object in PCR modal doesn't take a value"

    def check_responsible_person_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_RESPONSIBLE_PERSON}.length"), "The Responsible_person object in PCR modal is not accessible"
        pcrrp = self.browser.execute_script(f"return {PatientCardLocators.PCR_RESPONSIBLE_PERSON}.find('input').val()")
        print(pcrrp)
        assert pcrrp == respon_person_choice, "the Responsible person object in PCR modal doesn't take a value"

    def check_services_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_SERVICES}.length"), "The Services object in PCR modal is not accessible"
        pcrser = self.browser.execute_script(f"return {PatientCardLocators.PCR_SERVICES}.val()")
        print(pcrser)
        assert pcrser == '262' or 'положительный', "The Services object in PCR modal doesn't take a value"

    def check_cancel_button_pcr_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCR_CANCEL}.length"), "Cancel button in PCR modal is not accessible"
        self.make(f"{PatientCardLocators.PCR_CANCEL}.click();")





    def should_test_result_modal(self):
        self.fill_result_modal()
        self.check_result_modal()

    def fill_result_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.RESULT}.click()")
        self.make(f"{PatientCardLocators.RESULT_ADD}.click()")
        self.make(f"{PatientCardLocators.RESULT_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.RESULT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.RESULT_RESPONSIBLE_PERSON}.dropdown('set selected', '{respon_person_choice}');")
        self.make(f"{PatientCardLocators.LAB_SUPERVISER}.dropdown('set selected', '{respon_person_choice}');")
        result_choice = random.choice(['7', '9', '12', '14', '19'])
        self.make(f"{PatientCardLocators.ANALYSIS_RESULT}.dropdown('set selected', '{result_choice}');")
        self.make(f"{PatientCardLocators.RESEARCH_BAZIS}.click()")
        self.make(f"{PatientCardLocators.RESULT_SAVE}.click()")

    def check_result_modal(self):
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in Result modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('zaklyuchenie_NIB').get_attribute("data-field") == numbers5, "Data in Result modal or object Result Number weren't preserved"
        # assert self.is_element_present(*PatientCardLocators.RESULT_PRINT), "Data in Result modal weren't preserved or Print object isn't clickable"

    def should_test_family_members_modal(self):
        self.fill_family_members_modal()
        self.check_family_members_modal()

    def fill_family_members_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.EPID_HISTORY_HIV_ANALYSIS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_ANALYSIS_YEAR}.dropdown('set selected', '2021');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_ANALYSIS_RESULT}.dropdown('set selected', '2');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_ADD}.click()")
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_LASTNAME).send_keys(surname)
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_NAME).send_keys(name)
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_MIDDLE_NAME).send_keys(midname)
        self.make(f"{PatientCardLocators.FAMILY_MEM_GENDER}.dropdown('set selected', '{two_choice}');")
        self.make(f"$('#fam_members_birth_modal').val('{birthday}')")
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_ADDRESS).send_keys(street_choice)
        self.make(f"{PatientCardLocators.FAMILY_MEM_HIV_STATUS}.dropdown('set selected', '1');")
        fam_mem_rel_choice = random.choice(['10', '9', '11'])
        self.make(f"{PatientCardLocators.FAMILY_MEM_RELATION}.dropdown('set selected', '{fam_mem_rel_choice}');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_SAVE}.click()")
        self.make(f"{PatientCardLocators.EPID_HISTORY_FILLING_DATE}.val('{today}')")
        epid_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А.', 'НАУШАБЕКОВА Ж.', 'ДАРМЕНОВА Р. М.'])
        self.make(f"{PatientCardLocators.EPID_DOCTOR}.dropdown('set selected', '{epid_doc_choice}');")

    def check_family_members_modal(self):
        assert self.is_element_present(*PatientCardLocators.FAMILY_MEM_EDIT), "Data in Family members modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('fam_members_surname').get_attribute("data-field") == surname, "Data in Family members modal or object Result Family member's surname weren't preserved"

    def fill_luin_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.LUIN_RS}.click();")
        self.make(f"{PatientCardLocators.DRUG_EXPERIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_IN_TWELVE_MONTH}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_YEARS}.val('{years_choice}');")
        self.make(f"{PatientCardLocators.DRUG_USE_MONTH}.val('{month_choice}');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJECTION}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_HIV}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_SEXUAL_PARTNER}.click();")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_PERMANENT_GROUP}.click();")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_RANDOM_GROUP}.click();")
        self.make(f"{PatientCardLocators.HERAIN}.click();")
        self.make(f"{PatientCardLocators.HANKA}.click();")
        self.make(f"{PatientCardLocators.MAK}.click();")
        self.make(f"{PatientCardLocators.AMPHETAMIN}.click();")
        self.make(f"{PatientCardLocators.SINTETHICS}.click();")
        self.make(f"{PatientCardLocators.OTHER_DRUGS}.click();")
        self.make(f"{PatientCardLocators.ACCOUNTED_IN_NARCO_DISP}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ACCOUNTED_IN_POLICE_FILES}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_YEARS}.val('{years_choice}');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_MONTH}.val('{month_choice}');")
        com_sex_partners_choice = random.choice(['10', '20', '30', '14', '25', '36', '27', '18', '39', '17'])
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_PARTNER_NUM}.val('{com_sex_partners_choice}');")
        self.make(f"{PatientCardLocators.CONDOM_USAGE}.dropdown('set selected', '1');")
        self.browser.find_element(*PatientCardLocators.LUIN_RS_SAVE).click()

    def check_luin_modal(self):
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in LUIN/RS modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_css_selector('#form_luin div[data-field=luin_rs_drug_experiens_modal]').get_attribute("value") == '1', "The object was not filled"


    def should_test_sexual_contacts_modal(self):
        self.fill_sexual_contacts_modal()
        # self.check_sexual_contacts_modal()

    def fill_sexual_contacts_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.SEXUAL_CONTACTS}.click();")
        self.make(f"{PatientCardLocators.HOMO_EXPIRIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_EXP_YEAR}.dropdown('set selected', '1');")
        homo_sex_partners_choice = random.choice(['20', '30', '24', '25', '36', '27', '18', '39', '17'])
        self.make(f"{PatientCardLocators.HOMO_SEX_PARTNER_NUM}.val('{homo_sex_partners_choice}');")
        sex_partners_year_choice = random.choice(['10', '11', '12', '14', '13', '15', '16', '9', '17'])
        self.make(f"{PatientCardLocators.HOMO_SEX_PARTNER_NUM_YEAR}.val('{sex_partners_year_choice}');")
        self.make(f"{PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNER_YEAR}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_SEX_WITH_HIV}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_SEX_WITH_LUIN}.dropdown('set selected', '1');")
        # self.make(f"{PatientCardLocators.DRUG_EXPERIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS}.click();")
        self.make(f"{PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS}.click();")
        self.make(f"{PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS}.click();")
        self.make(f"{PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.HETERO_EXPIRIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.COMMERCIAL_HET_SEX_PARTNER}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HET_SEX_WITH_HIV}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HET_SEX_WITH_LUIN}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HET_SEX_EXP_YEAR}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HET_SEX_PARTNER_NUM_YEAR}.val('{sex_partners_year_choice}');")
        self.make(f"{PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.HET_RANDOM_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_YEAR}.click();")
        self.make(f"{PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_LIVE}.click();")
        self.make(f"{PatientCardLocators.HET_RANDOM_SEX_PARTNERS_LIVE}.click();")
        self.make(f"{PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_LIVE}.click();")
        self.browser.find_element(*PatientCardLocators.SEXUAL_CONTACTS_SAVE).click()

    def check_sexual_contacts_modal(self):
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in HIV antibody testing RESULT modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_css_selector('#form_luin div[data-field=luin_rs_drug_experiens_modal]').get_attribute("value") == '1', "The object was not filled"

    def should_test_mls_modal(self):
            self.fill_mls_modal()
            self.check_mls_modal()

    def fill_mls_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MLS}.click();")
        self.make(f"{PatientCardLocators.MLS_EXPERIENCE}.click();")
        self.make(f"{PatientCardLocators.MLS_ADD}.click();")
        deduction_choice = random.choice(['7', '9', '12', '14', '19', '10', '20', '30', '14', '25', '36', '27', '18', '39', '17'])
        self.make(f"{PatientCardLocators.MLS_NAME}.dropdown('set selected', '{deduction_choice}');")
        self.make(f"{PatientCardLocators.MLS_DATE_START}.val('01.01.2017');")
        self.make(f"{PatientCardLocators.MLS_DATE_END}.val('01.01.2020');")
        self.make(f"{PatientCardLocators.MLS_SAVE}.click();")

    def check_mls_modal(self):
        assert self.is_element_present(*PatientCardLocators.MLS_EDIT), "Data in MLS modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('mls_date_start').get_attribute("data-field") == '1', "The object has not filled"

    def should_test_blood_donor_modal(self):
        self.fill_blood_donor_modal()
        self.check_blood_donor_modal()

    def fill_blood_donor_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DONOR}.click();")
        self.make(f"{PatientCardLocators.BLOOD_DONOR}.click();")
        self.make(f"{PatientCardLocators.DONATION_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_ADD}.click();")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_LOCALITY}.dropdown('set selected', '{locality_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_MED_ORG}.dropdown('set selected', '{mo_choice}');")
        blood_don_cat_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CATEGORY}.dropdown('set selected', '{blood_don_cat_choice}');")
        blood_don_type_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.BLOOD_DONOR_TYPE}.dropdown('set selected', '{blood_don_type_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_CODE}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_SAVE}.click();")

    def check_blood_donor_modal(self):
        assert self.is_element_present(*PatientCardLocators.BLOOD_DONOR_EDIT), "Data in Blood Donor modal modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_organ_donor_modal(self):
        self.fill_organ_donor_modal()
        self.check_organ_donor_modal()

    def fill_organ_donor_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DONOR}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONOR}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_ADD}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_LOCALITY}.dropdown('set selected', '{locality_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG}.dropdown('set selected', '{mo_choice}');")
        organ_don_cat_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ORGAN_DONATION_CATEGORY}.dropdown('set selected', '{organ_don_cat_choice}');")
        organ_don_type_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ORGAN_DONOR_TYPE}.dropdown('set selected', '{organ_don_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE}.dropdown('set selected', '{organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_MED_ORG}.dropdown('set selected', '{mo_rec_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_SAVE}.click();")

    def check_organ_donor_modal(self):
        assert self.is_element_present(*PatientCardLocators.ORGAN_DONOR_EDIT), "Data in Organ Donor modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def fill_blood_recipient_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_LOCALITY}.dropdown('set selected', '{locality_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_NUM_REC}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE_REC}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_COMPONENT_CODE_REC}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS_REC}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_RECEIPT_SAVE}.click();")

    def check_blood_recipient_modal(self):
        assert self.is_element_present(*PatientCardLocators.BLOOD_RECEIPT_EDIT), "Data in Blood donor modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def fill_organ_recipient_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_LOCALITY}.dropdown('set selected', '{locality_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG_REC}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_MED_ORG}.dropdown('set selected', '{mo_rec_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO_REC}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE_REC}.dropdown('set selected', '{organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_NAME}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS_REC}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_SAVE}.click();")

    def check_organ_recipient_modal(self):
        assert self.is_element_present(*PatientCardLocators.ORGAN_RECEIPT_EDIT), "Data in Organ recipient modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('recipient_other_material_date_poluch_mater').get_attribute("data-field") == '01.01.2021', "Data in Organ recipient modal or object Organ transfusion date weren't preserved"

    def should_test_ippp_modal(self):
        self.fill_ippp_modal()
        self.check_ippp_modal()

    def fill_ippp_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.IPPP}.click();")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_EXISTENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DISP_ACCOUNTED_KVD}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DK_CONTACTING}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DK_CONTACTING_NUM_YEAR}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING_NUM}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_ADD}.click();")
        self.make(f"{PatientCardLocators.DIAGNOSIS_DATE}.calendar('set date', '{diagnosis_date}');")
        self.make(f"{PatientCardLocators.DIAGNOSIS}.val('{smth_random}');")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_SAVE}.click();")
        c_section_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.C_SECTION_DELIVERY}.dropdown('set selected', '{c_section_choice}');")
        mat_chem_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.MATERNAL_CHEMOPROPHYLAXIS}.dropdown('set selected', '{mat_chem_choice}');")
        feeding_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ARTIFICIAL_FEEDING}.dropdown('set selected', '{feeding_choice}');")
        child_chem_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.CHILD_CHEMOPROPHYLAXIS}.dropdown('set selected', '{child_chem_choice}');")

    def check_ippp_modal(self):
        assert self.is_element_present(*PatientCardLocators.IPPP_SYMPTOM_EDIT), "Data in IPPP modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('ippp_diag_diagnoz').get_attribute("data-field") == smth_random, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_manipulations_modal(self):
        self.fill_manipulations_modal()
        self.check_manipulations_modal()

    def fill_manipulations_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.MANIPULATION_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_ADD}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_DATE}.calendar('set date', '{manip_emerg_date}');")
        manip_sort_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.MANIPULATIONS_SORT}.dropdown('set selected', '{manip_sort_choice}');")
        manip_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '9', '11'])
        self.make(f"{PatientCardLocators.MANIPULATIONS_TYPE}.dropdown('set selected', '{manip_type_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_SAVE}.click();")

    def check_manipulations_modal(self):
        assert self.is_element_present(*PatientCardLocators.MANIPULATIONS_EDIT), "Data in Manipulations modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('manipulations_med_spr_type_vmeshat_id').get_attribute("data-field") == "{manip_sort_choice}", "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_emergencies_modal(self):
        self.fill_emergencies_modal()
        self.check_emergencies_modal()

    def fill_emergencies_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES_ADD}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES_DATE}.calendar('set date', '{manip_emerg_date}');")
        infection_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.INFECTION_RISK}.dropdown('set selected', '{infection_choice}');")
        self.make(f"{PatientCardLocators.EMERGENCIES_MED_ORG}.val('Pupkin cliniс');")
        trauma_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.TRAUMA_TYPE}.dropdown('set selected', '{trauma_choice}');")
        hours72_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.EMERGENCIES_72HOURS}.dropdown('set selected', '{hours72_choice}');")
        self.make(f"{PatientCardLocators.EMERGENCIES_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.EMERGENCIES_SAVE}.click();")

    def check_emergencies_modal(self):
        assert self.is_element_present(*PatientCardLocators.EMERGENCIES_EDIT), "Data in Emergencies modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_departure_modal(self):
        self.fill_departure_modal()
        self.check_departure_modal()

    def fill_departure_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_ADD}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_START}.calendar('set date', '{eighty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_END}.calendar('set date', '{sixty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_COUNTRY}.dropdown('set selected', '{country_choice}');")
        purpose_choice = random.choice(['1', '2', '3', '4', '5', '6'])
        self.make(f"{PatientCardLocators.DEPARTURE_PURPOSE}.dropdown('set selected', '{purpose_choice}');")
        self.make(f"{PatientCardLocators.DEPARTURE_SAVE}.click();")

    def check_departure_modal(self):
        assert self.is_element_present(*PatientCardLocators.DEPARTURE_EDIT), "Data in Departure modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_source_modal(self):
        self.fill_source_modal()
        # self.check_source_modal()
        self.check_switch_to_card_of_another_patient_modal()

    def fill_source_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.INFECTION_SOURCE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.SOURCE_ADD}.click();")
        self.make(f"{PatientCardLocators.SOURCE_IB_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.SOURCE_IB_DATE}.calendar('set date', '{ib_date}');")
        self.make(f"{PatientCardLocators.SOURCE_SURNAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.SOURCE_NAME}.val('{name}');")
        self.make(f"{PatientCardLocators.SOURCE_MIDDLE_NAME}.val('{midname}');")
        self.make(f"{PatientCardLocators.SOURCE_SAVE}.click();")

    def check_source_modal(self):
        assert self.is_element_present(*PatientCardLocators.SOURCE_EDIT), "Data in Source modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def check_switch_to_card_of_another_patient_modal(self):
        self.make(f"{PatientCardLocators.SOURCE_EDIT}.click();")
        self.make(f"{PatientCardLocators.SOURCE_IB_NUM}.val('91324');")
        self.make(f"{PatientCardLocators.SOURCE_IB_DATE}.calendar('set date', '03.12.2021');")
        self.make(f"{PatientCardLocators.SOURCE_SURNAME}.val('');")
        self.make(f"{PatientCardLocators.SOURCE_NAME}.val('');")
        self.make(f"{PatientCardLocators.SOURCE_MIDDLE_NAME}.val('');")
        self.make(f"{PatientCardLocators.SOURCE_FIND}.click();")
        self.make(f"{PatientCardLocators.SOURCE_SWITCH_TO_CARD}.click();")
        # self.browser.find_element(*RegisterPageLocators.IB_NO).send_keys(55)
        # assert self.make(f"{RegisterPageLocators.PATIENT_NAME}.val()") == "{BPRJXOSSKEVR}", "There weren't switched from Source modal to another patient's card."
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_contact_person_modal(self):
        self.fill_contact_person_modal()
        self.check_contact_person_modal()

    def fill_contact_person_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.CONTACT_PERSON}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_ADD}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_SURNAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_NAME}.val('{name}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_MIDDLE_NAME}.val('{midname}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_GENDER}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_BIRTHDAY}.val('{birthday}');")
        self.make(f"{PatientCardLocators.CONTACT_DATE_START}.val('{fifty_days_ago}');")
        contact_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
        self.make(f"{PatientCardLocators.CONTACT_TYPE}.dropdown('set selected', '{contact_type_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_IB_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.CONTACT_IB_NUM_DATE}.val('{ib_date}');")
        self.make(f"{PatientCardLocators.CONTACT_SURVEY_ADD}.click();")
        self.make(f"{PatientCardLocators.CONTACT_DIAGNOSTICS_DATE}.calendar('set date', '{diagnosis_date}');")
        contact_hiv_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.CONTACT_HIV_STATUS}.dropdown('set selected', '{contact_hiv_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_SURVEY_SAVE}.click();")
        contact_hiv_status = self.make(f"$('#obsled_state').attr('data-field')")
        if contact_hiv_status == "3":
            con_reason_not_surv_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
            self.make(f"{PatientCardLocators.REASON_NOT_SURVEYING}.dropdown('set selected', '{con_reason_not_surv_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_FINISHED}.click();")
        self.make(f"{PatientCardLocators.CONTACT_DAY_END}.val('{twenty_days_ago}');")
        self.make(f"{PatientCardLocators.CONTACT_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.click();")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.dropdown('hide');")
        self.make(f"{PatientCardLocators.CONTACT_LOCALITY}.dropdown('set selected', '{locality_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_STREET}.val('{street_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_HOUSE}.val('55');")
        self.make(f"{PatientCardLocators.CONTACT_APT}.val('47');")
        self.make(f"{PatientCardLocators.CONTACT_PHONE_NO}.val('87279876543');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_SAVE}.click();")

    def check_contact_person_modal(self):
        assert self.is_element_present(*PatientCardLocators.CONTACT_PERSON_EDIT), "Data in HIV antibody testing Contact Person modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def fill_dispensary_observation_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();") # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")
        self.make(f"{PatientCardLocators.D_OBSER_AIDC_CENTER}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.DATE_OF_REGIS}.calendar('set date', '{regis_date}');")

    def check_save_button_of_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_SAVE}.length"), "Dispensary observation modal's Save button is not accessible"
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")

    def check_add_button_of_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_OBSER_ADD}.length"), "Dispensary observation modal's Add button is not accessible"
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")

    def check_edit_button_of_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_OBSER_EDIT}.length"), "Dispensary observation modal's Edit button is not accessible"
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")

    def check_dispensary_registration_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object doesn't take a value"

    def check_cancel_button_of_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_CANCEL_BTN}.length"), "Dispensary observation modal's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.DISP_CANCEL_BTN}.click();")

    def fill_at_risk_modal(self):
        self.make(f"{PatientCardLocators.DRUG_INJ_CONSUMPTION}.dropdown('set selected', '{drug_cons_choice}');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_YEAR}.val('2');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_REGIS}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.ALCOHOL_CONSUMPTION}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.OUTPATIENT_CARD_NO}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.DISP_START_DATE}.calendar('set date', '{sixty_days_ago}');")
        self.make(f"{PatientCardLocators.DISP_DOCTORS_NAME}.dropdown('set selected', '{disp_doc_choice}');")

    def check_save_button_in_at_risk_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_SAVE_BTN}.length"), "Save button in At-risk modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.DISP_SAVE_BTN}.click();")

    def check_drug_injection(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_INJ_CONSUMPTION}.length"), "Drug consumption object in Dispensary observation is not accessible"
        dic = self.browser.execute_script(f"return {PatientCardLocators.DRUG_INJ_CONSUMPTION}.find('input').val()")
        print(dic)
        assert dic == drug_cons_choice, "Drug consumption object in Dispensary observation doesn't take a value"

    def check_drug_consumption_year(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_CONSUMPTION_YEAR}.length"), "Drug consumption year object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_CONSUMPTION_YEAR}.val()") == '2', "Drug consumption year object doesn't take a value"

    def check_registration_date_at_narcology(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_CONSUMPTION_REGIS}.length"), "Registration at narcology object in Dispensary observation is not accessible"
        dcr = self.browser.execute_script(f"return {PatientCardLocators.DRUG_CONSUMPTION_REGIS}.find('input').val()")
        print(dcr)
        assert dcr == two_choice, "Registration at narcology object in Dispensary observation doesn't take a value"

    def check_alcohol_consumption(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ALCOHOL_CONSUMPTION}.length"), "Alcohol consumption object in Dispensary observation is not accessible"
        ac = self.browser.execute_script(f"return {PatientCardLocators.ALCOHOL_CONSUMPTION}.find('input').val()")
        print(ac)
        assert ac == two_choice, "Alcohol consumption object in Dispensary observation doesn't take a value"

    def check_outpatient_card_num(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OUTPATIENT_CARD_NO}.length"), "Outpatient card number object in Dispensary observation is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OUTPATIENT_CARD_NO}.val()") == numbers4, "Outpatient card number object in Dispensary observation doesn't take a value"

    def check_initial_registration_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_START_DATE}.length"), "Initial registration date object in Dispensary observation is not accessible"
        ird = self.browser.execute_script(f"return {PatientCardLocators.DISP_START_DATE}.find('input').val()")
        print(ird)
        assert ird == sixty_days_ago, "Initial registration date object in Dispensary observation doesn't take a value"

    def check_doctor_name(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_DOCTORS_NAME}.length"), "Doctor name object in Dispensary observation is not accessible"
        ddn = self.browser.execute_script(f"return {PatientCardLocators.DISP_DOCTORS_NAME}.find('input').val()")
        print(ddn)
        assert ddn == disp_doc_choice, "Doctor name object in Dispensary observation doesn't take a value"

    def should_test_dispensary_observation_modal_when_patient_deregistered(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")
        self.make(f"{PatientCardLocators.D_OBSER_AIDC_CENTER}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{PatientCardLocators.DATE_OF_REGIS}.calendar('set date', '{regis_date}');")
        self.make(f"{PatientCardLocators.DATE_OF_DEREGIS}.calendar('set date', '{deregis_date}');")
        reason_deregis_choice = random.choice(['1', '2', '3', '4', '8', '9', '10'])
        self.make(f"{PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('set selected', '{reason_deregis_choice}');")
        if reason_deregis_choice == 2:
            self.make(f"{PatientCardLocators.D_OBSER_COUNTRY}.dropdown('set selected', '{country_choice}');")
            self.make(f"{PatientCardLocators.D_OBSER_AREA}.dropdown('set selected', '3');")
            self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.focus();")
            self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.click();")
            self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('set selected', '33');")
            self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('hide');")
            self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('set selected', '33');")
        if reason_deregis_choice == 1:
            self.make(f"{PatientCardLocators.DATE_OF_DEATH}.calendar('set date', '{deregis_date}');")
            aidc_death_choice = random.choice(['1', '2'])
            self.make(f"{PatientCardLocators.AIDC_RELATED_DEATH}.dropdown('set selected', '{aidc_death_choice}');")
            death_choice = random.choice(['1', '2', '13', '4', '17', '18', '12'])
            self.make(f"{PatientCardLocators.DEATH_REASON}.dropdown('set selected', '{death_choice}');")
            death_place_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
            self.make(f"{PatientCardLocators.DEATH_PLACE}.dropdown('set selected', '{death_place_choice}');")
            self.make(f"{PatientCardLocators.AUTOPSY}.click();")
            self.make(f"{PatientCardLocators.PATHOLOGOANATOMIC_DIAGNOSIS}.val('Положительный');")
        self.make("$('#modal_d_uchet_vzyatie .ui.green.approve.button').click();")
        drug_cons_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.DRUG_INJ_CONSUMPTION}.dropdown('set selected', '{drug_cons_choice}');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_YEAR}.val('2');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_REGIS}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.ALCOHOL_CONSUMPTION}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.OUTPATIENT_CARD_NO}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.DISP_START_DATE}.calendar('set date', '{sixty_days_ago}');")
        disp_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А ', 'КЕНЖЕЕВА Г ', 'НАУШАБЕКОВА Ж '])
        self.make(f"{PatientCardLocators.DISP_DOCTORS_NAME}.dropdown('set selected', '{disp_doc_choice}');")
        self.make(f"{PatientCardLocators.DISP_SAVE_BTN}.click();")
        # assert self.browser.find_element_by_id('duchet_reason').get_attribute("data-value") == {reason_deregis_choice}, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def fill_perinatal_registration_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_REGIS_ADD}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_MED_ORG}.dropdown('set selected', '{aidc_center_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_REGIS}.calendar('set date', '{regis_date}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.calendar('set date', '{deregis_date}');")
        reason_deregis_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.dropdown('set selected', '{reason_deregis_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_COUNTRY}.dropdown('set selected', '{country_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.PERINATAL_UNIT_AREA}.dropdown('set selected', '33');")
        if reason_deregis_choice == 4:
            self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEATH}.calendar('set date', '{deregis_date}');")
            death_choice = random.choice(['1', '2', '13', '4', '17', '18', '12'])
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_REASON}.dropdown('set selected', '{death_choice}');")
            death_place_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_PLACE}.dropdown('set selected', '{death_place_choice}');")

    def check_save_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_SAVE}.length"), "Perinatal registration modal's Save button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_SAVE}.click();")

    def check_add_button_operinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REGIS_ADD}.length"), "Perinatal registration modal's Add button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_REGIS_ADD}.click();")

    def check_edit_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_EDIT}.length"), "Perinatal registration's Edit button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_EDIT}.click();")

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_MED_ORG}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_MED_ORG}.find('input').val()")
        print(rd)
        assert rd == aidc_center_choice, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.find('input').val()")
        print(rd)
        assert rd == deregis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_dispensary_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()")
        print(rd)
        assert rd == regis_date, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_cancel_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_CANCEL}.length"), "Perinatal registration modal's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_CANCEL}.click();")

    def should_test_arv_prophylaxis_modal(self):
        self.fill_arv_prophylaxis_modal()
        self.check_arv_prophylaxis_modal()

    def fill_arv_prophylaxis_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        arv_proph_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ARV_PROPHYLAXIS}.dropdown('set selected', '{arv_proph_choice}');")
        self.make(f"{PatientCardLocators.ARV_START_DATE}.val('{eighty_days_ago}');")
        # self.make(f"{PatientCardLocators.ARV_END_DATE}.calendar('set date', '{fifty_days_ago}');")
        medication_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '201', '216'])
        self.make(f"{PatientCardLocators.ARV_MEDICATION}.dropdown('set selected', '{medication_choice}');")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME_CHOICE}.click();")
        #self.make(f"$('#add-row-preparaty-table tr:eq(0) td:eq(0) a').click();")
        self.make(f"{PatientCardLocators.ARV_RECIPE_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.ARV_DAY_NUM}.val('30');")
        self.make(f"{PatientCardLocators.ARV_NEXT_DATE}.calendar('set date', '{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_SAVE}.click();")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.calendar('set date', '{fifty_days_ago}');")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.calendar('set date', '{thirty_days_ago}');")
        arv_hiv_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ARV_HIV_STATUS}.dropdown('set selected', '{arv_hiv_choice}');")
        self.make(f"{PatientCardLocators.ARV_HIV_DETERMINATION_DATE}.calendar('set date', '{fifty_days_ago}');")

    def check_arv_prophylaxis_modal(self):
        assert self.is_element_present(*PatientCardLocators.RECOM_CONSULTATION_EDIT), "Data in Recommended Consultation modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def fill_hiv_diagnosis_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_ADD}.click();")
        self.make(f"{PatientCardLocators.FORMULATING_CHANGE_DATE}.val('{thirty_days_ago}');")
        self.make(f"{PatientCardLocators.HIV_STAGE}.dropdown('set selected', '{hiv_stage_choice}');")

    def check_save_button_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DIAGNOSIS_SAVE}.length"), "Save button in HIV diagnosis modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_SAVE}.click();")

    def check_add_button_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DIAGNOSIS_ADD}.length"), "Add button in HIV diagnosis modal is not accessible"

    def check_edit_button_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DIAGNOSIS_EDIT}.length"), "Edit button in HIV diagnosis modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_EDIT}.click();")

    def check_formulating_change_date_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FORMULATING_CHANGE_DATE}.length"), "The Formulating change date object in HIV diagnosis modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FORMULATING_CHANGE_DATE}.val()") == thirty_days_ago, "The Formulating change date object in HIV diagnosis modal doesn't take a value"

    def check_hiv_stage_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STAGE}.length"), "The HIV Stage object in HIV diagnosis modal is not accessible"
        hs = self.browser.execute_script(f"return {PatientCardLocators.HIV_STAGE}.find('input').val()")
        print(hs)
        assert hs == hiv_stage_choice, "The HIV Stage object in HIV diagnosis modal doesn't take a value"

    def check_cancel_button_hiv_diagnosis_modal(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DIAGNOSIS_CANCEL}.length"), "Cancel button in HIV diagnosis modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_CANCEL}.click();")

    def fill_hiv_related_disease_modal(self):
        sleep(1)
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_ADD}.click();")
        self.make(f"{PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.click();")
        self.make(f"{PatientCardLocators.RELATED_DISEASE_HIV_STAGE_CHOICE}.click();")
        self.make(f"{PatientCardLocators.DISEASE_START_DATE}.val('{thirty_days_ago}');")
        self.make(f"{PatientCardLocators.DISEASE_END_DATE}.val('{twenty_days_ago}');")
        self.make(f"{PatientCardLocators.DISEASE_NAME}.dropdown('set selected', '{disease_name_choice}');")

    def check_save_button_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_RELATED_DISEASE_SAVE}.length"), "Save button in HIV related disease modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_SAVE}.click();")

    def check_add_button_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_RELATED_DISEASE_ADD}.length"), "Add button in HIV related disease modal is not accessible"

    def check_edit_button_hiv_related_disease_modal(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_RELATED_DISEASE_EDIT}.length"), "Edit button in HIV related disease modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_EDIT}.click();")

    def check_hiv_stage_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.length"), "The HIV Stage object in HIV related disease is not accessible"
        rdhs = self.browser.execute_script(f"return {PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.find('input').val()")
        print(rdhs)
        assert rdhs == hiv_stage_choice, "The HIV Stage object in HIV related disease doesn't take a value"

    def check_disease_start_date_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISEASE_START_DATE}.length"), "The Disease start date object in HIV related disease is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DISEASE_START_DATE}.val()") == thirty_days_ago, "The Disease start date object in HIV related disease doesn't take a value"

    def check_disease_end_date_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISEASE_END_DATE}.length"), "The Disease end date object in HIV related disease is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DISEASE_END_DATE}.val()") == twenty_days_ago, "The Disease end date object in HIV related disease doesn't take a value"

    def check_cancel_button_hiv_related_disease_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_RELATED_DISEASE_CANCEL}.length"), "Cancel button in HIV diagnosis modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_CANCEL}.click();")

    def fill_recommended_consultation_modal(self):
        sleep(3)
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_ADD}.click();")
        self.make(f"{PatientCardLocators.CONSULTATION_DATE}.calendar('set date', '{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.CONSULTATION}.dropdown('set selected', '{consultation_choice}');")
        self.make(f"{PatientCardLocators.CONSULTATION_DESCRIPTION}.val('Положительный');")

    def check_save_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_SAVE}.length"), "Save button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_SAVE}.click();")

    def check_add_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_ADD}.length"), "Add button in Recommended consultation modal is not accessible"

    def check_edit_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_EDIT}.length"), "Edit button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_EDIT}.click();")

    def check_consultation_date_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DATE}.length"), "The Consultation date object in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DATE}.find('input').val()") == thirty_days_forward, "The Consultation date object in Recommended consultation modaldoesn't take a value"

    def check_consultation_type_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION}.length"), "The Consultation in Recommended consultation modal is not accessible"
        ct = self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION}.find('input').val()")
        print(ct)
        assert ct == consultation_choice, "The Consultation in Recommended consultation modal doesn't take a value"

    def check_consultation_description_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DESCRIPTION}.length"), "The Consultation description  in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DESCRIPTION}.find('input').val()") == 'Положительный', "The Consultation description object in Recommended consultation modal doesn't take a value"

    def check_cancel_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_CANCEL}.length"), "Cancel button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_CANCEL}.click();")

    def fill_recommended_screening_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.RECOM_SCREENING_ADD}.click();")
        self.make(f"{PatientCardLocators.SCREENING_DATE}.calendar('set date', '{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.SURVEY}.dropdown('set selected', '{survey_choice}');")
        self.make(f"{PatientCardLocators.SCREENING_DESCRIPTION}.val('Положительный');")

    def check_save_button_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_SAVE}.length"), "Save button in Recommended screening modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_SCREENING_SAVE}.click();")

    def check_add_button_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_ADD}.length"), "Add button in Recommended screening modal is not accessible"

    def check_edit_button_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_EDIT}.length"), "Edit button in Recommended screening modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_SCREENING_EDIT}.click();")

    def check_consultation_date_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DATE}.length"), "The Consultation date object in Recommended screening modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DATE}.find('input').val()") == thirty_days_forward, "The Consultation date object in Recommended screening modaldoesn't take a value"

    def check_consultation_type_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SURVEY}.length"), "The Consultation in Recommended screening modal is not accessible"
        ct = self.browser.execute_script(f"return {PatientCardLocators.SURVEY}.find('input').val()")
        print(ct)
        assert ct == survey_choice, "The Consultation in Recommended screening modal doesn't take a value"

    def check_consultation_description_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DESCRIPTION}.length"), "The Consultation screening  in Recommended screening modal is not accessible"
        cdrc = self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DESCRIPTION}.find('input').val()")
        print(cdrc)
        assert cdrc == 'Положительный', "The Consultation screening object in Recommended screening modal doesn't take a value"

    def check_cancel_button_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_CANCEL}.length"), "Cancel button in Recommended screening modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_SCREENING_CANCEL}.click();")

    def check_result_modal_in_additional_analysis_tab(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.REFERRAL_ADD}.click();")
        self.make(f"{PatientCardLocators.REFERRAL_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.REFERRAL_NAME}.dropdown('set selected', '{referral_name_choice1}');")
        self.make(f"{PatientCardLocators.REFERRAL_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.SENDER_ORG}.dropdown('set selected', '{mo_choice2}');")
        self.make(f"{PatientCardLocators.RECIPIENT_ORG}.dropdown('set selected', '{mo_choice2}');")
        self.make(f"{PatientCardLocators.REFERRAL_SAVE}.click();")
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click();")
        self.make(f"{PatientCardLocators.ADDITIONAL_ANALYSIS}.click();")
        self.make(f"{PatientCardLocators.AA_EDIT}.click();")
        self.make(f"{PatientCardLocators.AA_RESULT}.val('положительный');")
        self.make(f"{PatientCardLocators.AA_SAVE}.click();")
        # assert self.browser.execute_script(f"$('#additional_research_table tr:eq(1) td:eq(7)')[0].innerText") == 'Подтвержден', "Data in Result modal in Additional Analysis Tab weren't preserved"


    def check_referral_modal(self):
        assert self.is_element_present(*PatientCardLocators.REFERRAL_EDIT), "Data in Referral modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('add_row_refferals_table').get_attribute("action-type") == 'edit', "Data in Referral modal weren't preserved"

    def fill_cd4_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CD4_VL_SURVEY}.click();")
        self.make(f"{PatientCardLocators.CD4_DETERMINATION_ADD}.click();")
        self.make(f"{PatientCardLocators.REGISTRATION_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.CD4_BLOOD_DONOR_MED_ORG}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.CD4_MATERIAL_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.CD4_SAMPLE_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.CD4_REGISTERING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.CD4}.val('1');")
        self.make(f"{PatientCardLocators.CD3}.val('2');")
        self.make(f"{PatientCardLocators.CD8}.val('2');")
        self.make(f"{PatientCardLocators.CD4_CD8}.val('2');")
        self.make(f"{PatientCardLocators.CD4_rate}.val('2');")
        self.make(f"{PatientCardLocators.CD4_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.CD4_REMARK}.val('Положительный');")
        self.make(f"{PatientCardLocators.CD4_SERVICES}.dropdown('set selected', '{service_choice}');")

    def check_save_button_cd4_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SAVE}.length"), "Save button in CD4 modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.CD4_SAVE}.click();")

    def check_add_button_cd4_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_DETERMINATION_ADD}.length"), "Add button in CD4 modal is not accessible"

    def check_edit_button_cd4_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_EDIT}.length"), "Edit button in CD4 modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.CD4_EDIT}.click();")

    def check_registration_num(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.REGISTRATION_NUM}.length"), "Registration number object in CD4 is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.REGISTRATION_NUM}.val()") == numbers5, "Registration number object in CD4 doesn't take a value"

    def check_cd4_blood_donor_medical_org(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_BLOOD_DONOR_MED_ORG}.length"), "Blood donor medical organization object in CD4 is not accessible"
        bdmo = self.browser.execute_script(f"return {PatientCardLocators.CD4_BLOOD_DONOR_MED_ORG}.find('input').val()")
        print(bdmo)
        assert bdmo == mo_choice1, "Blood donor medical organization object in CD4 doesn't take a value"

    def check_cd4_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in CD4 is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object object in CD4 doesn't take a value"

    def check_cd4_sample_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SAMPLE_RECEIPT_DATE}.length"), "Sample receipt date object in CD4 is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SAMPLE_RECEIPT_DATE}.val()") == today, "Sample receipt date object object in CD4 doesn't take a value"

    def check_cd4_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REGISTERING_DATE}.length"), "Registering date object in CD4 is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REGISTERING_DATE}.val()") == today, "Registering date object in CD4 in CD4 doesn't take a value"

    def check_cd4(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4}.length"), "CD4 object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4}.val()") == '1', "CD4 object doesn't take a value"

    def check_cd3(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD3}.length"), "CD3 object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD3}.val()") == '2', "CD3 object doesn't take a value"

    def check_cd8(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD8}.length"), "CD8 object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD8}.val()") == '2', "CD8 object doesn't take a value"

    def check_cd4_cd8(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_CD8}.length"), "CD4_CD8 object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_CD8}.val()") == '2', "CD4_CD8 object doesn't take a value"

    def check_cd4_rate(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_rate}.length"), "CD4 rate object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_rate}.val()") == '2', "CD4 rate object doesn't take a value"

    def check_cd4_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in CD4 is not accessible"
        mopa = self.browser.execute_script(f"return {PatientCardLocators.CD4_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()")
        print(mopa)
        assert mopa == mo_choice1, "Medical organization which provided analysis in CD4 doesn't take a value"

    def check_cd4_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REMARK}.length"), "CD4 note object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REMARK}.val()") == 'Положительный', "CD4 note object in CD4 doesn't take a value"

    def check_cd4_services(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SERVICES}.length"), "Services object in CD4 is not accessible"
        mopa = self.browser.execute_script(f"return {PatientCardLocators.CD4_SERVICES}.find('input').val()")
        print(mopa)
        assert mopa == service_choice, "Services object  in CD4 doesn't take a value"

    def check_cancel_button_cd4_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_CANCEL}.length"), "Cancel button in CD4 modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.CD4_CANCEL}.click();")

    def fill_viral_load_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CD4_VL_SURVEY}.click();")
        self.make(f"{PatientCardLocators.VIRAL_LOAD_ADD}.click();")
        self.make(f"{PatientCardLocators.VL_ANALYSIS_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.VL_DONOR_MED_ORG}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VL_MATERIAL_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VL_MATERIAL_SAMPLING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VL_REGISTERING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VL_RESULT}.dropdown('set selected', '{vl_res_choice}');")
        self.make(f"{PatientCardLocators.VL_RESULT_ML}.val('{vl_res_ml_choice}');")
        self.make(f"{PatientCardLocators.LOG}.val('2');")
        self.make(f"{PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VL_REMARK}.dropdown('set selected', '{remark_choice}');")
        self.make(f"{PatientCardLocators.VL_SERVICES}.dropdown('set selected', '{vl_service_choice}');")

    def check_save_button_cd4_vl_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_SAVE}.length"), "Save button in Viral load modal in CD4&VL is not accessible"
        self.make(f"{PatientCardLocators.VL_SAVE}.click();")

    def check_add_button_cd4_vl_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VIRAL_LOAD_ADD}.length"), "Add button in Viral load modal is not accessible"

    def check_edit_button_cd4_vl_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_EDIT}.length"), "Edit button in Viral load is not accessible"
        self.make(f"{PatientCardLocators.VL_EDIT}.click();")

    def check_vl_analysis_num(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_ANALYSIS_NUM}.length"), "Analysis number object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_ANALYSIS_NUM}.val()") == numbers5, "Analysis number object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_donor_medical_org(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_DONOR_MED_ORG}.length"), "Donor medical organization object in Viral load in CD4&VL is not accessible"
        dmo = self.browser.execute_script(f"return {PatientCardLocators.VL_DONOR_MED_ORG}.find('input').val()")
        print(dmo)
        assert dmo == mo_choice1, "Donor medical organization object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object in Viral load in CD4&VLdoesn't take a value"

    def check_cd4_vl_material_sampling_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MATERIAL_SAMPLING_DATE}.length"), "Material sampling date object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MATERIAL_SAMPLING_DATE}.val()") == today, "Material sampling date object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REGISTERING_DATE}.length"), "Registering date object in Viral load is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REGISTERING_DATE}.val()") == today, "Registering date object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_result(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT}.length"), "Result object in Viral load in CD4&VL is not accessible"
        vlr = self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT}.find('input').val()")
        print(vlr)
        assert vlr == vl_res_choice, "Result object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_result_ml(self):
        assert self.browser.execute_script(
            f"return {PatientCardLocators.VL_RESULT_ML}.length"), "Result ML object in Viral load in CD4&VL is not accessible"
        rml = self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT_ML}.find('input').val()")
        print(rml)
        assert rml == vl_res_ml_choice, "Result ML in Viral load in CD4&VL doesn't take a value"

    def check_log(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LOG}.length"), "Log object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.LOG}.val()") == '2', "Log object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in Viral load in CD4&VL is not accessible"
        vmopa = self.browser.execute_script(f"return {PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()")
        print(vmopa)
        assert vmopa == mo_choice1, "Medical organization which provided analysis in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REMARK}.length"), "Note object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REMARK}.val()") == remark_choice, "Note object in Viral load in CD4&VLdoesn't take a value"

    def check_cd4_vl_services(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_SERVICES}.length"), "Services object in Viral load in CD4&VL is not accessible"
        vls = self.browser.execute_script(f"return {PatientCardLocators.VL_SERVICES}.find('input').val()")
        print(vls)
        assert vls == vl_service_choice, "Services object in Viral load in CD4&VL doesn't take a value"

    def check_cancel_button_cd4_vl_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_CANCEL}.length"), "Cancel button in Viral load in CD4&VLmodal is not accessible"
        self.make(f"{PatientCardLocators.VL_CANCEL}.click();")

    def fill_vgv_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGV_ADD}.click();")
        self.make(f"{PatientCardLocators.VGV_REGISTRATION_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.VGV_MAT_DONOR_MED_ORG}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VGV_REGISTERING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.MARKER}.dropdown('set selected', '{marker_choice}');")
        self.make(f"{PatientCardLocators.VGV_RESULT}.dropdown('set selected', '1');")
        # self.make(f"{PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VGV_REMARK}.val('Положительный');")

    def check_save_button_vgv_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_SAVE}.length"), "Save button in VGV modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_SAVE}.click();")

    def check_add_button_vgv_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_ADD}.length"), "Add button in VGV modal is not accessible"

    def check_edit_button_vgv_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_EDIT}.length"), "Edit button in VGV modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_EDIT}.click();")

    def check_vgv_registration_num(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTRATION_NUM}.length"), "Registration number object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTRATION_NUM}.val()") == numbers5, "Registration number object in VGV modal doesn't take a value"

    def check_vgv_donor_medical_org(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MAT_DONOR_MED_ORG}.length"), "Donor medical organization object in VGV modal is not accessible"
        mdmo = self.browser.execute_script(f"return {PatientCardLocators.VGV_MAT_DONOR_MED_ORG}.find('input').val()")
        print(mdmo)
        assert mdmo == mo_choice1, "Donor medical organization object in VGV modal doesn't take a value"

    def check_vgv_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object in VGV modal doesn't take a value"

    def check_vgv_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTERING_DATE}.length"), "Registering date object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTERING_DATE}.val()") == today, "Registering date object in VGV modal doesn't take a value"

    def check_marker(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MARKER}.length"), "Marker object in VGV modal is not accessible"
        vgvm = self.browser.execute_script(f"return {PatientCardLocators.MARKER}.find('input').val()")
        print(vgvm)
        assert vgvm == marker_choice, "Marker object in VGV modal doesn't take a value"

    def check_vgv_result(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_RESULT}.length"), "Result object in VGV modal is not accessible"
        vgvres = self.browser.execute_script(f"return {PatientCardLocators.VGV_RESULT}.find('input').val()")
        print(vgvres)
        assert vgvres == '1', "Result object in VGV modal doesn't take a value"

    def check_vgv_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in VGV modal is not accessible"
        mopa = self.browser.execute_script(f"return {PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()")
        print(mopa)
        assert mopa == mo_choice1, "Medical organization which provided analysis in VGV modal doesn't take a value"

    def check_vgv_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REMARK}.length"), "Note object in VGV modal is not accessible"
        vgvr = self.browser.execute_script(f"return {PatientCardLocators.VGV_REMARK}.find('input').val()")
        print(vgvr)
        assert vgvr == 'Положительный', "Note object in VGV modal doesn't take a value"

    def check_cancel_button_vgv_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_CANCEL}.length"), "Cancel button in VGV modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_CANCEL}.click();")

    def fill_vgs_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGS_ADD}.click();")
        self.make(f"{PatientCardLocators.VGS_REGISTRATION_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.VGS_MAT_DONOR_MED_ORG}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VGS_REGISTERING_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VGS_ANALYSIS_TYPE}.dropdown('set selected', '{analysis_choice}');")
        self.make(f"{PatientCardLocators.VGS_RESULT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{mo_choice1}');")
        self.make(f"{PatientCardLocators.VGS_REMARK}.val('Положительный');")

    def check_save_button_vgs_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_SAVE}.length"), "Save button in VGS modal is not accessible"
        self.make(f"{PatientCardLocators.VGS_SAVE}.click();")

    def check_add_button_vgs_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_ADD}.length"), "Add button in VGS modal is not accessible"

    def check_edit_button_vgs_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_EDIT}.length"), "Edit button in VGS modal is not accessible"
        self.make(f"{PatientCardLocators.VGS_EDIT}.click();")

    def check_vgs_registration_num(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTRATION_NUM}.length"), "Registration number object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTRATION_NUM}.val()") == numbers5, "Registration number object in VGS modal doesn't take a value"

    def check_vgs_donor_medical_org(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MAT_DONOR_MED_ORG}.length"), "Donor medical organization object in VGS modal is not accessible"
        mdmo = self.browser.execute_script(f"return {PatientCardLocators.VGS_MAT_DONOR_MED_ORG}.find('input').val()")
        print(mdmo)
        assert mdmo == mo_choice1, "Donor medical organization object in VGS modal doesn't take a value"

    def check_vgs_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object in VGS modal doesn't take a value"

    def check_vgs_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTERING_DATE}.length"), "Registering date object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTERING_DATE}.val()") == today, "Registering date object in VGS modal doesn't take a value"

    def check_vgs_analysis_type(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_ANALYSIS_TYPE}.length"), "Marker object in VGS modal is not accessible"
        vgvm = self.browser.execute_script(f"return {PatientCardLocators.VGS_ANALYSIS_TYPE}.find('input').val()")
        print(vgvm)
        assert vgvm == analysis_choice, "Marker object in VGS modal doesn't take a value"

    def check_vgs_result(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_RESULT}.length"), "Result object in VGS modal is not accessible"
        vgsres = self.browser.execute_script(f"return {PatientCardLocators.VGS_RESULT}.find('input').val()")
        print(vgsres)
        assert vgsres == '1', "Result object in VGS modal doesn't take a value"

    def check_vgs_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in VGS modal is not accessible"
        mopa = self.browser.execute_script(f"return {PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()")
        print(mopa)
        assert mopa == mo_choice1, "Medical organization which provided analysis in VGS modal doesn't take a value"

    def check_vgs_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REMARK}.length"), "Note object in VGS modal is not accessible"
        vgvr = self.browser.execute_script(f"return {PatientCardLocators.VGS_REMARK}.find('input').val()")
        print(vgvr)
        assert vgvr == 'Положительный', "Note object in VGS modal doesn't take a value"

    def check_cancel_button_vgs_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_CANCEL}.length"), "Cancel button in VGS modal is not accessible"
        self.make(f"{PatientCardLocators.VGS_CANCEL}.click();")

    def fill_vgv_vac_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGV_VAC_ADD}.click();")
        self.make(f"{PatientCardLocators.VGV_VAC_MULTIPLICITY}.dropdown('set selected', '{vac_multi_choice}');")
        self.make(f"{PatientCardLocators.IMMUNIZATION_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.VGV_VAC_DOSE_VOLUME}.val('{dose}');")
        self.make(f"{PatientCardLocators.VGV_VAC_SERIES}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.val('{vac_multi_choice}');")
        self.make(f"{PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.dropdown('set selected', '{mo_choice1}');")

    def check_save_button_vgv_vac_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_SAVE}.length"), "Save button in VGV vaccination modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_VAC_SAVE}.click();")

    def check_add_button_vgv_vac_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_ADD}.length"), "Add button in VGV vaccination modal is not accessible"

    def check_edit_button_vgv_vac_modal(self):
        assert self.browser.execute_script(
            f"return {PatientCardLocators.VGV_VAC_EDIT}.length"), "Edit button in VGV vaccination modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_VAC_EDIT}.click();")

    def check_vgv_vac_multiplicity(self):
        assert self.browser.execute_script(
            f"return {PatientCardLocators.VGV_VAC_MULTIPLICITY}.length"), "Multilicity object in VGV vaccination modal is not accessible"
        mdmo = self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_MULTIPLICITY}.find('input').val()")
        print(mdmo)
        assert mdmo == vac_multi_choice, "Multilicity object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_immunization_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IMMUNIZATION_DATE}.length"), "Immunization date object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IMMUNIZATION_DATE}.val()") == today, "Immunization receipt date object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_dose_volume(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_DOSE_VOLUME}.length"), "Registering date object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_DOSE_VOLUME}.val()") == dose, "Registering date object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_series(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_SERIES}.length"), "Marker object in VGV vaccination modal is not accessible"
        ser = self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_SERIES}.find('input').val()")
        print(ser)
        assert ser == numbers5, "Marker object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_country_producer(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.length"), "Result object in VGV vaccination modal is not accessible"
        vgvcp = self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.find('input').val()")
        print(vgvcp)
        assert vgvcp == vac_multi_choice, "Result object in VGV vaccination modal doesn't take a value"

    def check_vgv_medical_org_provided_vaccination(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.length"), "Medical organization which provided vaccination in VGV vaccination modal is not accessible"
        mopv = self.browser.execute_script(f"return {PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.find('input').val()")
        print(mopv)
        assert mopv == mo_choice1, "Medical organization which provided analysis in VGV vaccination modal doesn't take a value"

    def check_cancel_button_vgv_vgs_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_CANCEL}.length"), "Cancel button in VGV vaccination modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_VAC_CANCEL}.click();")

    def fill_fluoroscopy_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.TUBERCULOSIS}.click();")
        self.make(f"{PatientCardLocators.FLUOROSCOPY_ADD}.click();")
        self.make(f"{PatientCardLocators.FLUOR_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.FLUOR_RESULT}.dropdown('set selected', '{fluor_choice}');")

    def check_save_button_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOROSCOPY_SAVE}.length"), "Save button in Fluoroscopy modal is not accessible"
        self.make(f"{PatientCardLocators.FLUOROSCOPY_SAVE}.click();")

    def check_add_button_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOROSCOPY_ADD}.length"), "Add button in Fluoroscopy modal is not accessible"

    def check_edit_button_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOROSCOPY_EDIT}.length"), "Edit button in Fluoroscopy modal is not accessible"
        self.make(f"{PatientCardLocators.FLUOROSCOPY_EDIT}.click();")

    def check_registering_date_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_REGISTERING_DATE}.length"), "The Registering date object in Fluoroscopy modal is not accessible"
        frt = self.browser.execute_script(f"return {PatientCardLocators.FLUOR_REGISTERING_DATE}.find('input').val()")
        print(frt)
        assert frt == today, "The Registering date object in Fluoroscopy modal doesn't take a value"

    def check_result_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_RESULT}.length"), "Tne Result object in Fluoroscopy modal is not accessible"
        rr = self.browser.execute_script(f"return {PatientCardLocators.FLUOR_RESULT}.find('input').val()")
        print(rr)
        assert rr == fluor_choice, "The Result object in Fluoroscopy modal doesn't take a value"

    def check_cancel_button_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOROSCOPY_CANCEL}.length"), "Cancel button in Fluoroscopy modal is not accessible"
        self.make(f"{PatientCardLocators.FLUOROSCOPY_CANCEL}.click();")

    def fill_radiography_modal(self):
        self.make(f"{PatientCardLocators.RADIOGRAPHY_ADD}.click();")
        self.make(f"{PatientCardLocators.RADIO_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.RADIO_RESULT}.dropdown('set selected', '{radio_choice}');")

    def check_save_button_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIOGRAPHY_SAVE}.length"), "Save button in Radiography modal is not accessible"
        self.make(f"{PatientCardLocators.RADIOGRAPHY_SAVE}.click();")

    def check_add_button_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIOGRAPHY_ADD}.length"), "Add button in Radiography modal is not accessible"

    def check_edit_button_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIOGRAPHY_EDIT}.length"), "Edit button in Radiography modal is not accessible"
        self.make(f"{PatientCardLocators.RADIOGRAPHY_EDIT}.click();")

    def check_registering_date_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIO_REGISTERING_DATE}.length"), "The Registering date object in Radiography modal is not accessible"
        rrd = self.browser.execute_script(f"return {PatientCardLocators.RADIO_REGISTERING_DATE}.find('input').val()")
        print(rrd)
        assert rrd == today, "The Registering date in Radiography modal doesn't take a value"

    def check_result_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIO_RESULT}.length"), "The Result object in Radiography modal is not accessible"
        rr = self.browser.execute_script(f"return {PatientCardLocators.RADIO_RESULT}.find('input').val()")
        print(rr)
        assert rr == radio_choice, "The Result object in Radiography modal doesn't take a value"

    def check_cancel_button_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIOGRAPHY_CANCEL}.length"), "Cancel button in Radiography modal is not accessible"
        self.make(f"{PatientCardLocators.RADIOGRAPHY_CANCEL}.click();")

    def fill_sputum_smear_modal(self):
        self.make(f"{PatientCardLocators.SPUTUM_SMEAR_EXAMINATION_ADD}.click();")
        self.make(f"{PatientCardLocators.SPUTUM_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.SPUTUM_RESULT}.dropdown('set selected', '{sputum_choice}');")

    def check_save_button_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_SAVE}.length"), "Save button in Sputum smear modal is not accessible"
        self.make(f"{PatientCardLocators.SPUTUM_SAVE}.click();")

    def check_add_button_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_SMEAR_EXAMINATION_ADD}.length"), "Add button in Sputum smear modal is not accessible"

    def check_edit_button_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_EDIT}.length"), "Edit button in Sputum smear modal is not accessible"
        self.make(f"{PatientCardLocators.SPUTUM_EDIT}.click();")

    def check_registering_date_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_REGISTERING_DATE}.length"), "The Registering date object in Sputum smear modal is not accessible"
        rrd = self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_REGISTERING_DATE}.find('input').val()")
        print(rrd)
        assert rrd == today, "The Registering date object in Sputum smear modal doesn't take a value"

    def check_result_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_RESULT}.length"), "The Result object in Sputum smear modal is not accessible"
        rr = self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_RESULT}.find('input').val()")
        print(rr)
        assert rr == sputum_choice, "The Result object in Sputum smear modal doesn't take a value"

    def check_cancel_button_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_CANCEL}.length"), "Cancel button in Sputum smear modal is not accessible"
        self.make(f"{PatientCardLocators.SPUTUM_CANCEL}.click();")

    def fill_tb_symphtoms_modal(self):
        self.make(f"{PatientCardLocators.TB_SYMPHTOMS_ADD}.click();")
        self.make(f"{PatientCardLocators.TB_SYMPH_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.TB_SYMPH_RESULT}.dropdown('set selected', '{tb_symph_choice}');")

    def check_save_button_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_SAVE}.length"), "Save button in TB symphtoms modal is not accessible"
        self.make(f"{PatientCardLocators.TB_SYMPH_SAVE}.click();")

    def check_add_button_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPHTOMS_ADD}.length"), "Add button in TB symphtoms modal is not accessible"

    def check_edit_button_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_EDIT}.length"), "Edit button in TB symphtoms modal is not accessible"
        self.make(f"{PatientCardLocators.TB_SYMPH_EDIT}.click();")

    def check_registering_date_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_REGISTERING_DATE}.length"), "The Registering date object in TB symphtoms modal is not accessible"
        srd = self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_REGISTERING_DATE}.find('input').val()")
        print(srd)
        assert srd == today, "The Registering date object in TB symphtoms modal doesn't take a value"

    def check_result_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_RESULT}.length"), "The Result object in TB symphtoms modal is not accessible"
        sr = self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_RESULT}.find('input').val()")
        print(sr)
        assert sr == tb_symph_choice, "The Result object in TB symphtoms modal doesn't take a value"

    def check_cancel_button_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_CANCEL}.length"), "Cancel button in TB symphtoms modal is not accessible"
        self.make(f"{PatientCardLocators.TB_SYMPH_CANCEL}.click();")

    def fill_xpert_mtb_modal(self):
        self.make(f"{PatientCardLocators.XPERT_MTB_ADD}.click();")
        self.make(f"{PatientCardLocators.XPERT_MTB_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.XPERT_MTB_RESULT}.dropdown('set selected', '{xpert_choice}');")

    def check_save_button_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_SAVE}.length"), "Save button in Xpert MTB modal is not accessible"
        self.make(f"{PatientCardLocators.XPERT_MTB_SAVE}.click();")

    def check_add_button_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_ADD}.length"), "Add button in Xpert MTB modal is not accessible"

    def check_edit_button_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_EDIT}.length"), "Edit button in Xpert MTB modal is not accessible"
        self.make(f"{PatientCardLocators.XPERT_MTB_EDIT}.click();")

    def check_registering_date_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_REGISTERING_DATE}.length"), "The Registering date object in Xpert MTB modal is not accessible"
        xrd = self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_REGISTERING_DATE}.find('input').val()")
        print(xrd)
        assert xrd == today, "The Registering date object in Xpert MTB modal doesn't take a value"

    def check_result_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_RESULT}.length"), "The Result object in Xpert MTB modal is not accessible"
        xr = self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_RESULT}.find('input').val()")
        print(xr)
        assert xr == xpert_choice, "The Result object in Xpert MTB modal doesn't take a value"

    def check_cancel_button_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_CANCEL}.length"), "Cancel button in Xpert MTB modal is not accessible"
        self.make(f"{PatientCardLocators.XPERT_MTB_CANCEL}.click();")

    def fill_kt_mrt_modal(self):
        self.make(f"{PatientCardLocators.KT_MRT_ADD}.click();")
        self.make(f"{PatientCardLocators.KT_MRT_REGISTERING_DATE}.calendar('set date', '{today}');")
        self.make(f"{PatientCardLocators.KT_MRT_RESULT}.dropdown('set selected', '{mrt_choice}');")

    def check_save_button_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_SAVE}.length"), "Save button in KT/MRT modal is not accessible"
        self.make(f"{PatientCardLocators.KT_MRT_SAVE}.click();")

    def check_add_button_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_ADD}.length"), "Add button in KT/MRT modal is not accessible"

    def check_edit_button_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_EDIT}.length"), "Edit button in KT/MRT modal is not accessible"
        self.make(f"{PatientCardLocators.KT_MRT_EDIT}.click();")

    def check_registering_date_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_REGISTERING_DATE}.length"), "The Registering date object in KT/MRT modal is not accessible"
        ktrd = self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_REGISTERING_DATE}.find('input').val()")
        print(ktrd)
        assert ktrd == today, "The Registering date object in KT/MRT modal doesn't take a value"

    def check_result_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_RESULT}.length"), "The Result object in KT/MRT modal is not accessible"
        ktr = self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_RESULT}.find('input').val()")
        print(ktr)
        assert ktr == mrt_choice, "The Result object in KT/MRT modal doesn't take a value"

    def check_cancel_button_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_CANCEL}.length"), "Cancel button in KT/MRT modal is not accessible"
        self.make(f"{PatientCardLocators.KT_MRT_CANCEL}.click();")

    def fill_tb_treatment_modal(self):
        self.make(f"{PatientCardLocators.TB_TREATMENT_ADD}.click();")
        self.make(f"{PatientCardLocators.LAB_NAME_CONFIRMED_TB}.val('Random lab');")
        self.make(f"{PatientCardLocators.TB_DIAG_REGISTERING_DATE}.val('{thirty_days_ago}')")
        self.make(f"{PatientCardLocators.SICK_TYPE}.dropdown('set selected', '{case_choice}');")
        self.make(f"{PatientCardLocators.TB_DIAG_MKB10}.dropdown('set selected', '{tb_analysis_choice}');")
        self.make(f"{PatientCardLocators.LOCATION}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.BAC_SECRETION}.dropdown('set selected', '{bac_secr_choice}');")
        self.make(f"{PatientCardLocators.TREATMENT_START_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.TREATMENT_END_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.OUTCOME}.dropdown('set selected', '{outcome_choice}');")

    def check_save_button_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_TREATMENT_SAVE}.length"), "Save button in TB treatment modal is not accessible"
        self.make(f"{PatientCardLocators.TB_TREATMENT_SAVE}.click();")

    def check_add_button_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_TREATMENT_ADD}.length"), "Add button in TB treatment modal is not accessible"

    def check_edit_button_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_TREATMENT_EDIT}.length"), "Edit button in TB treatment modal is not accessible"
        self.make(f"{PatientCardLocators.TB_TREATMENT_EDIT}.click();")

    def check_lab_name_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LAB_NAME_CONFIRMED_TB}.length"), "Confirmed labaratory name object in TB treatment modal is not accessible"
        lnc = self.browser.execute_script(f"return {PatientCardLocators.LAB_NAME_CONFIRMED_TB}.val()")
        print(lnc)
        assert lnc == 'Random lab', "Confirmed labaratory name object in TB treatment modal doesn't take a value"

    def check_diagnosis_registering_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_REGISTERING_DATE}.length"), "Diagnosis registering date in TB treatment modal is not accessible"
        tbdrd = self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_REGISTERING_DATE}.find('input').val()")
        print(tbdrd)
        assert tbdrd == thirty_days_ago, "Diagnosis registering date in TB treatment doesn't take a value"

    def check_sick_type_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SICK_TYPE}.length"), "The Sick type object in TB treatment modal is not accessible"
        ktr = self.browser.execute_script(f"return {PatientCardLocators.SICK_TYPE}.find('input').val()")
        print(ktr)
        assert ktr == case_choice, "The Sick type object in TB treatment doesn't take a value"

    def check_diagnosis_mkb10_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_MKB10}.length"), "The diagnosis MKB10 object in TB treatment modal is not accessible"
        mkb10 = self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_MKB10}.find('input').val()")
        print(mkb10)
        assert mkb10 == tb_analysis_choice, "The diagnosis MKB10 object in TB treatment doesn't take a value"

    def check_location_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LOCATION}.length"), "The Location object in TB treatment modal is not accessible"
        tbloc = self.browser.execute_script(f"return {PatientCardLocators.LOCATION}.find('input').val()")
        print(tbloc)
        assert tbloc == two_choice, "The Location object in TB treatment doesn't take a value"

    def check_bac_secretion_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BAC_SECRETION}.length"), "The BAC secretion object in TB treatment modal is not accessible"
        bac = self.browser.execute_script(f"return {PatientCardLocators.BAC_SECRETION}.find('input').val()")
        print(bac)
        assert bac == bac_secr_choice, "The BAC secretion object in TB treatment doesn't take a value"

    def check_treatment_start_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_START_DATE}.length"), "The Treatment start date object in TB treatment modal is not accessible"
        tsd = self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_START_DATE}.find('input').val()")
        print(tsd)
        assert tsd == today, "The Treatment start date object in TB treatment modal doesn't take a value"

    def check_treatment_end_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_END_DATE}.length"), "The Treatment end date object in TB treatment modal is not accessible"
        ted = self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_END_DATE}.find('input').val()")
        print(ted)
        assert ted == today, "The Treatment end date object in TB treatment modal doesn't take a value"

    def check_outcome_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OUTCOME}.length"), "The Outcome object in TB treatment modal is not accessible"
        ktr = self.browser.execute_script(f"return {PatientCardLocators.OUTCOME}.find('input').val()")
        print(ktr)
        assert ktr == outcome_choice, "The Outcome object in TB treatment doesn't take a value"

    def check_cancel_button_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_TREATMENT_CANCEL}.length"), "Cancel button in TB treatment modal is not accessible"
        self.make(f"{PatientCardLocators.TB_TREATMENT_CANCEL}.click();")

    def check_presence_in_history_tb_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.length"), "The Presence in history object in TB tab is not accessible"
        self.make(f"{PatientCardLocators.PRESENCE_TB_IN_HISTORY}.dropdown('set selected', '{two_choice}');")
        tbh = self.browser.execute_script(f"return {PatientCardLocators.PRESENCE_TB_IN_HISTORY}.find('input').val()")
        print(tbh)
        assert tbh == two_choice, "The Presence in history object in TB tab doesn't take a value"

    def check_d_registered_date_tb_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.length"), "The Disp registered date object in TB tab is not accessible"
        self.make(f"{PatientCardLocators.D_ACCOUNTED_DATE}.calendar('set date', '{today}');")
        drd = self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.find('input').val()")
        print(drd)
        assert drd == today, "The Disp registered date object in TB tab doesn't take a value"

    def should_test_art_information_modal(self):
        self.fill_art_information_modal()
        self.check_art_information_modal()

    def fill_art_information_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_REASONS_DEFINE_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_READINESS_DEFINE_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.WRITTEN_CONSENT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_START_DATE}.val('{today}')")
        row_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ART_ROW}.dropdown('set selected', '{row_choice}');")
        self.make(f"{PatientCardLocators.ART_SCHEME}.dropdown('set selected', '{preg_medic_choice}');")
        art_mo_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ART_MED_ORG}.dropdown('set selected', '{art_mo_choice}');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")
        self.browser.find_element(*PatientCardLocators.ART_INFORMATION_EDIT).click()
        self.make(f"{PatientCardLocators.ART_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_MEDICATION_NAME}.click();")
        if PatientCardLocators.ART_MEDICATION_NAME_CHOICE:
            self.make(f"{PatientCardLocators.ART_MEDICATION_NAME_CHOICE}.click();")
            self.make(f"{PatientCardLocators.ART_RECIPE_NUM}.val('{numbers4}');")
            self.make(f"{PatientCardLocators.ART_ISSUANCE_SAVE}.click();")
        else:
            self.make(f"{PatientCardLocators.ART_MEDICATION_NAME_DENY}.click();")
            self.make(f"{PatientCardLocators.ART_ISSUANCE_DENY}.click();")
            print(f"Medicines are not available")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGED_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_TYPE}.dropdown('set selected', '1');")
        art_change_choice = random.choice(['1', '5', '6', '7', '8', '18', '20'])
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_REASON}.dropdown('set selected', '{art_change_choice}');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")

    def check_art_information_modal(self):
        assert self.is_element_present(*PatientCardLocators.ART_INFORMATION_EDIT), "Data in Art Information modal weren't preserved or invalid selector for Edit button"

    def should_test_art_adherence_level_modal(self):
        self.fill_art_adherence_level_modal()
        self.check_art_adherence_level_modal()

    def fill_art_adherence_level_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        support_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ART_ADHERENCE_SUPPORT}.dropdown('set selected', '{support_choice}');")
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_ADHER_YEAR}.val('2021');")
        quater_choice = random.choice(['1', '2', '3', '4'])
        self.make(f"{PatientCardLocators.ART_ADHER_QUARTER}.dropdown('set selected', '{quater_choice}');")
        adherence_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ART_ADHERENCE}.dropdown('set selected', '{adherence_choice}');")
        if adherence_choice == "3":
            adher_reas_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
            self.make(f"{PatientCardLocators.ART_ADHER_LOW_REASONS}.dropdown('set selected', '{adher_reas_choice}');")
        side_effect_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        self.make(f"{PatientCardLocators.SIDE_EFFECTS}.dropdown('set selected', '{side_effect_choice}');")
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_SAVE}.click();")

    def check_art_adherence_level_modal(self):
        assert self.is_element_present(*PatientCardLocators.ART_ADHER_LEVEL_EDIT), "Data in Art Adherence modal weren't preserved or invalid selector for Edit button"

    def should_test_recipe_modal(self):
        self.fill_recipe_modal()
        # self.check_recipe_modal()

    def fill_recipe_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_RECIPE_ADD}.click();")
        self.make(f"{PatientCardLocators.RECIPE_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.RECIPE_DATE}.val('{today}')")
        art_med_choice = random.choice(['111'])
        self.make(f"{PatientCardLocators.ART_MEDICATION}.dropdown('set selected', '{art_med_choice}');")
        self.make(f"{PatientCardLocators.DOSE}.val('1 таблетка');")
        dose_code_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.DOSE_CODE}.dropdown('set selected', '{dose_code_choice}');")
        self.make(f"{PatientCardLocators.CONCENTRATION}.val('1');")
        self.make(f"{PatientCardLocators.PACKING}.val('Да');")
        self.make(f"{PatientCardLocators.QUANTITY}.val('30');")
        unpacking_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.UNPACKING_SIGNS}.dropdown('set selected', '{unpacking_choice}');")
        self.make(f"{PatientCardLocators.SIGNATURE}.val('{smth_random}');")
        self.make(f"{PatientCardLocators.ART_RECIPE_SAVE}.click();")

    def check_recipe_modal(self):
        assert self.is_element_present(*PatientCardLocators.ART_RECIPE_EDIT), "Data in Recipe modal weren't preserved or invalid selector for Edit button"

    def should_test_pregnancy_modal(self):
        self.fill_pregnancy_modal()
        # self.check_pregnancy_modal()

    def fill_pregnancy_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CHILDREN_PREGNANCY}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_ADD}.click();")
        pregnancy_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.make(f"{PatientCardLocators.PREGNANCY}.dropdown('set selected', '{pregnancy_choice}');")
        preg_partner_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.PREG_SEX_PARTNER}.dropdown('set selected', '{preg_partner_choice}');")
        self.make(f"{PatientCardLocators.PREG_PARTNER_HIV_STATUS}.dropdown('set selected', '{hiv_status_choice}');")
        self.make(f"{PatientCardLocators.OGC_REGIS_DATE}.val('{regis_date}');")
        preg_weeks_choice = random.choice(['1', '12', '2', '3', '4', '5', '6', '7', '8', '9', '10', '31', '42'])
        self.make(f"{PatientCardLocators.OGC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.ANTENATAL_CLINIC_REGIS_DATE}.val('{regis_date}');")
        self.make(f"{PatientCardLocators.AC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        preg_res_choice = random.choice(['1', '12', '2', '3', '11', '13'])
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT}.dropdown('set selected', '{preg_res_choice}');")
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPHILAXYS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_START_DATE}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_START}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_END_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_END}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_MEDICATIONS}.dropdown('set selected', '{preg_medic_choice}');")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_ADD}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME_CHOICE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_RECIPE_NUM}.val('{numbers4}');")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_SAVE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")


    def check_pregnancy_modal(self):
        assert self.is_element_present(*PatientCardLocators.PREGNANCY_EDIT), "Data in Pregnancy modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_children_modal(self):
        self.fill_children_modal()
        self.check_children_modal()

    def fill_children_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CHILDREN_PREGNANCY}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_ADD}.click();")
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CHILD}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_NAME}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_NAME_CHOICE}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_RECIPE_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_SAVE}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_ADD}.click();")
        child_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ALIVE_CHILD}.dropdown('set selected', '{child_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_SURNAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.CHILDS_NAME}.val('{name}');")
        self.make(f"{PatientCardLocators.CHILDS_MIDNAME}.val('{midname}');")
        self.make(f"{PatientCardLocators.CHILDS_BIRTHDAY}.val('{birthday}');")
        self.make(f"{PatientCardLocators.CHILDS_GENDER}.dropdown('set selected', '{two_choice}');")
        pathology_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.PATHALOGY_AT_BIRTH}.dropdown('set selected', '{pathology_choice}');")
        feeding_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.CHILDS_FEEDING}.dropdown('set selected', '{feeding_choice}');")
        full_term_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.FULL_TERM_CHILD}.dropdown('set selected', '{full_term_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_DEATH_DATE}.val('{deregis_date}');")
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_SAVE}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")

    def check_children_modal(self):
        assert self.is_element_present(*PatientCardLocators.PREGNANCY_EDIT), "Data in Pregnancy modal weren't preserved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == numbers3, "Data in Blood donor modal or object Blood donor code weren't preserved"

    def should_test_preventive_therapy_and_ost_modals(self):
        self.fill_preventive_therapy_and_ost_modals()
        self.check_preventive_therapy_and_ost_modals()

    def fill_preventive_therapy_and_ost_modals(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.THERAPHY}.click();")
        self.make(f"{PatientCardLocators.PREVENTIVE_THERAPHY_ADD}.click();")
        prev_med_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.PREV_THER_MEDICATION}.dropdown('set selected', '{prev_med_choice}');")
        self.make(f"{PatientCardLocators.REASONS_SET_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREV_THER_START_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREV_THER_END_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREV_THER_SAVE}.click();")
        self.make(f"{PatientCardLocators.OPIOID_SUBSTITUTION_THERAPHY_ADD}.click();")
        self.make(f"{PatientCardLocators.OST_START_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.OST_END_DATE}.val('{today}');")
        ost_med_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.OST_MEDICATION_TYPE}.dropdown('set selected', '{ost_med_choice}');")
        # reas_fin_choice = random.choice(['1', '2'])
        # self.make(f"{PatientCardLocators.REASONS_OF_FINISHING}.dropdown('set selected', '{reas_fin_choice}');")
        self.make(f"{PatientCardLocators.OST_SAVE}.click();")

    def check_preventive_therapy_and_ost_modals(self):
        assert self.is_element_present(*PatientCardLocators.PREV_THER_EDIT), "Data in Preventive therapy modal weren't preserved or invalid selector for Edit button"
        assert self.is_element_present(*PatientCardLocators.OST_EDIT), "Data in OST modal weren't preserved or invalid selector for Edit button"

    def should_test_vgs_treatment_modal(self):
        self.fill_vgs_treatment_modal()
        self.check_vgs_treatment_modal()

    def fill_vgs_treatment_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.THERAPHY}.click();")
        self.make(f"{PatientCardLocators.VGS_TREATMENT_ADD}.click();")
        self.make(f"{PatientCardLocators.VGS_TREAT_START_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.VGS_TREAT_END_DATE}.val('{today}');")
        treat_res_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
        self.make(f"{PatientCardLocators.VGS_TREAT_RESULT}.dropdown('set selected', '{treat_res_choice}');")
        self.make(f"{PatientCardLocators.VGS_TREAT_SAVE}.click();")

    def check_edit_button_vgs_treatment_modal(self):
        assert self.is_element_present(*PatientCardLocators.VGS_TREAT_EDIT), "Data in VGS treatment modal weren't preserved or invalid selector for Edit button"


    def fill_d_screening_hospitalization_modal(self):
        self.make(f"{PatientCardLocators.D_SCREENING_HOSPITALIZATION}.click();")
        self.make(f"{PatientCardLocators.D_SCRN_HOSP_ADD}.click();")
        self.make(f"{PatientCardLocators.DATE_OF_ELIGIBILITY_FOR_TREATMENT}.val('{today}');")
        self.make(f"{PatientCardLocators.D_SCRN_TREAT_TYPE}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.MPI_PROFILE}.dropdown('set selected', '{treat_res_choice}');")
        self.make(f"{PatientCardLocators.HOSP_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.DATE_OF_DISCHARGE}.val('{today}');")
        self.make(f"{PatientCardLocators.D_SCRN_TREAT_RESULT}.dropdown('set selected', '{treat_outc_choice}');")

    def check_save_button_d_screening_hospitalization_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_HOSP_SAVE}.length"), "Save button in D-screening, hospitalization modal is not accessible"
        self.make(f"{PatientCardLocators.D_SCRN_HOSP_SAVE}.click();")

    def check_add_button_d_screening_hospitalization_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_HOSP_ADD}.length"), "Add button in D-screening, hospitalization modal is not accessible"

    def check_edit_button_d_screening_hospitalization_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_HOSP_EDIT}.length"), "Edit button in D-screening, hospitalization modal is not accessible"
        self.make(f"{PatientCardLocators.D_SCRN_HOSP_EDIT}.click();")

    def check_date_of_eligibility_for_treatment_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_ELIGIBILITY_FOR_TREATMENT}.length"), "Date of eligibility for treatment object in D-screening, hospitalization modal is not accessible"
        doeft = self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_ELIGIBILITY_FOR_TREATMENT}.val()")
        print(doeft)
        assert doeft == today, "Date of eligibility for treatment objectt in D-screening, hospitalization modal doesn't take a value"

    def check_treatment_type_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_TYPE}.length"), "The Treatment type object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_TYPE}.find('input').val()") == two_choice, "The Treatment type object in D-screening, hospitalization modal doesn't take a value"

    def check_mpi_profile_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MPI_PROFILE}.length"), "The MPI profile object in D-screening, hospitalization modal is not accessible"
        mpif = self.browser.execute_script(f"return {PatientCardLocators.MPI_PROFILE}.find('input').val()")
        print(mpif)
        assert mpif == treat_res_choice, "The MPI profile object in D-screening, hospitalization modal doesn't take a value"

    def check_hosp_date_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOSP_DATE}.length"), "Hospitalization date in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOSP_DATE}.val()") == today, "Hospitalization date in D-screening, hospitalization modal doesn't take a value"

    def check_date_of_discharge_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DISCHARGE}.length"), "The Date of discharge object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DISCHARGE}.val()") == today, "The Date of discharge object  in D-screening, hospitalization modal doesn't take a value"

    def check_treatment_result_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_RESULT}.length"), "Treatment result in D-screening, hospitalization modal is not accessible"
        tr = self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_RESULT}.find('input').val()")
        print(tr)
        assert tr == treat_outc_choice, "Treatment result in D-screening, hospitalization modal doesn't take a value"

    def check_cancel_button_d_screening_hospitalization_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_HOSP_CANCEL}.length"), "Cancel button in D-screening, hospitalization modal is not accessible"
        self.make(f"{PatientCardLocators.D_SCRN_HOSP_CANCEL}.click();")

    def fill_visits_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VISITS}.click();")
        self.browser.execute_script("document.querySelector('div.ui.secondary.padding_ext_07.segment a.ui.green.button.add_osmotr').click()")
        sleep(3)
        new_window = self.browser.window_handles[1]
        first_window = self.browser.window_handles[0]
        self.browser.switch_to.window(new_window)
        self.make(f"{PatientCardLocators.ATTENDANCE_DATE}.val('{today}');")
        exam_choice = random.choice(['infection', 'pediatr', 'ftiziatr', 'ginekolog', 'terapevt', 'dermatolog', 'psiholog', 'social_worker', 'narkolog'])
        self.make(f"{PatientCardLocators.SCREENING_HELD}.dropdown('set selected', '{exam_choice}');")
        service_choice = random.choice(['2', '3', '348', '328', '33', '25', '322', '331', '14'])
        self.make(f"{PatientCardLocators.VISITS_SERVICES}.dropdown('set selected', '{service_choice}');")
        place_choice = random.choice(['home', 'mls', 'stacionar', 'center_hiv', 'ambulatorno'])
        self.make(f"{PatientCardLocators.SCREENING_PLACE}.dropdown('set selected', '{place_choice}');")
        attendance_choice = random.choice(['perv_osmotr', 'd_osmotr', 'po_zabolev', 'current_reception'])
        self.make(f"{PatientCardLocators.ATTENDANCE_TYPE}.dropdown('set selected', '{attendance_choice}');")
        self.make(f"{PatientCardLocators.TEMPERATURE}.val('36.6');")
        self.make(f"{PatientCardLocators.WEIGHT}.val('32');")
        self.make(f"{PatientCardLocators.HEIGHT}.val('100');")
        self.make(f"{PatientCardLocators.IMT}.val('25');")
        self.make(f"{PatientCardLocators.COMPLAINTS}.val('{surname}');")
        self.make(f"{PatientCardLocators.HISTORY_INFORMATION}.val('{midname}');")
        self.make(f"{PatientCardLocators.LAST_MENSIS}.val('{today}');")
        self.make(f"{PatientCardLocators.CONTRACEPTION}.click();")
        contraception_choice = random.choice(['condoms', 'spiral', 'hirurg_sterialize', 'drug', 'kok', 'another'])
        self.make(f"{PatientCardLocators.CONTRACEPTION_TYPES}.dropdown('set selected', '{contraception_choice}');")
        self.make(f"{PatientCardLocators.VISITS_SEX_PARTNER}.click();")
        self.make(f"{PatientCardLocators.ART_RECEIPT}.click();")
        planned_pregnancy_choice = random.choice(['Yes', 'No'])
        if planned_pregnancy_choice == "Yes":
            self.make(f"{PatientCardLocators.PLANNED_PREGNANCY_YES}.click();")
        else:
            self.make(f"{PatientCardLocators.PLANNED_PREGNANCY_NO}.click();")
        self.make(f"{PatientCardLocators.VISITS_ALCOHOL}.click();")
        self.make(f"{PatientCardLocators.VISITS_DRUGS}.click();")
        choices_for_visits_modal = random.choice(['10', '20'])
        self.make(f"{PatientCardLocators.VISITS_INJ_DRUG_LAST_HALF_YEAR}.dropdown('set selected', '{choices_for_visits_modal}');")
        self.make(f"{PatientCardLocators.VISITS_COM_SEX_LAST_HALF_YEAR}.dropdown('set selected', '{choices_for_visits_modal}');")
        self.make(f"{PatientCardLocators.VISITS_HOMO_SEX_LAST_HALF_YEAR}.dropdown('set selected', '{choices_for_visits_modal}');")
        state_choice = random.choice(['satisfactory', 'moderate_severity', 'severe_severity', 'extremely_heavy'])
        self.make(f"{PatientCardLocators.STATE}.dropdown('set selected', '{state_choice}');")
        conscious_choice = random.choice(['clear', 'stupor', 'sopor', 'coma'])
        self.make(f"{PatientCardLocators.CONSCIOUSNESS}.dropdown('set selected', '{conscious_choice}');")
        position_choice = random.choice(['active', 'passive', 'forced'])
        self.make(f"{PatientCardLocators.POSITION}.dropdown('set selected', '{position_choice}');")
        body_choice = random.choice(['normostenic', 'astenik', 'hypersthenic'])
        self.make(f"{PatientCardLocators.BODY_TYPE}.dropdown('set selected', '{body_choice}');")
        feeding_choice1 = random.choice(['moderate', 'low', 'high', 'cachexia'])
        self.make(f"{PatientCardLocators.FEEDING}.dropdown('set selected', '{feeding_choice1}');")
        self.make(f"{PatientCardLocators.LIPODYSTROPHY}.dropdown('set selected', '{choices_for_visits_modal}');")
        skin_choice = random.choice(['regular_coloring', 'pale_pink', 'icteric', 'another'])
        self.make(f"{PatientCardLocators.SKIN_MUCOSA}.dropdown('set selected', '{skin_choice}');")
        if skin_choice == 'another':
            self.make(f"{PatientCardLocators.SKIN_DESCRIPTION}.val('пятнистый');")
        nails_choice = random.choice(['not_changed', 'changed'])
        self.make(f"{PatientCardLocators.NAILS}.dropdown('set selected', '{nails_choice}');")
        if nails_choice == 'changed':
            self.make(f"{PatientCardLocators.NAILS_DESCRIPTION}.val('странный');")
        self.make(f"{PatientCardLocators.RASH}.dropdown('set selected', '{choices_for_visits_modal}');")
        if choices_for_visits_modal == '10':
            rash_choice = random.choice(['punctate', 'papular', 'vesicular', 'urtikarnaya'])
            self.make(f"{PatientCardLocators.RASH_TYPE}.dropdown('set selected', '{rash_choice}');")
            self.make(f"{PatientCardLocators.RASH_LOCALITY}.val('высыпания на шее');")
        lymph_choice = random.choice(['not_palpable', 'not_enlarged', 'palpable', 'enlarged', 'painful', 'not_painful',
                                     'single', 'multiple', 'not_soldered'])
        self.make(f"{PatientCardLocators.PERIFEPHERAL_LYMPH_NODES}.dropdown('set selected', '{lymph_choice}');")
        if lymph_choice == 'enlarged':
            self.make(f"{PatientCardLocators.LYMPH_NODES_DESCRIPTION}.val('0,5');")
        osteo_choice = random.choice(['no_pathological_changes', 'with_pathological_changes'])
        self.make(f"{PatientCardLocators.OSTEO_ARTICULAR_SYSTEM}.dropdown('set selected', '{osteo_choice}');")
        if osteo_choice == 'with_pathological_changes':
            self.make(f"{PatientCardLocators.OSTEO_DESCRIPTION}.val('хрустящий');")
        breath_choice = random.choice(['vesicular', 'tough', 'weakened', 'another'])
        self.make(f"{PatientCardLocators.BREATH_SOUNDS}.dropdown('set selected', '{breath_choice}');")
        if breath_choice == 'another':
            self.make(f"{PatientCardLocators.BREATH_SOUNDS_DESCRIPTION}.val('поскрипывает');")
        wheesing_choice = random.choice(['Yes', 'No'])
        if wheesing_choice == "Yes":
            self.make(f"{PatientCardLocators.WHEEZING_YES}.click();")
            wheezing_choice = random.choice(['dry', 'wet', 'whistling', 'crepitus'])
            self.make(f"{PatientCardLocators.WHEEZING_TYPE}.dropdown('set selected', '{wheezing_choice}');")
        else:
            self.make(f"{PatientCardLocators.WHEEZING_NO}.click();")
        self.make(f"{PatientCardLocators.RESPIRATORY_RATE}.val('100');")
        heart_choice = random.choice(['clear', 'muffled', 'rhythmic', 'arrhythmic'])
        self.make(f"{PatientCardLocators.HEART_SOUNDS}.dropdown('set selected', '{heart_choice}');")
        self.make(f"{PatientCardLocators.HEART_RATE}.val('100');")
        self.make(f"{PatientCardLocators.BLOOD_PREASURE}.val('100');")
        noise_choice = random.choice(['not_heard', 'heard'])
        self.make(f"{PatientCardLocators.NOISE}.dropdown('set selected', '{noise_choice}');")
        if noise_choice == 'heard':
            self.make(f"{PatientCardLocators.NOISE_DESCRIPTION}.val('журчит');")
        tongue_choice = random.choice(['dry', 'wet', 'clean_of_plaque', 'white_coated', 'patches_on_side_surfaces',
                                      'cheesy_patina', 'another'])
        self.make(f"{PatientCardLocators.TONGUE}.dropdown('set selected', '{tongue_choice}');")
        if tongue_choice == 'another':
            self.make(f"{PatientCardLocators.TONGUE_DESCRIPTION}.val('язык высунут');")
        self.make(f"{PatientCardLocators.ORAL_MUCOSA}.val('{surname}');")
        stomach_choice = random.choice(['painless_on_palpation', 'tense', 'painful_on_palpation', 'another'])
        self.make(f"{PatientCardLocators.STOMACH}.dropdown('set selected', '{stomach_choice}');")
        if stomach_choice == 'another' or 'painful_on_palpation':
            self.make(f"{PatientCardLocators.STOMACH_DESCRIPTION}.val('язык высунут');")
        liver_choice = random.choice(['not_increased', 'on_the_edge_of_the_costal_arch',
                                     'protrudes_from_under_the_edge_of_the_costal_arch', 'consistency_dense', 'soft',
                                     'elastic', 'another'])
        self.make(f"{PatientCardLocators.LIVER}.dropdown('set selected', '{liver_choice}');")
        if liver_choice == 'on_the_edge_of_the_costal_arch':
            self.make(f"{PatientCardLocators.LIVER_CM}.val('2');")
        if liver_choice == 'another':
            self.make(f"{PatientCardLocators.LIVER_DESCRIPTION}.val('опухший');")
        spleen_choice = random.choice(['not_palpable', 'increased_from_under_the_edge', 'deleted', 'another'])
        self.make(f"{PatientCardLocators.SPLEEN}.dropdown('set selected', '{spleen_choice}');")
        if spleen_choice == 'increased_from_under_the_edge':
            self.make(f"{PatientCardLocators.SPLEEN_CM}.val('1,5');")
        if spleen_choice == 'another':
            self.make(f"{PatientCardLocators.SPLEEN_DESCRIPTION}.val('пупырчатый');")
        sym_choice = random.choice(['negative', 'positive', 'two_side', 'left', 'right'])
        self.make(f"{PatientCardLocators.SYMPTOMS_OF_BANGING}.dropdown('set selected', '{sym_choice}');")
        stool_choice = random.choice(['decorated', 'liquid', 'without_pathological_impurities', 'blood', 'slime',
                                     'ordinary_paint', 'green', 'acholic', 'another'])
        self.make(f"{PatientCardLocators.STOOL}.dropdown('set selected', '{stool_choice}');")
        self.make(f"{PatientCardLocators.STOOL_MULTIPLICITY}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.URINATION_FREE}.click();")
        self.make(f"{PatientCardLocators.URINATION_PAINLESS}.click();")
        self.make(f"{PatientCardLocators.URINATION_PAINFUL}.click();")
        diuresis_choice = random.choice(['breached', 'frequent', 'norm'])
        if diuresis_choice == "frequent":
            self.make(f"{PatientCardLocators.DIURESIS_FREQUENT}.click();")
        if diuresis_choice == "norm":
            self.make(f"{PatientCardLocators.DIURESIS_NORM}.click();")
        else:
            self.make(f"{PatientCardLocators.DIURESIS_BREACHED}.click();")
            self.make(f"{PatientCardLocators.DIURESIS_BREACHED_DESCRIPTION}.val('что-то случилось');")
        self.make(f"{PatientCardLocators.SWELLING}.val('yes');")
        self.make(f"{PatientCardLocators.VISITS_DIAGNOSIS}.val('Болеет');")
        self.make(f"{PatientCardLocators.VISITS_NOTES}.val('{surname}');")
        self.make(f"{PatientCardLocators.PLANNED_SCREENING}.val('{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.VISITS_SAVE}.click();")
        self.browser.close()
        self.browser.switch_to.window(first_window)

    def check_visits_modal(self):
        self.make(f"{PatientCardLocators.VISITS_REFRESH}.click();")
        sleep(3)
        assert self.is_element_present(*PatientCardLocators.VISITS_EDIT), "Data in Visits modal weren't preserved or invalid selector for Edit button"

    def register_new_woman(self):
        # автозаполнение формы регистрации для взрослого
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        res_code_choice = random.choice(['45', '53', '1', '4'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        trans_choice = random.choice(['1', '2'])
        self.make(f"{RegisterPageLocators.TRANSGENDER}.dropdown('set selected', '{trans_choice}');")
        self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.PATIENT_IIN}.val('{woman_iin}')")
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.PATIENT_SURNAME}.val('{w_surname}')")
        self.make(f"{RegisterPageLocators.PATIENT_NAME}.val('{w_name}')")
        self.make(f"{RegisterPageLocators.PATIENT_MIDNAME}.val('{w_midname}')")
        self.make(f"{RegisterPageLocators.BIRTH_DATE}.calendar('set date', '{w_birthday}');")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{gen_choice}');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        if self.browser.find_element(By.CSS_SELECTOR, 'div[data-field=general_data_adm_obl_viyav] input').get_attribute("value") == "33":
            pass
        else:
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        soc_status_choice = random.choice(['3', '4'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{RegisterPageLocators.RESID_AREA}.dropdown('set selected', '3');")
        sleep(3)
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('hide');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_LOCALITY}.dropdown('set selected', '170000000008');")
        self.make(f"{RegisterPageLocators.RESID_PLACE}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.REGIS_STREET}.val('{street_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_HOUSE}.val('{55}');")
        self.make(f"{RegisterPageLocators.REGIS_APT}.val('{44}');")
        self.make(f"{RegisterPageLocators.REGIS_PHONE_NO}.val('{87273456987}');")
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '80000000546');")
        self.make(f"{RegisterPageLocators.DUPLICATE_RESID_ADR}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click()")
        allure.attach(self.browser.get_screenshot_as_png(), name="register_new_child",
                      attachment_type=AttachmentType.PNG)
        sleep(5)
        global patient_id_woman
        patient_id_woman = self.get_patient_id()
        print(f"ID of woman patient is {patient_id_woman}")

    def register_new_homeless(self):
        # автозаполнение формы регистрации для бомжа
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        res_code_choice = random.choice(['1', '3', '59', '49'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        self.make(f"{RegisterPageLocators.PATIENT_IIN}.val('{homeless_iin}')")
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.PATIENT_SURNAME}.val('{h_surname}')")
        self.make(f"{RegisterPageLocators.PATIENT_NAME}.val('{h_name}')")
        self.make(f"{RegisterPageLocators.PATIENT_MIDNAME}.val('{h_midname}')")
        self.make(f"{RegisterPageLocators.BIRTH_DATE}.calendar('set date', '{h_birthday}');")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{gen_choice}');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        if self.browser.find_element(By.CSS_SELECTOR, 'div[data-field=general_data_adm_obl_viyav] input').get_attribute("value") == "33":
            pass
        else:
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        soc_status_choice = random.choice(['4', '8'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{RegisterPageLocators.HOMELESS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click();")
        # allure.attach(self.browser.get_screenshot_as_png(), name="register_new_child", attachment_type=AttachmentType.PNG)
        sleep(5)
        global patient_id_homeless
        patient_id_homeless = self.get_patient_id()
        print(f"ID of homeless patient is {patient_id_homeless}")

    def register_new_foreigner(self):
        # автозаполнение формы регистрации для иностранного гражданина
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        res_code_choice = random.choice(['47', '48', '11', '22'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        self.make(f"{RegisterPageLocators.PATIENT_IIN}.val('{foreigner_iin}')")
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.PATIENT_SURNAME}.val('{f_surname}')")
        self.make(f"{RegisterPageLocators.PATIENT_NAME}.val('{f_name}')")
        self.make(f"{RegisterPageLocators.PATIENT_MIDNAME}.val('{f_midname}')")
        self.make(f"{RegisterPageLocators.BIRTH_DATE}.calendar('set date', '{f_birthday}');")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{gen_choice}');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        if self.browser.find_element(By.CSS_SELECTOR, 'div[data-field=general_data_adm_obl_viyav] input').get_attribute("value") == "33":
            pass
        else:
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
            sleep(2)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
            sleep(1)
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '2');")
        soc_status_choice = random.choice(['3', '4'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{mo_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_AREA}.dropdown('set selected', '5');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('hide');")
        # self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_LOCALITY}.dropdown('set selected', '177');")
        self.make(f"{RegisterPageLocators.REGIS_PLACE}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.REGIS_STREET}.val('{street_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_HOUSE}.val('{55}');")
        self.make(f"{RegisterPageLocators.REGIS_APT}.val('{44}');")
        self.make(f"{RegisterPageLocators.REGIS_PHONE_NO}.val('{87273456987}');")
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '170000000558');")
        self.make(f"{RegisterPageLocators.DUPLICATE_REGIS_ADR}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click();")
        # allure.attach(self.browser.get_screenshot_as_png(), name="register_new_child", attachment_type=AttachmentType.PNG)
        sleep(5)
        global patient_id_foreigner
        patient_id_foreigner = self.get_patient_id()
        print(f"ID of foreign patient is {patient_id_foreigner}")


    #     self.browser.find_element(*PatientCardLocators.OPEN_PATIENT_CARD).click()
    #     self.browser.find_element(*PatientCardLocators.TARIFIKATOR).click()
    #     self.browser.find_element(*PatientCardLocators.OPEN_PATIENT_CARD).click()
    #     self.browser.find_element(*PatientCardLocators.PRINT).click()
    #     self.browser.find_element(*PatientCardLocators.OPEN_PATIENT_CARD).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_EMAIL).click()
    #     self.browser.find_element(*PatientCardLocators.PHONE_NUMBER).send_keys("87001592322")
    #     self.browser.find_element(*PatientCardLocators.EMAIL).send_keys("ivanov@mail.ru")
    #     self.browser.find_element(*PatientCardLocators.SMS_D_SEARCH).click()
    #     self.browser.find_element(*PatientCardLocators.EMAIL_D_SEARCH).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_ART).click()
    #     self.browser.find_element(*PatientCardLocators.EMAIL_ART).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_FLG).click()
    #     self.browser.find_element(*PatientCardLocators.EMAIL_FLG).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_CD4).click()
    #     self.browser.find_element(*PatientCardLocators.EMAIL_CD4).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_VN).click()
    #     self.browser.find_element(*PatientCardLocators.EMAIL_VN).click()
    #     self.browser.find_element(*PatientCardLocators.SMS_EMAIL_SAVE).click()

