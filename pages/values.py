from random import randrange
from datetime import datetime, timedelta
import string
import random



def get_date(date_start, date_end):
    d1 = datetime.strptime(date_start, '%d.%m.%Y')
    d2 = datetime.strptime(date_end, '%d.%m.%Y')
    delta = d2 - d1
    int_delta = delta.days
    random_date = d1 + timedelta(randrange(int_delta))
    return random_date

gen_choice = random.choice(['female', 'male'])
two_choice = random.choice(['1', '2'])
mo_choice = random.choice(['290000000001', '290000000002', '290000000003', '290000000004', '290000000073'])
mo_choice1 = random.choice(['20000000025', '20000000011', '20000000012', '20000000070', '20000000135'])
mo_choice2 = random.choice(['290000000001', '290000000002', '290000000003', '290000000004', '290000000005'])
mo_choice3 = random.choice(['280000000228', '290000000074', '280000000230', '280000000315', '280000000350'])
mo_rec_choice = random.choice(['160000000037', '290000000022', '160000000701', '160000000266', '160000000287', '160000000425'])
mo_rec_choice1 = random.choice(['290000000073', '280000000241', '280000000314', '280000000350', '280000000429', '160000000157'])
locality_choice = random.choice(['170000000020', '170000000008', '170000000032', '170000000085', '170000000242', '170000000253'])
locality_choice1 = random.choice(['290000000002', '290000000004', '290000000017', '290000000051', '290000000033'])
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
child_status_choice = random.choice(['1', '2', '3', '4', '5'])
soc_status_choice = random.choice(['3', '4'])
p_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
p_name = ''.join(random.choices(string.ascii_uppercase, k=6))
p_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
child_period = get_date('01.01.2009', '01.12.2021')
p_birthday = child_period.strftime('%d.%m.%Y')
others = random.randrange(100000, 999999)
iin = f"{child_period.strftime('%y%m%d')}{others}"
homeless_period = get_date('01.01.1970', '01.12.2000')
h_birthday = child_period.strftime('%d.%m.%Y')
homeless_iin = f"{child_period.strftime('%y%m%d')}{others}"
h_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
h_name = ''.join(random.choices(string.ascii_uppercase, k=6))
h_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
foreigner_period = get_date('01.01.1970', '01.12.2003')
f_birthday = child_period.strftime('%d.%m.%Y')
foreigner_iin = f"{foreigner_period.strftime('%y%m%d')}{others}"
f_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
f_name = ''.join(random.choices(string.ascii_uppercase, k=6))
f_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
woman_period = get_date('01.01.1970', '01.12.2003')
w_birthday = child_period.strftime('%d.%m.%Y')
woman_iin = f"{woman_period.strftime('%y%m%d')}{others}"
w_surname = ''.join(random.choices(string.ascii_uppercase, k=9))
w_name = ''.join(random.choices(string.ascii_uppercase, k=6))
w_midname = ''.join(random.choices(string.ascii_uppercase, k=10))
disp_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А ', 'КЕНЖЕЕВА Г ', 'НАУШАБЕКОВА Ж '])
service_choice = random.choice(['304', '238'])
vl_service_choice = random.choice(['242', '263'])
remark_choice = random.choice(['Плановое обследование', 'Внелановое обследование'])
vl_res_choice = random.choice(['0', '1', '2'])
vl_res_ml_choice = random.randint(150, 500)
marker_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])
vac_multi_choice = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8'])
dose = random.choice(['5', '10', '15'])
vac_multi_choice = random.choice(['США', 'Казахстан', 'Россия', 'Китай', 'Южная Корея', 'Индия', 'Япония', 'Германия', 'Турция'])
fluor_choice = random.choice(['1', '2', '3', '4', '5'])
radio_choice = random.choice(['1', '2', '3', '4', '5'])
sputum_choice = random.choice(['1', '2', '4'])
tb_symph_choice = random.choice(['1', '2'])
xpert_choice = random.choice(['1', '2', '3', '4', '5'])
mrt_choice = random.choice(['1', '2', '3', '4', '5'])
case_choice = random.choice(['9', '1', '2', '3', '4', '5', '6', '7', '8'])
tb_analysis_choice = random.choice(['35', '1', '2', '3', '4', '5', '6', '7', '47'])
bac_secr_choice = random.choice(['1', '2', '4'])
outcome_choice = random.choice(['1', '2', '4', '5', '6', '7', '8'])
treat_res_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
treat_outc_choice = random.choice(['1', '2', '3', '4', '5'])
ifa_res_choice = random.choice(['1', '2'])
ifa_resp_person_choice = random.choice(['290000000001', '290000000004', '290000000014', '290000000018'])
ifa_services_choice = random.choice(['233'])
test_cat_choice = random.choice(['1', '2', '0'])
gp160 = random.choice(['1', '2', '3'])
gp110_120 = random.choice(['1', '2', '3'])
p68 = random.choice(['1', '2', '3'])
p55 = random.choice(['1', '2', '3'])
p52 = random.choice(['1', '2', '3'])
gp41 = random.choice(['1', '2', '3'])
p40 = random.choice(['1', '2', '3'])
p34 = random.choice(['1', '2', '3'])
p25 = random.choice(['1', '2', '3'])
p18 = random.choice(['1', '2', '3'])
disease_name_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '33', '27'])
consultation_choice = random.choice(['548', '5', '25', '12', '17', '310', '312'])
survey_choice = random.choice(['279', '266', '290'])
referral_name_choice1 = random.choice(['57', '62', '138', '144', '133'])
drug_cons_choice = random.choice(['1', '2'])
service_choice = random.choice(['304', '238'])
reason_deregis_choice = random.choice(['1', '2', '3', '4', '5'])
death_choice = random.choice(['1', '2', '13', '4', '17', '18', '12'])
death_place_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
arv_proph_choice = random.choice(['1', '2'])
medication_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '201', '216'])
arv_hiv_choice = random.choice(['1', '2', '3'])
homo_sex_partners_choice = random.choice(['20', '30', '24', '25', '36', '27', '18', '39', '17'])
sex_partners_year_choice = random.choice(['10', '11', '12', '14', '13', '15', '16', '9', '17'])
reason_perinatal_deregis_choice = random.choice(['1', '2', '3', '4', '5'])
reason_d_deregis_choice = random.choice(['0', '1', '2', '3', '4', '8', '9', '10'])
death_choice = random.choice(['1', '2', '13', '4', '17', '18', '12'])
death_place_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
epid_doc_choice = random.choice(['ХАЙДАРОВА Д. И.', 'МАСИЯЕВА А.', 'НАУШАБЕКОВА Ж.', 'ДАРМЕНОВА Р. М.'])
fam_mem_rel_choice = random.choice(['10', '9', '11'])
com_sex_partners_choice = random.choice(['10', '20', '30', '14', '25', '36', '27', '18', '39', '17'])
deduction_choice = random.choice(['114', '115', '20', '30', '25', '36', '27', '39', '54'])
blood_don_cat_choice = random.choice(['1', '2', '3'])
organ_don_cat_choice = random.choice(['1', '2', '3'])
three_choice = random.choice(['1', '2', '3'])
manip_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '10', '9', '11'])
trauma_choice = random.choice(['1', '2', '3', '4', '5'])
purpose_choice = random.choice(['1', '2', '3', '4', '5', '6'])
result_choice = random.choice(['7', '9', '12', '14', '19'])
treat_res_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
art_med_choice = random.choice(['111'])
exam_choice = random.choice(['infection', 'pediatr', 'ftiziatr', 'ginekolog', 'terapevt', 'dermatolog', 'psiholog', 'social_worker', 'narkolog'])
service_choice = random.choice(['2', '3', '348', '328', '33', '25', '322', '331', '14'])
attendance_choice = random.choice(['perv_osmotr', 'd_osmotr', 'po_zabolev', 'current_reception'])
place_choice = random.choice(['home', 'mls', 'stacionar', 'center_hiv', 'ambulatorno'])
choices_for_visits_modal = random.choice(['10', '20'])
state_choice = random.choice(['satisfactory', 'moderate_severity', 'severe_severity', 'extremely_heavy'])
conscious_choice = random.choice(['clear', 'stupor', 'sopor', 'coma'])
position_choice = random.choice(['active', 'passive', 'forced'])
contraception_choice = random.choice(['condoms', 'spiral', 'hirurg_sterialize', 'drug', 'kok', 'another'])
body_choice = random.choice(['normostenic', 'astenik', 'hypersthenic'])
feeding_choice1 = random.choice(['moderate', 'low', 'high', 'cachexia'])
skin_choice = random.choice(['regular_coloring', 'pale_pink', 'icteric', 'another'])
nails_choice = random.choice(['not_changed', 'changed'])
rash_choice = random.choice(['punctate', 'papular', 'vesicular', 'urtikarnaya'])
lymph_choice = random.choice(['not_palpable', 'not_enlarged', 'palpable', 'enlarged', 'painful', 'not_painful',
                                     'single', 'multiple', 'not_soldered'])
