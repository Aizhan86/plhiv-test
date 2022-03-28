from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import RegisterPageLocators, PatientCardLocators, WorkJournalLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random

global patient_id_child
global patient_id_homeless
global patient_id_foreigner
global patient_id_woman

class RegisterPage(BasePage):
    gen_choice = random.choice(['female', 'male'])
    gen_choice1 = random.choice(['1', '2'])
    mo_choice = random.choice(['290000000001', '290000000002', '290000000003', '290000000004', '290000000073'])
    mo_choice1 = random.choice(['20000000025', '20000000011', '20000000012', '20000000070', '20000000135'])
    mo_choice2 = random.choice(['290000000001', '290000000002', '290000000003', '290000000004', '290000000005'])
    mo_rec_choice = random.choice(['160000000037', '290000000022', '160000000701', '160000000266', '160000000287', '160000000425'])
    locality_choice = random.choice(['170000000020', '170000000008', '170000000032', '170000000085', '170000000242', '170000000253'])
    serum_num_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    test_sys_choice = random.choice(['1', '2', '3', '4', '5', '6', '60', '61', '62'])
    aidc_center_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '28', '29'])
    test_name_choice = random.choice(['1', '2', '3', '64'])
    respon_person_choice = random.choice(['10000000011', '10000000012', '10000000022', '10000000023'])
    street_choice = random.choice(['Назарбаев', 'Абай', 'Конаев', 'Кабанбай батыр'])
    preg_medic_choice = random.choice(['1', '12', '2', '3', '4', '5', '6', '7', '8', '9', '10', '31', '211'])
    surname = ''.join(random.choices(string.ascii_uppercase, k=10))
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    midname = ''.join(random.choices(string.ascii_uppercase, k=10))
    numbers3 = ''.join(random.choices(string.digits, k=3))
    numbers4 = ''.join(random.choices(string.digits, k=4))
    numbers5 = ''.join(random.choices(string.digits, k=5))
    contacting_num = random.randint(1, 4)
    today = datetime.now().strftime('%d.%m.%Y')
    d1 = datetime.strptime('01.01.1990', '%d.%m.%Y')
    d2 = datetime.strptime('01.12.2005', '%d.%m.%Y')
    delta = d2 - d1
    int_delta = delta.days
    birthday = datetime.strftime(d1 + timedelta(randrange(int_delta)), '%d.%m.%Y')
    years_choice = random.choice(['1', '2', '3'])
    month_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '9', '11'])
    organ_mat_type_choice = random.choice(['1', '2', '3', '4', '5'])
    hiv_status_choice = random.choice(['1', '2', '3'])
    smth_random = ''.join(random.choices(string.ascii_uppercase, k=10))
    country_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '9', '11'])
    manip_emerg_date = datetime.strftime(datetime.now() - timedelta(days=200), '%d.%m.%Y')
    eighty_days_ago = datetime.strftime(datetime.now() - timedelta(days=80), '%d.%m.%Y')
    sixty_days_ago = datetime.strftime(datetime.now() - timedelta(days=60), '%d.%m.%Y')
    fifty_days_ago = datetime.strftime(datetime.now() - timedelta(days=50), '%d.%m.%Y')
    thirty_days_ago = datetime.strftime(datetime.now() - timedelta(days=30), '%d.%m.%Y')
    twenty_days_ago = datetime.strftime(datetime.now() - timedelta(days=20), '%d.%m.%Y')
    regis_date = datetime.strftime(datetime.now() - timedelta(days=50), '%d.%m.%Y')
    deregis_date = datetime.strftime(datetime.now() - timedelta(days=5), '%d.%m.%Y')
    ib_date = datetime.strftime(datetime.now() - timedelta(days=180), '%d.%m.%Y')
    diagnosis_date = datetime.strftime(datetime.now() - timedelta(days=190), '%d.%m.%Y')
    thirty_days_forward = datetime.strftime(datetime.now() + timedelta(days=30), '%d.%m.%Y')
    fifty_days_forward = datetime.strftime(datetime.now() + timedelta(days=50), '%d.%m.%Y')
    expiration_date = datetime.strftime(datetime.now() + timedelta(days=365), '%d.%m.%Y')

    def register_new_child(self):
        # автозаполнение формы регистрации для ребенка
        res_code_choice = random.choice(['47', '48', '11', '22'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        d1 = datetime.strptime('01.01.2005', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2021', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(randrange(int_delta))
        first_numbers = random_date.strftime('%y%m%d')
        p_birthday = random_date.strftime('%d.%m.%Y')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        p_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
        self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(p_surname)
        p_name = ''.join(random.choices(string.ascii_uppercase, k=6))
        self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(p_name)
        p_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*RegisterPageLocators.PATIENT_MIDNAME).send_keys(p_midname)
        # self.make(f"$('{RegisterPageLocators.BIRTH_DATE}').val('{birthday}')")
        self.make(f"$('#general_data_birth').val('{p_birthday}')")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{self.gen_choice}');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        child_status_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{RegisterPageLocators.CHILD_STATUS}.dropdown('set selected', '{child_status_choice}');")
        soc_status_choice = random.choice(['3', '4'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_AREA}.dropdown('set selected', '5');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('hide');")
        # self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_LOCALITY}.dropdown('set selected', '177');")
        self.make(f"{RegisterPageLocators.REGIS_PLACE}.dropdown('set selected', '2');")
        self.browser.find_element(*RegisterPageLocators.REGIS_STREET).send_keys(self.street_choice)
        self.browser.find_element(*RegisterPageLocators.REGIS_HOUSE).send_keys(55)
        self.browser.find_element(*RegisterPageLocators.REGIS_APT).send_keys(44)
        self.browser.find_element(*RegisterPageLocators.REGIS_PHONE_NO).send_keys(87273456987)
        self.make(f"{RegisterPageLocators.RESID_AREA}.dropdown('set selected', '3');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('hide');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_LOCALITY}.dropdown('set selected', '170000000008');")
        self.make(f"{RegisterPageLocators.RESID_PLACE}.dropdown('set selected', '2');")
        self.browser.find_element(*RegisterPageLocators.RESID_STREET).send_keys(self.street_choice)
        self.browser.find_element(*RegisterPageLocators.RESID_HOUSE).send_keys(25)
        self.browser.find_element(*RegisterPageLocators.RESID_APT).send_keys(45)
        self.browser.find_element(*RegisterPageLocators.RESID_PHONE_NO).send_keys(87273456789)
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '170000000558');")
        self.make(f"{RegisterPageLocators.RETROSPECTIVE_CHILD}.checkbox('set checked');")
        self.browser.find_element(*RegisterPageLocators.MOTHERS_SURNAME).send_keys(self.surname)
        self.browser.find_element(*RegisterPageLocators.MOTHERS_NAME).send_keys(self.name)
        self.browser.find_element(*RegisterPageLocators.MOTHERS_MIDNAME).send_keys(self.midname)
        self.browser.find_element(*RegisterPageLocators.MOTHERS_IB_NO).send_keys(self.numbers5)
        self.browser.find_element(*RegisterPageLocators.IB_NO_DATE).send_keys(self.ib_date)
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click()")
        # self.browser.take_screenshot()
        sleep(5)
        id_url = self.browser.current_url
        url_part = id_url.split('/')[5]
        global patient_id_child
        patient_id_child = url_part.split('?')[0]
        if patient_id_child == "0000000000":
            sleep(5)
            id_url = self.browser.current_url
            url_part = id_url.split('/')[5]
            patient_id_child = url_part.split('?')[0]
            print(f"ID of child patient is {patient_id_child}")
        else:
            print(f"ID of child patient is {patient_id_child}")

    def edit_card(self):
        self.make(f"{RegisterPageLocators.EDIT_REGIS_ADDRESS}.click()")
        self.browser.find_element(*RegisterPageLocators.REGIS_APT2).send_keys(77)
        self.make(f"{RegisterPageLocators.ERROR_REGIS_ADDRESS_SAVE}.click()")
        self.make(f"{RegisterPageLocators.REASON_NOT_EPID}.dropdown('set selected', '3');")
        self.make(f"{RegisterPageLocators.REASON_NOT_DISP_REG}.dropdown('set selected', '6');")
        self.make(f"{RegisterPageLocators.PATIENT_CARD_SAVE}.click()")

    def should_test_HIV_antibody_testing_OGC_modal(self):
        self.fill_HIV_antibody_testing_OGC_modal()
        self.check_HIV_antibody_testing_OGC_modal()

    def fill_HIV_antibody_testing_OGC_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IFA_OGC_ADD}.click()")
        self.make(f"{PatientCardLocators.IFA_MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.SURNAME_PERSON_MEDORG}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.REFERRAL_NO}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.BLOOD_SAMPLING_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PRODUCTION_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.SERUM_NUM}.dropdown('set selected', '{self.serum_num_choice}');")
        self.make(f"{PatientCardLocators.SERUM_NUM2}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.TEST_SYSTEM_TYPE}.dropdown('set selected', '{self.test_sys_choice}');")
        self.make(f"{PatientCardLocators.EXPIRATION_DATE}.val('{self.expiration_date}');")
        self.make(f"{PatientCardLocators.SERIES_NUM}.val('{self.numbers3}');")
        test_cat_choice = random.choice(['1', '2', '0'])
        self.make(f"{PatientCardLocators.TEST_CATEGORY}.dropdown('set selected', '{test_cat_choice}');")
        self.make(f"{PatientCardLocators.OP_CRITICAL}.val('1');")
        self.make(f"{PatientCardLocators.OP_SERUM}.val('2');")
        ifa_res_choice = random.choice(['1', '2', '3', '4'])
        self.make(f"{PatientCardLocators.IFA_RESULT}.dropdown('set selected', '{ifa_res_choice}');")
        ifa_resp_person_choice = random.choice(['290000000001', '290000000004', '290000000014', '290000000018'])
        self.make(f"{PatientCardLocators.RESPONSIBLE_PERSON}.dropdown('set selected', '{ifa_resp_person_choice}');")
        ifa_services_choice = random.choice(['127'])
        self.make(f"{PatientCardLocators.IFA_SERVICES}.dropdown('set selected', '{ifa_services_choice}');")
        self.make(f"{PatientCardLocators.IFA_OGC_SAVE}.click()")

    def check_HIV_antibody_testing_OGC_modal(self):
        assert self.is_element_present(*PatientCardLocators.IFA_OGC_EDIT), "Data in HIV antibody testing OGC modal wasn't saved or invalid selector for Edit button"

    def should_test_HIV_antibody_testing_KNCDIZ_modal(self):
        self.fill_HIV_antibody_testing_KNCDIZ_modal()
        self.check_HIV_antibody_testing_KNCDIZ_modal()

    def fill_HIV_antibody_testing_KNCDIZ_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IFA_KNCDIZ_ADD}.click()")
        self.make(f"{PatientCardLocators.SCREANING_NUM}.val('{self.numbers5}')")
        self.make(f"{PatientCardLocators.SERUM_NUM_RC}.dropdown('set selected', '{self.serum_num_choice}');")
        self.make(f"{PatientCardLocators.REFERRAL_NO_RC}.val('{self.numbers4}')")
        self.browser.find_element(*PatientCardLocators.RECEIPT_DATE_RC).send_keys(self.today)
        self.browser.find_element(*PatientCardLocators.PRODUCTION_DATE_RC).send_keys(self.today)
        self.make(f"{PatientCardLocators.TEST_SYSTEM_NAME_RC}.dropdown('set selected', '{self.test_sys_choice}');")
        self.browser.find_element(*PatientCardLocators.EXPIRATION_DATE_RC).send_keys(self.expiration_date)
        self.browser.find_element(*PatientCardLocators.SERIES_NUM_RC).send_keys(self.numbers3)
        self.browser.find_element(*PatientCardLocators.OP_CRITICAL_RC).send_keys(1)
        self.browser.find_element(*PatientCardLocators.OP_SERUM_RC).send_keys(2)
        ifa_res_rc_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.IFA_RESULT_RC}.dropdown('set selected', '{ifa_res_rc_choice}');")
        self.browser.find_element(*PatientCardLocators.IFA_RC_SAVE).click()

    def check_HIV_antibody_testing_KNCDIZ_modal(self):
        assert self.is_element_present(*PatientCardLocators.IFA_RC_EDIT), "Data in HIV antibody testing KNCDIZ modal wasn't saved or invalid selector for Edit button"

    def should_test_IB_modal(self):
        self.fill_IB_modal()
        self.check_IB_modal()

    def fill_IB_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IB_PCR}.click()")
        self.make(f"{PatientCardLocators.IB_ADD}.click()")
        self.make(f"{PatientCardLocators.IB_NUMBER}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.IB_SERUM_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.SAMPLE_NUM}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.IB_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.IB_REGISTER_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.IB_RESULT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.TEST_SYSTEM_NAME}.dropdown('set selected', '{self.test_name_choice}');")
        self.make(f"{PatientCardLocators.IB_EXPIRATION_DATE}.val('{self.expiration_date}');")
        self.make(f"{PatientCardLocators.IB_SERIES_NUM}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.IB_RESPONSIBLE_PERSON}.dropdown('set selected', '{self.respon_person_choice}');")
        gp160 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.GP160}.dropdown('set selected', '{gp160}');")
        gp110_120 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.GP110_120}.dropdown('set selected', '{gp110_120}');")
        p68 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P68}.dropdown('set selected', '{p68}');")
        p55 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P55}.dropdown('set selected', '{p55}');")
        p52 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P52}.dropdown('set selected', '{p52}');")
        gp41 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.GP41}.dropdown('set selected', '{gp41}');")
        p40 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P40}.dropdown('set selected', '{p40}');")
        p34 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P34}.dropdown('set selected', '{p34}');")
        p25 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P25}.dropdown('set selected', '{p25}');")
        p18 = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.P18}.dropdown('set selected', 'p18');")
        self.make(f"{PatientCardLocators.IB_SERVICES}.dropdown('set selected', '234');")
        self.make(f"{PatientCardLocators.IB_SAVE}.click()")

    def check_IB_modal(self):
        assert self.is_element_present(*PatientCardLocators.IB_EDIT), "Data in IB modal wasn't saved or invalid selector for Edit button"


    def should_test_PCR_modal(self):
        self.fill_PCR_modal()
        self.check_PCR_modal()

    def fill_PCR_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.IB_PCR}.click()")
        self.make(f"{PatientCardLocators.PCR_ADD}.click()")
        self.make(f"{PatientCardLocators.PCR_NUMBER}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.PCR_SERUM_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.PCR_SAMPLE_NUM}.val('{self.numbers3}');")
        type_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.PCR_TYPE}.dropdown('set selected', '{type_choice}');")
        self.make(f"{PatientCardLocators.PCR_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PCR_REGISTER_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PCR_TEST_SYSTEM_NAME}.dropdown('set selected', '{self.test_name_choice}');")
        self.make(f"{PatientCardLocators.PCR_EXPIRATION_DATE}.val('{self.expiration_date}');")
        self.make(f"{PatientCardLocators.PCR_SERIES_NUM}.val('{self.numbers3}');")
        if type_choice == 1:
            self.make(f"{PatientCardLocators.PCR_DNA_RESULT}.dropdown('set selected', '1');")
        else:
            self.make(f"{PatientCardLocators.PCR_RNA_RESULT}.val('положительный');")
        self.make(f"{PatientCardLocators.PCR_RESPONSIBLE_PERSON}.dropdown('set selected', '{self.respon_person_choice}');")
        if type_choice == 1:
            self.make(f"{PatientCardLocators.PCR_SERVICES}.dropdown('set selected', '262');")
        else:
            self.make(f"{PatientCardLocators.PCR_SERVICES}.dropdown('set selected', '263');")
        self.make(f"{PatientCardLocators.PCR_SAVE}.click()")

    def check_PCR_modal(self):
        assert self.is_element_present(*PatientCardLocators.PCR_EDIT), "Data in PCR modal wasn't saved or invalid selector for Edit button"

    def should_test_result_modal(self):
        self.fill_result_modal()
        self.check_result_modal()

    def fill_result_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.LAB_RESEARCH}.click()")  # Открываем Эпидемиологический анамнез
        self.make(f"{PatientCardLocators.RESULT}.click()")
        self.make(f"{PatientCardLocators.RESULT_ADD}.click()")
        self.make(f"{PatientCardLocators.RESULT_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.RESULT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.RESULT_RESPONSIBLE_PERSON}.dropdown('set selected', '{self.respon_person_choice}');")
        self.make(f"{PatientCardLocators.LAB_SUPERVISER}.dropdown('set selected', '{self.respon_person_choice}');")
        result_choice = random.choice(['7', '9', '12', '14', '19'])
        self.make(f"{PatientCardLocators.ANALYSIS_RESULT}.dropdown('set selected', '{result_choice}');")
        self.make(f"{PatientCardLocators.RESEARCH_BAZIS}.click()")
        self.make(f"{PatientCardLocators.RESULT_SAVE}.click()")

    def check_result_modal(self):
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in Result modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('zaklyuchenie_NIB').get_attribute("data-field") == self.numbers5, "Data in Result modal or object Result Number weren't saved"
        # assert self.is_element_present(*PatientCardLocators.RESULT_PRINT), "Data in Result modal wasn't saved or Print object isn't clickable"

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
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_LASTNAME).send_keys(self.surname)
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_NAME).send_keys(self.name)
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_MIDDLE_NAME).send_keys(self.midname)
        self.make(f"{PatientCardLocators.FAMILY_MEM_GENDER}.dropdown('set selected', '{self.gen_choice1}');")
        self.make(f"$('#fam_members_birth_modal').val('{self.birthday}')")
        self.browser.find_element(*PatientCardLocators.FAMILY_MEM_ADDRESS).send_keys(self.street_choice)
        self.make(f"{PatientCardLocators.FAMILY_MEM_HIV_STATUS}.dropdown('set selected', '1');")
        fam_mem_rel_choice = random.choice(['10', '9', '11'])
        self.make(f"{PatientCardLocators.FAMILY_MEM_RELATION}.dropdown('set selected', '{fam_mem_rel_choice}');")
        self.make(f"{PatientCardLocators.FAMILY_MEM_SAVE}.click()")
        self.make(f"{PatientCardLocators.EPID_HISTORY_FILLING_DATE}.val('{self.today}')")
        epid_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А.', 'НАУШАБЕКОВА Ж.', 'ДАРМЕНОВА Р. М.'])
        self.make(f"{PatientCardLocators.EPID_DOCTOR}.dropdown('set selected', '{epid_doc_choice}');")

    def check_family_members_modal(self):
        assert self.is_element_present(*PatientCardLocators.FAMILY_MEM_EDIT), "Data in Family members modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('fam_members_surname').get_attribute("data-field") == self.surname, "Data in Family members modal or object Result Family member's surname weren't saved"

    def should_test_luin_modal(self):
        self.fill_luin_modal()
        # self.check_luin_modal()

    def fill_luin_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.LUIN_RS}.click();")
        self.make(f"{PatientCardLocators.DRUG_EXPERIENCE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_IN_TWELVE_MONTH}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.DRUG_USE_YEARS}.val('{self.years_choice}');")
        self.make(f"{PatientCardLocators.DRUG_USE_MONTH}.val('{self.month_choice}');")
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
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_YEARS}.val('{self.years_choice}');")
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_EXP_MONTH}.val('{self.month_choice}');")
        com_sex_partners_choice = random.choice(['10', '20', '30', '14', '25', '36', '27', '18', '39', '17'])
        self.make(f"{PatientCardLocators.COMMERCIAL_SEX_PARTNER_NUM}.val('{com_sex_partners_choice}');")
        self.make(f"{PatientCardLocators.CONDOM_USAGE}.dropdown('set selected', '1');")
        self.browser.find_element(*PatientCardLocators.LUIN_RS_SAVE).click()

    def check_luin_modal(self):
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in LUIN/RS modal wasn't saved or invalid selector for Edit button"
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
        assert self.is_element_present(*PatientCardLocators.RESULT_EDIT), "Data in HIV antibody testing RESULT modal wasn't saved or invalid selector for Edit button"
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
        assert self.is_element_present(*PatientCardLocators.MLS_EDIT), "Data in MLS modal wasn't saved or invalid selector for Edit button"
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
        self.make(f"{PatientCardLocators.BLOOD_DONATION_LOCALITY}.dropdown('set selected', '{self.locality_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        blood_don_cat_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CATEGORY}.dropdown('set selected', '{blood_don_cat_choice}');")
        blood_don_type_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.BLOOD_DONOR_TYPE}.dropdown('set selected', '{blood_don_type_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_DONATION_CODE}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_SAVE}.click();")

    def check_blood_donor_modal(self):
        assert self.is_element_present(*PatientCardLocators.BLOOD_DONOR_EDIT), "Data in Blood Donor modal modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

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
        self.make(f"{PatientCardLocators.ORGAN_DONATION_LOCALITY}.dropdown('set selected', '{self.locality_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONATION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        organ_don_cat_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ORGAN_DONATION_CATEGORY}.dropdown('set selected', '{organ_don_cat_choice}');")
        organ_don_type_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ORGAN_DONOR_TYPE}.dropdown('set selected', '{organ_don_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE}.dropdown('set selected', '{self.organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_MED_ORG}.dropdown('set selected', '{self.mo_rec_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_ANALYSIS_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_SAVE}.click();")

    def check_organ_donor_modal(self):
        assert self.is_element_present(*PatientCardLocators.ORGAN_DONOR_EDIT), "Data in Organ Donor modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_blood_recipient_modal(self):
        self.fill_blood_recipient_modal()
        self.check_blood_recipient_modal()

    def fill_blood_recipient_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.BLOOD_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_LOCALITY}.dropdown('set selected', '{self.locality_choice}');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.BLOOD_TRANSFUSION_MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.EPID_HISTORY_NUM_REC}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.BLOOD_DONOR_CODE_REC}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.BLOOD_COMPONENT_CODE_REC}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.BLOOD_HIV_STATUS_REC}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.BLOOD_RECEIPT_SAVE}.click();")

    def check_blood_recipient_modal(self):
        assert self.is_element_present(*PatientCardLocators.BLOOD_RECEIPT_EDIT), "Data in Blood donor modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_organ_recipient_modal(self):
        self.fill_organ_recipient_modal()
        self.check_organ_recipient_modal()

    def fill_organ_recipient_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT}.click();")
        self.make(f"{PatientCardLocators.ORGAN_RECIPIENT_ADD}.click();")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_PLACE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_LOCALITY}.dropdown('set selected', '{self.locality_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MED_ORG_REC}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_MED_ORG}.dropdown('set selected', '{self.mo_rec_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_TRANSFUSION_DATE}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_NO_REC}.val('{self.numbers3}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_MAT_TYPE_REC}.dropdown('set selected', '{self.organ_mat_type_choice}');")
        self.make(f"{PatientCardLocators.ORGAN_DONOR_NAME}.val('01.01.2021');")
        self.make(f"{PatientCardLocators.ORGAN_HIV_STATUS_REC}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ORGAN_RECEIPT_SAVE}.click();")

    def check_organ_recipient_modal(self):
        assert self.is_element_present(*PatientCardLocators.ORGAN_RECEIPT_EDIT), "Data in Organ recipient modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('recipient_other_material_date_poluch_mater').get_attribute("data-field") == '01.01.2021', "Data in Organ recipient modal or object Organ transfusion date weren't saved"

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
        self.make(f"{PatientCardLocators.DK_CONTACTING_NUM_YEAR}.val('{self.contacting_num}');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PRIVATE_CLINICS_CONTACTING_NUM}.val('{self.contacting_num}');")
        self.make(f"{PatientCardLocators.IPPP_SYMPTOM_ADD}.click();")
        self.make(f"{PatientCardLocators.DIAGNOSIS_DATE}.calendar('set date', '{self.diagnosis_date}');")
        self.make(f"{PatientCardLocators.DIAGNOSIS}.val('{self.smth_random}');")
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
        assert self.is_element_present(*PatientCardLocators.IPPP_SYMPTOM_EDIT), "Data in IPPP modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('ippp_diag_diagnoz').get_attribute("data-field") == self.smth_random, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_manipulations_modal(self):
        self.fill_manipulations_modal()
        self.check_manipulations_modal()

    def fill_manipulations_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.MANIPULATION_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_ADD}.click();")
        self.make(f"{PatientCardLocators.MANIPULATIONS_DATE}.calendar('set date', '{self.manip_emerg_date}');")
        manip_sort_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.MANIPULATIONS_SORT}.dropdown('set selected', '{manip_sort_choice}');")
        manip_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '9', '11'])
        self.make(f"{PatientCardLocators.MANIPULATIONS_TYPE}.dropdown('set selected', '{manip_type_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.MANIPULATIONS_SAVE}.click();")

    def check_manipulations_modal(self):
        assert self.is_element_present(*PatientCardLocators.MANIPULATIONS_EDIT), "Data in Manipulations modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('manipulations_med_spr_type_vmeshat_id').get_attribute("data-field") == "{manip_sort_choice}", "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_emergencies_modal(self):
        self.fill_emergencies_modal()
        self.check_emergencies_modal()

    def fill_emergencies_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.MANIPULATIONS_EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES_ADD}.click();")
        self.make(f"{PatientCardLocators.EMERGENCIES_DATE}.calendar('set date', '{self.manip_emerg_date}');")
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
        assert self.is_element_present(*PatientCardLocators.EMERGENCIES_EDIT), "Data in Emergencies modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_departure_modal(self):
        self.fill_departure_modal()
        self.check_departure_modal()

    def fill_departure_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_ADD}.click();")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_START}.calendar('set date', '{self.eighty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_DATE_END}.calendar('set date', '{self.sixty_days_ago}');")
        self.make(f"{PatientCardLocators.DEPARTURE_COUNTRY}.dropdown('set selected', '{self.country_choice}');")
        purpose_choice = random.choice(['1', '2', '3', '4', '5', '6'])
        self.make(f"{PatientCardLocators.DEPARTURE_PURPOSE}.dropdown('set selected', '{purpose_choice}');")
        self.make(f"{PatientCardLocators.DEPARTURE_SAVE}.click();")

    def check_departure_modal(self):
        assert self.is_element_present(*PatientCardLocators.DEPARTURE_EDIT), "Data in Departure modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_source_modal(self):
        self.fill_source_modal()
        self.check_source_modal()

    def fill_source_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.DEPARTURES_SOURCES}.click();")
        self.make(f"{PatientCardLocators.INFECTION_SOURCE_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.SOURCE_ADD}.click();")
        self.make(f"{PatientCardLocators.SOURCE_IB_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.SOURCE_IB_DATE}.calendar('set date', '{self.ib_date}');")
        self.make(f"{PatientCardLocators.SOURCE_SURNAME}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.SOURCE_NAME}.val('{self.name}');")
        self.make(f"{PatientCardLocators.SOURCE_MIDDLE_NAME}.val('{self.midname}');")
        self.make(f"{PatientCardLocators.SOURCE_SAVE}.click();")

    def check_source_modal(self):
        assert self.is_element_present(*PatientCardLocators.SOURCE_EDIT), "Data in Source modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_contact_person_modal(self):
        self.fill_contact_person_modal()
        self.check_contact_person_modal()

    def fill_contact_person_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.EPID_HISTORY}.click()")
        self.make(f"{PatientCardLocators.CONTACT_PERSON}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_EXISTENCE}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_ADD}.click();")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_SURNAME}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_NAME}.val('{self.name}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_MIDDLE_NAME}.val('{self.midname}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_GENDER}.dropdown('set selected', '{self.gen_choice1}');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_BIRTHDAY}.val('{self.birthday}');")
        self.make(f"{PatientCardLocators.CONTACT_DATE_START}.val('{self.fifty_days_ago}');")
        contact_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
        self.make(f"{PatientCardLocators.CONTACT_TYPE}.dropdown('set selected', '{contact_type_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_IB_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.CONTACT_IB_NUM_DATE}.val('{self.ib_date}');")
        self.make(f"{PatientCardLocators.CONTACT_SURVEY_ADD}.click();")
        self.make(f"{PatientCardLocators.CONTACT_DIAGNOSTICS_DATE}.calendar('set date', '{self.diagnosis_date}');")
        contact_hiv_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.CONTACT_HIV_STATUS}.dropdown('set selected', '{contact_hiv_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_SURVEY_SAVE}.click();")
        contact_hiv_status = self.make(f"$('#obsled_state').attr('data-field')")
        if contact_hiv_status == "3":
            con_reason_not_surv_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
            self.make(f"{PatientCardLocators.REASON_NOT_SURVEYING}.dropdown('set selected', '{con_reason_not_surv_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_FINISHED}.click();")
        self.make(f"{PatientCardLocators.CONTACT_DAY_END}.val('{self.twenty_days_ago}');")
        self.make(f"{PatientCardLocators.CONTACT_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.click();")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.CONTACT_UNIT_AREA}.dropdown('hide');")
        self.make(f"{PatientCardLocators.CONTACT_LOCALITY}.dropdown('set selected', '{self.locality_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_STREET}.val('{self.street_choice}');")
        self.make(f"{PatientCardLocators.CONTACT_HOUSE}.val('55');")
        self.make(f"{PatientCardLocators.CONTACT_APT}.val('47');")
        self.make(f"{PatientCardLocators.CONTACT_PHONE_NO}.val('87279876543');")
        self.make(f"{PatientCardLocators.CONTACT_PERSON_SAVE}.click();")

    def check_contact_person_modal(self):
        assert self.is_element_present(*PatientCardLocators.CONTACT_PERSON_EDIT), "Data in HIV antibody testing Contact Person modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_dispensary_observation_modal(self):
        self.fill_dispensary_observation_modal()
        self.check_dispensary_observation_modal()

    def fill_dispensary_observation_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();") # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")
        self.make(f"{PatientCardLocators.D_OBSER_AIDC_CENTER}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.DATE_OF_REGIS}.calendar('set date', '{self.regis_date}');")
        self.make(f"{PatientCardLocators.D_OBSER_SAVE}.click();")
        drug_cons_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.DRUG_INJ_CONSUMPTION}.dropdown('set selected', '{drug_cons_choice}');")
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_YEAR}.val('2');")
        drug_regis_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_REGIS}.dropdown('set selected', '{drug_regis_choice}');")
        alc_cons_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ALCOHOL_CONSUMPTION}.dropdown('set selected', '{alc_cons_choice}');")
        self.make(f"{PatientCardLocators.OUTPATIENT_CARD_NO}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.DISP_START_DATE}.calendar('set date', '{self.sixty_days_ago}');")
        disp_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А ', 'КЕНЖЕЕВА Г ', 'НАУШАБЕКОВА Ж '])
        self.make(f"{PatientCardLocators.DISP_DOCTORS_NAME}.dropdown('set selected', '{disp_doc_choice}');")
        self.make(f"{PatientCardLocators.DISP_SAVE_BTN}.click();")

    def check_dispensary_observation_modal(self):
        assert self.is_element_present(*PatientCardLocators.DISP_OBSER_EDIT), "Data in Dispensary Observation modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('duchet_country').get_attribute("data-field") == '4', "Data in Blood donor modal or object Blood donor code weren't saved"
        # assert self.browser.find_element_by_id('patient_ambulator_card').get_attribute("data-value") == {self.numbers4}, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_dispensary_observation_modal_when_patient_deregistered(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.DISP_OBSER_ADD}.click();")
        self.make(f"{PatientCardLocators.D_OBSER_AIDC_CENTER}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{PatientCardLocators.DATE_OF_REGIS}.calendar('set date', '{self.regis_date}');")
        self.make(f"{PatientCardLocators.DATE_OF_DEREGIS}.calendar('set date', '{self.deregis_date}');")
        reason_deregis_choice = random.choice(['1', '2', '3', '4', '8', '9', '10'])
        self.make(f"{PatientCardLocators.D_OBSER_REASON_OF_DEREGIS}.dropdown('set selected', '{reason_deregis_choice}');")
        self.make(f"{PatientCardLocators.D_OBSER_COUNTRY}.dropdown('set selected', '{self.country_choice}');")
        self.make(f"{PatientCardLocators.D_OBSER_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.focus();")
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA_CLICK}.click();")
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('hide');")
        self.make(f"{PatientCardLocators.D_OBSER_UNIT_AREA}.dropdown('set selected', '33');")
        if reason_deregis_choice == 1:
            self.make(f"{PatientCardLocators.DATE_OF_DEATH}.calendar('set date', '{self.deregis_date}');")
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
        drug_regis_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.DRUG_CONSUMPTION_REGIS}.dropdown('set selected', '{drug_regis_choice}');")
        alc_cons_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ALCOHOL_CONSUMPTION}.dropdown('set selected', '{alc_cons_choice}');")
        self.make(f"{PatientCardLocators.OUTPATIENT_CARD_NO}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.DISP_START_DATE}.calendar('set date', '{self.sixty_days_ago}');")
        disp_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А ', 'КЕНЖЕЕВА Г ', 'НАУШАБЕКОВА Ж '])
        self.make(f"{PatientCardLocators.DISP_DOCTORS_NAME}.dropdown('set selected', '{disp_doc_choice}');")
        self.make(f"{PatientCardLocators.DISP_SAVE_BTN}.click();")
        # assert self.browser.find_element_by_id('duchet_reason').get_attribute("data-value") == {reason_deregis_choice}, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_perinatal_registration_modal(self):
        self.fill_perinatal_registration_modal()
        self.check_perinatal_registration_modal()

    def fill_perinatal_registration_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_REGIS_ADD}.click();")
        self.make(f"{PatientCardLocators.PERINATAL_MED_ORG}.dropdown('set selected', '{self.aidc_center_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_REGIS}.calendar('set date', '{self.regis_date}');")
        self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEREGIS}.calendar('set date', '{self.deregis_date}');")
        reason_deregis_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.PERINATAL_REASON_OF_DEREGIS}.dropdown('set selected', '{reason_deregis_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_COUNTRY}.dropdown('set selected', '{self.country_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_AREA}.dropdown('set selected', '3');")
        self.make(f"{PatientCardLocators.PERINATAL_UNIT_AREA}.dropdown('set selected', '33');")
        if reason_deregis_choice == 4:
            self.make(f"{PatientCardLocators.PERINATAL_DATE_OF_DEATH}.calendar('set date', '{self.deregis_date}');")
            death_choice = random.choice(['1', '2', '13', '4', '17', '18', '12'])
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_REASON}.dropdown('set selected', '{death_choice}');")
            death_place_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
            self.make(f"{PatientCardLocators.PERINATAL_DEATH_PLACE}.dropdown('set selected', '{death_place_choice}');")
        self.make(f"{PatientCardLocators.PERINATAL_SAVE}.click();")

    def check_perinatal_registration_modal(self):
        assert self.is_element_present(*PatientCardLocators.DISP_OBSER_EDIT), "Data in Dispensary Observation modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_arv_prophylaxis_modal(self):
        self.fill_arv_prophylaxis_modal()
        self.check_arv_prophylaxis_modal()

    def fill_arv_prophylaxis_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.PERINATAL_REGISTRATION}.click();")
        arv_proph_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ARV_PROPHYLAXIS}.dropdown('set selected', '{arv_proph_choice}');")
        self.make(f"{PatientCardLocators.ARV_START_DATE}.val('{self.eighty_days_ago}');")
        # self.make(f"{PatientCardLocators.ARV_END_DATE}.calendar('set date', '{self.fifty_days_ago}');")
        medication_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '201', '216'])
        self.make(f"{PatientCardLocators.ARV_MEDICATION}.dropdown('set selected', '{medication_choice}');")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME_CHOICE}.click();")
        #self.make(f"$('#add-row-preparaty-table tr:eq(0) td:eq(0) a').click();")
        self.make(f"{PatientCardLocators.ARV_RECIPE_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.ARV_DAY_NUM}.val('30');")
        self.make(f"{PatientCardLocators.ARV_NEXT_DATE}.calendar('set date', '{self.thirty_days_forward}');")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_SAVE}.click();")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.calendar('set date', '{self.fifty_days_ago}');")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.calendar('set date', '{self.thirty_days_ago}');")
        arv_hiv_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ARV_HIV_STATUS}.dropdown('set selected', '{arv_hiv_choice}');")
        self.make(f"{PatientCardLocators.ARV_HIV_DETERMINATION_DATE}.calendar('set date', '{self.fifty_days_ago}');")

    def check_arv_prophylaxis_modal(self):
        assert self.is_element_present(*PatientCardLocators.RECOM_CONSULTATION_EDIT), "Data in Recommended Consultation modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_hiv_diagnosis_modal(self):
        self.fill_hiv_diagnosis_modal()
        self.check_hiv_diagnosis_modal()

    def fill_hiv_diagnosis_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_ADD}.click();")
        self.make(f"{PatientCardLocators.FORMULATING_CHANGE_DATE}.val('{self.thirty_days_ago}');")
        hiv_stage_choice = random.choice(['1', '2', '3', '4'])
        self.make(f"{PatientCardLocators.HIV_STAGE}.dropdown('set selected', '{hiv_stage_choice}');")
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS_SAVE}.click();")

    def check_hiv_diagnosis_modal(self):
        assert self.is_element_present(*PatientCardLocators.HIV_DIAGNOSIS_EDIT), "Data in HIV Diagnosis modal wasn't saved or invalid selector for Edit button"

    def should_test_hiv_related_disease_modal(self):
        self.fill_hiv_related_disease_modal()
        self.check_hiv_related_disease_modal()

    def fill_hiv_related_disease_modal(self):
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_ADD}.click();")
        self.make(f"{PatientCardLocators.RELATED_DISEASE_HIV_STAGE}.click();")
        self.make(f"{PatientCardLocators.RELATED_DISEASE_HIV_STAGE_CHOICE}.click();")
        self.make(f"{PatientCardLocators.DISEASE_START_DATE}.val('{self.thirty_days_ago}');")
        self.make(f"{PatientCardLocators.DISEASE_END_DATE}.val('{self.twenty_days_ago}');")
        disease_name_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '33', '27'])
        self.make(f"{PatientCardLocators.DISEASE_NAME}.dropdown('set selected', '{disease_name_choice}');")
        self.make(f"{PatientCardLocators.HIV_RELATED_DISEASE_SAVE}.click();")

    def check_hiv_related_disease_modal(self):
        assert self.is_element_present(*PatientCardLocators.HIV_RELATED_DISEASE_EDIT), "Data in HIV Related Disease modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('add_row_hiv_table').get_attribute("action-type") == 'edit', "Data in HIV diagnosis modal wasn't saved"
        # assert self.browser.find_element_by_id('add_row_diag_opurt_table').get_attribute("action-type") == 'edit', "Data in HIV related diseas modal wasn't saved"

    def should_test_recommended_consultation_modal(self):
        self.fill_recommended_consultation_modal()
        self.check_recommended_consultation_modal()

    def fill_recommended_consultation_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_ADD}.click();")
        self.make(f"{PatientCardLocators.CONSULTATION_DATE}.calendar('set date', '{self.thirty_days_forward}');")
        consultation_choice = random.choice(['325', '340', '13', '337', '308', '310', '312'])
        self.make(f"{PatientCardLocators.CONSULTATION}.dropdown('set selected', '{consultation_choice}');")
        self.make(f"{PatientCardLocators.CONSULTATION_DESCRIPTION}.val('Положительный');")
        self.make(f"{PatientCardLocators.RECOM_CONSULTATION_SAVE}.click();")

    def check_recommended_consultation_modal(self):
        assert self.is_element_present(*PatientCardLocators.RECOM_CONSULTATION_EDIT), "Data in Recommended Consultation modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('add_row_recomended_consultation_table').get_attribute("action-type") == 'edit', "Data in Recommended consultation modal wasn't saved"

    def should_test_recommended_screening_modal(self):
        self.fill_recommended_screening_modal()
        self.check_recommended_screening_modal()

    def fill_recommended_screening_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.RECOM_SCREENING_ADD}.click();")
        self.make(f"{PatientCardLocators.SCREENING_DATE}.calendar('set date', '{self.thirty_days_forward}');")
        survey_choice = random.choice(['53', '175', '281', '384', '426', '517', '525'])
        self.make(f"{PatientCardLocators.SURVEY}.dropdown('set selected', '{survey_choice}');")
        self.make(f"{PatientCardLocators.SCREENING_DESCRIPTION}.val('Положительный');")
        self.make(f"{PatientCardLocators.RECOM_SCREENING_SAVE}.click();")

    def check_recommended_screening_modal(self):
        assert self.is_element_present(*PatientCardLocators.RECOM_SCREENING_EDIT), "Data in Recommended Screening modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('add_row_recomended_obsled_table').get_attribute("action-type") == 'edit', "Data in Recommended screening modal wasn't saved"

    def should_test_referral_modal(self):
        self.fill_referral_modal()
        self.check_referral_modal()

    def fill_referral_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.HIV_DIAGNOSIS}.click();")
        self.make(f"{PatientCardLocators.REFERRAL_ADD}.click();")
        self.make(f"{PatientCardLocators.REFERRAL_DATE}.calendar('set date', '{self.today}');")
        referral_name_choice = random.choice(['178', '35', '36', '37', '38', '40', '46'])
        self.make(f"{PatientCardLocators.REFERRAL_NAME}.dropdown('set selected', '{referral_name_choice}');")
        self.make(f"{PatientCardLocators.REFERRAL_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.SENDER_ORG}.dropdown('set selected', '{self.mo_choice2}');")
        self.make(f"{PatientCardLocators.RECIPIENT_ORG}.dropdown('set selected', '{self.mo_choice2}');")
        category_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])
        self.make(f"{PatientCardLocators.CATEGORY}.dropdown('set selected', '{category_choice}');")
        self.make(f"{PatientCardLocators.NOSOLOGY}.click();")
        self.make(f"{PatientCardLocators.NOSOLOGY_CHOICE}.click();")
        # self.make(f"{PatientCardLocators.SURVEY_ELEMENTS}.val('Не знаю');")
        # self.make(f"{PatientCardLocators.SCREENING_RESULT}.val('Положительный');")
        self.make(f"{PatientCardLocators.REFERRAL_SAVE}.click();")

    def check_referral_modal(self):
        assert self.is_element_present(*PatientCardLocators.REFERRAL_EDIT), "Data in Referral modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('add_row_refferals_table').get_attribute("action-type") == 'edit', "Data in Referral modal wasn't saved"

    def should_test_cd4_modal(self):
        self.fill_cd4_modal()
        self.check_cd4_modal()

    def fill_cd4_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CD4_VL_SURVEY}.click();")
        self.make(f"{PatientCardLocators.CD4_DETERMINATION_ADD}.click();")
        self.make(f"{PatientCardLocators.REGISTRATION_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.CD4_BLOOD_DONOR_MED_ORG}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.CD4_MATERIAL_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.CD4_SAMPLE_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.CD4_REGISTERING_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.CD4}.val('1');")
        self.make(f"{PatientCardLocators.CD3}.val('2');")
        self.make(f"{PatientCardLocators.CD8}.val('2');")
        self.make(f"{PatientCardLocators.CD4_CD8}.val('2');")
        self.make(f"{PatientCardLocators.CD4_rate}.val('2');")
        self.make(f"{PatientCardLocators.CD4_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.CD4_REMARK}.val('Положительный');")
        service_choice = random.choice(['304', '238'])
        self.make(f"{PatientCardLocators.CD4_SERVICES}.dropdown('set selected', '{service_choice}');")
        self.make(f"{PatientCardLocators.CD4_SAVE}.click();")

    def check_cd4_modal(self):
        assert self.is_element_present(*PatientCardLocators.CD4_EDIT), "Data in CD4 Determination modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('obsled_cd4_lab_N_registr').get_attribute("data-field") == self.numbers5, "Data in CD4 modal weren't saved"

    def should_test_viral_load_modal(self):
        self.fill_viral_load_modal()
        self.check_viral_load_modal()

    def fill_viral_load_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CD4_VL_SURVEY}.click();")
        self.make(f"{PatientCardLocators.VIRAL_LOAD_ADD}.click();")
        self.make(f"{PatientCardLocators.VL_ANALYSIS_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.VL_DONOR_MED_ORG}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VL_MATERIAL_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.VL_MATERIAL_SAMPLING_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.VL_REGISTERING_DATE}.val('{self.today}');")
        vl_res_choice = random.choice(['0', '1', '2'])
        self.make(f"{PatientCardLocators.VL_RESULT}.dropdown('set selected', '{vl_res_choice}');")
        vl_res_ml_choice = random.randint(150, 500)
        self.make(f"{PatientCardLocators.VL_RESULT_ML}.val('{vl_res_ml_choice}');")
        self.make(f"{PatientCardLocators.LOG}.val('2');")
        self.make(f"{PatientCardLocators.VL_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{self.mo_choice1}');")
        remark_choice = random.choice(['Плановое обследование', 'Внелановое обследование'])
        self.make(f"{PatientCardLocators.VL_REMARK}.dropdown('set selected', '{remark_choice}');")
        vl_service_choice = random.choice(['242', '263'])
        self.make(f"{PatientCardLocators.VL_SERVICES}.dropdown('set selected', '{vl_service_choice}');")
        self.make(f"{PatientCardLocators.VL_SAVE}.click();")

    def check_viral_load_modal(self):
        assert self.is_element_present(*PatientCardLocators.VL_EDIT), "Data in VL modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('vn_N_isledov').get_attribute("data-field") == self.numbers5, "Data in Viral load modal weren't saved"

    def should_test_vgv_modal(self):
        self.fill_vgv_modal()
        self.check_vgv_modal()

    def fill_vgv_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGV_ADD}.click();")
        self.make(f"{PatientCardLocators.VGV_REGISTRATION_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.VGV_MAT_DONOR_MED_ORG}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VGV_MATERIAL_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.VGV_REGISTERING_DATE}.val('{self.today}');")
        marker_choice = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        self.make(f"{PatientCardLocators.MARKER}.dropdown('set selected', '{marker_choice}');")
        self.make(f"{PatientCardLocators.VGV_RESULT}.dropdown('set selected', '1');")
        # self.make(f"{PatientCardLocators.VGV_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VGV_REMARK}.val('Положительный');")
        self.make(f"{PatientCardLocators.VGV_SAVE}.click();")

    def check_vgv_modal(self):
        assert self.is_element_present(*PatientCardLocators.VGV_EDIT), "Data in VGV analysis modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('vgv_disp_table').get_attribute(
        #     "action-type") == 'edit', "Data in VGV modal weren't preserved"

    def should_test_vgs_modal(self):
        self.fill_vgs_modal()
        self.check_vgs_modal()

    def fill_vgs_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGS_ADD}.click();")
        self.make(f"{PatientCardLocators.VGS_REGISTRATION_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.VGS_MAT_DONOR_MED_ORG}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VGS_MATERIAL_RECEIPT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.VGS_REGISTERING_DATE}.val('{self.today}');")
        analysis_choice = random.choice([ '1', '2', '3', '4'])
        self.make(f"{PatientCardLocators.VGS_ANALYSIS_TYPE}.dropdown('set selected', '{analysis_choice}');")
        self.make(f"{PatientCardLocators.VGS_RESULT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.VGS_MED_ORG_PROVIDED_ANALYSIS}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VGS_REMARK}.val('Положительный');")
        self.make(f"{PatientCardLocators.VGS_SAVE}.click();")

    def check_vgs_modal(self):
        assert self.is_element_present(*PatientCardLocators.VGS_EDIT), "Data in VGS analysis modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('vgc-').get_attribute(
        #     "action-type") == 'edit', "Data in VGS modal weren't preserved"

    def should_test_vgv_vac_modal(self):
        self.fill_vgv_vac_modal()
        self.check_vgv_vac_modal()

    def fill_vgv_vac_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.VIRAL_HEPATITIS}.click();")
        self.make(f"{PatientCardLocators.VGV_VAC_ADD}.click();")
        vac_multi_choice = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        self.make(f"{PatientCardLocators.VGV_VAC_MULTIPLICITY}.dropdown('set selected', '{vac_multi_choice}');")
        self.make(f"{PatientCardLocators.IMMUNIZATION_DATE}.calendar('set date', '{self.today}');")
        dose = random.choice(['5', '10', '15'])
        self.make(f"{PatientCardLocators.VGV_VAC_DOSE_VOLUME}.val('{dose}');")
        self.make(f"{PatientCardLocators.VGV_VAC_SERIES}.val('{self.numbers5}');")
        vac_multi_choice = random.choice(['США', 'Казахстан', 'Россия', 'Китай', 'Южная Корея', 'Индия', 'Япония', 'Германия', 'Турция'])
        self.make(f"{PatientCardLocators.VGV_VAC_COUNTRY_PRODUCER}.val('{vac_multi_choice}');")
        self.make(f"{PatientCardLocators.MED_ORG_PROVIDED_VACCINATION}.dropdown('set selected', '{self.mo_choice1}');")
        self.make(f"{PatientCardLocators.VGV_VAC_SAVE}.click();")

    def check_vgv_vac_modal(self):
        assert self.is_element_present(*PatientCardLocators.VGV_VAC_EDIT), "Data in VGV Vaccination modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('vgv_vakcin_disp_table').get_attribute(
        #     "action-type") == 'edit', "Data in VGV vaccination modal weren't preserved"

    def should_test_fluoroscopy_and_radiography_modals(self):
        self.fill_fluoroscopy_and_radiography_modals()
        self.check_fluoroscopy_and_radiography_modals()

    def fill_fluoroscopy_and_radiography_modals(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.TUBERCULOSIS}.click();")
        self.make(f"{PatientCardLocators.FLUOROSCOPY_ADD}.click();")
        self.make(f"{PatientCardLocators.FLUOR_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        fluor_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.FLUOR_RESULT}.dropdown('set selected', '{fluor_choice}');")
        self.make(f"{PatientCardLocators.FLUOROSCOPY_SAVE}.click();")

        self.make(f"{PatientCardLocators.RADIOGRAPHY_ADD}.click();")
        self.make(f"{PatientCardLocators.RADIO_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        radio_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.RADIO_RESULT}.dropdown('set selected', '{radio_choice}');")
        self.make(f"{PatientCardLocators.RADIOGRAPHY_SAVE}.click();")

    def check_fluoroscopy_and_radiography_modals(self):
        assert self.is_element_present(*PatientCardLocators.FLUOROSCOPY_EDIT), "Data in Fluoroscopy modal wasn't saved or invalid selector for Edit button"
        assert self.is_element_present(*PatientCardLocators.RADIOGRAPHY_EDIT), "Data in Radiography modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('vgv_vakcin_disp_table').get_attribute(
        #     "action-type") == 'edit', "Data in VGV vaccination modal weren't preserved"
        # assert self.browser.find_element_by_id('vgv_vakcin_disp_table').get_attribute(
        #     "action-type") == 'edit', "Data in VGV vaccination modal weren't preserved"

    def should_test_sputum_smear_and_tb_symphtoms_modals(self):
        self.fill_sputum_smear_and_tb_symphtoms_modals()
        self.check_sputum_smear_and_tb_symphtoms_modals()

    def fill_sputum_smear_and_tb_symphtoms_modals(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.TUBERCULOSIS}.click();")
        self.make(f"{PatientCardLocators.SPUTUM_SMEAR_EXAMINATION_ADD}.click();")
        self.make(f"{PatientCardLocators.SPUTUM_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        sputum_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.SPUTUM_RESULT}.dropdown('set selected', '{sputum_choice}');")
        self.make(f"{PatientCardLocators.SPUTUM_SAVE}.click();")

        self.make(f"{PatientCardLocators.TB_SYMPHTOMS_ADD}.click();")
        self.make(f"{PatientCardLocators.TB_SYMPH_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        tb_symph_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.TB_SYMPH_RESULT}.dropdown('set selected', '{tb_symph_choice}');")
        self.make(f"{PatientCardLocators.TB_SYMPH_SAVE}.click();")

    def check_sputum_smear_and_tb_symphtoms_modals(self):
        assert self.is_element_present(*PatientCardLocators.SPUTUM_EDIT), "Data in Sputum Smear Examination modal wasn't saved or invalid selector for Edit button"
        assert self.is_element_present(*PatientCardLocators.TB_SYMPH_EDIT), "Data in TB Symphtoms modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute(
        #     "data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_xpert_mtb_and_kt_mrt_modals(self):
        self.fill_xpert_mtb_and_kt_mrt_modals()
        self.check_xpert_mtb_and_kt_mrt_modals()

    def fill_xpert_mtb_and_kt_mrt_modals(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.TUBERCULOSIS}.click();")
        self.make(f"{PatientCardLocators.XPERT_MTB_ADD}.click();")
        self.make(f"{PatientCardLocators.XPERT_MTB_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        xpert_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.XPERT_MTB_RESULT}.dropdown('set selected', '{xpert_choice}');")
        self.make(f"{PatientCardLocators.XPERT_MTB_SAVE}.click();")

        self.make(f"{PatientCardLocators.KT_MRT_ADD}.click();")
        self.make(f"{PatientCardLocators.KT_MRT_REGISTERING_DATE}.calendar('set date', '{self.today}');")
        mrt_choice = random.choice(['1', '2', '3', '4', '5'])
        self.make(f"{PatientCardLocators.KT_MRT_RESULT}.dropdown('set selected', '{mrt_choice}');")
        self.make(f"{PatientCardLocators.KT_MRT_SAVE}.click();")

    def check_xpert_mtb_and_kt_mrt_modals(self):
        assert self.is_element_present(*PatientCardLocators.XPERT_MTB_EDIT), "Data in Xpert MTB modal wasn't saved or invalid selector for Edit button"
        assert self.is_element_present(*PatientCardLocators.KT_MRT_EDIT), "Data in KT/MRT modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute(
        #     "data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_tb_treatment_modal(self):
        self.fill_tb_treatment_modal()
        self.check_tb_treatment_modal()

    def fill_tb_treatment_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.TUBERCULOSIS}.click();")
        self.make(f"{PatientCardLocators.TB_TREATMENT_ADD}.click();")
        self.make(f"{PatientCardLocators.LAB_NAME_CONFIRMED_TB}.val('Random lab');")
        self.make(f"{PatientCardLocators.TB_DIAG_REGISTERING_DATE}.val('{self.thirty_days_ago}')")
        case_choice = random.choice(['9', '1', '2', '3', '4', '5', '6', '7', '8'])
        self.make(f"{PatientCardLocators.SICK_TYPE}.dropdown('set selected', '{case_choice}');")
        analysis_choice = random.choice(['35', '1', '2', '3', '4', '5', '6', '7', '47'])
        self.make(f"{PatientCardLocators.TB_DIAG_MKB10}.dropdown('set selected', '{analysis_choice}');")
        location1_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.LOCATION}.dropdown('set selected', '{location1_choice}');")
        bac_secr_choice = random.choice(['1', '2', '4'])
        self.make(f"{PatientCardLocators.BAC_SECRETION}.dropdown('set selected', '{bac_secr_choice}');")
        self.make(f"{PatientCardLocators.TREATMENT_START_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.TREATMENT_END_DATE}.val('{self.today}');")
        outcome_choice = random.choice(['1', '2', '4', '5', '6', '7', '8'])
        self.make(f"{PatientCardLocators.OUTCOME}.dropdown('set selected', '{outcome_choice}');")
        self.make(f"{PatientCardLocators.TB_TREATMENT_SAVE}.click();")
        tb_hist_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.PRESENCE_TB_IN_HISTORY}.dropdown('set selected', '{tb_hist_choice}');")
        self.make(f"{PatientCardLocators.D_ACCOUNTED_DATE}.calendar('set date', '{self.today}');")

    def check_tb_treatment_modal(self):
        assert self.is_element_present(*PatientCardLocators.TB_TREATMENT_EDIT), "Data in TB treatment modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute(
        #     "data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def should_test_art_information_modal(self):
        self.fill_art_information_modal()
        self.check_art_information_modal()

    def fill_art_information_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_REASONS_DEFINE_DATE}.val('{self.today}')")
        self.make(f"{PatientCardLocators.ART_READINESS_DEFINE_DATE}.val('{self.today}')")
        self.make(f"{PatientCardLocators.WRITTEN_CONSENT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_START_DATE}.val('{self.today}')")
        row_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ART_ROW}.dropdown('set selected', '{row_choice}');")
        self.make(f"{PatientCardLocators.ART_SCHEME}.dropdown('set selected', '{self.preg_medic_choice}');")
        art_mo_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.ART_MED_ORG}.dropdown('set selected', '{art_mo_choice}');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")
        self.browser.find_element(*PatientCardLocators.ART_INFORMATION_EDIT).click()
        self.make(f"{PatientCardLocators.ART_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_MEDICATION_NAME}.click();")
        if PatientCardLocators.ART_MEDICATION_NAME_CHOICE:
            self.make(f"{PatientCardLocators.ART_MEDICATION_NAME_CHOICE}.click();")
            self.make(f"{PatientCardLocators.ART_RECIPE_NUM}.val('{self.numbers4}');")
            self.make(f"{PatientCardLocators.ART_ISSUANCE_SAVE}.click();")
        else:
            self.make(f"{PatientCardLocators.ART_MEDICATION_NAME_DENY}.click();")
            self.make(f"{PatientCardLocators.ART_ISSUANCE_DENY}.click();")
            print(f"Medicines are not available")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGED_DATE}.val('{self.today}')")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_TYPE}.dropdown('set selected', '1');")
        art_change_choice = random.choice(['1', '5', '6', '7', '8', '18', '20'])
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_REASON}.dropdown('set selected', '{art_change_choice}');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")

    def check_art_information_modal(self):
        assert self.is_element_present(*PatientCardLocators.ART_INFORMATION_EDIT), "Data in Art Information modal wasn't saved or invalid selector for Edit button"

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
        assert self.is_element_present(*PatientCardLocators.ART_ADHER_LEVEL_EDIT), "Data in Art Adherence modal wasn't saved or invalid selector for Edit button"

    def should_test_recipe_modal(self):
        self.fill_recipe_modal()
        self.check_recipe_modal()

    def fill_recipe_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_RECIPE_ADD}.click();")
        self.make(f"{PatientCardLocators.RECIPE_NUM}.val('{self.numbers4}');")
        self.make(f"{PatientCardLocators.RECIPE_DATE}.val('{self.today}')")
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
        self.make(f"{PatientCardLocators.SIGNATURE}.val('{self.smth_random}');")
        self.make(f"{PatientCardLocators.ART_RECIPE_SAVE}.click();")

    def check_recipe_modal(self):
        assert self.is_element_present(*PatientCardLocators.ART_RECIPE_EDIT), "Data in Recipe modal wasn't saved or invalid selector for Edit button"

    def should_test_pregnancy_modal(self):
        self.fill_pregnancy_modal()
        self.check_pregnancy_modal()

    def fill_pregnancy_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CHILDREN_PREGNANCY}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_ADD}.click();")
        pregnancy_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.make(f"{PatientCardLocators.PREGNANCY}.dropdown('set selected', '{pregnancy_choice}');")
        preg_partner_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.PREG_SEX_PARTNER}.dropdown('set selected', '{preg_partner_choice}');")
        self.make(f"{PatientCardLocators.PREG_PARTNER_HIV_STATUS}.dropdown('set selected', '{self.hiv_status_choice}');")
        self.make(f"{PatientCardLocators.OGC_REGIS_DATE}.val('{self.regis_date}');")
        preg_weeks_choice = random.choice(['1', '12', '2', '3', '4', '5', '6', '7', '8', '9', '10', '31', '42'])
        self.make(f"{PatientCardLocators.OGC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.ANTENATAL_CLINIC_REGIS_DATE}.val('{self.regis_date}');")
        self.make(f"{PatientCardLocators.AC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        preg_res_choice = random.choice(['1', '12', '2', '3', '11', '13'])
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT}.dropdown('set selected', '{preg_res_choice}');")
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPHILAXYS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_START_DATE}.val('{self.contacting_num}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_START}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_END_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_END}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_MEDICATIONS}.dropdown('set selected', '{self.preg_medic_choice}');")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_ADD}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME_CHOICE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_RECIPE_NUM}.val('{self.numbers4}');")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_SAVE}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")


    def check_pregnancy_modal(self):
        assert self.is_element_present(*PatientCardLocators.PREGNANCY_EDIT), "Data in Pregnancy modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

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
        self.make(f"{PatientCardLocators.CHILD_ARV_RECIPE_NUM}.val('{self.numbers5}');")
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_SAVE}.click();")
        self.make(f"{PatientCardLocators.CHILD_ARV_ISSUANCE_SAVE}.click();")
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_ADD}.click();")
        child_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.ALIVE_CHILD}.dropdown('set selected', '{child_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_SURNAME}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.CHILDS_NAME}.val('{self.name}');")
        self.make(f"{PatientCardLocators.CHILDS_MIDNAME}.val('{self.midname}');")
        self.make(f"{PatientCardLocators.CHILDS_BIRTHDAY}.val('{self.birthday}');")
        self.make(f"{PatientCardLocators.CHILDS_GENDER}.dropdown('set selected', '{self.gen_choice1}');")
        pathology_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.PATHALOGY_AT_BIRTH}.dropdown('set selected', '{pathology_choice}');")
        feeding_choice = random.choice(['1', '2', '3'])
        self.make(f"{PatientCardLocators.CHILDS_FEEDING}.dropdown('set selected', '{feeding_choice}');")
        full_term_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.FULL_TERM_CHILD}.dropdown('set selected', '{full_term_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_DEATH_DATE}.val('{self.deregis_date}');")
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_SAVE}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")

    def check_children_modal(self):
        assert self.is_element_present(*PatientCardLocators.PREGNANCY_EDIT), "Data in Pregnancy modal wasn't saved or invalid selector for Edit button"
        # assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute("data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

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
        self.make(f"{PatientCardLocators.REASONS_SET_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PREV_THER_START_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PREV_THER_END_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.PREV_THER_SAVE}.click();")
        self.make(f"{PatientCardLocators.OPIOID_SUBSTITUTION_THERAPHY_ADD}.click();")
        self.make(f"{PatientCardLocators.OST_START_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.OST_END_DATE}.val('{self.today}');")
        ost_med_choice = random.choice(['1', '2'])
        self.make(f"{PatientCardLocators.OST_MEDICATION_TYPE}.dropdown('set selected', '{ost_med_choice}');")
        # reas_fin_choice = random.choice(['1', '2'])
        # self.make(f"{PatientCardLocators.REASONS_OF_FINISHING}.dropdown('set selected', '{reas_fin_choice}');")
        self.make(f"{PatientCardLocators.OST_SAVE}.click();")

    def check_preventive_therapy_and_ost_modals(self):
        assert self.is_element_present(*PatientCardLocators.PREV_THER_EDIT), "Data in Preventive therapy modal wasn't saved or invalid selector for Edit button"
        assert self.is_element_present(*PatientCardLocators.OST_EDIT), "Data in OST modal wasn't saved or invalid selector for Edit button"

    def should_test_vgs_treatment_modal(self):
        self.fill_vgs_treatment_modal()
        self.check_vgs_treatment_modal()

    def fill_vgs_treatment_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.THERAPHY}.click();")
        self.make(f"{PatientCardLocators.VGS_TREATMENT_ADD}.click();")
        self.make(f"{PatientCardLocators.VGS_TREAT_START_DATE}.val('{self.today}');")
        self.make(f"{PatientCardLocators.VGS_TREAT_END_DATE}.val('{self.today}');")
        treat_res_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
        self.make(f"{PatientCardLocators.VGS_TREAT_RESULT}.dropdown('set selected', '{treat_res_choice}');")
        self.make(f"{PatientCardLocators.VGS_TREAT_SAVE}.click();")

    def check_vgs_treatment_modal(self):
        assert self.is_element_present(*PatientCardLocators.VGS_TREAT_EDIT), "Data in VGS treatment modal wasn't saved or invalid selector for Edit button"

    def should_test_d_exam_hospitalization_modal(self):
        self.fill_d_exam_hospitalization_modal()
        self.check_d_exam_hospitalization_modal()

    def fill_d_exam_hospitalization_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.D_EXAM_HOSPITALIZATION}.click();")
        self.browser.execute_script("document.querySelector('div.ui.secondary.padding_ext_07.segment a.ui.green.button.add_osmotr').classList.remove('trollface');")
        sleep(5)
        # self.make(f"{PatientCardLocators.ATTENDANCE_DATE}.val('{self.today}');")
        exam_choice = random.choice('infection', 'pediatr', 'ftiziatr', 'ginekolog', 'terapevt', 'dermatolog',
                                    'psiholog', 'social_worker', 'narkolog')
        self.make(f"{PatientCardLocators.D_EXAM_HELD}.dropdown('set selected', 'exam_choice');")
        service_choice = random.choice('2', '3', '348', '328', '33', '25', '322', '331', '14')
        self.make(f"{PatientCardLocators.D_SERVICES}.dropdown('set selected', 'service_choice');")
        place_choice = random.choice('home', 'mls', 'stacionar', 'center_hiv', 'ambulatorno')
        self.make(f"{PatientCardLocators.D_EXAM_PLACE}.dropdown('set selected', 'place_choice');")
        attendance_choice = random.choice('perv_osmotr', 'd_osmotr', 'po_zabolev', 'current_reception')
        self.make(
            f"{PatientCardLocators.ATTENDANCE_TYPE}.dropdown('set selected', 'attendance_choice');")
        self.make(f"{PatientCardLocators.TEMPERATURE}.val('36.6');")
        self.make(f"{PatientCardLocators.WEIGHT}.val('32');")
        self.make(f"{PatientCardLocators.HEIGHT}.val('100');")
        self.make(f"{PatientCardLocators.COMPLAINTS}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.HISTORY_INFORMATION}.val('{self.midname}');")
        self.make(f"{PatientCardLocators.LAST_MENSIS}.val('{self.today}');")
        self.make(f"{PatientCardLocators.CONTRACEPTION}.click();")
        self.make(f"{PatientCardLocators.D_EXAM_SEX_PARTNER}.click();")
        self.make(f"{PatientCardLocators.ART_RECEIPT}.click();")
        self.make(f"{PatientCardLocators.PLANNED_PREGNANCY_YES}.click();")
        self.make(f"{PatientCardLocators.PLANNED_PREGNANCY_NO}.click();")
        self.make(f"{PatientCardLocators.D_EXAM_ALCOHOL}.click();")
        self.make(f"{PatientCardLocators.D_EXAM_DRUGS}.click();")
        # D_EXAM_INJ_DRUG_LAST_HALF_YEAR = "$('div[data-field=inek_nark_six_month] .ui.dropdown')"
        # D_EXAM_COM_SEX_LAST_HALF_YEAR = "$('div[data-field=komerc_sex_six_month] .ui.dropdown')"
        # D_EXAM_HOMO_SEX_LAST_HALF_YEAR = "$('div[data-field=gomo_sex_six_month] .ui.dropdown')"
        state_choice = random.choice('satisfactory', 'moderate_severity', 'severe_severity', 'extremely_heavy')
        self.make(f"{PatientCardLocators.STATE}.dropdown('set selected', 'state_choice');")
        conscious_choice = random.choice('clear', 'stupor', 'sopor', 'coma')
        self.make(
            f"{PatientCardLocators.CONSCIOUSNESS}.dropdown('set selected', 'conscious_choice');")
        position_choice = random.choice('active', 'passive', 'forced')
        self.make(f"{PatientCardLocators.POSITION}.dropdown('set selected', 'position_choice');")
        body_choice = random.choice('normostenic', 'astenik', 'hypersthenic')
        self.make(f"{PatientCardLocators.BODY_TYPE}.dropdown('set selected', 'body_choice');")
        feeding_choice1 = random.choice('moderate', 'low', 'high', 'cachexia')
        self.make(f"{PatientCardLocators.FEEDING}.dropdown('set selected', 'feeding_choice1');")
        lipo_choice = random.choice('10', '20')
        self.make(f"{PatientCardLocators.LIPODYSTROPHY}.dropdown('set selected', 'lipo_choice');")
        skin_choice = random.choice('regular_coloring', 'pale_pink', 'icteric', 'another')
        self.make(f"{PatientCardLocators.SKIN_MUCOSA}.dropdown('set selected', 'skin_choice');")
        nails_choice = random.choice('not_changed', 'changed')
        self.make(f"{PatientCardLocators.NAILS}.dropdown('set selected', 'nails_choice');")
        rash_choice = random.choice('10', '20')
        self.make(f"{PatientCardLocators.RASH}.dropdown('set selected', 'rash_choice');")
        lymph_choice = random.choice('not_palpable', 'not_enlarged', 'palpable', 'enlarged', 'painful', 'not_painful',
                                     'single', 'multiple', 'not_soldered')
        self.make(
            f"{PatientCardLocators.PERIFEPHERAL_LYMPH_NODES}.dropdown('set selected', 'lymph_choice');")
        osteo_choice = random.choice('no_pathological_changes', 'with_pathological_changes')
        self.make(
            f"{PatientCardLocators.OSTEO_ARTICULAR_SYSTEM}.dropdown('set selected', 'osteo_choice');")
        breath_choice = random.choice('vesicular', 'tough', 'weakened', 'another')
        self.make(f"{PatientCardLocators.BREATH_SOUNDS}.dropdown('set selected', 'breath_choice');")
        self.make(f"{PatientCardLocators.WHEEZING_YES}.click();")
        self.make(f"{PatientCardLocators.WHEEZING_NO}.click();")
        wheezing_choice = random.choice('dry', 'wet', 'whistling', 'crepitus')
        self.make(f"{PatientCardLocators.WHEEZING_TYPE}.dropdown('set selected', 'wheezing_choice');")
        self.make(f"{PatientCardLocators.RESPIRATORY_RATE}.val('100');")
        heart_choice = random.choice('clear', 'muffled', 'rhythmic', 'arrhythmic')
        self.make(f"{PatientCardLocators.HEART_SOUNDS}.dropdown('set selected', 'heart_choice');")
        self.make(f"{PatientCardLocators.HEART_RATE}.val('100');")
        self.make(f"{PatientCardLocators.BLOOD_PREASURE}.val('100');")
        noise_choice = random.choice('not_heard', 'heard')
        self.make(f"{PatientCardLocators.NOISE}.dropdown('set selected', 'noise_choice');")
        tongue_choice = random.choice('decorated', 'liquid', 'without_pathological_impurities', 'blood', 'slime',
                                      'ordinary_paint', 'green', 'acholic', 'another')
        self.make(f"{PatientCardLocators.TONGUE}.dropdown('set selected', 'tongue_choice');")
        self.make(f"{PatientCardLocators.ORAL_MUCOSA}.val('{self.surname}');")
        stomach_choice = random.choice('painless_on_palpation', 'tense', 'painful_on_palpation', 'another')
        self.make(f"{PatientCardLocators.STOMACH}.dropdown('set selected', 'stomach_choice');")
        liver_choice = random.choice('not_increased', 'on_the_edge_of_the_costal_arch',
                                     'protrudes_from_under_the_edge_of_the_costal_arch', 'consistency_dense', 'soft',
                                     'elastic', 'another')
        self.make(f"{PatientCardLocators.LIVER}.dropdown('set selected', 'liver_choice');")
        spleen_choice = random.choice('not_palpable', 'increased_from_under_the_edge', 'deleted', 'another')
        self.make(f"{PatientCardLocators.SPLEEN}.dropdown('set selected', 'spleen_choice');")
        sym_choice = random.choice('negative', 'positive', 'two_side', 'left', 'right')
        self.make(
            f"{PatientCardLocators.SYMPTOMS_OF_BANGING}.dropdown('set selected', 'sym_choice');")
        stool_choice = random.choice('decorated', 'liquid', 'without_pathological_impurities', 'blood', 'slime',
                                     'ordinary_paint', 'green', 'acholic', 'another')
        self.make(f"{PatientCardLocators.STOOL}.dropdown('set selected', 'stool_choice');")
        self.make(f"{PatientCardLocators.STOOL_MULTIPLICITY}.val('{self.contacting_num}');")
        self.make(f"{PatientCardLocators.URINATION_FREE}.click();")
        self.make(f"{PatientCardLocators.URINATION_PAINLESS}.click();")
        self.make(f"{PatientCardLocators.URINATION_PAINFUL}.click();")
        self.make(f"{PatientCardLocators.DIURESIS_FREQUENT}.click();")
        self.make(f"{PatientCardLocators.DIURESIS_BREACHED}.click();")
        self.make(f"{PatientCardLocators.DIURESIS_NORM}.click();")
        self.make(f"{PatientCardLocators.SWELLING}.val('yes');")
        self.make(f"{PatientCardLocators.D_EXAM_DIAGNOSIS}.val('{self.midname}');")
        self.make(f"{PatientCardLocators.D_EXAM_NOTES}.val('{self.surname}');")
        self.make(f"{PatientCardLocators.PLANNED_D_EXAM}.val('{self.today}');")
        self.make(f"{PatientCardLocators.D_EXAM_SAVE}.click();")

    def check_d_exam_hospitalization_modal(self):
        assert self.browser.find_element_by_id('donor_blood_kod_donor').get_attribute(
            "data-field") == self.numbers3, "Data in Blood donor modal or object Blood donor code weren't saved"

    def register_new_woman(self):
        # автозаполнение формы регистрации для взрослого
        res_code_choice = random.choice(['47', '48', '11', '22'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2003', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(randrange(int_delta))
        first_numbers = random_date.strftime('%y%m%d')
        p_birthday = random_date.strftime('%d.%m.%Y')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
        trans_choice = random.choice(['1', '2'])
        self.make(f"{RegisterPageLocators.TRANSGENDER}.dropdown('set selected', '{trans_choice}');")
        self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        p_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
        self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(p_surname)
        p_name = ''.join(random.choices(string.ascii_uppercase, k=6))
        self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(p_name)
        p_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*RegisterPageLocators.PATIENT_MIDNAME).send_keys(p_midname)
        # self.make(f"$('{RegisterPageLocators.BIRTH_DATE}').val('{birthday}')")
        self.make(f"$('#general_data_birth').val('{p_birthday}')")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', 'female');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        if self.browser.find_element(By.CSS_SELECTOR, 'div[data-field=general_data_adm_obl_viyav] input').get_attribute("value") == "33":
            pass
        else:
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
            self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        soc_status_choice = random.choice(['3', '4'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{RegisterPageLocators.RESID_AREA}.dropdown('set selected', '3');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('hide');")
        self.make(f"{RegisterPageLocators.RESID_UNIT_AREA}.dropdown('set selected', '33');")
        self.make(f"{RegisterPageLocators.RESID_LOCALITY}.dropdown('set selected', '170000000008');")
        self.make(f"{RegisterPageLocators.RESID_PLACE}.dropdown('set selected', '2');")
        self.browser.find_element(*RegisterPageLocators.RESID_STREET).send_keys(self.street_choice)
        self.browser.find_element(*RegisterPageLocators.RESID_HOUSE).send_keys(25)
        self.browser.find_element(*RegisterPageLocators.RESID_APT).send_keys(45)
        self.browser.find_element(*RegisterPageLocators.RESID_PHONE_NO).send_keys(87273456789)
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '80000000546');")
        self.make(f"{RegisterPageLocators.DUPLICATE_RESID_ADR}.checkbox('set checked');")
        # self.browser.take_screenshot()
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click()")
        sleep(5)
        id_url = self.browser.current_url
        url_part = id_url.split('/')[5]
        global patient_id_woman
        patient_id_woman = url_part.split('?')[0]
        if patient_id_woman == "0000000000":
            sleep(5)
            id_url = self.browser.current_url
            url_part = id_url.split('/')[5]
            patient_id_woman = url_part.split('?')[0]
            print(f"ID of adult patient is {patient_id_woman}")
        else:
            print(f"ID of adult patient is {patient_id_woman}")


    def register_new_homeless(self):
        # автозаполнение формы регистрации для бомжа
        res_code_choice = random.choice(['1', '3', '59', '49'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2000', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(randrange(int_delta))
        first_numbers = random_date.strftime('%y%m%d')
        p_birthday = random_date.strftime('%d.%m.%Y')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
        p_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
        self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(p_surname)
        p_name = ''.join(random.choices(string.ascii_uppercase, k=6))
        self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(p_name)
        p_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*RegisterPageLocators.PATIENT_MIDNAME).send_keys(p_midname)
        # self.make(f"$('{RegisterPageLocators.BIRTH_DATE}').val('{birthday}')")
        self.make(f"$('#general_data_birth').val('{p_birthday}')")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', 'male');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '1');")
        soc_status_choice = random.choice(['4', '8'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{RegisterPageLocators.HOMELESS}.checkbox('set checked');")
        # self.browser.take_screenshot()
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click();")
        sleep(5)
        id_url = self.browser.current_url
        url_part = id_url.split('/')[5]
        global patient_id_homeless
        patient_id_homeless = url_part.split('?')[0]
        if patient_id_homeless == "0000000000":
            sleep(5)
            id_url = self.browser.current_url
            url_part = id_url.split('/')[5]
            patient_id_homeless = url_part.split('?')[0]
            print(f"ID of homeless patient is {patient_id_homeless}")
        else:
            print(f"ID of homeless patient is {patient_id_homeless}")

    def register_new_foreigner(self):
        # автозаполнение формы регистрации для иностранного гражданина
        res_code_choice = random.choice(['47', '48', '11', '22'])
        self.make(f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
        d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
        d2 = datetime.strptime('01.12.2003', '%d.%m.%Y')
        delta = d2 - d1
        int_delta = delta.days
        random_date = d1 + timedelta(randrange(int_delta))
        first_numbers = random_date.strftime('%y%m%d')
        p_birthday = random_date.strftime('%d.%m.%Y')
        others = random.randrange(100000, 999999)
        iin = f'{first_numbers}{others}'
        self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
        # self.make(f"{RegisterPageLocators.ANONIMOUS}.checkbox('set checked');")
        p_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
        self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(p_surname)
        p_name = ''.join(random.choices(string.ascii_uppercase, k=6))
        self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(p_name)
        p_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
        self.browser.find_element(*RegisterPageLocators.PATIENT_MIDNAME).send_keys(p_midname)
        # self.make(f"$('{RegisterPageLocators.BIRTH_DATE}').val('{birthday}')")
        self.make(f"$('#general_data_birth').val('{p_birthday}')")
        self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{self.gen_choice}');")
        self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').focus();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] input.search').click();")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('set selected', '33');")
        self.make(f"$('div[data-field=general_data_adm_obl_viyav] .ui.dropdown').dropdown('hide');")
        self.make(f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', '2');")
        soc_status_choice = random.choice(['3', '4'])
        self.make(f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
        self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{self.mo_choice}');")
        self.make(f"{RegisterPageLocators.REGIS_AREA}.dropdown('set selected', '5');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.click();")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('hide');")
        # self.make(f"{RegisterPageLocators.REGIS_UNIT_AREA}.dropdown('set selected', '180');")
        self.make(f"{RegisterPageLocators.REGIS_LOCALITY}.dropdown('set selected', '177');")
        self.make(f"{RegisterPageLocators.REGIS_PLACE}.dropdown('set selected', '2');")
        self.browser.find_element(*RegisterPageLocators.REGIS_STREET).send_keys(self.street_choice)
        self.browser.find_element(*RegisterPageLocators.REGIS_HOUSE).send_keys(55)
        self.browser.find_element(*RegisterPageLocators.REGIS_APT).send_keys(44)
        self.browser.find_element(*RegisterPageLocators.REGIS_PHONE_NO).send_keys(87273456987)
        self.make(f"{RegisterPageLocators.RESID_MED_ORG}.dropdown('set selected', '170000000558');")
        self.make(f"{RegisterPageLocators.DUPLICATE_REGIS_ADR}.checkbox('set checked');")
        self.make(f"{RegisterPageLocators.REGISTER_SAVE_BTN}.click();")
        sleep(5)
        id_url = self.browser.current_url
        url_part = id_url.split('/')[5]
        global patient_id_foreigner
        patient_id_foreigner = url_part.split('?')[0]
        if patient_id_foreigner == "0000000000":
            sleep(5)
            id_url = self.browser.current_url
            url_part = id_url.split('/')[5]
            patient_id_foreigner = url_part.split('?')[0]
            print(f"ID of foreigner patient is {patient_id_foreigner}")
        else:
            print(f"ID of foreigner patient is {patient_id_foreigner}")
        # self.browser.take_screenshot()

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
    #
    #
    #
    #
    # def register_new_bomj_and_edit_card(self):
    #     # автозаполнение формы регистрации для бомжа
    #     res_code_choice = random.choice(['3', '4', '16'])
    #     self.make(
    #         f"{RegisterPageLocators.RESEARCH_CODE}.dropdown('set selected', '{res_code_choice}');")
    #     d1 = datetime.strptime('01.01.1970', '%d.%m.%Y')
    #     d2 = datetime.strptime('01.12.2000', '%d.%m.%Y')
    #     delta = d2 - d1
    #     int_delta = delta.days
    #     random_date = d1 + timedelta(randrange(int_delta))
    #     first_numbers = random_date.strftime('%y%m%d')
    #     birthday = random_date.strftime('%d.%m.%Y')
    #     others = random.randrange(100000, 999999)
    #     iin = f'{first_numbers}{others}'
    #     self.browser.find_element(*RegisterPageLocators.PATIENT_IIN).send_keys(iin)
    #     self.browser.find_element(*RegisterPageLocators.ANONIMOUS).click()
    #     surname = ''.join(random.choices(string.ascii_uppercase, k=10))
    #     self.browser.find_element(*RegisterPageLocators.PATIENT_SURNAME).send_keys(surname)
    #     name = ''.join(random.choices(string.ascii_uppercase, k=5))
    #     self.browser.find_element(*RegisterPageLocators.PATIENT_NAME).send_keys(name)
    #     midname = ''.join(random.choices(string.ascii_uppercase, k=10))
    #     self.browser.find_element(*RegisterPageLocators.PATIENT_MIDNAME).send_keys(midname)
    #     # self.make(f"$('{RegisterPageLocators.BIRTH_DATE}').val('{birthday}')")
    #     self.make(f"$('#general_data_birth').val('{birthday}')")
    #     gen_choice = random.choice(['female', 'male'])
    #     self.make(f"{RegisterPageLocators.PATIENT_GENDER}.dropdown('set selected', '{gen_choice}');")
    #
    #     self.make(f"{RegisterPageLocators.EMERGENCE_AREA}.dropdown('set selected', '3');")
    #     # self.make(f"{RegisterPageLocators.EMERGENCE_UNIT_AREA}.dropdown('show');")
    #     self.browser.find_element(f"{RegisterPageLocators.EMERGENCE_UNIT_AREA}.dropdown();").click()
    #     self.make(f"{RegisterPageLocators.EMERGENCE_UNIT_AREA}.dropdown('set value', '33');")
    #     self.make(
    #         f"{RegisterPageLocators.PATIENT_CITIZENSHIP}.dropdown('set selected', 'without-citizenship');")
    #     soc_status_choice = random.choice(['4', '8'])
    #     self.make(
    #         f"{RegisterPageLocators.SOCIAL_STATUS}.dropdown('set selected', '{soc_status_choice}');")
    #     self.make(f"{RegisterPageLocators.BOMJ_CHECKBOX}.checkbox('set checked');")
    #     med_org_choice = random.choice(['170000000003', '170000000105', '170000000004', '170000000008', '170000000009'])
    #     self.make(f"{RegisterPageLocators.MED_ORG}.dropdown('set selected', '{med_org_choice}');")
    #     self.browser.find_element(*RegisterPageLocators.REGISTER_SAVE_BTN).click()


