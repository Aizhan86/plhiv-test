from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_URL = "https://plhiv-demo.dec.kz/login?next=%2F"
    LOGIN_LINK = "https://plhiv-demo.dec.kz/login?next=%2F"
    LOGIN_FORM = (By.CLASS_NAME, 'login_panel_block')
    USER_NAME = (By.ID, "username")
    USER_PASS = (By.ID, "password")
    LOGIN_BTN = (By.ID, "submit")
    MODAL_AGR = (By.ID, "modal_agreement")
    AGR_BTN = (By.CSS_SELECTOR, '#modal_agreement .ui.green.inverted.ok.button')

class RegisterPageLocators(object):
    FOREIGNER_IB_NO = (By.ID, 'general_data_nib_out')
    FOREIGNER_IB_NO_DATE = (By.ID, 'general_data_date_nib_out')
    ADD_PATIENT = (By.CSS_SELECTOR, 'a[href="/visits/patient_card/0000000000?new=1&in_rk=1&add=1"]')
    ADD_FOREIGN_PATIENT = (By.CSS_SELECTOR, 'a[href="/visits/patient_card/0000000000?new=1&in_rk=0&add=1"]')
    RESEARCH_CODE = "$('form[name=general-data-form] div[data-field=general_data_contengent] .ui.dropdown')"
    PATIENT_BIRTH_DATE = (By.ID, 'general_data_birth"]')
    PATIENT_GENDER = "$('form[name=general-data-form] div[data-field=general_data_gender] .ui.dropdown')"
    PATIENT_IIN = (By.ID, "general_data_iin")
    TRANSGENDER = "$('form[name=general-data-form] div[data-field=general_data_transgender] .ui.dropdown')"
    ANONIMOUS = "$('form[name=general-data-form] div[data-field=general_data_anonim] .ui.toggle.checkbox')"
    PATIENT_SURNAME = (By.ID,  'general_data_surname')
    PATIENT_NAME = (By.ID, 'general_data_name')
    PATIENT_MIDNAME = (By.ID, 'general_data_patronymic')
    BIRTH_DATE = (By.ID, 'general_data_birth')
    EMERGENCE_AREA = "$('form[name=general-data-form] div[data-field=general_data_oblast_viyav] .ui.dropdown')"
    EMERGENCE_UNIT_AREA = "$('form[name=general-data-form] div[data-field=general_data_adm_obl_viyav] .ui.dropdown')"
    EMERGENCE_UNIT_AREA_CLICK = (By.CSS_SELECTOR, 'form[name=general-data-form] div[data-field=general_data_adm_obl_viyav] .search')
    EMERGENCE_PLACE = "$('form[name=general-data-form] div[data-field=general_data_place_viyav] .ui.dropdown')"
    INFECTION_PLACE = "$('form[name=general-data-form] div[data-field=general_data_place_zarajeniya] .ui.dropdown')"
    INFECTION_ORG = "$('form[name=general-data-form] div[data-field=general_data_ucherejdenie_zarajeniya] .ui.dropdown')"
    PENITENTIARY = "$('form[name=general-data-form] div[data-field=general_data_peniterc] .ui.dropdown')"
    ADM_TER_REG = "$('form[name=general-data-form] div[data-field=general_data_adm_registr] .ui.dropdown')"
    SUPPOSED_WAY_INF = "$('form[name=general-data-form] div[data-field=general_data_peredachi] .ui.dropdown')"
    PATIENT_CITIZENSHIP = "$('form[name=general-data-form] div[data-field=general_data_citizenship] .ui.dropdown')"
    ARRIVAL_DATE = (By.ID, 'general_data_date_priezd')
    COUNTRY_FROM_WHICH_CAME = "$('form[name=general-data-form] div[data-field=general_data_from_country] .ui.dropdown')"
    ARRIVAL_PURPOSE = "$('form[name=general-data-form] div[data-field=general_data_citizenship] .ui.dropdown')"
    MARITAL_STATUS = "$('form[name=general-data-form] div[data-field=general_data_fam_state] .ui.dropdown')"
    CHILD_STATUS = "$('form[name=general-data-form] div[data-field=general_data_child_state] .ui.dropdown')"
    EDUCATION = "$('form[name=general-data-form] div[data-field=general_data_education] .ui.dropdown')"
    SOCIAL_STATUS = "$('form[name=general-data-form] div[data-field=genaral_data_soc_state] .ui.dropdown')"
    MED_ORG = "$('form[name=general-data-form] div[data-field=general_data_org_viyav] .ui.dropdown')"
    BOMJ_CHECKBOX = "$('input[name=general_data_bomj] .checkbox')"
    REGIS_AREA = "$('form[name=general-data-form] div[data-field=registration_address_region_name] .ui.dropdown')"
    REGIS_UNIT_AREA = "$('form[name=general-data-form] div[data-field=registration_address_unit_area] .ui.dropdown')"
    REGIS_UNIT_AREA_CLICK = (By.CSS_SELECTOR, 'form[name=general-data-form] div[data-field=registration_address_unit_area] .ui.dropdown')
    REGIS_LOCALITY = "$('form[name=general-data-form] div[data-field=registration_address_locality_name] .ui.dropdown')"
    REGIS_PLACE = "$('form[name=general-data-form] div[data-field=registration_address_place_live] .ui.dropdown')"
    REGIS_STREET = (By.ID, 'registration_address_street')
    REGIS_HOUSE = (By.ID, 'registration_address_house')
    REGIS_APT = (By.ID, 'registration_address_kvart')
    REGIS_PHONE_NO = (By.ID, 'registration_address_telephone')
    RESID_AREA = "$('form[name=general-data-form] div[data-field=fact_address_region_name] .ui.dropdown')"
    RESID_UNIT_AREA = "$('form[name=general-data-form] div[data-field=fact_address_unit_area] .ui.dropdown')"
    RESID_UNIT_AREA_CLICK = (By.CSS_SELECTOR, 'form[name=general-data-form] div[data-field=fact_address_unit_area] .ui.dropdown')
    RESID_LOCALITY = "$('form[name=general-data-form] div[data-field=fact_address_locality_name] .ui.dropdown')"
    RESID_PLACE =  "$('form[name=general-data-form] div[data-field=fact_address_place_live] .ui.dropdown')"
    RESID_STREET = (By.ID, 'fact_address_street')
    RESID_HOUSE = (By.ID, 'fact_address_hous')
    RESID_APT = (By.ID, 'fact_address_flat')
    RESID_PHONE_NO = (By.ID, 'fact_address_telephone')
    RESID_MED_ORG = "$('form[name=general-data-form] div[data-field=fact_address_pp_name] .ui.dropdown')"
    REASON_NOT_EPID = "$('form[name=general-data-form] div[data-field=general_data_reason_not_epid] .ui.dropdown')"
    REASON_NOT_DISP_REG = "$('form[name=general-data-form] div[data-field=general_data_reason_dispuchet] .ui.dropdown')"
    RETROSPECTIVE_CHILD = "$('form[name=general-data-form] div[data-field=general_data_mother_child] .ui.toggle.checkbox')"
    MOTHERS_SURNAME = (By.ID, 'general_data_mother_surname')
    MOTHERS_NAME = (By.ID, 'general_data_mother_name')
    MOTHERS_MIDNAME = (By.ID, 'general_data_mother_patronymic')
    MOTHERS_IB_NO = (By.ID, 'general_data_mother_ib_number')
    IB_NO_DATE = (By.ID, 'general_data_mother_date_ib')
    REGISTER_SAVE_BTN = (By.CSS_SELECTOR, ".ui.bottom.attached.tab.segment.active .right.floated.green.approve.button")
    EDIT_PATIENT_CARD = "$('#registration_address_table a[action-type=edit] .ui.button')"
    REGIS_APT2 = (By.ID, 'registration_address_kvart_modal')
    ERROR_REGIS_ADDRESS_SAVE = (By.CSS_SELECTOR, "#error_address_reg .ui.green.approve.button")
    PATIENT_CARD_SAVE = (By.ID, 'general_data_save_button')

