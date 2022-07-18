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
        self.make(f"{RegisterPageLocators.REGIS_LOCALITY}.dropdown('set selected', '290000000002');")
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
        self.make(f"{RegisterPageLocators.RESID_LOCALITY}.dropdown('set selected', '290000000004');")
        self.make(f"{RegisterPageLocators.RESID_PLACE}.dropdown('set selected', '2');")
        self.make(f"{RegisterPageLocators.RESID_STREET}.val('{street_choice}');")
        self.make(f"{RegisterPageLocators.RESID_HOUSE}.val('25');")
        self.make(f"{RegisterPageLocators.RESID_APT}.val('45');")
        self.make(f"{RegisterPageLocators.RESID_PHONE_NO}.val('87273456789');")
        # self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '280000000448');")
        self.make(f"{RegisterPageLocators.RETROSPECTIVE_CHILD}.click();")
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

    def fill_mothers_data(self):
        self.make(f"{RegisterPageLocators.GENERAL_DATA}.click()")  # Открываем Общие данные
        sleep(2)
        element = self.browser.find_element(By.ID, "find_sources_general_data")
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # self.make(f"{RegisterPageLocators.SEARCH}).click()")
        sleep(2)
        self.make(f"{RegisterPageLocators.MOTHERS_IB_NO_SEARCH}.val('94100');")
        sleep(5)
        self.make(f"{RegisterPageLocators.FIND}.click()")
        sleep(3)
        self.make(f"{RegisterPageLocators.CHOOSE_MOTHER_ID}.click()")
        sleep(2)
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click()")
        sleep(5)

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
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_GENDER}.dropdown('get value')") == gen_choice, "Patient's gender object doesn't take a value"

    def check_emergence_area(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.EMERGENCE_AREA}.length"), "Patient's emergence area object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.EMERGENCE_AREA}.dropdown('get value')") == '3', "Patient's emergence area object doesn't take a value"

    def check_patient_citizenship(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.length"), "Patient's citizenship object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('get value')") == '1', "Patient's citizenship object doesn't take a value"

    def check_child_status(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.CHILD_STATUS}.length"), "Child status object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.CHILD_STATUS}.dropdown('get value')") == child_status_choice, "Child status object doesn't take a value"

    def check_social_status(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.SOCIAL_STATUS}.length"), "Patient's region of living object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.SOCIAL_STATUS}.dropdown('get value')") == soc_status_choice, "Patient's region of living object doesn't take a value"

    def check_registration_medical_organization(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.length"), "Social status object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.dropdown('get value')") == 'mo_choice', "Social status object doesn't take a value"

    def check_edit_button_registration_address_modal(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.EDIT_REGIS_ADDRESS}.length"), "Edit button in Registration address modal is not accessible"
        self.make(f"{RegisterPageLocators.EDIT_REGIS_ADDRESS}.click();")

    def check_registration_area(self):
        sleep(2)
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_region_name_modal] .ui.dropdown').length"), "Patient's registration area object is not accessible"
        a = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_region_name_modal] .ui.dropdown input[type=hidden]').val()")
        print(a)
        assert a == '5', "Patient's registration area object doesn't take a value"

    def check_registration_unit_area(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_unit_area_modal] .ui.dropdown').length"), "Patient's registration unit area object is not accessible"
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_unit_area_modal] .ui.dropdown').dropdown('get value')") == '180', "Patient's registration unit area object doesn't take a value"

    def check_registration_locality(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_locality_name_modal] .ui.dropdown').length"), "Patient's registration locality object is not accessible"
        n = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_locality_name_modal] .ui.dropdown').dropdown('get value')")
        assert n == '290000000002', "Patient's registration locality object doesn't take a value"

    def check_registration_place(self):
        assert self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_place_live_modal] .ui.dropdown').length"), "Patient's registration place object is not accessible"
        o = self.browser.execute_script(f"return $('#modal_registration_address div[data-field=registration_address_place_live_modal] .ui.dropdown').dropdown('get value')")
        assert o == '2', "Patient's registration place object doesn't take a value"

    def check_registration_street(self):
        sleep(1)
        assert self.browser.execute_script(f"return $('#registration_address_street_modal').length"), "Patient's registration street object is not accessible"
        assert self.browser.execute_script(f"return $('#registration_address_street_modal').val()") == street_choice, "Patient's registration street object doesn't take a value"

    def check_registration_house(self):
        assert self.browser.execute_script(f"return $('#registration_address_house_modal').length"), "Patient's registration house object is not accessible"
        q = self.browser.execute_script(f"return $('#registration_address_house_modal').val()")
        assert q == '55', "Patient's registration house object doesn't take a value"

    def check_registration_apartment(self):
        assert self.browser.execute_script(f"return $('#registration_address_kvart_modal').length"), "Patient's registration apartment object is not accessible"
        r = self.browser.execute_script(f"return $('#registration_address_kvart_modal').val()")
        assert r == '44', "Patient's registration apartment object doesn't take a value"

    def check_registration_phone_number(self):
        assert self.browser.execute_script(f"return $('#registration_address_telephone_modal').length"), "Patient's registration phone number object is not accessible"
        s = self.browser.execute_script(f"return $('#registration_address_telephone_modal').val()")
        assert s == '87273456987', "Patient's registration phone number object doesn't take a value"

    def check_cancel_button_registration_address_modal(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.CANCEL_REGIS_ADDRESS}.length"), "Cancel button in Registration address modal is not accessible"
        self.make(f"{RegisterPageLocators.CANCEL_REGIS_ADDRESS}.click();")

    def check_edit_button_residence_address_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {RegisterPageLocators.EDIT_RESID_ADDRESS}.length"), "Edit button in Residence address modal is not accessible"
        self.make(f"{RegisterPageLocators.EDIT_RESID_ADDRESS}.click();")

    def check_residence_area(self):
        sleep(2)
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_region_name_modal] .ui.dropdown').length"), "Patient's residence area object is not accessible"
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_region_name_modal] .ui.dropdown').dropdown('get value')") == '3', "Patient's residence area object doesn't take a value"

    def check_residence_unit_area(self):
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_unit_area_modal] .ui.dropdown').length"), "Patient's residence unit area object is not accessible"
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_unit_area_modal] .ui.dropdown').dropdown('get value')") == '33', "Patient's residence unit area object doesn't take a value"

    def check_residence_locality(self):
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_locality_name_modal] .ui.dropdown').length"), "Patient's residence locality object is not accessible"
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_locality_name_modal] .ui.dropdown').dropdown('get value')") == '290000000004', "Patient's residence locality object doesn't take a value"

    def check_residence_place(self):
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_place_live_modal] .ui.dropdown').length"), "Patient's residence place object is not accessible"
        assert self.browser.execute_script(f"return $('#modal_fact_address div[data-field=fact_address_place_live_modal] .ui.dropdown').dropdown('get value')") == '2', "Patient's residence place object doesn't take a value"

    def check_residence_street(self):
        assert self.browser.execute_script(f"return $('#fact_address_street_modal').length"), "Patient's residence street object is not accessible"
        assert self.browser.execute_script(f"return $('#fact_address_street_modal').val()") == street_choice, "Patient's residence street object doesn't take a value"

    def check_residence_house(self):
        assert self.browser.execute_script(f"return $('#fact_address_hous_modal').length"), "Patient's residence house object is not accessible"
        assert self.browser.execute_script(f"return $('#fact_address_hous_modal').val()") == '25', "Patient's residence house object doesn't take a value"

    def check_residence_apartment(self):
        assert self.browser.execute_script(f"return $('#fact_address_flat_modal').length"), "Patient's residence apartment object is not accessible"
        assert self.browser.execute_script(f"return $('#fact_address_flat_modal').val()") == '45', "Patient's residence apartment object doesn't take a value"

    def check_residence_phone_number(self):
        assert self.browser.execute_script(f"return $('#fact_address_flat_modal').length"), "Patient's residence phone number object is not accessible"
        assert self.browser.execute_script(f"return $('#fact_address_flat_modal').val()") == '87273456789', "Patient's residence phone number object doesn't take a value"

    def check_residence_medical_organization(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.length"), "Residence medical organization object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MED_ORG}.dropdown('get value')") == '170000000558', "Residence medical organization object doesn't take a value"

    def check_cancel_button_residence_address_modal(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.CANCEL_RESID_ADDRESS}.length"), "Edit button in Residence address modal is not accessible"
        self.make(f"{RegisterPageLocators.CANCEL_RESID_ADDRESS}.click();")

    def check_retrospective_child_checkbox(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.RETROSPECTIVE_CHILD}.length"), "Retrospective child checkbox object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.RETROSPECTIVE_CHILD}.is(':checked')"), "Retrospective child checkbox object doesn't take a value"


        # assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.length"), "Mother's surname object is not accessible"
        # assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.find('input').val('100014')") , "Mother's surname object doesn't take a value"

    def check_surname_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.length"), "Mother's surname object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_SURNAME}.val()") == 'BFNAGB', "Mother's surname object doesn't take a value"

    def check_name_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_NAME}.length"), "Mother's name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_NAME}.val()") == 'PQYMOLXQP', "Mother's name object doesn't take a value"

    def check_midname_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_MIDNAME}.length"), "Mother's middle name object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_MIDNAME}.val()") == 'VNBZIIZZB', "Mother's middle name object doesn't take a value"

    def check_ib_number_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO}.length"), "Mother's ib number object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO}.val()") == '94100(1)', "Mother's ib number object doesn't take a value"

    def check_ib_number_date_of_mother(self):
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO_DATE}.length"), "Mother's ib number date object is not accessible"
        assert self.browser.execute_script(f"return {RegisterPageLocators.MOTHERS_IB_NO_DATE}.val()") == '12.05.2022', "Mother's ib number date object doesn't take a value"

    def fill_hiv_antibody_testing_ogc_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
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
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_OGC_EDIT}.length"), "Edit button in HIV antibody testing OGC modal is not accessible"
        self.make(f"{PatientCardLocators.IFA_OGC_EDIT}.click();")

    def check_medical_organization_hiv_ogc_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_MED_ORG}.length"), "Medical organization in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_MED_ORG}.dropdown('get value')") == mo_choice, "Medical organization object in HIV antibody testing OGC modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM}.dropdown('get value')") == serum_num_choice, "Serum number in HIV antibody testing OGC modal doesn't take a value"

    def check_serum_number2_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM2}.length"), "Serum number 2 in HIV antibody testing OGC modal is not accessible"
        sn2 = self.browser.execute_script(f"return {PatientCardLocators.SERUM_NUM2}.val()")
        print(sn2)
        assert sn2 == numbers5, "Serum number 2 in HIV antibody testing OGC modal doesn't take a value"

    def check_test_system_type_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_TYPE}.length"), "Test system type in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_TYPE}.dropdown('get value')") == test_sys_choice, "Test system type in HIV antibody testing OGC modal doesn't take a value"

    def check_expiration_date_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE}.length"), "Expiration date in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE}.val()") == expiration_date, "Expiration date in HIV antibody testing OGC modal doesn't take a value"

    def check_series_number_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM}.length"), "Series number in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM}.val()") == numbers3, "Series number in HIV antibody testing OGC modal doesn't take a value"

    def check_test_category_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_CATEGORY}.length"), "Test category in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_CATEGORY}.dropdown('get value')") == test_cat_choice, "Test category in HIV antibody testing OGC modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT}.dropdown('get value')") == ifa_res_choice, "Result object in HIV antibody testing OGC modal doesn't take a value"

    def check_responsible_person_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RESPONSIBLE_PERSON}.length"), "Responsible_person in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RESPONSIBLE_PERSON}.dropdown('get value')") == ifa_resp_person_choice, "Responsible person in HIV antibody testing OGC modal doesn't take a value"

    def check_services_hiv_ogc_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_SERVICES}.length"), "The Services object in HIV antibody testing OGC modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_SERVICES}.dropdown('get value')") == ifa_services_choice, "The Services object in HIV antibody testing OGC modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREANING_NUM}.dropdown('get value')") == numbers5, "The Screening number object in HIV antibody testing KNCDIZ modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME_RC}.dropdown('get value')") == test_sys_choice, "Test system type in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_expiration_date_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE_RC}.length"), "Expiration date in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EXPIRATION_DATE_RC}.val()") == expiration_date, "Expiration date in HIV antibody testing KNCDIZ modal doesn't take a value"

    def check_series_number_hiv_kncdiz_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM_RC}.length"), "Series number in HIV antibody testing KNCDIZ modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SERIES_NUM_RC}.val()") == numbers3, "Series number in HIV antibody testing KNCDIZ modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.IFA_RESULT_RC}.dropdown('get value')") == two_choice, "Result object in HIV antibody testing OGC modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.SAMPLE_NUM}.val()") == numbers3, "The Sample number object in IB modal doesn't take a value"

    def check_receipt_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RECEIPT_DATE}.length"), "The IB Receipt date object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RECEIPT_DATE}.val()") == today, "The IB Receipt date object in IB modal doesn't take a value"

    def check_register_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_REGISTER_DATE}.length"), "The IB Register date object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_REGISTER_DATE}.val()") == today, "The IB Register date object in IB modal doesn't take a value"

    def check_result_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESULT}.length"), "The Result object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESULT}.dropdown('get value')") == '1', "The Result object in IB modal doesn't take a value"

    def check_test_system_name_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME}.length"), "The Test system name object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TEST_SYSTEM_NAME}.dropdown('get value')") == test_name_choice, "The Test system name object in IB modal doesn't take a value"

    def check_expiration_date_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_EXPIRATION_DATE}.length"), "Expiration date in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_EXPIRATION_DATE}.val()") == expiration_date, "Expiration date in IB modal doesn't take a value"

    def check_series_number_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERIES_NUM}.length"), "Series number in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERIES_NUM}.val()") == numbers3, "Series number in IB modal doesn't take a value"

    def check_responsible_person_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESPONSIBLE_PERSON}.length"), "The Responsible_person object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_RESPONSIBLE_PERSON}.dropdown('get value')") == respon_person_choice, "the Responsible person object in IB modal doesn't take a value"

    def check_gp160_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP160}.length"), "The GP160 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.GP160}.dropdown('get value')") == gp160, "The GP160 object in IB modal doesn't take a value"

    def check_gp110_120_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP110_120}.length"), "The GP110_120 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.GP110_120}.dropdown('get value')") == gp110_120, "The GP110_120 object in IB modal doesn't take a value"

    def check_p68_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P68}.length"), "The P68 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P68}.dropdown('get value')") == p68, "The P68 object in IB modal doesn't take a value"

    def check_p55_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P55}.length"), "The P55 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P55}.dropdown('get value')") == p55, "The P55 object in IB modal doesn't take a value"

    def check_p52_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P52}.length"), "The P52 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P52}.dropdown('get value')") == p52, "The P52 object in IB modal doesn't take a value"

    def check_gp41_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.GP41}.length"), "The GP41 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.GP41}.dropdown('get value')") == gp41, "The GP41 object in IB modal doesn't take a value"

    def check_p40_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P40}.length"), "The P40 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P40}.fdropdown('get value')") == p40, "The P40 object in IB modal doesn't take a value"

    def check_p34_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P34}.length"), "The P34 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P34}.dropdown('get value')") == p34, "The P34 object in IB modal doesn't take a value"

    def check_p25_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P25}.length"), "The P25 objectin IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P25}.dropdown('get value')") == p25, "The P25 object in IB modal doesn't take a value"

    def check_p18_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.P18}.length"), "The P18 object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.P18}.dropdown('get value')") == p18, "The P18 object in IB modal doesn't take a value"

    def check_services_ib_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERVICES}.length"), "The Services object in IB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IB_SERVICES}.val()") == '234', "The Services object in IB modal doesn't take a value"

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

    def fill_family_members_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.EPID_HISTORY_HIV_ANALYSIS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_ANALYSIS_YEAR}.dropdown('set selected', '2021');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_ANALYSIS_RESULT}.dropdown('set selected', '2');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_FILLING_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.EPID_DOCTOR}.dropdown('set selected', '{epid_doc_choice}');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_ADD}.click()")
        self.make(f"{PatientCardLocators.FAMILY_MEM_LASTNAME}.val('{surname}')")
        self.make(f"{PatientCardLocators.FAMILY_MEM_NAME}.val('{name}')")
        self.make(f"{PatientCardLocators.FAMILY_MEM_MIDDLE_NAME}.val('{midname}')")
        self.make(f"{PatientCardLocators.FAMILY_MEM_GENDER}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_BIRTHDAY}.val('{birthday}')")
        self.make(f"{PatientCardLocators.FAMILY_MEM_ADDRESS}.val('{street_choice}')")
        self.make(f"{PatientCardLocators.FAMILY_MEM_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_RELATION}.dropdown('set selected', '{fam_mem_rel_choice}');")

    def check_save_button_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_SAVE}.length"), "Save button in Family members modal is not accessible"
        self.make(f"{PatientCardLocators.FAMILY_MEM_SAVE}.click();")

    def check_add_button_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_ADD}.length"), "Add button in Family members modal is not accessible"

    def check_edit_button_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_EDIT}.length"), "Edit button in Family members modal is not accessible"
        self.make(f"{PatientCardLocators.FAMILY_MEM_EDIT}.click();")

    def check_surname_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_LASTNAME}.length"), "The Surname object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_LASTNAME}.val()") == surname, "The Surname object in Family members modal doesn't take a value"

    def check_name_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_NAME}.length"), "The Name object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_NAME}.val()") == name, "The Name object in Family members modal doesn't take a value"

    def check_middle_name_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_MIDDLE_NAME}.length"), "The Middle name object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_MIDDLE_NAME}.val()") == midname, "The Middle name object in Family members modal doesn't take a value"

    def check_gender_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_GENDER}.length"), "The Gender object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_GENDER}.find('input').val()") == two_choice, "The Gender object in Family members modal doesn't take a value"

    def check_birthday_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_BIRTHDAY}.length"), "The Birthday object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_BIRTHDAY}.val()") == birthday, "The Birthday object in Family members modal doesn't take a value"

    def check_street_choice_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_ADDRESS}.length"), "The Address object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_ADDRESS}.find('input').val()") == street_choice, "The Address object in Family members modal doesn't take a value"

    def check_hiv_status_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_HIV_STATUS}.length"), "The HIV status object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_HIV_STATUS}.find('input').val()") == hiv_status_choice, "The HIV status object in Family members modal doesn't take a value"

    def check_family_connection_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_RELATION}.length"), "The Family connection object in Family members modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_RELATION}.find('input').val()") == fam_mem_rel_choice, "The Family connection object in Family members modal doesn't take a value"

    def check_cancel_button_family_members_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FAMILY_MEM_CANCEL}.length"), "Cancel button in Family members modal is not accessible"
        self.make(f"{PatientCardLocators.FAMILY_MEM_CANCEL}.click();")

    def fill_luin_tab(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.LUIN_RS}.click();")
        self.make(f"{PatientCardLocators.DRUG_EXPERIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_IN_TWELVE_MONTH}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_YEARS}.val('{years_choice}');")
        self.make(f"{PatientCardLocators.DRUG_USE_MONTH}.val('{month_choice}');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJECTION}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_HIV}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_SEXUAL_PARTNER}.click()")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_PERMANENT_GROUP}.click()")
        self.make(f"{PatientCardLocators.SHARING_DRUG_INJ_WITH_RANDOM_GROUP}.click()")
        self.make(f"{PatientCardLocators.HERAIN}.click()")
        self.make(f"{PatientCardLocators.HANKA}.click()")
        self.make(f"{PatientCardLocators.MAK}.click()")
        self.make(f"{PatientCardLocators.AMPHETAMIN}.click()")
        self.make(f"{PatientCardLocators.SINTETHICS}.click()")
        self.make(f"{PatientCardLocators.OTHER_DRUGS}.click()")
        self.make(f"{PatientCardLocators.ACCOUNTED_IN_NARCO_DISP}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ACCOUNTED_IN_POLICE_FILES}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_YEARS}.val('{years_choice}');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_MONTH}.val('{month_choice}');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_PARTNER_NUM}.val('{com_sex_partners_choice}');")
        self.make(f"{PatientCardLocators.CONDOM_USAGE}.dropdown('set selected', '1');")

    def check_save_button_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LUIN_RS_SAVE}.length"), "Save button in LUIN/SW tab is not accessible"
        self.make(f"{PatientCardLocators.LUIN_RS_SAVE}.click();")

    def check_experience_injection_drug_use_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_EXPERIENCE}.length"), "The Experience injection drug use object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_EXPERIENCE}.find('input').val()") == '1', "The Experience injection drug use object in LUIN/SW tab doesn't take a value"

    def check_drug_usage_in_twelve_month_with_police_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_IN_TWELVE_MONTH}.length"), "The Experience injection drug use in twelve month object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_IN_TWELVE_MONTH}.find('input').val()") == '1', "The Experience injection drug use in twelve month object in LUIN/SW tab doesn't take a value"

    def check_drug_use_years_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_YEARS}.length"), "The Drug use year object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_YEARS}.val()") == years_choice, "The Drug use year object in LUIN/SW  tab doesn't take a value"

    def check_drug_use_month_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_MONTH}.length"), "The Drug use month object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DRUG_USE_MONTH}.val()") == month_choice, "The Drug use month object in LUIN/SW  tab doesn't take a value"

    def check_sharing_drug_injection_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJECTION}.length"), "The Registered in narcological dispensary object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJECTION}.find('input').val()") == '1', "The Registered in narcological dispensary object in LUIN/SW tab doesn't take a value"

    def check_sharing_drug_injection_with_hiv_positiv_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_HIV}.length"), "The Sharing drug injection with HIV positiv object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_HIV}.find('input').val()") == '1', "The Sharing drug injection with HIV positiv object in LUIN/SW tab doesn't take a value"

    def check_sharing_drug_injection_with_sexual_partner_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_SEXUAL_PARTNER}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_SEXUAL_PARTNER}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_sharing_drug_injection_with_permanent_group_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_PERMANENT_GROUP}.length"), "The Sharing drug injection with permanent group checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_PERMANENT_GROUP}.is(':checked')"), "The Sharing drug injection with permanent group checkbox in LUIN/SW tab is not ticked"

    def check_sharing_drug_injection_with_random_group_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_RANDOM_GROUP}.length"), "The Sharing drug injection with random group checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SHARING_DRUG_INJ_WITH_RANDOM_GROUP}.is(':checked')"), "The Sharing drug injection with random group checkbox in LUIN/SW tab is not ticked"

    def check_heroin_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HERAIN}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HERAIN}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_hanka_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HANKA}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HANKA}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_mak_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MAK}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MAK}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_amphetamin_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.AMPHETAMIN}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.AMPHETAMIN}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_sintethics_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SINTETHICS}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SINTETHICS}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_other_drugs_checkbox_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OTHER_DRUGS}.length"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OTHER_DRUGS}.is(':checked')"), "The Sharing drug injection with sex partner checkbox in LUIN/SW tab is not ticked"

    def check_registered_in_narcological_dispensary_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ACCOUNTED_IN_NARCO_DISP}.length"), "The Registered in narcological dispensary object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ACCOUNTED_IN_NARCO_DISP}.find('input').val()") == '1', "The Registered in narcological dispensary object in LUIN/SW tab doesn't take a value"

    def check_registered_with_police_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ACCOUNTED_IN_POLICE_FILES}.length"), "The Registered with police object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ACCOUNTED_IN_POLICE_FILES}.find('input').val()") == '1', "The Registered with police object in LUIN/SW tab doesn't take a value"

    def check_commercial_sex_experience_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP}.length"), "The Condom usage object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP}.find('input').val()") == '1', "The Condom usage object in LUIN/SW tab doesn't take a value"

    def check_commercial_sex_experience_year_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP_YEARS}.length"), "The Commercial sex experience year object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP_YEARS}.val()") == years_choice, "The Commercial sex experience year object in LUIN/SW  tab doesn't take a value"

    def check_commercial_sex_experience_month_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP_MONTH}.length"), "The Commercial sex experience month object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_EXP_MONTH}.val()") == month_choice, "The Commercial sex experience month object in LUIN/SW  tab doesn't take a value"

    def check_number_of_sex_partners_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_PARTNER_NUM}.length"), "The Number of sex partners object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_SEX_PARTNER_NUM}.val()") == com_sex_partners_choice, "The Number of sex partners object in LUIN/SW  tab doesn't take a value"

    def check_condom_use_luin_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONDOM_USAGE}.length"), "The Condom usage object in LUIN/SW  tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONDOM_USAGE}.find('input').val()") == '1', "The Condom usage object in LUIN/SW tab doesn't take a value"

    def fill_sexual_contacts_tab(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.SEXUAL_CONTACTS}.click();")
        self.make(f"{PatientCardLocators.HOMO_EXPIRIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_EXP_YEAR}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.HOMO_SEX_PARTNER_NUM}.val('{homo_sex_partners_choice}');")
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

    def check_save_button_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SEXUAL_CONTACTS_SAVE}.length"), "Save button in Sexual contacts tab is not accessible"
        self.make(f"{PatientCardLocators.SEXUAL_CONTACTS_SAVE}.click();")

    def check_homosexual_experience_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_EXPIRIENCE}.length"), "The Homosexual experience object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_EXPIRIENCE}.dropdown('get value')") == '1', "The Homosexual experience object in Sexual contacts tab doesn't take a value"

    def check_homosexual_contacts_existence_last_12month_dispensary_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_EXP_YEAR}.length"), "The Homosexual contacts existence last 12 month  object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_EXP_YEAR}.dropdown('get value')") == '1', "The Homosexual contacts existence last 12 month  object in Sexual contacts tab doesn't take a value"

    def check_homosexual_partners_number_during_life_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_PARTNER_NUM}.length"), "The Homosexual partners number during life object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_PARTNER_NUM}.val()") == homo_sex_partners_choice, "The Homosexual partners number during life object in Sexual contacts tab doesn't take a value"

    def check_homosexual_partners_number_last_12month_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_PARTNER_NUM_YEAR}.length"), "The Homosexual partners number last 12 month object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_PARTNER_NUM_YEAR}.val()") == sex_partners_year_choice, "The Homosexual partners number last 12 month object in Sexual contacts tab doesn't take a value"

    def check_commercial_homosexual_contacts_last_12month_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNER_YEAR}.length"), "The Commercial homosexual contacts last 12 month object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNER_YEAR}.dropdown('get value')") == '1', "The Commercial homosexual contacts last 12 month object in Sexual contacts tab doesn't take a value"

    def check_homosexual_contact_with_hiv_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_WITH_HIV}.length"), "The Homosexual contact with HIV object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_WITH_HIV}.dropdown('get value')") == '1', "The Homosexual contact with HIV object in Sexual contacts tab doesn't take a value"

    def check_homosexual_contact_with_luin_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_WITH_LUIN}.length"), "The Homosexual contact with LUIN object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_SEX_WITH_LUIN}.dropdown('get value')") == '1', "The Homosexual contact with LUIN object in Sexual contacts tab doesn't take a value"

    def check_permanent_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS}.length"), "The Permanent homosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS}.is(':checked')"), "The Permanent homosexual partners during life checkbox in Sexual contacts tab is not ticked"

    def check_random_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS}.length"), "The Random homosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS}.is(':checked')"), "The Random homosexual partners during life checkbox in Sexual contacts tab is not ticked"

    def check_commercial_homosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS}.length"), "The Commercial homosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS}.is(':checked')"), "The Commercial homosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_permanent_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS_YEAR}.length"), "The Permanent homosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_PERMANENT_SEX_PARTNERS_YEAR}.is(':checked')"), "The Permanent homosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_random_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS_YEAR}.length"), "The Random homosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOMO_RANDOM_SEX_PARTNERS_YEAR}.is(':checked')"), "The Random homosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_commercial_homosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS_YEAR}.length"), "The Commercial homosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HOMO_SEX_PARTNERS_YEAR}.is(':checked')"), "The Commercial homosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_heterosexual_experience_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HETERO_EXPIRIENCE}.length"), "The Heterosexual experience object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HETERO_EXPIRIENCE}.dropdown('get value')") == '1', "The Heterosexual experience object in Sexual contacts tab doesn't take a value"

    def check_commercial_heterosexual_contacts_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNER}.length"), "The Commercial heterosexual contacts  last 12 month  object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNER}.dropdown('get value')") == '1', "The Commercial heterosexual contacts  last 12 month  object in Sexual contacts tab doesn't take a value"

    def check_heterosexual_contact_with_hiv_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_WITH_HIV}.length"), "The Heterosexual contact with HIV object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_WITH_HIV}.dropdown('get value')") == '1', "The Heterosexual contact with HIV object in Sexual contacts tab doesn't take a value"

    def check_heterosexual_contact_with_luin_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_WITH_LUIN}.length"), "The Heterosexual contact with LUIN object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_WITH_LUIN}.dropdown('get value')") == '1', "The Heterosexual contact with LUIN object in Sexual contacts tab doesn't take a value"

    def check_heterosexual_experience_last_12month_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_EXP_YEAR}.length"), "The Heterosexual experience last 12 month object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_EXP_YEAR}.dropdown('get value')") == '1', "The Heterosexual experience last 12 month object in Sexual contacts tab doesn't take a value"

    def check_heterosexual_partners_number_last_12month_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_EXP_YEAR}.length"), "The Heterosexual partners number last 12 month object in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_SEX_EXP_YEAR}.dropdown('get value')") == '1', "The Heterosexual partners number last 12 month object in Sexual contacts tab doesn't take a value"

    def check_permanent_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_YEAR}.length"), "The Permanent heterosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_YEAR}.is(':checked')"), "The Permanent heterosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_random_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_RANDOM_SEX_PARTNERS_YEAR}.length"), "The Random heterosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_RANDOM_SEX_PARTNERS_YEAR}.is(':checked')"), "The Random heterosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_commercial_heterosexual_partners_last_12month_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_YEAR}.length"), "The Commercial heterosexual partners last 12 month checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_YEAR}.is(':checked')"), "The Commercial heterosexual partners last 12 month checkbox in Sexual contacts tab is not ticked"

    def check_permanent_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_LIVE}.length"), "The Permanent heterosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_PERMANENT_SEX_PARTNERS_LIVE}.is(':checked')"), "The Permanent heterosexual partners during life checkbox in Sexual contacts tab is not ticked"

    def check_random_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_RANDOM_SEX_PARTNERS_LIVE}.length"), "The Random heterosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HET_RANDOM_SEX_PARTNERS_LIVE}.is(':checked')"), "The Random heterosexual partners during life checkbox in Sexual contacts tab is not ticked"

    def check_commercial_heterosexual_partners_during_life_checkbox_sexual_contacts_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_LIVE}.length"), "The Commercial heterosexual partners during life checkbox in Sexual contacts tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.COMMERCIAL_HET_SEX_PARTNERS_LIVE}.is(':checked')"), "The Commercial heterosexual partners during life checkbox in Sexual contacts tab is not ticked"

    def fill_mls_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MLS}.click();")
        self.make(f"{PatientCardLocators.MLS_EXPERIENCE}.click();")
        self.make(f"{PatientCardLocators.MLS_ADD}.click();")
        sleep(3)
        self.make(f"{PatientCardLocators.MLS_NAME}.dropdown('set selected', '{deduction_choice}');")
        sleep(2)
        self.make(f"{PatientCardLocators.MLS_NAME}.dropdown('hide');")
        sleep(2)
        self.make(f"{PatientCardLocators.MLS_DATE_START}.val('01.01.2017');")
        self.make(f"{PatientCardLocators.MLS_DATE_END}.val('01.01.2020');")

    def check_save_button_mls_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_SAVE}.length"), "Save button in MLS modal is not accessible"
        self.make(f"{PatientCardLocators.MLS_SAVE}.click();")

    def check_mls_experience_checkbox_mls_tab(self):
        sleep(5)
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_EXPERIENCE}.length"), "MLS Experience checkbox in MLS modal is not accessible"
        assert self.make(f"{PatientCardLocators.MLS_EXPERIENCE}.is(':checked')"), "Edit button in MLS modal is not accessible"

    def check_add_button_mls_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_ADD}.length"), "Add button in MLS modal is not accessible"

    def check_edit_button_mls_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_EDIT}.length"), "Edit button in MLS modal is not accessible"
        self.make(f"{PatientCardLocators.MLS_EDIT}.click();")

    def check_mls_name_mls_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_NAME}.length"), "The MLS Name object in MLS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_NAME}.dropdown('get value')") == deduction_choice, "The MLS Name object in MLS modal doesn't take a value"

    def check_start_date_mls_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_DATE_START}.length"), "The Start date object in MLS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_DATE_START}.val()") == '01.01.2017', "The Start date object in MLS modal doesn't take a value"

    def check_end_date_mls_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_DATE_END}.length"), "The End date object in MLS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_DATE_END}.val()") == '01.01.2020', "The End date object in MLS modal doesn't take a value"

    def check_cancel_button_mls_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MLS_CANCEL}.length"), "Cancel button in MLS modal is not accessible"
        self.make(f"{PatientCardLocators.MLS_CANCEL}.click();")

    def fill_blood_donor_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DONOR}.click();")
        self.make(f"{PatientCardLocators.BLOOD_DONOR}.click();")
        self.make(f"{PatientCardLocators.DONATION_EXISTENCE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.BLOOD_DONOR_ADD}.click();")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_LOCALITY}.dropdown('set selected', '{locality_choice1}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_MED_ORG}.dropdown('set selected', '280000000228');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CATEGORY}.dropdown('set selected', '{blood_don_cat_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_TYPE}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_CODE}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS}.dropdown('set selected', '1');")

    def check_save_button_blood_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_SAVE}.length"), "Save button in Blood donor modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_DONOR_SAVE}.click();")

    def check_blood_donor_last_5years_checkbox_donor_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR}.length"), "The Blood donor in last 5 years checkbox in Donor tab is not accessible"
        assert self.make(f"{PatientCardLocators.BLOOD_DONOR}.is(':checked')"), "The Blood donor in last 5 years checkbox in Donor tab  is not ticked"

    def check_donation_existence_checkbox_donor_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DONATION_EXISTENCE}.length"), "The Donation existence upon detection checkbox in Donor tab is not accessible"
        assert self.make(f"{PatientCardLocators.DONATION_EXISTENCE}.is(':checked')"), "Blood donor checkbox in Donor tab is not ticked"

    def check_add_button_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_ADD}.length"), "Add button in Blood donor modal is not accessible"

    def check_edit_button_blood_donor_modal(self):
        sleep(5)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_EDIT}.length"), "Edit button in Blood donor modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_DONOR_EDIT}.click();")

    def check_donation_place_blood_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_PLACE}.length"), "The Donation place object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_PLACE}.find('input').val()") == '1', "The Donation place object in Blood donor modal doesn't take a value"

    def check_donation_area_blood_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_AREA}.length"), "The Donation area object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_AREA}.find('input').val()") == '3', "The Donation area object in Blood donor modal doesn't take a value"

    def check_donation_unit_area_blood_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_UNIT_AREA}.length"), "The Donation unit area object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_UNIT_AREA}.find('input').val()") == '33', "The Donation unit area object in Blood donor modal doesn't take a value"

    def check_locality_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_LOCALITY}.length"), "The Locality object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_LOCALITY}.find('input').val()") == locality_choice1, "The Locality object in Blood donor modal doesn't take a value"

    def check_donation_date_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_DATE}.length"), "The Donation date object in Blood donor  modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_DATE}.val()") == '01.01.2021', "The Donation date object in Blood donor  modal doesn't take a value"

    def check_medical_organization_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_MED_ORG}.length"), "The Medical organization object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_MED_ORG}.dropdown('get text')") == 'МЕД ЦЕНТР КЕНТАУ', "The Medical organization object in Blood donor modal doesn't take a value"

    def check_blood_donor_category_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CATEGORY}.length"), "The Blood donor category object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CATEGORY}.find('input').val()") == blood_don_cat_choice, "The Blood donor category object in Blood donor modal doesn't take a value"

    def check_donor_type_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_TYPE}.length"), "The Donor type object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_TYPE}.find('input').val()") == two_choice, "The Donor type object in Blood donor modal doesn't take a value"

    def check_donor_code_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CODE}.length"), "The Donor code object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CODE}.val()") == numbers3, "The Donor code object in Blood donor modal doesn't take a value"

    def check_donation_code_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_CODE}.length"), "The Donation code object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONATION_CODE}.val()") == numbers4, "The Donation code object in Blood donor modal doesn't take a value"

    def check_hiv_analysis_date_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_ANALYSIS_DATE}.length"), "The HIV analysis date object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_ANALYSIS_DATE}.val()") == '01.01.2021', "The HIV analysis object in Blood donor modal doesn't take a value"

    def check_hiv_status_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_STATUS}.length"), "The Donor type object in Blood donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_STATUS}.find('input').val()") == '1', "The Donor type object in Blood donor modal doesn't take a value"

    def check_cancel_button_blood_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CANCEL}.length"), "Cancel button in Blood donor modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CANCEL}.click();")

    def fill_organ_donor_modal(self):
        sleep(2)
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        # self.make(f"{PatientCardLocators.DONOR}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONOR}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_ADD}.click();")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_LOCALITY}.dropdown('set selected', '{locality_choice1}');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG}.dropdown('set selected', '280000000228');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_CATEGORY}.dropdown('set selected', '{organ_don_cat_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_TYPE}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE}.dropdown('set selected', '{organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_MED_ORG}.dropdown('set selected', '280000000228');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS}.dropdown('set selected', '1');")

    def check_save_button_organ_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_SAVE}.length"), "Save button in Organ donor modal is not accessible"
        self.make(f"{PatientCardLocators.ORGAN_DONOR_SAVE}.click();")

    def check_material_donor_last_5years_checkbox_donor_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR}.length"), "The Material donor in last 5 years checkbox in Donor tab is not accessible"
        assert self.make(f"{PatientCardLocators.ORGAN_DONOR}.is(':checked')"), "The Material donor in last 5 years checkbox in Donor tab  is not accessible"

    def check_add_button_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_ADD}.length"), "Add button in Organ donor modal is not accessible"

    def check_edit_button_organ_donor_modal(self):
        sleep(5)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_EDIT}.length"), "Edit button in Organ donor modal is not accessible"
        self.make(f"{PatientCardLocators.ORGAN_DONOR_EDIT}.click();")

    def check_donation_place_organ_donor_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_PLACE}.length"), "The Donation place object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_PLACE}.find('input').val()") == '1', "The Donation place object in Organ donor modal doesn't take a value"

    def check_donation_area_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_AREA}.length"), "The Donation area object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_AREA}.find('input').val()") == '3', "The Donation area object in Organ donor modal doesn't take a value"

    def check_donation_unit_area_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_UNIT_AREA}.length"), "The Donation unit area object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_UNIT_AREA}.find('input').val()") == '33', "The Donation unit area object in Organ donor modal doesn't take a value"

    def check_locality_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_LOCALITY}.length"), "The Locality object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_LOCALITY}.find('input').val()") == locality_choice1, "The Locality object in Organ donor modal doesn't take a value"

    def check_donation_date_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_DATE}.length"), "The Donation date object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_DATE}.val()") == '01.01.2021', "The Donation date object in Organ donor modal doesn't take a value"

    def check_medical_organization_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MED_ORG}.length"), "The Medical organization object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MED_ORG}.dropdown('get text')") == 'МЕД ЦЕНТР КЕНТАУ', "The Medical organization object in Organ donor modal doesn't take a value"

    def check_blood_donor_category_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_CATEGORY}.length"), "The Blood donor category object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONATION_CATEGORY}.find('input').val()") == organ_don_cat_choice, "The Blood donor category object in Organ donor modal doesn't take a value"

    def check_donor_type_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_TYPE}.length"), "The Donor type object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_TYPE}.find('input').val()") == two_choice, "The Donor type object in Organ donor modal doesn't take a value"

    def check_donor_material_type_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_TYPE}.length"), "The Donor material type object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_TYPE}.find('input').val()") == organ_mat_type_choice, "The Donor material type object in Organ donor modal doesn't take a value"

    def check_donor_material_number_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_NO}.length"), "The Donor material number object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_NO}.val()") == numbers3, "The Donor material number object in Organ donor modal doesn't take a value"

    def check_recipient_medical_organization_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECIPIENT_MED_ORG}.length"), "The HIV analysis date object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECIPIENT_MED_ORG}.dropdown('get text')") == 'МЕД ЦЕНТР КЕНТАУ', "The HIV analysis object in Organ donor modal doesn't take a value"

    def check_hiv_analysis_date_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_ANALYSIS_DATE}.length"), "The HIV analysis date object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_ANALYSIS_DATE}.val()") == '01.01.2021', "The HIV analysis object in Organ donor modal doesn't take a value"

    def check_hiv_status_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_STATUS}.length"), "The HIV Status object in Organ donor modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_STATUS}.find('input').val()") == '1', "The HIV Status object in Organ donor modal doesn't take a value"

    def check_cancel_button_organ_donor_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_CANCEL}.length"), "Cancel button in Organ donor modal is not accessible"
        self.make(f"{PatientCardLocators.ORGAN_DONOR_CANCEL}.click();")

    def fill_blood_recipient_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_LOCALITY}.dropdown('set selected', '{locality_choice1}');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_MED_ORG}.dropdown('set selected', '280000000028');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_NUM_REC}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE_REC}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_COMPONENT_CODE_REC}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS_REC}.dropdown('set selected', '1');")

    def check_save_button_blood_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECEIPT_SAVE}.length"), "Save button in Blood recipient modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_RECEIPT_SAVE}.click();")

    def check_blood_recipient_last_5years_checkbox_recipient_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECIPIENT}.length"), "The Blood recipient in last 5 years checkbox in Recipient tab is not accessible"
        assert self.make(f"{PatientCardLocators.BLOOD_RECIPIENT}.is(':checked')"), "The Blood recipient in last 5 years checkbox in Recipient tab  is not ticked"

    def check_add_button_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECIPIENT_ADD}.length"), "Add button in Blood recipient modal is not accessible"

    def check_edit_button_blood_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECEIPT_EDIT}.length"), "Edit button in Blood recipient modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_RECEIPT_EDIT}.click();")

    def check_transfusion_place_blood_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.TRANSFUSION_PLACE}.length"), "The Transfusion place object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TRANSFUSION_PLACE}.find('input').val()") == '1', "The Transfusion place recipient in Blood recipient modal doesn't take a value"

    def check_transfusion_area_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_AREA}.length"), "The Transfusion area object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_AREA}.find('input').val()") == '3', "The Transfusion area object in Blood recipient modal doesn't take a value"

    def check_transfusion_unit_area_blood_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_UNIT_AREA}.length"), "The Transfusion unit area object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_UNIT_AREA}.find('input').val()") == '33', "The Transfusion unit area object in Blood recipient modal doesn't take a value"

    def check_locality_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_LOCALITY}.length"), "The Transfusion locality object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_LOCALITY}.find('input').val()") == locality_choice1, "The Transfusion locality object in Blood recipient modal doesn't take a value"

    def check_transfusion_date_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_DATE}.length"), "The Transfusion date object in Blood recipient  modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_DATE}.val()") == '01.01.2021', "The Transfusion date object in Blood recipient  modal doesn't take a value"

    def check_medical_organization_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_MED_ORG}.length"), "The Medical organization object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_TRANSFUSION_MED_ORG}.dropdown('get text')") == 'ОЦ СПИД  ГТУРКЕСТАН', "The Medical organization object in Blood recipient modal doesn't take a value"

    def check_epid_history_number_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EPID_HISTORY_NUM_REC}.length"), "The Epidemiological history number object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EPID_HISTORY_NUM_REC}.val()") == numbers5, "The Epidemiological history number object in Blood recipient modal doesn't take a value"

    def check_donor_code_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CODE_REC}.length"), "The Donor code object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_DONOR_CODE_REC}.val()") == numbers3, "The Donor code object in Blood recipient modal doesn't take a value"

    def check_blood_component_code_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_COMPONENT_CODE_REC}.length"), "The Blood component code object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_COMPONENT_CODE_REC}.val()") == numbers4, "The Blood component code object in Blood recipient modal doesn't take a value"

    def check_hiv_status_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_STATUS_REC}.length"), "The HIV Status object in Blood recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_HIV_STATUS_REC}.find('input').val()") == '1', "The HIV Status object in Blood recipient modal doesn't take a value"

    def check_cancel_button_blood_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECIPIENT_CANCEL}.length"), "Cancel button in Blood recipient modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CANCEL}.click();")

    def fill_organ_recipient_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        # self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_LOCALITY}.dropdown('set selected', '{locality_choice1}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG_REC}.dropdown('set selected', '290000000074');")
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_MED_ORG}.dropdown('set selected', '280000000228');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO_REC}.val('{numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE_REC}.dropdown('set selected', '{organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_NAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS_REC}.dropdown('set selected', '1');")

    def check_save_button_organ_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECEIPT_SAVE}.length"), "Save button in Organ recipient modal is not accessible"
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_SAVE}.click();")

    def check_organ_recipient_last_5years_checkbox_recipient_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECIPIENT}.length"), "The Organ recipient in last 5 years checkbox in Recipient tab is not accessible"
        assert self.make(f"{PatientCardLocators.ORGAN_RECIPIENT}.is(':checked')"), "The Organ recipient in last 5 years checkbox in Recipient tab  is not ticked"

    def check_add_button_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECIPIENT_ADD}.length"), "Add button in Organ recipient modal is not accessible"

    def check_edit_button_organ_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECEIPT_EDIT}.length"), "Edit button in Organ recipient modal is not accessible"
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_EDIT}.click();")

    def check_transfusion_place_organ_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_PLACE}.length"), "The Transfusion place object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_PLACE}.find('input').val()") == '1', "The Transfusion place recipient in Organ recipient modal doesn't take a value"

    def check_transfusion_area_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_AREA}.length"), "The Transfusion area object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_AREA}.find('input').val()") == '3', "The Transfusion area object in Organ recipient modal doesn't take a value"

    def check_transfusion_unit_area_organ_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_UNIT_AREA}.length"), "The Transfusion unit area object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_UNIT_AREA}.find('input').val()") == '33', "The Transfusion unit area object in Organ recipient modal doesn't take a value"

    def check_locality_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_LOCALITY}.length"), "The Transfusion locality object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_LOCALITY}.find('input').val()") == locality_choice1, "The Transfusion locality object in Organ recipient modal doesn't take a value"

    def check_transfusion_date_organ_recipient_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_DATE}.length"), "The Transfusion date object in Organ recipient  modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_TRANSFUSION_DATE}.val()") == '01.01.2021', "The Transfusion date object in Organ recipient  modal doesn't take a value"

    def check_donor_medical_organization_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MED_ORG_REC}.length"), "The Donor medical organization object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MED_ORG_REC}.dropdown('get text')") == 'АСЫКАТИНСАКАЯ ПОЛИКЛИНИКА', "The Donor medical organization object in Organ recipient modal doesn't take a value"

    def check_recipient_medical_organization_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECEIPT_MED_ORG}.length"), "The Recipient medical organization object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_RECEIPT_MED_ORG}.dropdown('get text')") == 'МЕД ЦЕНТР КЕНТАУ', "The Recipient medical organization object in Organ recipient modal doesn't take a value"

    def check_organ_material_number_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_NO_REC}.length"), "The Organ material number object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_NO_REC}.val()") == numbers3, "The Organ material number object in Organ recipient modal doesn't take a value"

    def check_organ_material_type_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_TYPE_REC}.length"), "The Organ material type object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_MAT_TYPE_REC}.find('input').val()") == organ_mat_type_choice, "The Organ material type object in Organ recipient modal doesn't take a value"

    def check_organ_donor_name_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_NAME}.length"), "The Organ donor name object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_DONOR_NAME}.val()") == surname, "The Organ donor name object in Organ recipient modal doesn't take a value"

    def check_hiv_status_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_STATUS_REC}.length"), "The HIV Status object in Organ recipient modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ORGAN_HIV_STATUS_REC}.find('input').val()") == '1', "The HIV Status object in Organ recipient modal doesn't take a value"

    def check_cancel_button_organ_recipient_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BLOOD_RECIPIENT_CANCEL}.length"), "Cancel button in Organ recipient modal is not accessible"
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT_CANCEL}.click();")

    def fill_ippp_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.IPPP}.click();")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_EXISTENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DISP_REGISTERED_KVD}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DK_CONTACTING}.dropdown('set selected', '1');")
        sleep(2)
        self.make(f"{PatientCardLocators.DK_CONTACTING_NUM_YEAR}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING_NUM}.val('{contacting_num}');")
        self.make(f"{PatientCardLocators.C_SECTION_BIRTH}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.MATERNAL_CHEMOPROPHYLAXIS}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.ARTIFICIAL_FEEDING}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.CHILD_CHEMOPROPHYLAXIS}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_ADD}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.DIAGNOSIS_DATE}.val('{diagnosis_date}');")
        self.make(f"{PatientCardLocators.DIAGNOSIS}.val('{smth_random}');")

    def check_save_button_ippp_symptoms_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_SAVE}.length"), "Save button in IPPP Symptoms modal is not accessible"
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_SAVE}.click();")

    def check_ippp_symptoms_existence_checkbox_ippp_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_EXISTENCE}.length"), "The IPPP Symptoms existence checkbox in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_EXISTENCE}.dropdown('get value')") == '1', "The IPPP Symptoms checkbox object in IPPP/Information on children tab doesn't take a value"

    def check_dispencary_registered_in_kvd_area_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_REGISTERED_KVD}.length"), "The Dispencary registered in KVD object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_REGISTERED_KVD}.dropdown('get value')") == '1', "The Dispencary registered in KVD object in IPPP/Information on children tab doesn't take a value"

    def check_dk_contacting_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DK_CONTACTING}.length"), "The Contacting into DK object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DK_CONTACTING}.dropdown('get value')") == '1', "The DK contacting object in IPPP/Information on children tab doesn't take a value"

    def check_dk_contacting_number_last_12month_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DK_CONTACTING_NUM_YEAR}.length"), "The DK contacts number last 12 month object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DK_CONTACTING_NUM_YEAR}.val()") == contacting_num, "The DK contacts number last 12 month object in IPPP/Information on children tab doesn't take a value"

    def check_private_clinics_contacting_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PRIVATE_CLINICS_CONTACTING}.length"), "The Contacting into private clinics object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PRIVATE_CLINICS_CONTACTING}.dropdown('get value')") == '1', "The Contacting into private clinics object in IPPP/Information on children tab doesn't take a value"

    def check_private_clinics_contacting_number_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PRIVATE_CLINICS_CONTACTING_NUM}.length"), "The Number of contacting into private clinics object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PRIVATE_CLINICS_CONTACTING_NUM}.val()") == contacting_num, "The Number of contacting into private clinics object in IPPP/Information on children tab doesn't take a value"

    def check_born_by_caesarean_section_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.C_SECTION_BIRTH}.length"), "The Child born by caesarean section object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.C_SECTION_BIRTH}.dropdown('get value')") == two_choice, "The Child born by caesarean section object in IPPP/Information on children tab doesn't take a value"

    def check_chemoprophylaxis_of_mother_during_pregnancy_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MATERNAL_CHEMOPROPHYLAXIS}.length"), "The Chemoprophylaxis in a mother during pregnancy object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MATERNAL_CHEMOPROPHYLAXIS}.dropdown('get value')") == three_choice, "The Chemoprophylaxis in a mother during pregnancy object in IPPP/Information on children tab doesn't take a value"

    def check_child_had_artificial_feeding_ippp_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARTIFICIAL_FEEDING}.length"), "The Child had artificial feeding object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ARTIFICIAL_FEEDING}.dropdown('get value')") == three_choice, "The Child had artificial feeding object in IPPP/Information on children tab doesn't take a value"

    def check_chemoprophylaxis_of_child_during_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILD_CHEMOPROPHYLAXIS}.length"), "The Chemoprophylaxis in a child during neonatal period object in IPPP/Information on children tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILD_CHEMOPROPHYLAXIS}.dropdown('get value')") == three_choice, "The Chemoprophylaxis in a child during neonatal period object in IPPP/Information on children tab doesn't take a value"

    def check_add_button_ippp_symptoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_ADD}.length"), "Add button in IPPP Symptoms modal is not accessible"

    def check_edit_button_ippp_symptoms_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_EDIT}.length"), "Edit button in IPPP Symptoms modal is not accessible"
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_EDIT}.click();")

    def check_diagnosis_date_symptoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DIAGNOSIS_DATE}.length"), "The Diagnosis date object in IPPP Symptoms is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DIAGNOSIS_DATE}.val()") == diagnosis_date, "The Diagnosis date object in IPPP Symptoms modal doesn't take a value"

    def check_diagnosis_ippp_symptoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DIAGNOSIS}.length"), "The Diagnosis object in IPPP Symptoms modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DIAGNOSIS}.val()") == smth_random, "The Diagnosis object in IPPP Symptoms modal doesn't take a value"

    def check_cancel_button_ippp_symptoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IPPP_SYMPTOM_CANCEL}.length"), "Cancel button in IPPP Symptoms modal is not accessible"
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_CANCEL}.click();")

    def fill_manipulations_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.MANIPULATION_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_ADD}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_DATE}.val('{manip_emerg_date}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_SORT}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_TYPE}.dropdown('set selected', '{manip_type_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_MED_ORG}.dropdown('set selected', '280000000227');")

    def check_save_button_manipulations_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_SAVE}.length"), "Save button in Manipulations is not accessible"
        self.make(f"{PatientCardLocators.MANIPULATIONS_SAVE}.click();")

    def check_manipulations_existence_checkbox_manipulations_emergencies_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATION_EXISTENCE}.length"), "The Manipulations existence checkbox in Manipulations emergencies tab is not accessible"
        assert self.make(f"{PatientCardLocators.MANIPULATION_EXISTENCE}.is(':checked')"), "The Manipulations existence checkbox in Manipulations emergencies is not ticked"

    def check_add_button_manipulations_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_ADD}.length"), "Add button in Manipulations modal is not accessible"

    def check_edit_button_manipulations_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_EDIT}.length"), "Edit button in Manipulations modal is not accessible"
        self.make(f"{PatientCardLocators.MANIPULATIONS_EDIT}.click();")

    def check_date_manipulations_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_DATE}.length"), "The Manipulation date object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_DATE}.val()") == manip_emerg_date, "The Manipulation date in Manipulations modal doesn't take a value"

    def check_sort_manipulations_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_SORT}.length"), "The Manipulation sort object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_SORT}.dropdown('get value')") == two_choice, "The Manipulation sort object in Manipulations modal doesn't take a value"

    def check_type_manipulations_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_TYPE}.length"), "The Manipulation type object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_TYPE}.dropdown('get value')") == manip_type_choice, "The Manipulation type object in Manipulations modal doesn't take a value"

    def check_medical_organization_manipulations_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_MED_ORG}.length"), "The Medical organization object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_MED_ORG}.dropdown('get text')") == 'ОБЛАСТНОЙ ЦЕНТР ПСИХИЧЕСКОГО ЗДОРОВЬЕ', "The Medical organization object in Manipulations modal doesn't take a value"

    def check_cancel_button_manipulations_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MANIPULATIONS_CANCEL}.length"), "Cancel button in Manipulations modal is not accessible"
        self.make(f"{PatientCardLocators.MANIPULATIONS_CANCEL}.click();")

    def fill_emergencies_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        # self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES_ADD}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.EMERGENCIES_DATE}.val('{manip_emerg_date}');")
        self.make(f"{PatientCardLocators.INFECTION_RISK}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.EMERGENCIES_MED_ORG}.val('Pupkin cliniс');")
        self.make(f"{PatientCardLocators.TRAUMA_TYPE}.dropdown('set selected', '{trauma_choice}');")
        self.make(f"{PatientCardLocators.EMERGENCIES_72HOURS}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.EMERGENCIES_HIV_STATUS}.dropdown('set selected', '1');")

    def check_save_button_emergencies_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_SAVE}.length"), "Save button in Emergencies is not accessible"
        self.make(f"{PatientCardLocators.EMERGENCIES_SAVE}.click();")

    def check_emergencies_existence_checkbox_manipulations_emergencies_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES}.length"), "The Emergencies existence checkbox in Manipulations emergencies tab is not accessible"
        assert self.make(f"{PatientCardLocators.EMERGENCIES}.is(':checked')"), "The Emergencies existence checkbox in Recipient tab  is not ticked"

    def check_add_button_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_ADD}.length"), "Add button in Emergencies modal is not accessible"

    def check_edit_button_emergencies_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_EDIT}.length"), "Edit button in Emergencies modal is not accessible"
        self.make(f"{PatientCardLocators.EMERGENCIES_EDIT}.click();")

    def check_date_emergencies_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_DATE}.length"), "The Emergency date object in Emergencies modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_DATE}.val()") == manip_emerg_date, "The Manipulation date in Emergencies modal doesn't take a value"

    def check_sort_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.INFECTION_RISK}.length"), "The Manipulation sort object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.INFECTION_RISK}.dropdown('get value')") == two_choice, "The Manipulation sort object in Manipulations modal doesn't take a value"

    def check_medical_organization_emergencies_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_MED_ORG}.length"), "The Manipulation type object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_MED_ORG}.val()") == 'Pupkin cliniс', "The Manipulation type object in Manipulations modal doesn't take a value"

    def check_trauma_type_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TRAUMA_TYPE}.length"), "The Medical organization object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TRAUMA_TYPE}.dropdown('get value')") == trauma_choice, "The Medical organization object in Manipulations modal doesn't take a value"

    def check_72hours_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_72HOURS}.length"), "The Medical organization object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_72HOURS}.dropdown('get value')") == three_choice, "The Medical organization object in Manipulations modal doesn't take a value"

    def check_hiv_status_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_HIV_STATUS}.length"), "The Medical organization object in Manipulations modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_HIV_STATUS}.dropdown('get value')") == '1', "The Medical organization object in Manipulations modal doesn't take a value"

    def check_cancel_button_emergencies_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.EMERGENCIES_CANCEL}.length"), "Cancel button in Manipulations modal is not accessible"
        self.make(f"{PatientCardLocators.EMERGENCIES_CANCEL}.click();")

    def fill_departure_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_ADD}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_START}.val('{eighty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_END}.val('{sixty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_COUNTRY}.dropdown('set selected', '{country_choice}');")
        self.make(f"{PatientCardLocators.DEPARTURE_PURPOSE}.dropdown('set selected', '{purpose_choice}');")

    def check_save_button_departure_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_SAVE}.length"), "Save button in Departure is not accessible"
        self.make(f"{PatientCardLocators.DEPARTURE_SAVE}.click();")

    def check_departure_existence_checkbox_departure_source_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_EXISTENCE}.length"), "The Departure existence checkbox in Departure/source tab is not accessible"
        assert self.make(f"{PatientCardLocators.EMERGENCIES}.is(':checked')"), "The Departure existence checkbox in Departure/source tab  is not ticked"

    def check_add_button_departure_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_ADD}.length"), "Add button in Departure modal is not accessible"

    def check_edit_button_departure_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_EDIT}.length"), "Edit button in Departure modal is not accessible"
        self.make(f"{PatientCardLocators.DEPARTURE_EDIT}.click();")

    def check_departure_start_date_departure_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_DATE_START}.length"), "The Departure start date object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_DATE_START}.val()") == eighty_days_ago, "The Departure start date in Departure modal doesn't take a value"

    def check_departure_end_date_departure_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_DATE_END}.length"), "The Departure end date object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_DATE_END}.val()") == sixty_days_ago, "The Departure end date object in Departure modal doesn't take a value"

    def check_departure_country_departure_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_COUNTRY}.length"), "The Departure country type object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_COUNTRY}.dropdown('get value')") == country_choice, "The Departure country object in Departure modal doesn't take a value"

    def check_departure_purpose_departure_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_PURPOSE}.length"), "The Departure purpose object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_PURPOSE}.dropdown('get value')") == purpose_choice, "The Departure purpose object in Departure modal doesn't take a value"

    def check_cancel_button_departure_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_CANCEL}.length"), "Cancel button in Departure modal is not accessible"
        self.make(f"{PatientCardLocators.DEPARTURE_CANCEL}.click();")

    def fill_source_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        # self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.INFECTION_SOURCE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.SOURCE_ADD}.click();")
        self.make(f"{PatientCardLocators.SOURCE_IB_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.SOURCE_IB_DATE}.val('{ib_date}');")
        self.make(f"{PatientCardLocators.SOURCE_SURNAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.SOURCE_NAME}.val('{name}');")
        self.make(f"{PatientCardLocators.SOURCE_MIDDLE_NAME}.val('{midname}');")

    def check_save_button_source_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_SAVE}.length"), "Save button in Source is not accessible"
        self.make(f"{PatientCardLocators.SOURCE_SAVE}.click();")

    def check_infection_source_existence_checkbox_departure_source_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.INFECTION_SOURCE_EXISTENCE}.length"), "The Infection source existence checkbox in Departure/source tab is not accessible"
        assert self.make(f"{PatientCardLocators.INFECTION_SOURCE_EXISTENCE}.is(':checked')"), "The Departure existence checkbox in Departure/source tab  is not ticked"

    def check_add_button_source_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEPARTURE_ADD}.length"), "Add button in Source modal is not accessible"

    def check_edit_button_source_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_EDIT}.length"), "Edit button in Departure modal is not accessible"
        self.make(f"{PatientCardLocators.SOURCE_EDIT}.click();")

    def check_ib_number_source_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_IB_NUM}.length"), "The Departure start date object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_IB_NUM}.val()") == numbers4, "The Departure start date in Departure modal doesn't take a value"

    def check_ib_date_source_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_IB_DATE}.length"), "The Departure end date object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_IB_DATE}.val()") == ib_date, "The Departure end date object in Departure modal doesn't take a value"

    def check_surname_source_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_SURNAME}.length"), "The Departure end date object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_SURNAME}.val()") == surname, "The Departure end date object in Departure modal doesn't take a value"

    def check_name_source_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_NAME}.length"), "The Departure country type object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_NAME}.val()") == name, "The Departure country object in Departure modal doesn't take a value"

    def check_midname_source_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_MIDDLE_NAME}.length"), "The Departure purpose object in Departure modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_MIDDLE_NAME}.val()") == midname, "The Departure purpose object in Departure modal doesn't take a value"

    def check_cancel_button_source_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SOURCE_CANCEL}.length"), "Cancel button in Departure modal is not accessible"
        self.make(f"{PatientCardLocators.SOURCE_CANCEL}.click();")

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

    def check_save_button_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_SAVE}.length"), "Dispensary observation modal's Save button is not accessible"
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")

    def check_add_button_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_OBSER_ADD}.length"), "Dispensary observation modal's Add button is not accessible"
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")

    def check_edit_button_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_OBSER_EDIT}.length"), "Dispensary observation modal's Edit button is not accessible"
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")

    def check_dispensary_registration_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.length"), "Patient's birth date object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_REGIS}.find('input').val()") == regis_date, "Patient's D-registration date object doesn't take a value"

    def check_cancel_button_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_CANCEL_BTN}.length"), "Dispensary observation modal's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.DISP_CANCEL_BTN}.click();")

    def fill_at_risk_modal(self):
        sleep(2)
        self.make(f"{PatientCardLocators.DRUG_INJ_CONSUMPTION}.dropdown('set selected', '{drug_cons_choice}');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_YEAR}.val('2');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_REGIS}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.ALCOHOL_CONSUMPTION}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.OUTPATIENT_CARD_NO}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.DISP_START_DATE}.val('{sixty_days_ago}');")
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
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_START_DATE}.val()") == sixty_days_ago, "Initial registration date object in Dispensary observation doesn't take a value"

    def check_doctor_name(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DISP_DOCTORS_NAME}.length"), "Doctor name object in Dispensary observation is not accessible"
        ddn = self.browser.execute_script(f"return {PatientCardLocators.DISP_DOCTORS_NAME}.find('input').val()")
        print(ddn)
        assert ddn == disp_doc_choice, "Doctor name object in Dispensary observation doesn't take a value"

    def fill_dispensary_observation_modal_when_patient_died(self):
        sleep(2)
        self.fill_dispensary_observation_modal()
        sleep(2)
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")
        self.make(f"{PatientCardLocators.DATE_OF_DEREGIS}.val('{deregis_date}');")
        self.make(f"{PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DATE_OF_DEATH}.val('{deregis_date}');")
        self.make(f"{PatientCardLocators.AIDC_RELATED_DEATH}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.DEATH_REASON}.dropdown('set selected', '{death_choice}');")
        self.make(f"{PatientCardLocators.DEATH_PLACE}.dropdown('set selected', '{death_place_choice}');")
        self.make(f"{PatientCardLocators.AUTOPSY}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.PATHOLOGOANATOMIC_DIAGNOSIS}.val('Положительный');")
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")

    def check_patients_death_date_dispensary_observation_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DEATH}.length"), "The Patient's death date object in Dispensary observation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DEATH}.val()") == deregis_date, "The Patient's death date object in Dispensary observation modal doesn't take a value"

    def check_aidc_related_death_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.AIDC_RELATED_DEATH}.length"), "The AIDC related death object in Dispensary observation modal is not accessible"
        self.make(f"{PatientCardLocators.AIDC_RELATED_DEATH}.dropdown('get value')") == two_choice, "The AIDC related death object in Dispensary observation modal doesn't take a value"

    def check_death_reason_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEATH_REASON}.length"), "The Death reason object in Dispensary observation modal is not accessible"
        self.make(f"{PatientCardLocators.DEATH_REASON}.dropdown('get value')") == death_choice, "The Death reason object object in Dispensary observation modal doesn't take a value"

    def check_death_place_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DEATH_PLACE}.length"), "The Death place object in Dispensary observation modal is not accessible"
        self.make(f"{PatientCardLocators.DEATH_PLACE}.dropdown('get value')") == death_place_choice, "The Death place object in Dispensary observation modal doesn't take a value"

    def check_autopsy_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.AUTOPSY}.length"), "The Autopsy object in Dispensary observation modal is not accessible"
        self.make(f"{PatientCardLocators.AUTOPSY}.dropdown('get value')") == two_choice, "The Autopsy object in Dispensary observation modal doesn't take a value"

    def check_pathologoanatomic_diagnosis_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PATHOLOGOANATOMIC_DIAGNOSIS}.length"), "The Pathologoanatomic diagnosis object in Dispensary observation modal is not accessible"
        self.make(f"{PatientCardLocators.PATHOLOGOANATOMIC_DIAGNOSIS}.val()") == 'Положительный', "The Pathologoanatomic diagnosis object in Dispensary observation doesn't take a value"

    def fill_dispensary_observation_modal_when_patient_left_rk(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")
        self.make(f"{PatientCardLocators.DATE_OF_DEREGIS}.val('{deregis_date}');")
        self.make(f"{PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('set selected', '2');")
        self.make(f"{PatientCardLocators.D_OBSER_COUNTRY}.dropdown('set selected', '{country_choice}');")
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")

    def check_deregistration_date_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DEREGIS}.length"), "The Deregistration date object in Dispensary observation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DEREGIS}.val()") == deregis_date, "The Deregistration date object in Dispensary observation modal doesn't take a value"

    def check_deregistration_reason_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.length"), "The Deregistration reason object in Dispensary observation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('get value')") == '2', "The Deregistration reason object in Dispensary observation modal doesn't take a value"

    def check_country_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_COUNTRY}.length"), "The Country object in Dispensary observation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_COUNTRY}.dropdown('get value')") == country_choice, "The Country object in Dispensary observation modal doesn't take a value"

    def fill_dispensary_observation_modal_when_patient_left_region(self):
        sleep(2)
        self.fill_dispensary_observation_modal()
        sleep(1)
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        sleep(3)
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")
        self.make(f"{PatientCardLocators.DATE_OF_DEREGIS}.val('{deregis_date}');")
        self.make(f"{PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.D_OBSER_AREA}.dropdown('set selected', '3');")
        sleep(2)
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.focus();")
        sleep(2)
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('set selected', '33');")
        sleep(1)
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('hide');")
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.DISP_OBSER_EDIT}.click();")

    def check_area_dispensary_observation_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_AREA}.length"), "The Area object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_AREA}.dropdown('get value')") == '3', "The area date object in Perinatal registration modal doesn't take a value"


    def check_unit_area_dispensary_observation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_UNIT_AREA}.length"), "The Unit area object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('get value')") == '33', "The Unit area object in Perinatal registration modal doesn't take a value"

    def fill_perinatal_registration_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_REGIS_ADD}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_MED_ORG}.dropdown('set selected', '{aidc_center_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_REGIS}.calendar('set date', '{regis_date}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.calendar('set date', '{deregis_date}');")
        self.make(f"{PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.dropdown('set selected', '{reason_perinatal_deregis_choice}');")
        if reason_perinatal_deregis_choice == 2:
            self.make(f"{PatientCardLocators.PERINATAL_COUNTRY}.dropdown('set selected', '{country_choice}');")
        if reason_perinatal_deregis_choice == 3:
            sleep(2)
            self.make(f"{PatientCardLocators.PERINATAL_AREA}.dropdown('set selected', '3');")
            sleep(3)
            self.make(f"{PatientCardLocators.PERINATAL_UNIT_AREA}.dropdown('set selected', '33');")
        if reason_perinatal_deregis_choice == 4:
            self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEATH}.calendar('set date', '{deregis_date}');")
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_REASON}.dropdown('set selected', '{death_choice}');")
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_PLACE}.dropdown('set selected', '{death_place_choice}');")

    def check_save_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_SAVE}.length"), "Perinatal registration modal's Save button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_SAVE}.click();")

    def check_add_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REGIS_ADD}.length"), "Perinatal registration modal's Add button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_REGIS_ADD}.click();")

    def check_edit_button_perinatal_registration_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_EDIT}.length"), "Perinatal registration's Edit button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_EDIT}.click();")

    def check_medical_organization_perinatal_registration_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_MED_ORG}.length"), "The Medical organization object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_MED_ORG}.find('input').val()") == aidc_center_choice, "The Medical organization object in Perinatal registration modal doesn't take a value"

    def check_registration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_REGIS}.length"), "The Registration date object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_REGIS}.find('input').val()") == regis_date, "The Registration date object in Perinatal registration modal doesn't take a value"

    def check_deregistration_date_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.length"), "The Deregistration date object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.find('input').val()") == deregis_date, "The Deregistration date object in Perinatal registration modal doesn't take a value"

    def check_deregistration_reason_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.length"), "The Deregistration reason object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.find('input').val()") == reason_perinatal_deregis_choice, "The Deregistration reason object in Perinatal registration modal doesn't take a value"

    def check_country_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_COUNTRY}.length"), "The Country object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_COUNTRY}.find('input').val()") == country_choice, "The Country object in Perinatal registration modal doesn't take a value"

    def check_area_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_AREA}.length"), "The Area object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_AREA}.find('input').val()") == '3', "The area date object in Perinatal registration modal doesn't take a value"

    def check_unit_area_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_UNIT_AREA}.length"), "The Unit area object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_UNIT_AREA}.find('input').val()") == '33', "The Unit area object in Perinatal registration modal doesn't take a value"

    def check_date_of_death_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEATH}.length"), "The Date of death object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DATE_OF_DEATH}.find('input').val()") == deregis_date, "The Date of death object in Perinatal registration modal doesn't take a value"

    def check_death_reason_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DEATH_REASON}.length"), "The Death reason object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DEATH_REASON}.find('input').val()") == death_choice, "The Death reason object in Perinatal registration modal doesn't take a value"

    def check_death_place_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DEATH_PLACE}.length"), "Patient's birth date object in Perinatal registration modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_DEATH_PLACE}.find('input').val()") == death_place_choice, "Patient's D-registration date object in Perinatal registration modal doesn't take a value"

    def check_cancel_button_perinatal_registration_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_CANCEL}.length"), "Perinatal registration modal's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_CANCEL}.click();")

    def fill_perinatal_registration_tab(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        # self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        self.make(f"{PatientCardLocators.ARV_PROPHYLAXIS}.dropdown('set selected', '{arv_proph_choice}');")
        self.make(f"{PatientCardLocators.ARV_START_DATE}.val('{eighty_days_ago}');")
        # self.make(f"{PatientCardLocators.ARV_END_DATE}.calendar('set date', '{fifty_days_ago}');")
        # self.make(f"{PatientCardLocators.ARV_MEDICATION}.dropdown('set selected', '{medication_choice}');")
        # self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")
        # self.make(f"{PatientCardLocators.ARV_ISSUANCE_ADD}.click();")
        # self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME}.click();")
        # self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME_CHOICE}.click();")
        # #self.make(f"$('#add-row-preparaty-table tr:eq(0) td:eq(0) a').click();")
        # self.make(f"{PatientCardLocators.ARV_RECIPE_NUM}.val('{numbers4}');")
        # self.make(f"{PatientCardLocators.ARV_DAY_NUM}.val('30');")
        # self.make(f"{PatientCardLocators.ARV_NEXT_DATE}.calendar('set date', '{thirty_days_forward}');")
        # self.make(f"{PatientCardLocators.ARV_MEDICATION_SAVE}.click();")
        # self.make(f"{PatientCardLocators.ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.calendar('set date', '{fifty_days_ago}');")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.calendar('set date', '{thirty_days_ago}');")
        self.make(f"{PatientCardLocators.HIV_STATUS_P_TAB}.dropdown('set selected', '{arv_hiv_choice}');")
        self.make(f"{PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.calendar('set date', '{fifty_days_ago}');")

    def check_medical_organization_perinatal_registration_tab(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_PROPHYLAXIS}.length"), "The Medical organization object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.ARV_PROPHYLAXIS}.find('input').val()")
        print(rd)
        assert rd == arv_proph_choice, "The Medical organization object in Perinatal registration tab doesn't take a value"

    def check_registration_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_START_DATE}.length"), "The Registration date object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.ARV_START_DATE}.find('input').val()")
        print(rd)
        assert rd == eighty_days_ago, "The Registration date object in Perinatal registration tab doesn't take a value"

    def check_deregistration_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION}.length"), "The Deregistration date object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION}.find('input').val()")
        print(rd)
        assert rd == medication_choice, "The Deregistration date object in Perinatal registration tab doesn't take a value"

    def check_cancel_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_ISSUANCE}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")

    def check_cancel_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_ISSUANCE_ADD}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_ADD}.click();")

    def check_cancel_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION_NAME}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME}.click();")

    def check_cancel_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_CANCEL}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.PERINATAL_CANCEL}.click();")

    def check_deregistration_reason_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.length"), "The Deregistration reason object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.find('input').val()")
        print(rd)
        assert rd == reason_deregis_choice, "The Deregistration reason object in Perinatal registration tab doesn't take a value"

    def check_country_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_COUNTRY}.length"), "The Country object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PERINATAL_COUNTRY}.find('input').val()")
        print(rd)
        assert rd == country_choice, "The Country object in Perinatal registration tab doesn't take a value"

    def check_area_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_NEXT_DATE}.length"), "The Area object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.ARV_NEXT_DATE}.find('input').val()")
        print(rd)
        assert rd == '3', "The area date object in Perinatal registration tab doesn't take a value"

    def check_save_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION_SAVE}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.ARV_MEDICATION_SAVE}.click();")

    def check_save_button_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_ISSUANCE_SAVE}.length"), "Perinatal registration tab's Cancel button is not accessible"
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_SAVE}.click();")

    def check_unit_area_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.length"), "The PCP Prophylaxis start date object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.find('input').val()")
        print(rd)
        assert rd == fifty_days_ago, "The PCP Prophylaxis start date object in Perinatal registration tab doesn't take a value"

    def check_date_of_death_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.length"), "The PCP Prophylaxis end date object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.find('input').val()")
        print(rd)
        assert rd == thirty_days_ago, "The PCP Prophylaxis end date object in Perinatal registration tab doesn't take a value"

    def check_death_reason_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STATUS_P_TAB}.length"), "The HIV Status object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.HIV_STATUS_P_TAB}.find('input').val()")
        print(rd)
        assert rd == arv_hiv_choice, "The HIV Status object in Perinatal registration tab doesn't take a value"

    def check_hiv_determination_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.length"), "The HIV Determination date object in Perinatal registration tab is not accessible"
        rd = self.browser.execute_script(f"return {PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.find('input').val()")
        print(rd)
        assert rd == fifty_days_ago, "The HIV Determination date object in Perinatal registration tab doesn't take a value"

    def fill_hiv_diagnosis_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
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
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DIAGNOSIS_EDIT}.length"), "Edit button in HIV diagnosis modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_EDIT}.click();")

    def check_formulating_change_date_hiv_diagnosis_modal(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.FORMULATING_CHANGE_DATE}.length"), "The Formulating change date object in HIV diagnosis modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FORMULATING_CHANGE_DATE}.val()") == thirty_days_ago, "The Formulating change date object in HIV diagnosis modal doesn't take a value"

    def check_hiv_stage_hiv_diagnosis_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STAGE}.length"), "The HIV Stage object in HIV diagnosis modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STAGE}.find('input').val()") == hiv_stage_choice, "The HIV Stage object in HIV diagnosis modal doesn't take a value"

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
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_RELATED_DISEASE_EDIT}.length"), "Edit button in HIV related disease modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_EDIT}.click();")

    def check_hiv_stage_hiv_related_disease_modal(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.length"), "The HIV Stage object in HIV related disease is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.find('input[type=hidden]').val()") == '290000000167' or '290000000168', "The HIV Stage object in HIV related disease doesn't take a value"

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
        self.make(f"{PatientCardLocators.SERVICE_WITHIN_TARIFICATOR}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.CONSULTATION_DATE}.calendar('set date', '{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.CONSULTATION}.dropdown('set selected', '{consultation_choice}');")
        self.make(f"{PatientCardLocators.CONSULTATION_DESCRIPTION}.val('Положительный');")

    def check_save_button_recommended_consultation_modal(self):
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_SAVE}.length"), "Save button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_SAVE}.click();")

    def check_add_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_ADD}.length"), "Add button in Recommended consultation modal is not accessible"

    def check_edit_button_recommended_consultation_modal(self):
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_EDIT}.length"), "Edit button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_EDIT}.click();")

    def check_service_within_tarificator_recommended_consultation_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SERVICE_WITHIN_TARIFICATOR}.length"), "The Service proveded within tarificator object in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SERVICE_WITHIN_TARIFICATOR}.find('input').val()") == two_choice, "The Service proveded within tarificator object in Recommended consultation modal doesn't take a value"

    def check_consultation_date_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DATE}.length"), "The Consultation date object in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DATE}.find('input').val()") == thirty_days_forward, "The Consultation date object in Recommended consultation modaldoesn't take a value"

    def check_consultation_type_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION}.length"), "The Consultation in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION}.find('input').val()")== consultation_choice, "The Consultation in Recommended consultation modal doesn't take a value"

    def check_consultation_description_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DESCRIPTION}.length"), "The Consultation description  in Recommended consultation modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONSULTATION_DESCRIPTION}.val()") == 'Положительный', "The Consultation description object in Recommended consultation modal doesn't take a value"

    def check_cancel_button_recommended_consultation_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_CONSULTATION_CANCEL}.length"), "Cancel button in Recommended consultation modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_CANCEL}.click();")

    def fill_recommended_screening_modal(self):
        sleep(3)
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        # self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.RECOM_SCREENING_ADD}.click();")
        self.make(f"{PatientCardLocators.SCREENEG_SERVICE_WITHIN_TARIFICATOR}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.SCREENING_DATE}.calendar('set date', '{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.SURVEY}.dropdown('set selected', '{survey_choice}');")
        self.make(f"{PatientCardLocators.SCREENING_DESCRIPTION}.val('Положительный');")

    def check_save_button_recommended_screening_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_SAVE}.length"), "Save button in Recommended screening modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_SCREENING_SAVE}.click();")

    def check_add_button_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_ADD}.length"), "Add button in Recommended screening modal is not accessible"

    def check_edit_button_recommended_screening_modal(self):
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.RECOM_SCREENING_EDIT}.length"), "Edit button in Recommended screening modal in Dispensary observation is not accessible"
        self.make(f"{PatientCardLocators.RECOM_SCREENING_EDIT}.click();")

    def check_service_within_tarificator_recommended_screening_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENEG_SERVICE_WITHIN_TARIFICATOR}.length"), "The Service proveded within tarificator object in Recommended screening modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENEG_SERVICE_WITHIN_TARIFICATOR}.find('input').val()") == two_choice, "The Service proveded within tarificator object in Recommended screening modal doesn't take a value"

    def check_consultation_date_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DATE}.length"), "The Consultation date object in Recommended screening modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DATE}.find('input').val()") == thirty_days_forward, "The Consultation date object in Recommended screening modaldoesn't take a value"

    def check_consultation_type_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SURVEY}.length"), "The Consultation in Recommended screening modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SURVEY}.find('input').val()") == survey_choice, "The Consultation in Recommended screening modal doesn't take a value"

    def check_consultation_description_recommended_screening_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DESCRIPTION}.length"), "The Consultation screening  in Recommended screening modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SCREENING_DESCRIPTION}.val()") == 'Положительный', "The Consultation screening object in Recommended screening modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_BLOOD_DONOR_MED_ORG}.find('input').val()") == mo_choice1, "Blood donor medical organization object in CD4 doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()") == mo_choice1, "Medical organization which provided analysis in CD4 doesn't take a value"

    def check_cd4_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REMARK}.length"), "CD4 note object is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_REMARK}.val()") == 'Положительный', "CD4 note object in CD4 doesn't take a value"

    def check_cd4_services(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SERVICES}.length"), "Services object in CD4 is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CD4_SERVICES}.find('input').val()") == service_choice, "Services object  in CD4 doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_DONOR_MED_ORG}.find('input').val()") == mo_choice1, "Donor medical organization object in Viral load in CD4&VL doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT}.find('input').val()") == vl_res_choice, "Result object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_result_ml(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT_ML}.length"), "Result ML object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_RESULT_ML}.find('input').val()") == vl_res_ml_choice, "Result ML in Viral load in CD4&VL doesn't take a value"

    def check_log(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LOG}.length"), "Log object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.LOG}.val()") == '2', "Log object in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()") == mo_choice1, "Medical organization which provided analysis in Viral load in CD4&VL doesn't take a value"

    def check_cd4_vl_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REMARK}.length"), "Note object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_REMARK}.val()") == remark_choice, "Note object in Viral load in CD4&VLdoesn't take a value"

    def check_cd4_vl_services(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_SERVICES}.length"), "Services object in Viral load in CD4&VL is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VL_SERVICES}.find('input').val()") == vl_service_choice, "Services object in Viral load in CD4&VL doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MAT_DONOR_MED_ORG}.find('input').val()") == mo_choice1, "Donor medical organization object in VGV modal doesn't take a value"

    def check_vgv_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object in VGV modal doesn't take a value"

    def check_vgv_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTERING_DATE}.length"), "Registering date object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REGISTERING_DATE}.val()") == today, "Registering date object in VGV modal doesn't take a value"

    def check_marker(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MARKER}.length"), "Marker object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MARKER}.find('input').val()") == marker_choice, "Marker object in VGV modal doesn't take a value"

    def check_vgv_result(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_RESULT}.length"), "Result object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_RESULT}.find('input').val()") == '1', "Result object in VGV modal doesn't take a value"

    def check_vgv_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()") == mo_choice1, "Medical organization which provided analysis in VGV modal doesn't take a value"

    def check_vgv_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REMARK}.length"), "Note object in VGV modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_REMARK}.find('input').val()") == 'Положительный', "Note object in VGV modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MAT_DONOR_MED_ORG}.find('input').val()") == mo_choice1, "Donor medical organization object in VGS modal doesn't take a value"

    def check_vgs_material_receipt_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.length"), "Material receipt date object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.val()") == today, "Material receipt date object in VGS modal doesn't take a value"

    def check_vgs_registering_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTERING_DATE}.length"), "Registering date object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REGISTERING_DATE}.val()") == today, "Registering date object in VGS modal doesn't take a value"

    def check_vgs_analysis_type(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_ANALYSIS_TYPE}.length"), "Marker object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_ANALYSIS_TYPE}.find('input').val()") == analysis_choice, "Marker object in VGS modal doesn't take a value"

    def check_vgs_result(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_RESULT}.length"), "Result object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_RESULT}.find('input').val()") == '1', "Result object in VGS modal doesn't take a value"

    def check_vgs_medical_org_provided_analysis(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.length"), "Medical organization which provided analysis in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.find('input').val()") == mo_choice1, "Medical organization which provided analysis in VGS modal doesn't take a value"

    def check_vgs_note(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REMARK}.length"), "Note object in VGS modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGS_REMARK}.find('input').val()") == 'Положительный', "Note object in VGS modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_EDIT}.length"), "Edit button in VGV vaccination modal is not accessible"
        self.make(f"{PatientCardLocators.VGV_VAC_EDIT}.click();")

    def check_vgv_vac_multiplicity(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_MULTIPLICITY}.length"), "Multilicity object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_MULTIPLICITY}.find('input').val()") == vac_multi_choice, "Multilicity object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_immunization_date(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.IMMUNIZATION_DATE}.length"), "Immunization date object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.IMMUNIZATION_DATE}.val()") == today, "Immunization receipt date object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_dose_volume(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_DOSE_VOLUME}.length"), "Registering date object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_DOSE_VOLUME}.val()") == dose, "Registering date object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_series(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_SERIES}.length"), "Marker object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_SERIES}.find('input').val()") == numbers5, "Marker object in VGV vaccination modal doesn't take a value"

    def check_vgv_vac_country_producer(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.length"), "Result object in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.find('input').val()") == vac_multi_choice, "Result object in VGV vaccination modal doesn't take a value"

    def check_vgv_medical_org_provided_vaccination(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.length"), "Medical organization which provided vaccination in VGV vaccination modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.find('input').val()") == mo_choice1, "Medical organization which provided analysis in VGV vaccination modal doesn't take a value"

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
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_REGISTERING_DATE}.length"), "The Registering date object in Fluoroscopy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_REGISTERING_DATE}.find('input').val()") == today, "The Registering date object in Fluoroscopy modal doesn't take a value"

    def check_result_fluoroscopy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_RESULT}.length"), "Tne Result object in Fluoroscopy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FLUOR_RESULT}.find('input').val()") == fluor_choice, "The Result object in Fluoroscopy modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIO_REGISTERING_DATE}.find('input').val()") == today, "The Registering date in Radiography modal doesn't take a value"

    def check_result_radiography_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIO_RESULT}.length"), "The Result object in Radiography modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RADIO_RESULT}.find('input').val()") == radio_choice, "The Result object in Radiography modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_REGISTERING_DATE}.find('input').val()") == today, "The Registering date object in Sputum smear modal doesn't take a value"

    def check_result_sputum_smear_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_RESULT}.length"), "The Result object in Sputum smear modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SPUTUM_RESULT}.find('input').val()") == sputum_choice, "The Result object in Sputum smear modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_REGISTERING_DATE}.find('input').val()") == today, "The Registering date object in TB symphtoms modal doesn't take a value"

    def check_result_tb_symphtoms_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_RESULT}.length"), "The Result object in TB symphtoms modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_SYMPH_RESULT}.find('input').val()") == tb_symph_choice, "The Result object in TB symphtoms modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_REGISTERING_DATE}.find('input').val()") == today, "The Registering date object in Xpert MTB modal doesn't take a value"

    def check_result_xpert_mtb_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_RESULT}.length"), "The Result object in Xpert MTB modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.XPERT_MTB_RESULT}.find('input').val()") == xpert_choice, "The Result object in Xpert MTB modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_REGISTERING_DATE}.find('input').val()") == today, "The Registering date object in KT/MRT modal doesn't take a value"

    def check_result_kt_mrt_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_RESULT}.length"), "The Result object in KT/MRT modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.KT_MRT_RESULT}.find('input').val()") == mrt_choice, "The Result object in KT/MRT modal doesn't take a value"

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
        assert self.browser.execute_script(f"return {PatientCardLocators.LAB_NAME_CONFIRMED_TB}.val()") == 'Random lab', "Confirmed labaratory name object in TB treatment modal doesn't take a value"

    def check_diagnosis_registering_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_REGISTERING_DATE}.length"), "Diagnosis registering date in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_REGISTERING_DATE}.val()") == thirty_days_ago, "Diagnosis registering date in TB treatment doesn't take a value"

    def check_sick_type_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SICK_TYPE}.length"), "The Sick type object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SICK_TYPE}.find('input').val()") == case_choice, "The Sick type object in TB treatment doesn't take a value"

    def check_diagnosis_mkb10_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_MKB10}.length"), "The diagnosis MKB10 object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_DIAG_MKB10}.find('input').val()") == tb_analysis_choice, "The diagnosis MKB10 object in TB treatment doesn't take a value"

    def check_location_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.LOCATION}.length"), "The Location object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.LOCATION}.find('input').val()") == two_choice, "The Location object in TB treatment doesn't take a value"

    def check_bac_secretion_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.BAC_SECRETION}.length"), "The BAC secretion object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.BAC_SECRETION}.find('input').val()") == bac_secr_choice, "The BAC secretion object in TB treatment doesn't take a value"

    def check_treatment_start_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_START_DATE}.length"), "The Treatment start date object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_START_DATE}.val()") == today, "The Treatment start date object in TB treatment modal doesn't take a value"

    def check_treatment_end_date_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_END_DATE}.length"), "The Treatment end date object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.TREATMENT_END_DATE}.val()") == today, "The Treatment end date object in TB treatment modal doesn't take a value"

    def check_outcome_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OUTCOME}.length"), "The Outcome object in TB treatment modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OUTCOME}.find('input').val()") == outcome_choice, "The Outcome object in TB treatment doesn't take a value"

    def check_cancel_button_tb_treatment_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.TB_TREATMENT_CANCEL}.length"), "Cancel button in TB treatment modal is not accessible"
        self.make(f"{PatientCardLocators.TB_TREATMENT_CANCEL}.click();")

    def check_presence_in_history_tb_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.length"), "The Presence in history object in TB tab is not accessible"
        self.make(f"{PatientCardLocators.PRESENCE_TB_IN_HISTORY}.dropdown('set selected', '{two_choice}');")
        assert self.browser.execute_script(f"return {PatientCardLocators.PRESENCE_TB_IN_HISTORY}.find('input').val()") == two_choice, "The Presence in history object in TB tab doesn't take a value"

    def check_d_registered_date_tb_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.length"), "The Disp registered date object in TB tab is not accessible"
        self.make(f"{PatientCardLocators.D_ACCOUNTED_DATE}.calendar('set date', '{today}');")
        assert self.browser.execute_script(f"return {PatientCardLocators.D_ACCOUNTED_DATE}.find('input').val()") == today, "The Disp registered date object in TB tab doesn't take a value"

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
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_HOSP_EDIT}.length"), "Edit button in D-screening, hospitalization modal is not accessible"
        self.make(f"{PatientCardLocators.D_SCRN_HOSP_EDIT}.click();")

    def check_date_of_eligibility_for_treatment_d_screening_hospitalization(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_ELIGIBILITY_FOR_TREATMENT}.length"), "Date of eligibility for treatment object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_ELIGIBILITY_FOR_TREATMENT}.val()") == today, "Date of eligibility for treatment objectt in D-screening, hospitalization modal doesn't take a value"

    def check_treatment_type_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_TYPE}.length"), "The Treatment type object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_TYPE}.find('input').val()") == two_choice, "The Treatment type object in D-screening, hospitalization modal doesn't take a value"

    def check_mpi_profile_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.MPI_PROFILE}.length"), "The MPI profile object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.MPI_PROFILE}.find('input').val()") == treat_res_choice, "The MPI profile object in D-screening, hospitalization modal doesn't take a value"

    def check_hosp_date_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HOSP_DATE}.length"), "Hospitalization date in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HOSP_DATE}.val()") == today, "Hospitalization date in D-screening, hospitalization modal doesn't take a value"

    def check_date_of_discharge_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DISCHARGE}.length"), "The Date of discharge object in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DATE_OF_DISCHARGE}.val()") == today, "The Date of discharge object  in D-screening, hospitalization modal doesn't take a value"

    def check_treatment_result_d_screening_hospitalization(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_RESULT}.length"), "Treatment result in D-screening, hospitalization modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.D_SCRN_TREAT_RESULT}.find('input').val()") == treat_outc_choice, "Treatment result in D-screening, hospitalization modal doesn't take a value"

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