osteo_choice = random.choice(['no_pathological_changes', 'with_pathological_changes'])
breath_choice = random.choice(['vesicular', 'tough', 'weakened', 'another'])
yes_no_choice = random.choice(['Yes', 'No'])
wheezing_choice = random.choice(['dry', 'wet', 'whistling', 'crepitus'])
heart_choice = random.choice(['clear', 'muffled', 'rhythmic', 'arrhythmic'])
noise_choice = random.choice(['not_heard', 'heard'])
tongue_choice = random.choice(['dry', 'wet', 'clean_of_plaque', 'white_coated', 'patches_on_side_surfaces',
                                      'cheesy_patina', 'another'])
stomach_choice = random.choice(['painless_on_palpation', 'tense', 'painful_on_palpation', 'another'])
liver_choice = random.choice(['not_increased', 'on_the_edge_of_the_costal_arch',
                                     'protrudes_from_under_the_edge_of_the_costal_arch', 'consistency_dense', 'soft',
                                     'elastic', 'another'])
spleen_choice = random.choice(['not_palpable', 'increased_from_under_the_edge', 'deleted', 'another'])
sym_choice = random.choice(['negative', 'positive', 'two_side', 'left', 'right'])
stool_choice = random.choice(['decorated', 'liquid', 'without_pathological_impurities', 'blood', 'slime',
                                     'ordinary_paint', 'green', 'acholic', 'another'])
diuresis_choice = random.choice(['breached', 'frequent', 'norm'])

con_reason_not_surv_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
contact_type_choice = random.choice(['1', '2', '3', '4', '5', '6', '7'])
cont_person_exist_choice = random.choice(['1', '0'])
budget_choice = random.choice(['1', '2', '3', '4', '5'])
four_choice = random.choice(['1', '2', '3', '4'])
adher_reas_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
side_effect_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
art_change_choice = random.choice(['1', '5', '6', '7', '8', '18', '20'])
unpacking_choice = random.choice(['0', '1'])
pregnancy_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
preg_weeks_choice = random.choice(['1', '12', '2', '3', '4', '5', '6', '7', '8', '9', '10', '31', '42'])
preg_res_choice = random.choice(['1', '12', '2', '3', '11', '13'])
category_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])