class PatientCardLocators(object):
    OPEN_PATIENT_MENU = "$('.basic.segment .ui.sidebar')"
    LAB_RESEARCH = "$('a[data-name=lab-research]')"

    IFA_OGC_ADD = (By.ID, 'ifa_ogc_add')
    IFA_MED_ORG = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_naprav_mo_modal] .ui.dropdown')"
    SURNAME_PERSON_MEDORG = (By.CSS_SELECTOR, '#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_fio_otvetstv_lica_mo_modal] input')
    REFERRAL_NO = (By.CSS_SELECTOR, '#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_nomer_napravlen_modal] input')
    BLOOD_SAMPLING_DATE = (By.ID, 'ifa_k_vich_ogc_date_blood_modal')
    RECEIPT_DATE = (By.ID, 'ifa_k_vich_ogc_date_lab_modal')
    PRODUCTION_DATE = (By.ID, 'ifa_k_vich_ogc_date_postanov_modal')
    SERUM_NUM = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_number_syvorotki_modal] .ui.dropdown')"
    SERUM_NUM2 = (By.CSS_SELECTOR, '#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_number_syvorotki_input_modal] input')
    EXPIRATION_DATE = (By.ID, 'ifa_k_vich_ogc_srok_godn_modal')
    SERIES_NUM = (By.CSS_SELECTOR, '#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_serial_number_modal] input')
    TEST_CATEGORY = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_test_category_modal] .ui.dropdown')"
    TEST_SYSTEM_TYPE = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_test_system_type_modal] .ui.dropdown')"
    OP_CRITICAL = (By.CSS_SELECTOR,'#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_op_critical_modal] input')
    OP_SERUM = (By.CSS_SELECTOR,'#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_op_syvorotki_modal] input')
    IFA_RESULT = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_result_modal] .ui.dropdown')"
    RESPONSIBLE_PERSON = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_fio_otvetstv_lica_lab_modal] .ui.dropdown')"
    IFA_SERVICES = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_which_services_modal] .ui.dropdown')"
    IFA_OGC_SAVE = (By.CSS_SELECTOR, '#ifa_k_vich_ogc_modal .ui.green.approve.button')

    USER_NAME = "$('div[data-name=account-settings]')"
    # PROFILE = "$('div[data-name=account-settings] div.menu').children()[0]')"
    PROFILE_EDIT = "$('a[href=/user/3/edit]')"
    MED_ORG = "$('div[data-field=org_id] .ui.dropdown')"

    IB_PCR = "$('div[data-tab=patient_card_menu-ib_pcr]')"
    IB_NUMBER = "$('#ib_modal div[data-field=ib_number_modal] input')"
    IB_SERUM_NUM = "$('#ib_modal div[data-field=ib_number_syvorotki_modal] input')"
    SAMPLE_NUM = "$('#ib_modal div[data-field=ib_number_sample_modal] input')"
    IB_RECEIPT_DATE = "$('#ib_modal div[data-field=ib_date_postup_modal] .ui.calendar')"
    IB_REGISTER_DATE = "$('#ib_modal div[data-field=ib_date_postanov_modal] .ui.calendar')"
    IB_RESULT = "$('#ib_modal div[data-field=ib_result_modal] .ui.dropdown')"
    TEST_SYSTEM_NAME = "$('#ib_modal div[data-field=ib_name_test_system_modal] .ui.dropdown')"
    IB_EXPIRATION_DATE = "$('#ib_srok_godn_modal')"
    IB_SERIES_NUM = "$('#ib_modal div[data-field=ib_serial_number_modal] input')"
    IB_RESPONSIBLE_PERSON = "$('#ib_modal div[data-field=ib_otvetstvennoe_lico_modal] .ui.dropdown')"
    GP160 = "$('#ib_modal div[data-field=ib_gp160_modal] .ui.dropdown')"
    GP110_120 = "$('#ib_modal div[data-field=ib_gp110_120_modal] .ui.dropdown')"
    P68 = "$('#ib_modal div[data-field=ib_p68_modal] .ui.dropdown')"
    P55 = "$('#ib_modal div[data-field=ib_p55_modal] .ui.dropdown')"
    P52 = "$('#ib_modal div[data-field=ib_p52_modal] .ui.dropdown')"
    GP41 = "$('#ib_modal div[data-field=ib_gp41_modal] .ui.dropdown')"
    P40 = "$('#ib_modal div[data-field=ib_p40_modal] .ui.dropdown')"
    P34 = "$('#ib_modal div[data-field=ib_p34_modal] .ui.dropdown')"
    P25 = "$('#ib_modal div[data-field=ib_p25_modal] .ui.dropdown')"
    P18 = "$('#ib_modal div[data-field=ib_p18_modal] .ui.dropdown')"
    IB_SERVICES = "$('#ifa_k_vich_ogc_modal div[data-field=ifa_k_vich_ogc_which_services_modal] .ui.dropdown')"
    IB_SAVE = "$('#ifa_k_vich_ogc_modal .ui.green.approve.button')"

    RESULT = (By.CSS_SELECTOR, 'div[data-block=main-menu] a[data-tab=patient_card_menu-zaklyuchenie]')
    RESULT_ADD = (By.CSS_SELECTOR, '#zaklyuchenie_table a[action-type=add]')
    RESULT_NUM = (By.CSS_SELECTOR, '#zaklyuchenie_modal div[data-field=zaklyuchenie_number_modal] input')
    RESULT_DATE = (By.ID, 'zaklyuchenie_date_vydachi_modal')
    RESULT_RESPONSIBLE_PERSON = "$('#zaklyuchenie_modal div[data-field=zaklyuchenie_otvetstvennoe_lico_modal] .ui.dropdown')"
    LAB_SUPERVISER = "$('#zaklyuchenie_modal div[data-field=zaklyuchenie_zav_lab_modal] .ui.dropdown')"
    ANALYSIS_RESULT = "$('#zaklyuchenie_modal div[data-field=zaklyuchenie_zaklyuchenie_modal] .ui.dropdown')"
    RESEARCH_BAZIS = (By.CSS_SELECTOR, '#table_conclusion input')
    RESULT_SAVE = (By.CSS_SELECTOR, '#zaklyuchenie_modal .ui.green.approve.button')

    # CD4_SCREENING
    # VGS_DIAGNOSTICS
    # RESISTANCE
    # ADDITIONAL_SURVEYS

    EPID_HISTORY = "$('a[data-name=epid-history]')"
    EPID_HISTORY_HIV_ANALYSIS = "$('div[data-field=epid_history_obsled_hiv] .ui.dropdown')"
    EPID_HISTORY_ANALYSIS_YEAR = "$('div[data-field=epid_history_obsled_year] .ui.dropdown')"
    EPID_HISTORY_ANALYSIS_RESULT = "$('div[data-field=epid_history_result] .ui.dropdown')"
    FAMILY_MEM_ADD = (By.CSS_SELECTOR, '#fam_members_table a[action-type=add]')
    FAMILY_MEM_LASTNAME = (By.CSS_SELECTOR, '#fam_members_modal div[data-field=fam_members_last_name_modal] input')
    FAMILY_MEM_NAME = (By.CSS_SELECTOR, '#fam_members_modal div[data-field=fam_members_name_modal] input')
    FAMILY_MEM_MIDDLE_NAME = (By.CSS_SELECTOR, '#fam_members_modal div[data-field=fam_members_middle_name_modal] input')
    FAMILY_MEM_GENDER = "$('#fam_members_modal div[data-field=fam_members_gender_modal] .ui.dropdown')"
    FAMILY_MEM_BIRTHDAY = (By.ID, 'fam_members_birth_modal')
    FAMILY_MEM_ADDRESS = (By.CSS_SELECTOR, '#fam_members_modal div[data-field=fam_members_address_modal] input')
    FAMILY_MEM_HIV_STATUS = "$('#fam_members_modal div[data-field=fam_members_hiv_status_modal] .ui.dropdown')"
    FAMILY_MEM_RELATION = "$('#fam_members_modal div[data-field=fam_members_rod_svyaz_modal] .ui.dropdown')"
    FAMILY_MEM_SAVE = (By.CSS_SELECTOR, '#fam_members_modal .ui.green.approve.button')
    EPID_HISTORY_FILLING_DATE = (By.ID, 'epid_history_date_zapolnen')
    EPID_DOCTOR = "$('div[data-field=epid_history_fio_doctor_epidemiolog] .ui.dropdown')"

    LUIN_RS = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-luin_rs]')"
    DRUG_EXPERIENCE = "$('#form_luin div[data-field=luin_rs_drug_experiens_modal] .ui.dropdown')"
    DRUG_USE_IN_TWELVE_MONTH = "$('#form_luin div[data-field=luin_rs_drug_experiens_in_twelve_month_modal] .ui.dropdown')"
    DRUG_USE_YEARS = "$('#nark_staj_year')"
    DRUG_USE_MONTH = "$('#nark_staj_mounth')"
    SHARING_DRUG_INJECTION = "$('#form_luin div[data-field=luin_rs_drug_together_experiens_modal] .ui.dropdown')"
    SHARING_DRUG_INJ_WITH_HIV = "$('#form_luin div[data-field=luin_rs_drug_experiens_hiv_modal] .ui.dropdown')"
    SHARING_DRUG_INJ_WITH_SEXUAL_PARTNER = "$('#form_luin div[data-field=pol_partner_sex] input')"
    SHARING_DRUG_INJ_WITH_PERMANENT_GROUP = "$('#form_luin div[data-field=permanent_group_sex] input')"
    SHARING_DRUG_INJ_WITH_RANDOM_GROUP = "$('#form_luin div[data-field=random_group_sex] input')"
    HERAIN = "$('#form_luin div[data-field=heroin] input')"
    HANKA = "$('#form_luin div[data-field=hanka] input')"
    MAK = "$('#form_luin div[data-field=mak] input')"
    AMPHETAMIN = "$('#form_luin div[data-field=amfetamin] input')"
    SINTETHICS = "$('#form_luin div[data-field=sintetic] input')"
    OTHER_DRUGS = "$('#form_luin div[data-field=another] input')"
    ACCOUNTED_IN_NARCO_DISP = "$('#form_luin div[data-field=luin_rs_uchet_narko_modal] .ui.dropdown')"
    ACCOUNTED_IN_POLICE_FILES = "$('#form_luin div[data-field=luin_rs_uchet_police_modal] .ui.dropdown')"
    COMMERCIAL_SEX_EXP = "$('#form_luin div[data-field=luin_commercial_sex_modal] .ui.dropdown')"
    COMMERCIAL_SEX_EXP_YEARS = "$('#RC_staj_year')"
    COMMERCIAL_SEX_EXP_MONTH = "$('#RC_staj_month')"
    COMMERCIAL_SEX_PARTNER_NUM = "$('#RC_pol_partn')"
    CONDOM_USAGE = "$('#form_luin div[data-field=luin_guard_on_last_sex_modal] .ui.dropdown')"
    LUIN_RS_SAVE = (By.ID, 'button_save_luin')

    SEXUAL_CONTACTS = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-sex]')"
    HOMO_EXPIRIENCE = "$('div[data-field=sex_gomosex_modal] .ui.dropdown')"
    HOMO_EXP_YEAR = "$('div[data-field=sex_gomosex_twelve_month_modal] .ui.dropdown')"
    HOMO_SEX_PARTNER_NUM = "$('div[data-field=sex_gomosex_count_modal] input')"
    HOMO_SEX_PARTNER_NUM_YEAR = "$('div[data-field=sex_gomosex_twelve_month_modal] input')"
    COMMERCIAL_HOMO_SEX_PARTNER_YEAR = "$('div[data-field=sex_commercial_gomosex_twelve_month_modal] .ui.dropdown')"
    HOMO_SEX_WITH_HIV = "$('div[data-field=sex_sex_with_hiv_modal] .ui.dropdown')"
    HOMO_SEX_WITH_LUIN = "$('div[data-field=sex_sex_with_luin_modal] .ui.dropdown')"
    HOMO_PERMANENT_SEX_PARTNERS = "$('div[data-field=gomo_permanent_live] input')"
    HOMO_RANDOM_SEX_PARTNERS = "$('div[data-field=gomo_random_live] input')"
    COMMERCIAL_HOMO_SEX_PARTNERS = "$('div[data-field=gomo_komer_live] input')"
    HOMO_PERMANENT_SEX_PARTNERS_YEAR = "$('div[data-field=gomo_permanent_last_twelve_month] input')"
    HOMO_RANDOM_SEX_PARTNERS_YEAR = "$('div[data-field=gomo_random_last_twelve_month] input')"
    COMMERCIAL_HOMO_SEX_PARTNERS_YEAR = "$('div[data-field=gomo_komer_last_twelve_month] input')"

    HETERO_EXPIRIENCE = "$('div[data-field=sex_geterosex_expiriens_modal] .ui.dropdown')"
    COMMERCIAL_HET_SEX_PARTNER = "$('div[data-field=sex_commercial_partner_modal] .ui.dropdown')"
    HET_SEX_WITH_HIV = "$('div[data-field=sex_with_hiv_partner_modal] .ui.dropdown')"
    HET_SEX_WITH_LUIN = "$('div[data-field=sex_with_luin_modal] .ui.dropdown')"
    HET_SEX_PARTNER_NUM_YEAR = "$('div[data-field=sex_twelve_month_modal] input')"
    HET_SEX_EXP_YEAR = "$('div[data-field=sex_geterosex_twelve_month_modal] .ui.dropdown')"
    HET_PERMANENT_SEX_PARTNERS_YEAR = "$('div[data-field=permanent_year] input')"
    HET_RANDOM_SEX_PARTNERS_YEAR = "$('div[data-field=random_year] input')"
    COMMERCIAL_HET_SEX_PARTNERS_YEAR = "$('div[data-field=komer_year] input')"
    HET_PERMANENT_SEX_PARTNERS_LIVE = "$('div[data-field=permanent_live] input')"
    HET_RANDOM_SEX_PARTNERS_LIVE = "$('div[data-field=random_live] input')"
    COMMERCIAL_HET_SEX_PARTNERS_LIVE = "$('div[data-field=komer_live] input')"
    SEXUAL_CONTACTS_SAVE = (By.ID, 'button_save_sex')

    MLS = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-mls]')"
    MLS_EXPERIENCE = "$('div[data-field=mls-opit-checkbox] input')"
    MLS_ADD = "$('#mls_table_edit')"
    MLS_NAME = "$('#modal_mls div[data-field=mls_name_modal] .ui.dropdown')"
    MLS_DATE_START = "$('#mls_date_start_modal')"
    MLS_DATE_END = "$('#mls_date_end_modal')"
    MLS_SAVE = "$('#modal_mls .ui.green.approve.button')"


    DONOR = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-donor]')"
    BLOOD_DONOR = "$('div[data-field=donor_krovi_opit_checkbox] input')"
    DONATION_EXISTENCE = "$('div[data-field=nalichie_donacii_pri_viyavlenii_checkbox] input')"
    BLOOD_DONOR_ADD = "$('#donor_blood_table a[action-type=add]')"
    BLOOD_DONATION_PLACE = "$('#donor_blood_modal div[data-field=donor_blood_place_modal] .ui.dropdown')"
    BLOOD_DONATION_AREA = "$('#donor_blood_modal div[data-field=donor_blood_obl_modal] .ui.dropdown')"
    BLOOD_DONATION_UNIT_AREA = "$('#donor_blood_modal div[data-field=donor_blood_adm_obl_modal] .ui.dropdown')"
    BLOOD_DONATION_LOCALITY = "$('#donor_blood_modal div[data-field=donor_blood_locality_modal] .ui.dropdown')"
    BLOOD_DONATION_DATE = "$('#donor_blood_date_donation_modal')"
    BLOOD_DONATION_MED_ORG = "$('#donor_blood_modal div[data-field=donor_blood_name_mo_modal] .ui.dropdown')"
    BLOOD_DONOR_CATEGORY = "$('#donor_blood_modal div[data-field=donor_blood_donor_category_modal] .ui.dropdown')"
    BLOOD_DONOR_TYPE = "$('#donor_blood_modal div[data-field=donor_blood_donor_type_modal] .ui.dropdown')"
    BLOOD_DONOR_CODE = "$('#donor_blood_modal div[data-field=donor_blood_donor_code_modal] input')"
    BLOOD_DONATION_CODE = "$('#donor_blood_modal div[data-field=donor_blood_donation_code_modal] input')"
    BLOOD_HIV_ANALYSIS_DATE = "$('#donor_blood_date_obsled_hiv_modal')"
    BLOOD_HIV_STATUS = "$('#donor_blood_modal div[data-field=donor_blood_hiv_status_modal] .ui.dropdown')"
    BLOOD_DONOR_SAVE = "$('#donor_blood_modal .ui.green.approve.button')"

    ORGAN_DONOR = "$('div[data-field=donor_organ_opit_checkbox] input')"
    ORGAN_DONOR_ADD = "$('#donor_other_material_table a[action-type=add]')"
    ORGAN_DONATION_PLACE = "$('#donor_other_material_modal div[data-field=donor_other_material_place_modal] .ui.dropdown')"
    ORGAN_DONATION_AREA = "$('#donor_other_material_modal div[data-field=donor_other_material_obl_modal] .ui.dropdown')"
    ORGAN_DONATION_UNIT_AREA = "$('#donor_other_material_modal div[data-field=donor_other_material_adm_obl_modal] .ui.dropdown')"
    ORGAN_DONATION_LOCALITY = "$('#donor_other_material_modal div[data-field=donor_other_material_locality_modal] .ui.dropdown')"
    ORGAN_DONATION_DATE = "$('#donor_other_material_date_donation_modal')"
    ORGAN_DONOR_MED_ORG = "$('#donor_other_material_modal div[data-field=donor_other_material_name_mo_get_modal] .ui.dropdown')"
    ORGAN_DONATION_CATEGORY = "$('#donor_other_material_modal div[data-field=donor_other_material_donor_category_modal] .ui.dropdown')"
    ORGAN_DONOR_TYPE = "$('#donor_other_material_modal div[data-field=donor_other_material_donor_type_modal] .ui.dropdown')"
    ORGAN_DONOR_MAT_TYPE = "$('#donor_other_material_modal div[data-field=donor_other_material_material_type_modal] .ui.dropdown')"
    ORGAN_DONOR_MAT_NO = "$('#donor_other_material_modal div[data-field=donor_blood_material_number_modal] input')"
    ORGAN_RECIPIENT_MED_ORG = "$('#donor_other_material_modal div[data-field=donor_blood_name_mo_post_modal] .ui.dropdown')"
    ORGAN_HIV_ANALYSIS_DATE = "$('#donor_other_material_date_obsled_hiv_modal')"
    ORGAN_HIV_STATUS = "$('#donor_other_material_modal div[data-field=donor_other_material_hiv_status_modal] .ui.dropdown')"
    ORGAN_DONOR_SAVE = "$('#donor_other_material_modal .ui.green.approve.button')"

    RECIPIENT = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-recipient]')"
    BLOOD_RECIPIENT = "$('div[data-field=recipient_krov_opit_checkbox] input')"
    BLOOD_RECIPIENT_ADD = "$('#recipient_blood_table a[action-type=add]')"
    TRANSFUSION_PLACE = "$('#recipient_blood_modal div[data-field=recipient_blood_place_modal] .ui.dropdown')"
    BLOOD_TRANSFUSION_AREA = "$('#recipient_blood_modal div[data-field=recipient_blood_obl_modal] .ui.dropdown')"
    BLOOD_TRANSFUSION_UNIT_AREA = "$('#recipient_blood_modal div[data-field=recipient_blood_adm_obl_modal] .ui.dropdown')"
    BLOOD_TRANSFUSION_LOCALITY = "$('#recipient_blood_modal div[data-field=recipient_blood_locality_modal] .ui.dropdown')"
    BLOOD_TRANSFUSION_DATE = "$('#recipient_blood_date_get_comp_modal')"
    BLOOD_TRANSFUSION_MED_ORG = "$('#recipient_blood_modal div[data-field=recipient_blood_name_mo_modal] .ui.dropdown')"
    EPID_HISTORY_NUM_REC = "$('#recipient_blood_modal div[data-field=recipient_blood_history_number_modal] input')"
    BLOOD_DONOR_CODE_REC = "$('#recipient_blood_modal div[data-field=recipient_blood_donor_code_modal] input')"
    BLOOD_COMPONENT_CODE_REC = "$('#recipient_blood_modal div[data-field=recipient_blood_comp_code_modal] input')"
    BLOOD_HIV_STATUS_REC = "$('#recipient_blood_modal div[data-field=recipient_blood_hiv_status_modal] .ui.dropdown')"
    BLOOD_RECEIPT_SAVE = "$('#recipient_blood_modal .ui.green.approve.button')"

    ORGAN_RECIPIENT =  "$('div[data-field=recipient_org_opit_checkbox] input')"
    ORGAN_RECIPIENT_ADD = "$('#recipient_other_material_table a[action-type=add]')"
    ORGAN_TRANSFUSION_PLACE = "$('#recipient_other_material_modal div[data-field=recipient_other_material_place_modal] .ui.dropdown')"
    ORGAN_TRANSFUSION_AREA = "$('#recipient_other_material_modal div[data-field=recipient_other_material_obl_modal] .ui.dropdown')"
    ORGAN_TRANSFUSION_UNIT_AREA = "$('#recipient_other_material_modal div[data-field=recipient_other_material_adm_obl_modal] .ui.dropdown')"
    ORGAN_TRANSFUSION_LOCALITY = "$('#recipient_other_material_modal div[data-field=recipient_other_material_locality_modal] .ui.dropdown')"
    ORGAN_DONOR_MED_ORG_REC = "$('#recipient_other_material_modal div[data-field=recipient_other_material_name_get_material_modal] .ui.dropdown')"
    ORGAN_RECEIPT_MED_ORG = "$('#recipient_other_material_modal div[data-field=recipient_other_material_name_mo_material_modal] .ui.dropdown')"
    ORGAN_TRANSFUSION_DATE = "$('#recipient_other_material_date_get_modal')"
    ORGAN_DONOR_MAT_NO_REC = "$('#recipient_other_material_modal div[data-field=recipient_other_material_number_modal] input')"
    ORGAN_DONOR_MAT_TYPE_REC = "$('#recipient_other_material_modal div[data-field=recipient_other_material_type_material_modal] .ui.dropdown')"
    ORGAN_DONOR_NAME = "$('#recipient_other_material_modal div[data-field=recipient_other_material_fio_donor_modal] input')"
    ORGAN_HIV_STATUS_REC = "$('#recipient_other_material_modal div[data-field=recipient_other_material_hiv_status_modal] .ui.dropdown')"
    ORGAN_RECEIPT_SAVE = "$('#recipient_other_material_modal .ui.green.approve.button')"

    IPPP = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-ippp]')"
    IPPP_SYMPTOM_EXISTENCE = "$('div[data-tab=patient_card_menu-ippp] div[data-field=ipp_data_ippp_symptom] .ui.dropdown')"
    DISP_ACCOUNTED_KVD = "$('div[data-tab=patient_card_menu-ippp] div[data-field=ipp_data_ippp_kvd] .ui.dropdown')"
    DK_CONTACTING = "$('div[data-tab=patient_card_menu-ippp] div[data-field=ipp_data_ippp_dk] .ui.dropdown')"
    DK_CONTACTING_NUM_YEAR = "$('input[name=ipp_data_dk_kol]')"
    PRIVATE_CLINICS_CONTACTING = "$('div[data-tab=patient_card_menu-ippp] div[data-field=ipp_data_ippp_chast_klin] .ui.dropdown')"
    PRIVATE_CLINICS_CONTACTING_NUM = "$('input[name=ipp_data_chast_klin_kol]')"
    IPPP_SYMPTOM_ADD = "$('#ippp_diag_table a[action-type=add]')"
    DIAGNOSIS_DATE = "$('#ippp_diag_modal .ui.calendar')"
    DIAGNOSIS = "$('#ippp_diag_modal div[data-field=ippp_diag_diag_modal] input')"
    IPPP_SYMPTOM_SAVE = "$('#ippp_diag_modal .ui.green.approve.button')"
    C_SECTION_DELIVERY = "$('div[data-tab=patient_card_menu-ippp] div[data-field=child_kesarev] .ui.dropdown')"
    MATERNAL_CHEMOPROPHYLAXIS = "$('div[data-tab=patient_card_menu-ippp] div[data-field=child_mather_himoi] .ui.dropdown')"
    ARTIFICIAL_FEEDING = "$('div[data-tab=patient_card_menu-ippp] div[data-field=child_iskust_vskam] .ui.dropdown')"
    CHILD_CHEMOPROPHYLAXIS = "$('div[data-tab=patient_card_menu-ippp] div[data-field=child_child_himio] .ui.dropdown')"

    MANIPULATIONS_EMERGENCIES = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-manipulations]')"
    MANIPULATION_EXISTENCE = "$('div[data-field=nalich_anam_manipul_checkbox] input')"
    MANIPULATIONS_ADD = "$('#manipulations_med_table a[action-type=add]')"
    MANIPULATIONS_DATE = "$('#manipulations_med_modal .ui.calendar')"
    MANIPULATIONS_SORT = "$('#manipulations_med_modal div[data-field=manipulations_med_vid_modal] .ui.dropdown')"
    MANIPULATIONS_TYPE = "$('#manipulations_med_modal div[data-field=manipulations_med_type_modal] .ui.dropdown')"
    MANIPULATIONS_MED_ORG = "$('#manipulations_med_modal div[data-field=manipulations_med_name_org_modal] .ui.dropdown')"
    MANIPULATIONS_SAVE = "$('#manipulations_med_modal .ui.green.approve.button')"

    EMERGENCIES = "$('div[data-field=avar_situac_checkbox] input')"
    EMERGENCIES_ADD = "$('#manipulations_avariya_table a[action-type=add]')"
    EMERGENCIES_DATE = "$('#manipulations_avariya_modal .ui.calendar')"
    INFECTION_RISK = "$('#manipulations_avariya_modal div[data-field=manipulations_avariya_risk_infection_modal] .ui.dropdown')"
    EMERGENCIES_MED_ORG = "$('#manipulations_avariya_modal div[data-field=manipulations_avariya_name_org_modal] input')"
    TRAUMA_TYPE = "$('#manipulations_avariya_modal div[data-field=manipulations_avariya_vid_travmy_modal] .ui.dropdown')"
    EMERGENCIES_72HOURS = "$('#manipulations_avariya_modal div[data-field=manipulations_avariya_pkp_modal] .ui.dropdown')"
    EMERGENCIES_HIV_STATUS = "$('#manipulations_avariya_modal div[data-field=manipulations_avariya_hiv_status_modal] .ui.dropdown')"
    EMERGENCIES_SAVE = "$('#manipulations_avariya_modal .ui.green.approve.button')"

    DEPARTURES_SOURCES = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-sources]')"
    DEPARTURE_EXISTENCE = "$('div[data-field=nalich_viezd_checkbox] input')"
    DEPARTURE_ADD = "$('#sources_za_predeli_rk_table a[action-type=add]')"
    DEPARTURE_DATE_START = "$('#sources_infection_modal div[data-field=sources_infection_date_start_modal] .ui.input')"
    DEPARTURE_DATE_END = "$('#sources_infection_modal div[data-field=sources_infection_date_end_modal] .ui.input')"
    DEPARTURE_COUNTRY = "$('#sources_infection_modal div[data-field=sources_infection_country_modal] .ui.dropdown')"
    DEPARTURE_PURPOSE = "$('#sources_infection_modal div[data-field=sources_infection_cel_modal] .ui.dropdown')"
    DEPARTURE_SAVE = "$('#sources_infection_modal .ui.green.approve.button')"

    INFECTION_SOURCE_EXISTENCE = "$('div[data-field=nalich_predpol_istoch_checkbox] input')"
    SOURCE_ADD = "$('#sources_infection_table a[action-type=add]')"
    SOURCE_IB_NUM = "$('#sources_contact_modal div[data-field=sources_contact_ib_number_modal] input')"
    SOURCE_IB_DATE = "$('#sources_contact_modal div[data-field=sources_contact_ib_date_modal] .ui.input')"
    SOURCE_SURNAME = "$('#sources_contact_modal div[data-field=sources_contact_last_name_modal] input')"
    SOURCE_NAME = "$('#sources_contact_modal div[data-field=sources_contact_name_modal] input')"
    SOURCE_MIDDLE_NAME = "$('#sources_contact_modal div[data-field=sources_contact_middle_name_modal] input')"
    SOURCE_SAVE = "$('#sources_contact_modal .ui.green.approve.button')"

    CONTACT_PERSON = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-contact]')"
    CONTACT_PERSON_EXISTENCE = "$('div[data-field=nalich_kontakt_lic_checkbox] input')"
    CONTACT_PERSON_ADD = "$('#contact_faces_table a[action-type=add]')"
    CONTACT_PERSON_SURNAME = "$('#contact_last_name_modal')"
    CONTACT_PERSON_NAME = "$('#contact_name_modal')"
    CONTACT_PERSON_MIDDLE_NAME = "$('#contact_middle_name_modal')"
    CONTACT_PERSON_GENDER = "$('#contact_modal div[data-field=contact_gender_modal] .ui.dropdown')"
    CONTACT_PERSON_BIRTHDAY = "$('#contact_modal div[data-field=sources_contact_ib_date_modal] .ui.input')"
    CONTACT_DATE_START = "$('#contact_date_start_modal')"
    CONTACT_TYPE = "$('#contact_modal div[data-field=contact_type_modal] .ui.dropdown')"
    CONTACT_IB_NUM = "$('#contact_ib_number_modal')"
    CONTACT_IB_NUM_DATE = "$('#contact_date_ib_modal')"
    CONTACT_SURVEY_ADD = "$('#obsled_table a[action-type=add]')"
    CONTACT_DIAGNOSTICS_DATE = "$('#obsled_modal .ui.calendar')"
    CONTACT_HIV_STATUS = "$('#obsled_modal div[data-field=obsled_status_modal] .ui.dropdown')"
    CONTACT_SURVEY_SAVE = "$('#obsled_modal .ui.green.approve.button')"
    REASON_NOT_SURVEYING = "$('#contact_modal div[data-field=contact_reason_not_obsled_modal] .ui.dropdown')"
    CONTACT_FINISHED = "$('#contact_modal div[data-field=contact_end_modal] input')"
    CONTACT_DAY_END = "$('#contact_date_end_modal')"
    CONTACT_AREA = "$('#contact_modal div[data-field=contact_obl_modal] .ui.dropdown')"
    CONTACT_UNIT_AREA = "$('#contact_modal div[data-field=contact_adm_ed_modal] .ui.dropdown')"
    CONTACT_LOCALITY = "$('#contact_modal div[data-field=contact_locality_modal] .ui.dropdown')"
    CONTACT_STREET = "$('#contact_street_modal')"
    CONTACT_HOUSE = "$('#contact_house_numb_modal')"
    CONTACT_APT = "$('#contact_parter_numb_modal')"
    CONTACT_PHONE_NO = "$('#contact_tel_numb_modal')"
    CONTACT_PERSON_SAVE = "$('#contact_modal .ui.green.approve.button')"

    DISP_OBSERVATION = "$('a[data-name=disp-search]')"
    DISP_OBSER_ADD = "$('#d_uchet_table a[action-type=add]')"
    D_OBSER_AIDC_CENTER = "$('#modal_d_uchet_vzyatie div[data-field=vzyatie_org_modal] .ui.dropdown')"
    DATE_OF_REGIS = "$('#modal_d_uchet_vzyatie div[data-field=vzyatie_date_modal] .ui.input')"
    DATE_OF_DEREGIS = "$('#modal_d_uchet_vzyatie div[data-field=duchet_date_snyatie_modal] .ui.input')"
    D_OBSER_REASON_OF_DEREGIS = "$('#modal_d_uchet_vzyatie div[data-field=duchet_reason_snyatie_modal] .ui.dropdown')"
    D_OBSER_COUNTRY = "$('#modal_d_uchet_vzyatie div[data-field=duchet_country_name_modal] .ui.dropdown')"
    D_OBSER_AREA = "$('#modal_d_uchet_vzyatie div[data-field=duchet_region_name_modal] .ui.dropdown')"
    D_OBSER_UNIT_AREA_CLICK = "$('#modal_d_uchet_vzyatie div[data-field=duchet_unit_area_modal] input.search')"
    D_OBSER_UNIT_AREA = "$('#modal_d_uchet_vzyatie div[data-field=duchet_unit_area_modal] .ui.dropdown')"
    DATE_OF_DEATH = "$('#modal_d_uchet_vzyatie div[data-field=death_date_modal] .ui.input')"
    AIDC_RELATED_DEATH = "$('#modal_d_uchet_vzyatie div[data-field=death_svyaz_hiv_modal] .ui.dropdown')"
    DEATH_REASON = "$('#modal_d_uchet_vzyatie div[data-field=death_reason_modal] .ui.dropdown')"
    DEATH_PLACE = "$('#modal_d_uchet_vzyatie div[data-field=death_place_modal] .ui.dropdown')"
    AUTOPSY = "$('#modal_d_uchet_vzyatie div[data-field=death_vskrit_modal] .ui.toggle.checkbox')"
    PATHOLOGOANATOMIC_DIAGNOSIS = "$('#modal_d_uchet_vzyatie div[data-field=death_patolog_diag] input')"
    D_OBSER_SAVE = "$('#modal_d_uchet_vzyatie .actions .ui.green.approve.button')"
    DRUG_INJ_CONSUMPTION = "$('div[data-field=d_uchet_upotren_inek_nark] .ui.dropdown')"
    DRUG_CONSUMPTION_YEAR = "$('div[data-field=d_uchet_year_upotreb_nark] input')"
    DRUG_CONSUMPTION_REGIS = "$('div[data-field=d_uchet_uchot_narkolog] .ui.dropdown')"
    ALCOHOL_CONSUMPTION = "$('div[data-field=d_uchet_zloupotreb_alk] .ui.dropdown')"
    OUTPATIENT_CARD_NO = "$('div[data-field=patient_ambulator_card] input')"
    DISP_START_DATE = "$('div[data-field=date_first_vzyat_d_uchet] .ui.input')"
    DISP_DOCTORS_NAME = "$('div[data-field=patient_fio_doctor_dd] .ui.dropdown')"
    DISP_SAVE_BTN = "$('#button_save_d_uchet_data')"

    PERINATAL_REGISTRATION = "$('a[data-tab=patient_card_menu-perenat_uchet]')"
    PERINATAL_REGIS_ADD = "$('#perenat_uchet_table a[action-type=add]')"
    PERINATAL_MED_ORG = "$('#modal_perinat_uchet div[data-field=perinat_uchet_vzyatie_org_modal] .ui.dropdown')"
    PERINATAL_DATE_OF_REGIS = "$('#modal_perinat_uchet div[data-field=perinat_uchet_vzyatie_date_modal] .ui.input')"
    PERINATAL_DATE_OF_DEREGIS = "$('#modal_perinat_uchet div[data-field=perinat_uchet_date_snyatie_modal] .ui.input')"
    PERINATAL_REASON_OF_DEREGIS = "$('#modal_perinat_uchet div[data-field=perinat_uchet_reason_snyatie_modal] .ui.dropdown')"
    PERINATAL_COUNTRY = "$('#modal_perinat_uchet div[data-field=perinat_uchet_country_name_modal] .ui.dropdown')"
    PERINATAL_AREA = "$('#modal_perinat_uchet div[data-field=perinat_uchet_region_name_modal] .ui.dropdown')"
    PERINATAL_UNIT_AREA = "$('#modal_perinat_uchet div[data-field=perinat_uchet_unit_area_modal] .ui.dropdown')"
    PERINATAL_DATE_OF_DEATH = "$('#modal_perinat_uchet div[data-field=death_date_modal] ui.input')"
    PERINATAL_DEATH_REASON = "$('#modal_perinat_uchet div[data-field=death_reason_modal] .ui.dropdown')"
    PERINATAL_DEATH_PLACE = "$('#modal_perinat_uchet div[data-field=death_place_modal] .ui.dropdown')"
    PERINATAL_SAVE = "$('#modal_perinat_uchet .ui.green.approve.button')"

    ARV_PROPHYLAXIS = "$('div[data-field=perinat_uchet_arv_profil] .ui.dropdown')"
    ARV_START_DATE = "$('div[data-field=perinat_uchet_arv_date_start] .ui.input')"
    ARV_END_DATE = "$('div[data-field=perinat_uchet_arv_date_end] .ui.input')"
    ARV_MEDICATION = "$('div[data-field=perinat_uchet_preparat] .ui.dropdown')"
    ARV_ISSUANCE = "$('#get_preparat_perenat')"
    ARV_ISSUANCE_ADD = "$('#is_table a[action-type=add]')"
    ARV_MEDICATION_NAME = "$('#modal_art_preparaty_perenat div[data-field=art_preparat_name_modal] .inverted.circular.icon')"
    ARV_MEDICATION_NAME_CHOICE = "$('#add-row-preparaty-table tr:eq(0) td:eq(0) a')"
    ARV_RECIPE_NUM = "$('div[data-field=art_preparat_number_receipt_modal] .ui.input')"
    ARV_DAY_NUM = "$('div[data-field=art_preparat_count_day_modal] .ui.input')"
    ARV_NEXT_DATE = "$('div[data-field=art_preparat_count_day_modal] input')"
    ARV_MEDICATION_SAVE = "$('#modal_art_preparaty_perenat .ui.green.approve.button')"
    ARV_ISSUANCE_SAVE = "$('#modal_perinat_uchet_preparat .ui.green.approve.button')"
    PCP_PROPHYLAXIS_START_DATE = "$('div[data-field=child_pcp_date_start_modal] .ui.input')"
    PCP_PROPHYLAXIS_END_DATE = "$('div[data-field=child_pcp_date_end_modal] .ui.input')"
    ARV_HIV_STATUS = "$('div[data-field=child_hiv_state_modal] .ui.dropdown')"
    ARV_HIV_DETERMINATION_DATE = "$('div[data-field=child_date_check_modal] .ui.input')"

    HIV_DIAGNOSIS = "$('div[data-field=patient_card_tabs] a[data-tab=patient_card_menu-diagnoz_vich]')"
    HIV_DIAGNOSIS_ADD = "$('#hiv_table  a[action-type=add]')"
    FORMULATING_CHANGE_DATE = "$('#modal_diagnoz_hiv  .ui.calendar')"
    HIV_STAGE = "$('#modal_diagnoz_hiv div[data-field=diagnoz_hiv_stage_hiv_modal] .ui.dropdown')"
    HIV_DIAGNOSIS_SAVE = "$('#modal_diagnoz_hiv .ui.green.approve.button')"
    HIV_RELATED_DISEASE_ADD = "$('#diag_opurt_table  a[action-type=add]')"
    RELATED_DISEASE_HIV_STAGE = "$('#modal_oppurt_hiv div[data-field=diagnoz_opurt_stage_modal]')"
    RELATED_DISEASE_HIV_STAGE_CHOICE = "$('#modal_oppurt_hiv div[data-field=diagnoz_opurt_stage_modal] div.menu').children()[0]"
    DISEASE_START_DATE = "$('#diagnoz_opurt_date_start_modal')"
    DISEASE_NAME = "$('#modal_oppurt_hiv div[data-field=diagnoz_opurt_name_modal] .ui.dropdown')"
    DISEASE_END_DATE = "$('#diagnoz_opurt_date_end_modal')"
    HIV_RELATED_DISEASE_SAVE = "$('#modal_oppurt_hiv .ui.green.approve.button')"
    RECOM_CONSULTATION_ADD = "$('#recomended_consultation_table_edit')"
    CONSULTATION_DATE = "$('#modal_recomended_consultation .ui.calendar')"
    CONSULTATION = "$('#modal_recomended_consultation div[data-field=recomended_consultation_consultation_modal] .ui.dropdown')"
    CONSULTATION_DESCRIPTION = "$('#recomended_consultation_description_modal')"
    RECOM_CONSULTATION_SAVE = "$('#modal_recomended_consultation .ui.green.approve.button')"
    RECOM_SCREENING_ADD = "$('#recomended_obledovaniya_table_edit')"
    SCREENING_DATE = "$('#modal_recomended_obsled .ui.calendar')"
    SURVEY = "$('#modal_recomended_obsled div[data-field=recomended_obsled_obsled_modal] .ui.dropdown')"
    SCREENING_DESCRIPTION = "$('#recomended_obsled_description_modal')"
    RECOM_SCREENING_SAVE = "$('#modal_recomended_obsled .ui.green.approve.button')"
    REFERRAL_ADD = "$('#refferals_table a[action-type=add]')"
    REFERRAL_DATE = "$('#modal_refferals .ui.calendar')"
    REFERRAL_NAME = "$('#modal_refferals div[data-field=refferals_name_modal] .ui.dropdown')"
    REFERRAL_NUM = "$('#refferals_number_modal')"
    SENDER_ORG = "$('#modal_refferals div[data-field=refferals_org_sender_modal] .ui.dropdown')"
    RECIPIENT_ORG = "$('#modal_refferals div[data-field=refferals_org_recipient_modal] .ui.dropdown')"
    CATEGORY = "$('#modal_refferals div[data-field=refferals_category_modal] .ui.dropdown')"
    NOSOLOGY = "$('#modal_refferals div[data-field=refferals_nozology_modal] .ui.dropdown')"
    NOSOLOGY_CHOICE = "$('#modal_refferals div[data-field=refferals_nozology_modal] div.menu').children()[0]"
    SURVEY_ELEMENTS = "$('#refferals_research_elements_modal')"
    SCREENING_RESULT = "$('#refferals_value_modal')"
    REFERRAL_SAVE = "$('#modal_refferals  .ui.green.approve.button')"

    CD4_VL_SURVEY = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-obsledovanie_cd4_disp]')"
    CD4_DETERMINATION_ADD = "$('#obsled_cd4_lab_table a[action-type=add]')"
    REGISTRATION_NUM = "$('#obsled_cd4_modal div[data-field=obsled_cd4_reg_number_modal] input')"
    CD4_BLOOD_DONOR_MED_ORG = "$('#obsled_cd4_modal div[data-field=obsled_cd4_mo_naprav_modal] .ui.dropdown')"
    CD4_MATERIAL_RECEIPT_DATE = "$('#obsled_cd4_date_postup_modal')"
    CD4_SAMPLE_RECEIPT_DATE = "$('#obsled_cd4_get_sample_modal')"
    CD4_REGISTERING_DATE = "$('#obsled_cd4_date_postanov_modal')"
    CD4 = "$('#obsled_cd4_modal div[data-field=obsled_cd4_cd4_modal] input')"
    CD3 = "$('#obsled_cd4_modal div[data-field=obsled_cd4_cd3_modal] input')"
    CD8 = "$('#obsled_cd4_modal div[data-field=obsled_cd4_cd8_modal] input')"
    CD4_CD8 = "$('#obsled_cd4_modal div[data-field=obsled_cd4_cd4_cd8_modal] input')"
    CD4_rate = "$('#obsled_cd4_modal div[data-field=obsled_cd4_procent_cd4_modal] input')"
    CD4_MED_ORG_PROVIDED_ANALYSIS = "$('#obsled_cd4_modal div[data-field=obsled_cd4_mo_provod_issled_modal] .ui.dropdown')"
    CD4_REMARK = "$('#obsled_cd4_modal div[data-field=obsled_cd4_note_modal] input')"
    CD4_SERVICES = "$('#obsled_cd4_modal div[data-field=obsled_cd4_which_services_modal] .ui.dropdown')"
    CD4_SAVE = "$('#obsled_cd4_modal .ui.green.approve.button')"
    VIRAL_LOAD_ADD = "$('#vn_table a[action-type=add]')"
    VL_ANALYSIS_NUM = "$('#vn_modal div[data-field=vn_issled_number_modal] input')"
    VL_DONOR_MED_ORG = "$('#vn_modal div[data-field=vn_mo_naprav_modal] .ui.dropdown')"
    VL_MATERIAL_RECEIPT_DATE = "$('#vn_date_zabor_modal')"
    VL_MATERIAL_SAMPLING_DATE = "$('#vn_date_postup_material_modal')"
    VL_REGISTERING_DATE = "$('#vn_date_postanov_modal')"
    VL_RESULT = "$('#vn_modal div[data-field=vn_type_result_modal] .ui.dropdown')"
    VL_RESULT_ML = "$('#vn_key')"
    LOG = "$('#vn_modal div[data-field=vn_log_modal] input')"
    VL_MED_ORG_PROVIDED_ANALYSIS = "$('#vn_modal div[data-field=vn_mo_provod_issled_modal] .ui.dropdown')"
    VL_REMARK = "$('#vn_modal div[data-field=vn_note_modal] .ui.dropdown')"
    VL_SERVICES = "$('#vn_modal div[data-field=vn_which_services_modal] .ui.dropdown')"
    VL_SAVE = "$('#vn_modal .ui.green.approve.button')"

    VIRAL_HEPATITIS = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-diagnozis_vgv_vgc_disp]')"
    VGV_ADD = "$('#vgv_disp_table a[action-type=add]')"
    VGV_REGISTRATION_NUM = "$('#vgv_modal div[data-field=vgv_reg_number_modal] input')"
    VGV_MAT_DONOR_MED_ORG = "$('#vgv_modal div[data-field=vgv_otkuda_postup_modal] .ui.dropdown')"
    VGV_MATERIAL_RECEIPT_DATE = "$('#vgv_date_postup_material_modal')"
    VGV_REGISTERING_DATE = "$('#vgv_date_postanov_modal')"
    MARKER = "$('#vgv_modal div[data-field=vgv_marker_modal] .ui.dropdown')"
    VGV_RESULT = "$('#vgv_modal div[data-field=vgv_result_modal] .ui.dropdown')"
    VGV_MED_ORG_PROVIDED_ANALYSIS = "$('#vgv_modal div[data-field=vgv_mo_provod_issled_modal] .ui.dropdown')"
    VGV_REMARK = "$('#vgv_modal div[data-field=vgv_note_modal] input')"
    VGV_SAVE = "$('#vgv_modal .ui.green.approve.button')"
    VGS_ADD = "$('#vgc_disp_table a[action-type=add]')"
    VGS_REGISTRATION_NUM = "$('#vgc_modal div[data-field=vgc_reg_number_modal] input')"
    VGS_MAT_DONOR_MED_ORG = "$('#vgc_modal div[data-field=vgc_otkuda_postup_modal] .ui.dropdown')"
    VGS_MATERIAL_RECEIPT_DATE = "$('#vgc_date_postup_material_modal')"
    VGS_REGISTERING_DATE = "$('#vgc_date_postanov_modal')"
    VGS_ANALYSIS_TYPE = "$('#vgc_modal div[data-field=vgc_research_type_modal] .ui.dropdown')"
    VGS_RESULT = "$('#vgc_modal div[data-field=vgc_result_modal] .ui.dropdown')"
    VGS_MED_ORG_PROVIDED_ANALYSIS = "$('#vgc_modal div[data-field=vgc_mo_provod_issled_modal] .ui.dropdown')"
    VGS_REMARK = "$('#vgc_modal div[data-field=vgc_note_modal] input')"
    VGS_SAVE = "$('#vgc_modal .ui.green.approve.button')"
    VGV_VAC_ADD = "$('#vgv_vakcin_disp_table a[action-type=add]')"
    VGV_VAC_MULTIPLICITY = "$('#vgv_vakcin_modal div[data-field=vgv_vakcin_kratnost_modal] .ui.dropdown')"
    IMMUNIZATION_DATE = "$('#vgv_vakcin_modal .ui.calendar')"
    VGV_VAC_DOSE_VOLUME = "$('#vgv_vakcin_modal div[data-field=vgv_vakcin_value_modal] input')"
    VGV_VAC_SERIES = "$('#vgv_vakcin_modal div[data-field=vgv_vakcin_series_modal] input')"
    VGV_VAC_COUNTRY_PRODUCER = "$('#vgv_vakcin_modal div[data-field=vgv_vakcin_country_modal] input')"
    MED_ORG_PROVIDED_VACCINATION = "$('#vgv_vakcin_modal div[data-field=vgv_vakcin_mo_modal] .ui.dropdown')"
    VGV_VAC_SAVE = "$('#vgv_vakcin_modal .ui.green.approve.button')"

    TUBERCULOSIS = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-tubik]')"
    FLUOROSCOPY_ADD = "$('#flura_table_add')"
    FLUOR_REGISTERING_DATE = "$('#modal_flura .ui.calendar')"
    FLUOR_RESULT = "$('#modal_flura div[data-field=flura_result_modal] .ui.dropdown')"
    FLUOROSCOPY_SAVE = "$('#modal_flura .ui.green.approve.button')"

    RADIOGRAPHY_ADD = "$('#rentgen_table_add')"
    RADIO_REGISTERING_DATE = "$('#modal_rentgen .ui.calendar')"
    RADIO_RESULT = "$('#modal_rentgen div[data-field=rentgen_result_modal] .ui.dropdown')"
    RADIOGRAPHY_SAVE = "$('#modal_rentgen .ui.green.approve.button')"

    SPUTUM_SMEAR_EXAMINATION_ADD = "$('#bakterioskop_table_add')"
    SPUTUM_REGISTERING_DATE = "$('#modal_bakterioskop .ui.calendar')"
    SPUTUM_RESULT = "$('#modal_bakterioskop div[data-field=bakterioskop_result_modal] .ui.dropdown')"
    SPUTUM_SAVE = "$('#modal_bakterioskop .ui.green.approve.button')"

    TB_SYMPHTOMS_ADD = "$('#symptom_tb_table_add')"
    TB_SYMPH_REGISTERING_DATE = "$('#modal_symptom_tb .ui.calendar')"
    TB_SYMPH_RESULT = "$('#modal_symptom_tb div[data-field=symptom_tb_result_modal] .ui.dropdown')"
    TB_SYMPH_SAVE = "$('#modal_symptom_tb .ui.green.approve.button')"

    XPERT_MTB_ADD ="$('#xpert_table_add')"
    XPERT_MTB_REGISTERING_DATE = "$('#modal_xpert .ui.calendar')"
    XPERT_MTB_RESULT = "$('#modal_xpert div[data-field=xpert_result_modal] .ui.dropdown')"
    XPERT_MTB_SAVE = "$('#modal_xpert .ui.green.approve.button')"

    KT_MRT_ADD = "$('#mrt_table_add')"
    KT_MRT_REGISTERING_DATE = "$('#modal_mrt .ui.calendar')"
    KT_MRT_RESULT = "$('#modal_mrt div[data-field=mrt_result_modal] .ui.dropdown')"
    KT_MRT_SAVE = "$('#modal_mrt .ui.green.approve.button')"

    TB_TREATMENT_ADD = "$('#lechenie_tb_table_add')"
    LAB_NAME_CONFIRMED_TB = "$('#lechenie_tb_lpo_name_modal')"
    TB_DIAG_REGISTERING_DATE = "$('#lechenie_tb_date_diag_modal]')"
    SICK_TYPE = "$('#modal_lechenie_tb div[data-field=lechenie_tb_sluchai_bolnogo_modal] .ui.dropdown')"
    TB_DIAG_MKB10 = "$('#modal_lechenie_tb div[data-field=lechenie_tb_diag_po_mkb_modal] .ui.dropdown')"
    LOCATION = "$('#modal_lechenie_tb div[data-field=lechenie_tb_localize_modal] .ui.dropdown')"
    TREATMENT_START_DATE = "$('#lechenie_tb_date_start_modal]')"
    TREATMENT_END_DATE = "$('#lechenie_tb_date_end_modal]')"
    BAC_SECRETION = "$('#modal_lechenie_tb div[data-field=lechenie_tb_bakovidelenie_modal] .ui.dropdown')"
    OUTCOME = "$('#modal_lechenie_tb div[data-field=lechenie_tb_ishod_modal] .ui.dropdown')"
    TB_TREATMENT_SAVE = "$('#modal_lechenie_tb .ui.green.approve.button')"
    PRESENCE_TB_IN_HISTORY = "$('div[data-tab=patient_card_menu-tubik] div[data-field=patient_detail_nalich_TB_anamnez] .ui.dropdown')"
    D_ACCOUNTED_DATE = "$('div[data-field=patient_detail_date_disp_uche_tub]')"

    ART = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-art]')"
    ART_REASONS_DEFINE_DATE = "$('#patient_detail_date_pokaz_art]')"
    ART_READINESS_DEFINE_DATE = "$('#patient_detail_date_priem_art]')"
    WRITTEN_CONSENT = "$('div[data-tab=patient_card_menu-art] div[data-field=patient_detail_get_sogl_art] .ui.dropdown')"
    ART_INFORMATION_ADD = "$('#svedeniya_art_table_add]')"
    ART_START_DATE = "$('#svedeniya_art_date_start_modal]')"
    ART_ROW = "$('#modal_svedeniya_art div[data-field=svedeniya_art_ryad_modal] .ui.dropdown')"
    ART_SCHEME = "$('#modal_svedeniya_art div[data-field=svedeniya_art_scheme_art_modal] .ui.dropdown')"
    ART_MED_ORG = "$('#modal_svedeniya_art div[data-field=svedeniya_art_art_conduct_modal] .ui.dropdown')"
    ART_SCHEME_CHANGED_DATE = "$('#svedeniya_art_treatment_date_change_scheme_modal]')"
    ART_SCHEME_CHANGE_TYPE = "$('#modal_svedeniya_art div[data-field=svedeniya_art_treatment_vid_change_modal] .ui.dropdown')"
    ART_SCHEME_CHANGE_REASON = "$('#modal_svedeniya_art div[data-field=svedeniya_art_treatment_reason_change_modal] .ui.dropdown')"
    ART_INFORMATION_SAVE = "$('#modal_svedeniya_art .ui.green.approve.button')"
    ART_ADHERENCE_SUPPORT = "$('div[data-tab=patient_card_menu-art] div[data-field=podderjky_priverj_art_conduct] .ui.dropdown')"
    ART_ADHER_LEVEL_ADD = "$('#commitment_assessment_table_add]')"
    ART_ADHER_YEAR = "$('#commitment_assessment_year_modal')"
    ART_ADHER_QUARTER = "$('#modal_commitment_assessment div[data-field=commitment_assessment_kvartal_modal] .ui.dropdown')"
    ART_ADHERENCE = "$('#modal_commitment_assessment div[data-field=commitment_assessment_priver_modal] .ui.dropdown')"
    ART_ADHER_LOW_REASONS = "$('#modal_commitment_assessment div[data-field=commitment_assessment_reason_name_modal] .ui.dropdown')"
    SIDE_EFFECTS = "$('#modal_commitment_assessment div[data-field=commitment_assessment_toksich_reak_name_modal] .ui.dropdown')"
    ART_ADHER_LEVEL_SAVE = "$('#modal_commitment_assessment .ui.green.approve.button')"
    ART_RECIPE_ADD =  "$('#recipes_table a[action-type=add]')"
    RECIPE_NUM = "$('#modal_recipes div[data-field=recipes_number_modal] input')"
    RECIPE_DATE = "$('#recipes_date_modal')"
    ART_MEDICATION = "$('#form-receipt-1-preparat_id')"
    DOSE = "$('#modal_recipes div[data-field=form-receipt-1-dozirovka] input')"
    DOSE_CODE = "$('#modal_recipes div[name=form-receipt-1-kod_ed_izm] .ui.dropdown')"
    CONCENTRATION = "$('#modal_recipes div[data-field=form-receipt-1-koncentration] input')"
    PACKING = "$('#modal_recipes div[data-field=form-receipt-{$=it.index$}-fasovka] input')"
    QUANTITY = "$('#modal_recipes div[data-field=form-receipt-1-count] input')"
    UNPACKING_SIGNS = "$('#modal_recipes div[data-field=form-receipt-1-priznak_vskritiya_pack] .ui.dropdown')"
    SIGNATURE = "$('#modal_recipes div[data-field=form-receipt-1-signature] input')"
    ART_RECIPE_SAVE = "$('#modal_svedeniya_art .ui.green.approve.button')"








    CHILDREN_PREGNANCY  = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-children]')"
    PREGNANCY_ADD = "$('#hiv_table_edit')"
    PREGNANCY = "$('#modal_preg div[data-field=preg_count_modal] .ui.dropdown')"
    PREG_SEX_PARTNER = "$('#modal_preg div[data-field=preg_sex_partner_modal] .ui.dropdown')"
    PREG_PARTNER_HIV_STATUS = "$('#modal_preg div[data-field=preg_hiv_state_modal] .ui.dropdown')"
    OGC_REGIS_DATE = "$('#preg_ogc_date_modal')"
    OGC_PREGNANCY_WEEKS = "$('#modal_preg div[data-field=preg_ogc_week_modal] .ui.dropdown')"
    ANTENATAL_CLINIC_REGIS_DATE = "$('#preg_consult_date_modal')"
    AC_PREGNANCY_WEEKS = "$('#modal_preg div[data-field=preg_consult_week_modal] .ui.dropdown')"
    PREGNANCY_RESULT = "$('#modal_preg div[data-field=preg_ishod_modal] .ui.dropdown')"
    PREGNANCY_RESULT_DATE = "$('#preg_date_ishod_modal')"
    PREG_ARV_PROPHILAXYS = "$('#modal_preg div[data-field=preg_arv_prof_modal] .ui.dropdown')"
    PREG_ARV_PROPH_START_DATE = "$('#preg_arv_date_start_modal')"
    PREGNANCY_WEEKS_ARV_START = "$('#modal_preg div[data-field=preg_arv_start_week_modal] .ui.dropdown')"
    PREG_ARV_PROPH_END_DATE = "$('#preg_arv_date_end_modal')"
    PREGNANCY_WEEKS_ARV_END = "$('#modal_preg div[data-field=preg_arv_end_week_modal] .ui.dropdown')"
    PREG_ARV_MEDICATIONS = "$('#modal_preg div[data-field=perinat_uchet_preparat] .ui.dropdown')"
    PREG_ARV_ISSUANCE = "$('#button_for_berem_preparat')"
    PREG_ARV_ISSUANCE_ADD = "$('#is_table a[action-type=add]')"
    PREG_ARV_MEDICATION_NAME = "$('#modal_art_preparaty_berem div[data-field=art_preparat_name_modal] .inverted.circular.icon')"
    PREG_ARV_MEDICATION_NAME_CHOICE = "$('#add-row-preparaty-table tr:eq(0) td:eq(0) a')"
    PREG_ARV_RECIPE_NUM = "$('div[data-field=art_preparat_number_receipt_modal] .ui.input')"
    PREG_ARV_DAY_NUM = "$('div[data-field=art_preparat_count_day_modal] .ui.input')"
    PREG_ARV_NEXT_DATE = "$('div[data-field=art_preparat_count_day_modal] input')"
    PREG_ARV_MEDICATION_SAVE = "$('#modal_art_preparaty_berem .ui.green.approve.button')"
    PREG_ARV_ISSUANCE_SAVE = "$('#modal_art_preparaty_berem_table .ui.green.approve.button')"
    PREG_ARV_ISSUANCE_CHILD = "$('#button_for_future_preparat')"
    CHILD_ARV_ISSUANCE_ADD = "$('#is_table a[action-type=add]')"
    CHILD_ARV_MEDICATION_NAME = "$('#modal_art_preparaty_berem div[data-field=art_preparat_name_modal] .inverted.circular.icon')"
    CHILD_ARV_MEDICATION_NAME_CHOICE = "$('#add-row-preparaty-table tr:eq(0) td:eq(0) a')"
    CHILD_ARV_RECIPE_NUM = "$('div[data-field=art_preparat_number_receipt_modal] .ui.input')"
    CHILD_ARV_MEDICATION_SAVE = "$('#modal_art_preparaty_berem .ui.green.approve.button')"
    CHILD_ARV_ISSUANCE_SAVE = "$('#modal_berem_preparat .ui.green.approve.button')"
    INFORMATION_CHILDREN_ADD = "$('#child_info_table a[action-type=first_add]')"
    ALIVE_CHILD = "$('#modal_child_info div[data-field=child_alive_modal] .ui.dropdown')"
    CHILDS_SURNAME = "$('#child_last_name_modal')"
    CHILDS_NAME = "$('#child_name_modal')"
    CHILDS_MIDNAME = "$('#child_middle_name_modal')"
    CHILDS_BIRTHDAY = "$('#child_date_birth_modal')"
    CHILDS_GENDER = "$('#modal_child_info div[data-field=child_gender_modal] .ui.dropdown')"
    PATHALOGY_AT_BIRTH = "$('#modal_child_info div[data-field=child_potologies_modal] .ui.dropdown')"
    FEEDING = "$('#modal_child_info div[data-field=child_korm_modal] .ui.dropdown')"
    FULL_TERM_CHILD = "$('#modal_child_info div[data-field=child_donosh_modal] .ui.dropdown')"
    CHILDS_DEATH_DATE = "$('#child_date_death_modal')"
    INFORMATION_CHILDREN_SAVE = "$('#modal_child_info .ui.green.approve.button')"
    PREGNANCY_SAVE = "$('#modal_preg .ui.green.approve.button')"

    THERAPHY  = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-therapy]')"
    PREVENTIVE_THERAPHY_ADD = "$('#therapy_opurt_zabolev_table_add')"
    PREV_THER_MEDICATION = "$('#modal_therapy_opurt_zabolev div[data-field=therapy_opurt_zabolev_preparat_modal] .ui.dropdown')"
    REASONS_SET_DATE = "$('#therapy_opurt_zabolev_date_ustanov_modal')"
    PREV_THER_START_DATE = "$('#therapy_opurt_zabolev_date_start_modal')"
    PREV_THER_END_DATE = "$('#therapy_opurt_zabolev_date_end_modal')"
    PREV_THER_SAVE = "$('#modal_therapy_opurt_zabolev .ui.green.approve.button')"
    OPIOID_SUBSTITUTION_THERAPHY_ADD = "$('#opioid_therapy_table_add')"
    OST_START_DATE = "$('#opioid_therapy_date_start_ozt_modal')"
    OST_END_DATE = "$('#opioid_therapy_date_end_ozt_modal')"
    OST_MEDICATION_TYPE = "$('#modal_opioid_therapy div[data-field=opioid_therapy_which_preparat_modal] .ui.dropdown')"
    REASONS_OF_FINISHING = "$('#modal_opioid_therapy div[data-field=opioid_therapy_reason_stop_modal] .ui.dropdown')"
    OST_SAVE = "$('#modal_opioid_therapy .ui.green.approve.button')"
    VGS_TREATMENT_ADD = "$('#hcv_therapy_table_add')"
    VGS_TREAT_START_DATE = "$('#hcv_therapy_date_start_modal')"
    VGS_TREAT_END_DATE = "$('#hcv_therapy_date_end_modal')"
    VGS_TREAT_RESULT = "$('#modal_hcv_therapy div[data-field=hcv_therapy_table_ishod_modal] .ui.dropdown')"
    VGS_TREAT_SAVE = "$('#modal_hcv_therapy .ui.green.approve.button')"

    D_EXAM_HOSPITALIZATION = "$('div[data-block=main-menu] a[data-tab=patient_card_menu-d_osmotr]')"
    D_EXAM_ADD = "$('div[data-name=account-settings] div.menu').children()[0]')"
    ATTENDANCE_DATE = "$('#visit_table_date_visit')"
    D_EXAM_HELD = "$('div[data-field=visit_table_who_conducted] .ui.dropdown')"
    D_SERVICES = "$('div[data-field=visit_table_which_services] .ui.dropdown')"
    D_EXAM_PLACE = "$('div[data-field=visit_table_place_of_inspection] .ui.dropdown')"
    ATTENDANCE_TYPE = "$('div[data-field=visit_table_visit_type] .ui.dropdown')"
    TEMPERATURE = "$('#row_for_total_info_table div[data-field=ljv_card_table_temp]')"
    WEIGHT = "$('#row_for_total_info_table div[data-field=ljv_card_table_weight]')"
    HEIGHT = "$('#row_for_total_info_table div[data-field=ljv_card_table_growth]')"
    COMPLAINTS = "$('#complaints')"
    HISTORY_INFORMATION = "$('#anamnez_data')"
    LAST_MENSIS = "$('input[name=last_mensis]')"
    CONTRACEPTION = "$('input[name=kontracepc]')"
    D_EXAM_SEX_PARTNER = "$('input[name=partner_ljv]')"
    ART_RECEIPT = "$('input[name=partner_art]')"
    PLANNED_PREGNANCY_YES = "$('input[name=pregnancy][value=10]')"
    PLANNED_PREGNANCY_NO = "$('input[name=pregnancy][value=20]')"
    D_EXAM_ALCOHOL = "$('input[name=alco_or_drugs]')"
    D_EXAM_DRUGS = "$('input[name=alco_or_drugs]')"
    D_EXAM_INJ_DRUG_LAST_HALF_YEAR = "$('div[data-field=inek_nark_six_month] .ui.dropdown')"
    D_EXAM_COM_SEX_LAST_HALF_YEAR = "$('div[data-field=komerc_sex_six_month] .ui.dropdown')"
    D_EXAM_HOMO_SEX_LAST_HALF_YEAR = "$('div[data-field=gomo_sex_six_month] .ui.dropdown')"
    STATE = "$('div[data-field=sostoyanie] .ui.dropdown')"
    CONSCIOUSNESS = "$('div[data-field=soznanie] .ui.dropdown')"
    POSITION = "$('div[data-field=polojenie] .ui.dropdown')"
    BODY_TYPE = "$('div[data-field=teloslojenie] .ui.dropdown')"
    FEEDING = "$('div[data-field=pitanie] .ui.dropdown')"
    LIPODYSTROPHY = "$('div[data-field=lipodistrofiya] .ui.dropdown')"
    SKIN_MUCOSA = "$('div[data-field=kojnie_pokrovy_slizistaya] .ui.dropdown')"
    NAILS = "$('div[data-field=nails] .ui.dropdown')"
    RASH = "$('div[data-field=rash] .ui.dropdown')"
    PERIFEPHERAL_LYMPH_NODES = "$('div[data-field=peripheral_lymphnodes] .ui.dropdown')"
    OSTEO_ARTICULAR_SYSTEM = "$('div[data-field=osteo_articular_system] .ui.dropdown')"
    BREATH_SOUNDS = "$('div[data-field=breath] .ui.dropdown')"
    WHEEZING_YES = "$('input[name=wheezing][value=10]')"
    WHEEZING_NO = "$('input[name=wheezing][value=20]')"
    WHEEZING_TYPE = "$('div[data-field=which_wheezing] .ui.dropdown')"
    RESPIRATORY_RATE = "$('#chdd_min_input')"
    HEART_SOUNDS = "$('div[data-field=heart_sounds] .ui.dropdown')"
    HEART_RATE = "$('#chss_min_input')"
    BLOOD_PREASURE = "$('#davlenie')"
    NOISE = "$('div[data-field=noise] .ui.dropdown')"
    TONGUE = "$('div[data-field=tongue] .ui.dropdown')"
    ORAL_MUCOSA = "$('#oral_mucosa')"
    STOMACH = "$('div[data-field=stomach] .ui.dropdown')"
    LIVER = "$('div[data-field=liver] .ui.dropdown')"
    SPLEEN = "$('div[data-field=spleen] .ui.dropdown')"
    SYMPTOMS_OF_BANGING = "$('div[data-field=symptom_tapping] .ui.dropdown')"
    STOOL = "$('div[data-field=stool] .ui.dropdown')"
    STOOL_MULTIPLICITY = "$('#count_stool')"
    URINATION_FREE = "$('div[data-field=urination_freedom]')"
    URINATION_PAINLESS = "$('div[data-field=urination_not_pain]')"
    URINATION_PAINFUL = "$('div[data-field=urination_painless]')"
    DIURESIS_FREQUENT = "$('input[name=diurez][value=speeded_up]')"
    DIURESIS_BREACHED = "$('input[name=diurez][value=broken]')"
    DIURESIS_NORM = "$('input[name=diurez][value=norm]')"
    SWELLING = "$('#edemas')"
    D_EXAM_DIAGNOSIS = "$('#diagnozis')"
    D_EXAM_NOTES = "$('#description')"
    PLANNED_D_EXAM = "$('input[value name=date_plan_d_osmotr]')"
    D_EXAM_SAVE = "$('#save_data')"









    TARIFIKATOR = "$('a[data-name=tarifikator] .item.patient_card')"
    PRINT = "$('a[data-name=direction] .item.patient_card')"
    SMS_EMAIL = "$('a[data-name=sms_email] .item.patient_card')"
    # PHONE_NUMBER =
    # EMAIL =
    SMS_D_SEARCH = "$('#form_sms div[data-field=sms_d_search] .ui.checkbox')"
    EMAIL_D_SEARCH = "$('#form_sms div[data-field=email_d_search] .ui.checkbox')"
    SMS_ART = "$('#form_sms div[data-field=sms_art] .ui.checkbox')"
    EMAIL_ART = "$('#form_sms div[data-field=email_art] .ui.checkbox')"
    SMS_FLG = "$('#form_sms div[data-field=sms_flg] .ui.checkbox')"
    EMAIL_FLG = "$('#form_sms div[data-field=email_flg] .ui.checkbox')"
    SMS_CD4 = "$('#form_sms div[data-field=sms_cd4] .ui.checkbox')"
    EMAIL_CD4 = "$('#form_sms div[data-field=email_cd4] .ui.checkbox')"
    SMS_VN = "$('#form_sms div[data-field=sms_vn] .ui.checkbox')"
    EMAIL_VN = "$('#form_sms div[data-field=email_vn] .ui.checkbox')"
    SMS_EMAIL_SAVE = "$('#button_save .ui.green.button')"


class WorkJournalLocators(object):
    EDIT_CARD = "$('#gridContainer div[data-name=action_buttons] .list.icon').children()[0]"
    LIST_BUTTON = "$('#gridContainer div[data-name=action_buttons] .list.icon')"
    HOME_ICON = "$('.header.item .home.icon')"
    WORK_JOURNAL_MENU = "$('div[data-name=main-menu] .ui.pointing.labeled.dropdown.link.item')"
    BOOK_ICON_MENU = "$('i[class=book icon] .right.menu')"
    ARV_LOG_MENU = "$('.ui.fixed.inverted.menu.main .ui.pointing.dropdown.link.item.active.visible')"
    SETTINGS_ICON_MENU = "$('i[class=settings icon] .right.menu')"
    DATE_RANGE_START = (By.CSS_SELECTOR, '#dateRangeStart .ui.icon.input')
    DATE_RANGE_END = (By.CSS_SELECTOR, '#dateRangeEnd')
    DATA_TYPE = "$('.ui.two.wide.column.field .ui.selection.dropdown')"
    DATE_RANGE_BTN = (By.ID, "dateRangeButton")
    EXPORT_REPORT = (By.ID, "exportToExcel")
    NOTE_CODE = "$('.dx-show-invalid-badge.dx-numberbox.dx-texteditor.dx-editor-outlined.dx-widget')"
    FILTER_BTN = "$('div[title=Применить фильтр] .dx-apply-button')"
    EDIT_BTN = "$('div[data-name=action_buttons] .pointing.dropdown.button')"
    # EPI_DATE_RANGE_START =
    # EPI_DATE_RANGE_END =
    EPI_DETECTED_IN_CUR_REG = "$('#identified_in_current_region .ui.checkbox')"
    EPI_D_ACCOUNTED_IN_CUR_REG = "$('#on_disp_in_current_region .ui.checkbox')"
    EPI_GENERATE = "$('#bt_export_epi_info .ui.positive')"

class VizitsPageLocators(object):
    VISITS_LINK = (By.CSS_SELECTOR, 'a[href="/visits"]')
    DATE_RANGE_START = (By.ID, "dateRangeStart")
    DATE_RANGE_END = (By.ID, "dateRangeEnd")
    DATE_RANGE_BTN = (By.ID, "dateRangeButton")
    EXPORT_REPORT = (By.ID, "exportToExcel")


class AnalysisPageLocators(object):
    DETECTED_CASES_LOG = "$('a[href=/identified_case] .item')"
    FILTER_SEGMENT = "$('div[class=title]')"
    # DETECTED_CASES_DATE_START =
    # DETECTED_CASES_DATE_END =
    # DETECTED_CASES_FILTER =
    # DETECTED_CASES_LOG_APPLY_BTN =
    DETECTED_CASES_LOG_EXPORT = "$('#exportToExcel')"
    D_ACCOUNTING_LOG = "$('a[href=/dispanser_uchet] .item')"
    # D_ACCOUNTING_LOG_DATE_START =
    # D_ACCOUNTING_LOG_DATE_END =
    # D_ACCOUNTING_LOG_GENERATE_BTN =
    D_ACCOUNTING_LOG_EXPORT = "$('#exportToExcel')"
    ART_LOG = "$('a[href=/art_journal] .item')"
    # ART_LOG_DATE_START =
    # ART_LOG_DATE_END =
    # ART_LOG_FILTER =
    # ART_LOG_GENERATE_BTN =
    ART_LOG_EXPORT = "$('#exportToExcel')"
    DEAD_LOG = "$('a[href=/dead_journal] .item')"
    # DEAD_LOG_DATE_START =
    # DEAD_LOG_DATE_END =
    # DEAD_LOG_FILTER =
    # DEAD_LOG_GENERATE_BTN =
    DEAD_LOG_EXPORT = "$('#exportToExcel')"
    CHILD_D_ACCOUNTING_LOG = "$('a[href=/children_uchet] .item')"
    # CHILD_D_ACCOUNTING_LOG_DATE_START =
    # CHILD_D_ACCOUNTING_LOG_DATE_END =
    # CHILD_D_ACCOUNTING_LOG_FILTER =
    # CHILD_D_ACCOUNTING_LOG_GENERATE_BTN =
    CHILD_D_ACCOUNTING_LOG_EXPORT = "$('#exportToExcel')"
    PREGNANCY_LOG = "$('a[href=/pregnancy_journal] .item')"
    # PREGNANCY_LOG_DATE_START =
    # PREGNANCY_LOG_DATE_END =
    # PREGNANCY_LOG_FILTER =
    # PREGNANCY_LOG_GENERATE_BTN =
    PREGNANCY_LOG_EXPORT = "$('#exportToExcel')"
    HIV_LOG = "$('a[href=/hiv_tb] .item')"
    # HIV_LOG_DATE_START =
    # HIV_LOG_DATE_END =
    # HIV_LOG_FILTER =
    # HIV_LOG_GENERATE_BTN =
    HIV_LOG_EXPORT = "$('#exportToExcel')"
    DROPOUT_LOG = "$('a[href=/dropout_journal] .item')"
    # DROPOUT_LOG_DATE_START =
    # DROPOUT_LOG_DATE_END =
    # DROPOUT_LOG_FILTER =
    # DROPOUT_LOG_GENERATE_BTN =
    DROPOUT_LOG_EXPORT = "$('#exportToExcel')"


class ArvLogLocators(object):
    CONTRACT_LOG = "$('a[href=/contract/index] .item')"
    # CONTRACT_LOG_DATE_START =
    # CONTRACT_LOG_DATE_END =
    # CONTRACT_LOG_APPLY_BTN =
    CONTRACT_LOG_EXPORT = "$('#exportToExcel')"
    DEBIT_LOG = "$('a[href=/debit/index] .item')"
    # DEBIT_LOG_DATE_START =
    # DEBIT_LOG_DATE_END =
    # DEBIT_LOG_FILTER =
    # DEBIT_LOG_APPLY_BTN =
    # DEBIT_LOG_ADD_BTN =
    DEBIT_LOG_EXPORT = "$('#exportToExcel')"
    ARRIVAL_LOG = "$('a[href=/coming/index] .item')"
    # ARRIVAL_LOG_DATE_START =
    # ARRIVAL_LOG_DATE_END =
    # ARRIVAL_LOG_FILTER1 =
    # ARRIVAL_LOG_FILTER2 =
    # ARRIVAL_LOG_APPLY_BTN =
    # ARRIVAL_LOG_ADD_BTN =
    ARRIVAL_LOG_EXPORT = "$('#exportToExcel')"
    EXPENSE_LOG = "$('a[href=/consumption/index] .item')"
    # EXPENSE_LOG_DATE_START =
    # EXPENSE_LOG_DATE_END =
    # EXPENSE_LOG_FILTER =
    # EXPENSE_LOG_APPLY_BTN =
    # EXPENSE_LOG_ADD_BTN =
    EXPENSE_LOG_EXPORT = "$('#exportToExcel')"


class BookPageLocators(object):
    POPULATION = "$('a[href=/population] .item.item-patient-index')"
    POPULATION_ADD_BTN = "$('button[class=ui green button add]')"
    POPULATION_YEAR = "$('div[data-field=population_5_m] .field')"
    MAN_LESS_5 = "$('div[data-field=population_5_m] .field')"
    MAN_5_14 = "$('div[data-field=population_5_14_m] .field')"
    MAN_0_14 = "$('div[data-field=population_0_14_m] .field')"
    MAN_15_49 = "$('div[data-field=population_15_49_m] .field')"
    MAN_50_MORE = "$('div[data-field=population_50_more_m] .field')"
    WOMAN_LESS_5 = "$('div[data-field=population_5_w] .field')"
    WOMAN_5_14 = "$('div[data-field=population_5_14_w] .field')"
    WOMAN_0_14 = "$('div[data-field=population_0_14_w] .field')"
    WOMAN_15_49 = "$('div[data-field=population_15_49_w] .field')"
    WOMAN_50_MORE = "$('div[data-field=population_50_more_w] .field')"
    # POPULATION_YES_BTN =

    TARIFFICATION = "$('a[href=/tarifikator_journal/index] .item.item-patient-index')"
    # TARIFFICATION_DATE_START =
    # TARIFFICATION_DATE_END =
    # TARIFFICATION_FILTER =
    TARIFFICATION_APPLY_BTN = "$('#dateRangeButton .ui.blue.button')"
    TARIFFICATION_EXPORT = "$('#exportToExcel .ui.floated.button')"

    FORM4 = "$('a[href=/fourth_form] .item.item-patient-index')"
    MONTHLY_BTN = "$('#month_tab .ui.button')"
    CUMULATIVE_BTN = "$('#cummulative_tab .ui.button')"
    FORM4_PARAM_FILTER = "$('div[data-field=param_dd] .field')"
    # FORM4_YEAR_CALENDAR = "$('div[class=calendar] .field')"
    # FORM4_MONTH_CALENDAR = "$('td[class=link] .field')"
    FORM4_MONTH_FILTER = "$('div[data-field=monthes_dd] .field')"
    FORM4_CALCULATE = "$('#calculate .ui.green.button')"
    FORM4_EXPORT = "$('#print_excell .ui.blue.button')"

    REPORTS_LOG = "$('a[href=/report_journal] .item.item-patient-index')"
    # REPORTS_LOG_DATE_START =
    # REPORTS_LOG_DATE_END =
    REPORTS_LOG_APPLY_BTN = "$('#dateRangeButton .ui.blue.button')"
    # REPORTS_LOG_EXPORT =



class SettingsPageLocators(object):
    ORGANIZATION = "$('a[href=/reference/spr_aids_center_index] .item')"
    ADD_CENTER = "$('a[href=/reference/spr_aids_center_index/spr_aids_center_add] .ui.green.button')"
    DROPPED_CENTER_NAME_RU = "$('div[data-field=shot_name] .field')"
    FULL_CENTER_NAME_RU = "$('div[data-field=aids_center_name] .field.required')"
    DROPPED_CENTER_NAME_KZ = "$('div[data-field=shot_name_lng] .field')"
    FULL_CENTER_NAME_KZ = "$('div[data-field=aids_center_name_lng] .field')"
    CENTER_AREA = "$('div[data-field=obl] .field')"
    CENTER_CITY = "$('div[data-field=city] .field')"
    CENTER_STREET = "$('div[data-field=street] .field')"
    CENTER_HOUSE = "$('div[data-field=hous] .field')"
    CENTER_APT = "$('div[data-field=flat] .field')"
    LEVEL = "$('div[data-field=prioritet] .field')"
    OKPO = "$('div[data-field=okpo] .field')"
    DIRECTOR_NAME = "$('div[data-field=director_name] .field')"
    MAIN_ORG = "$('div[data-field=parent_org] .field')"
    REPUB_SIGNIFICANCE = "$('div[data-field=rc] .ui.checkbox')"
    CSM = "$('div[data-field=csm] .ui.checkbox')"
    SMS_EMAIL = "$('div[data-field=sms_email_enabled] .ui.checkbox')"
    REPRESENT_ORG = "$('div[data-field=ui_filial] .field')"
    CENTER_ACCESS1 = "$('div[role=checkbox] .dx-show-invalid-badge.dx-checkbox.dx-widget.dx-state-hover')"
    CENTER_SAVE = "$('div[data-field=shot_name_lng] .field')"

    USERS = "$('a[href=/user] .item')"
    ADD_USER = "$('a[href=/user/add] .ui.green.button')"
    ROLE = "$('div[data-field=role] .field')"
    USER_SURNAME = "$('div[data-field=last_name] .field')"
    USER_NAME = "$('div[data-field=first_name] .field')"
    USER_MIDDLE_NAME = "$('div[data-field=middle_name] .field')"
    USER_IIN = "$('div[data-field=iin] .field')"
    DEVISION = "$('div[data-field=department] .field')"
    USER_OCCUPATION = "$('div[data-field=position] .field')"
    USER_PHONE = "$('div[data-field=phone] .field')"
    LABORATORY = "$('div[data-field=lab] .checkbox')"
    EPID_DEVISION = "$('div[data-field=epid] .checkbox')"
    DISP_DEVISION = "$('div[data-field=disp] .checkbox')"
    REVIEW = "$('div[data-field=is_readonly] .checkbox')"
    ARV_ACCOUNTING = "$('div[data-field=apteka] .checkbox')"
    LEGEND_REVISE = "$('div[data-field=is_legend] .checkbox')"
    USER_ORGANIZATION = "$('div[data-field=org_id] .field')"
    USER_ADD = "$('#submit .field')"

