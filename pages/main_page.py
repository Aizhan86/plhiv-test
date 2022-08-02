from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from .locators import PatientCardLocators, WorkJournalLocators, ArvRegisterLocators, AnalysisPageLocators
from time import sleep
from random import randrange
import datetime
from datetime import datetime, timedelta
import string
import random
from .values import *


class ArvRegisters(BasePage):
    party_id_for_adult = None
    party_id_for_child = None
    party_id_for_art_adult = None

    def fill_receipt_register_form(self, programm, waybill):
        self.make(f"{AnalysisPageLocators.REGISTERS_MENU}.click()")
        self.make(f"window.location = {ArvRegisterLocators.RECEIPT_REGISTER}.attr('href')")
        self.make(f"{ArvRegisterLocators.ORG_FILTER}.dropdown('set selected', '29')")
        self.make(f"window.location = {ArvRegisterLocators.RECEIPT_ADD}.attr('href')")
        sleep(2)
        self.make(f"{ArvRegisterLocators.RECEIPT_TYPE}.dropdown('set selected', '0');")
        self.make(f"{ArvRegisterLocators.BUDGET_TYPE}.dropdown('set selected', '{budget_choice}');")
        self.make(f"{ArvRegisterLocators.SUPPLIER}.dropdown('set selected', '{three_choice}');")
        self.make(f"{ArvRegisterLocators.WAYBILL_NUM}.val('{waybill}');")
        self.make(f"{ArvRegisterLocators.INVOICE_NUM}.val('{numbers5}');")
        self.make(f"{ArvRegisterLocators.RECEIPT_DATE}.val('{today}');")
        self.make(f"{ArvRegisterLocators.PROGRAMM}.dropdown('set selected', '{programm}');")
        self.make(f"{ArvRegisterLocators.RECIPIENT_NAME}.val('{surname}');")
        self.make(f"{ArvRegisterLocators.PROCUREMENT_TYPE}.dropdown('set selected', '{three_choice}');")
        self.make(f"{ArvRegisterLocators.CONTRACT_NUM_DATE}.val('№{numbers4} от {today}');")
        self.make(f"{ArvRegisterLocators.MEDICATION_ADD}.click()")
        sleep(2)

    def choose_medicine(self, medicine):
        self.make(f"$('#{medicine} > td:nth-child(1) > a').click()")

    def fill_receipt_register_table(self):
        # self.make(f"{ArvRegisterLocators.MEDICATION_SEARCH}.val('3TC');")
        self.make(f"{ArvRegisterLocators.MEDICATION_EXP_DATE}.val('{expiration_date}');")
        self.make(f"{ArvRegisterLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvRegisterLocators.MEDICATION_PRICE}.val('1500');")
        self.make(f"{ArvRegisterLocators.MEDICATION_SERIUS_NUM}.val('{numbers4}');")
        self.make(f"{ArvRegisterLocators.MEDICATION_SUM}.val('1500');")

    def check_save_button_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_REGISTER_SAVE}.length"), "Save button in Receipt register is not accessible"
        self.make(f"{ArvRegisterLocators.RECEIPT_REGISTER_SAVE}.click()")

    def check_add_button_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_ADD}.length"), "Add button in Receipt register is not accessible"

    def swift_on_editing_page_receipt_register(self, waybill):
        sleep(1)
        # Выбираем строку
        grid = self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.number === '{waybill}')[0].id_drug_waybill_receive")
        # Проводим накладную, чтобы лекарства сели в остатках
        self.make(f"window.location.href = `/coming/index/accept/{grid}/0`")
        # Переходим на страницу Редактирование в Журнале прихода
        self.make(f"window.location.href = `/coming/index/edit/{grid}/0?readonly=true`")
        sleep(2)
        assert self.browser.execute_script(f"return $('div.section.active').text()") == 'Редактирование', "Swifting on Edit page in Receipt register wasn't provided"

    def add_medication_for_art_adult_on_balance_register(self):
        self.swift_on_editing_page_receipt_register(numbers5)
        # Извлекаем код партии
        ArvRegisters.party_id_for_art_adult = self.browser.execute_script(f"return $('#add-preparat-for-prihod tr:eq(0) td:eq(1)').attr('data-field')")

    def add_medication_for_adult_on_balance_register(self):
        self.swift_on_editing_page_receipt_register(numbers4)
        # Извлекаем код партии
        ArvRegisters.party_id_for_adult = self.browser.execute_script(f"return $('#add-preparat-for-prihod tr:eq(0) td:eq(1)').attr('data-field')")

    def add_medication_for_child_on_balance_register(self):
        self.swift_on_editing_page_receipt_register(numbers3)
        # Извлекаем код партии
        ArvRegisters.party_id_for_child = self.browser.execute_script(f"return $('#add-preparat-for-prihod tr:eq(0) td:eq(1)').attr('data-field')")

    def check_receipt_type_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_TYPE}.length"), "The Receipt type object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_TYPE}.dropdown('get value')") == '0', "The Receipt type object in Receipt register doesn't take a value"

    def check_budget_type_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.BUDGET_TYPE}.length"), "The Receipt type object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.BUDGET_TYPE}.dropdown('get value')") == budget_choice, "The Receipt type object in Receipt register doesn't take a value"

    def check_supplier_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.SUPPLIER}.length"), "The Supplier object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.SUPPLIER}.dropdown('get value')") == three_choice, "The Supplier object in Receipt register doesn't take a value"

    def check_waybill_number_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_NUM}.length"), "The Consignment number object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_NUM}.val()") == numbers4, "The Consignment number object in Receipt register doesn't take a value"

    def check_invoice_number_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.INVOICE_NUM}.length"), "The Consignment number object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.INVOICE_NUM}.val()") == numbers5, "The Consignment number object in Receipt register doesn't take a value"

    def check_receipt_date_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_DATE}.length"), "The Receipt date object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_DATE}.val()") == today.strftime('%Y-%m-%d'), "The Receipt date object in Receipt register doesn't take a value"

    def check_programm_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROGRAMM}.length"), "The Programm object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROGRAMM}.dropdown('get value')") == '4', "The Programm object in Receipt register doesn't take a value"

    def check_recipient_name_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECIPIENT_NAME}.length"), "The Recipient name object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECIPIENT_NAME}.val()") == surname, "The Recipient name object in Receipt register doesn't take a value"

    def check_procurement_type_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROCUREMENT_TYPE}.length"), "The Procurement type object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROCUREMENT_TYPE}.dropdown('get value')") == three_choice, "The Procurement type object in Receipt register doesn't take a value"

    def check_contract_number_date_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.CONTRACT_NUM_DATE}.length"), "The Contract number date object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.CONTRACT_NUM_DATE}.val()") == f'№{numbers4} от {today}', "The Contract number date object in Receipt register doesn't take a value"

    def check_expiration_date_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_EXP_DATE}.length"), "The Expiration date object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_EXP_DATE}.val()") == expiration_date, "The Expiration date object in Receipt register doesn't take a value"

    def check_amount_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_AMOUNT}.length"), "The Amount object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_AMOUNT}.val()") == '1.0', "The Amount object in Receipt register doesn't take a value"

    def check_price_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_PRICE}.length"), "The Price object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_PRICE}.val()") == '1500.0', "The Price object in Receipt register doesn't take a value"

    def check_series_number_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SERIUS_NUM}.length"), "The Series number object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SERIUS_NUM}.val()") == numbers4, "The Series number object in Receipt register doesn't take a value"

    def check_sum_receipt_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SUM}.length"), "The Sum object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SUM}.val()") == '1500.0', "The Sum object in Receipt register doesn't take a value"

    def check_cancel_button_receipt_register(self):
        # assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_LOG_CANCEL}.length"), "Cancel button in Receipt register is not accessible"
        assert self.make(f"{ArvRegisterLocators.RECEIPT_REGISTER_CANCEL}.click();"), "Cancel button in Receipt register is not accessible"

    def fill_receipt_register_for_perinatal_modal(self):
        self.fill_receipt_register_form('2', numbers3)
        self.choose_medicine('29')
        self.fill_receipt_register_table()
        self.check_save_button_receipt_register()

    def fill_receipt_register_for_art_modal(self):
        self.fill_receipt_register_form('1', numbers5)
        self.choose_medicine('1')
        self.fill_receipt_register_table()
        self.check_save_button_receipt_register()

    def fill_receipt_register_for_pregnancy_modal(self):
        self.fill_receipt_register_form('4', numbers4)
        self.choose_medicine('1')
        self.fill_receipt_register_table()

    def fill_receipt_register_for_child_in_pregnancy_modal(self):
        self.fill_receipt_register_form('3', numbers3)
        self.choose_medicine('29')
        self.fill_receipt_register_table()
        self.check_save_button_receipt_register()

    def fill_write_off_register_form(self, programm, party_id, waybill):
        self.make(f"{AnalysisPageLocators.REGISTERS_MENU}.click()")
        self.make(f"window.location = {ArvRegisterLocators.WRITE_OFF_REGISTER}.attr('href')")
        self.make(f"{ArvRegisterLocators.ORG_FILTER}.dropdown('set selected', '29')")
        self.make(f"window.location = {ArvRegisterLocators.WRITE_OFF_ADD}.attr('href')")
        sleep(2)
        self.make(f"{ArvRegisterLocators.EXPENSE_TYPE}.dropdown('set selected', '4');")
        self.make(f"{ArvRegisterLocators.WAYBILL_NUM}.val('{waybill}');")
        self.make(f"{ArvRegisterLocators.WAYBILL_DATE}.val('{today}');")
        self.make(f"{ArvRegisterLocators.SENDER_NAME}.val('{surname}');")
        self.make(f"{ArvRegisterLocators.BUDGET_TYPE}.dropdown('set selected', '{four_choice}');")
        self.make(f"{ArvRegisterLocators.PROGRAMM}.dropdown('set selected', '{programm}');")
        self.make(f"{ArvRegisterLocators.RECIPIENT_ORG}.dropdown('set selected', '29');")
        self.make(f"{ArvRegisterLocators.WO_RECIPIENT_NAME}.val('{surname}');")
        self.make(f"{ArvRegisterLocators.WRITE_OFF_REASON}.dropdown('set selected', '{four_choice}');")
        self.make(f"{ArvRegisterLocators.MEDICATION_ADD}.click()")
        sleep(2)
        self.make(f"$('#{party_id}').click()")
        self.make(f"{ArvRegisterLocators.MEDICATION_AMOUNT}.val('1');")
        self.make(f"{ArvRegisterLocators.MEDICATION_SUM}.val('1500');")

    def fill_write_off_register_for_perinatal_modal(self):
        self.fill_write_off_register_form('2', ArvRegisters.party_id_for_child, numbers3)

    def fill_write_off_register_for_child_in_pregnancy_modal(self):
        self.fill_write_off_register_form('3', ArvRegisters.party_id_for_child, numbers3)

    def fill_write_off_register_for_art_modal(self):
        self.fill_write_off_register_form('1', ArvRegisters.party_id_for_art_adult, numbers5)

    def fill_write_off_register_for_pregnancy_modal(self):
        self.fill_write_off_register_form('4', ArvRegisters.party_id_for_adult, numbers4)

    def check_save_button_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WRITE_OFF_SAVE}.length"), "Save button in Receipt register is not accessible"
        self.make(f"{ArvRegisterLocators.WRITE_OFF_SAVE}.click()")

    def check_add_button_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WRITE_OFF_ADD}.length"), "Add button in Receipt register is not accessible"

    def check_expense_type_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.EXPENSE_TYPE}.length"), "The Consignment number object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.EXPENSE_TYPE}.val()") == '4', "The Consignment number object in Receipt register doesn't take a value"

    def swift_on_editing_page_write_off_register(self, waybill):
        sleep(1)
        # Выбираем нужную строку в таблице
        wo_grid = self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.number === '{waybill}')[0].id_drug_waybill_send")
        # Проводим накладную, чтобы лекарства сели в остатках
        self.make(f"window.location.href = `/debit/index/accept/{wo_grid}/1`")
        # Переходим на страницу Редактирование в Журнале прихода
        self.make(f"window.location.href = `/debit/index/edit/{wo_grid}?readonly=true`")
        sleep(2)
        assert self.browser.execute_script(f"return $('div.section.active').text()") == 'Редактирование', "Swifting on Edit page in Receipt register wasn't provided"

    def swift_on_editing_page_for_child_write_off_register(self):
        self.swift_on_editing_page_write_off_register(numbers3)

    def swift_on_editing_page_for_adult_write_off_register(self):
        self.swift_on_editing_page_write_off_register(numbers4)

    def swift_on_editing_page_for_art_adult_write_off_register(self):
        self.swift_on_editing_page_write_off_register(numbers5)

    def check_waybill_number_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_NUM}.length"), "The Consignment number object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_NUM}.val()") == numbers4, "The Consignment number object in Receipt register doesn't take a value"

    def check_waybill_date_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_DATE}.length"), "The Consignment date object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WAYBILL_DATE}.val()") == today, "The Consignment date object in Receipt register doesn't take a value"

    def check_sender_name_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.SENDER_NAME}.length"), "The Sender name object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.SENDER_NAME}.val()") == surname, "The Sender name object in Receipt register doesn't take a value"

    def check_budget_type_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.BUDGET_TYPE}.length"), "The Receipt type object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.BUDGET_TYPE}.dropdown('get value')") == four_choice, "The Receipt type object in Receipt register doesn't take a value"

    def check_programm_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROGRAMM}.length"), "The Programm object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.PROGRAMM}.dropdown('get value')") == '4', "The Programm object in Receipt register doesn't take a value"

    def check_recipient_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECIPIENT_ORG}.length"), "The Supplier object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.RECIPIENT_ORG}.dropdown('get value')") == '29', "The Supplier object in Receipt register doesn't take a value"

    def check_recipient_name_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WO_RECIPIENT_NAME}.length"), "The Recipient name object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WO_RECIPIENT_NAME}.val()") == surname, "The Recipient name object in Receipt register doesn't take a value"

    def check_write_off_reason_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WRITE_OFF_REASON}.length"), "The Procurement type object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.WRITE_OFF_REASON}.dropdown('get value')") == four_choice, "The Procurement type object in Receipt register doesn't take a value"

    def check_amount_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_AMOUNT}.length"), "The Amount object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_AMOUNT}.val()") == '1.0', "The Amount object in Receipt register doesn't take a value"

    def check_sum_write_off_register(self):
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SUM}.length"), "The Sum object in Receipt register is not accessible"
        assert self.browser.execute_script(f"return {ArvRegisterLocators.MEDICATION_SUM}.val()") == '1500.0', "The Sum object in Receipt register doesn't take a value"

    def check_cancel_button_write_off_register(self):
        # assert self.browser.execute_script(f"return {ArvRegisterLocators.RECEIPT_LOG_CANCEL}.length"), "Cancel button in Receipt register is not accessible"
        assert self.make(f"{ArvRegisterLocators.WRITE_OFF_CANCEL}.click();"), "Cancel button in Receipt register is not accessible"

    def receipt_medicine(self, waybill):
        self.make(f"{AnalysisPageLocators.REGISTERS_MENU}.click()")
        self.make(f"window.location = {ArvRegisterLocators.RECEIPT_REGISTER}.attr('href')")
        sleep(2)
        # Выбираем нужную строку в таблице
        rec_grid = self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.number === '{waybill}')[0].id_drug_waybill_receive")
        # Проводим накладную, чтобы лекарства сели в остатках
        self.make(f"window.location.href = `/coming/index/accept/{rec_grid}/8`")
        # Переходим на страницу Редактирование в Журнале прихода
        self.make(f"window.location.href = `/coming/index/edit/{rec_grid}/8?readonly=true`")
        sleep(2)
        assert self.browser.execute_script(f"return $('div.section.active').text()") == 'Редактирование', "Swifting on Edit page in Receipt register wasn't provided"

    def receipt_medicine_for_art_adult(self):
        self.receipt_medicine(numbers5)

    def receipt_medicine_for_adult(self):
        self.receipt_medicine(numbers4)

    def receipt_medicine_for_child(self):
        self.receipt_medicine(numbers3)

    def check_medicine_in_balance_register(self):
        self.make(f"{AnalysisPageLocators.REGISTERS_MENU}.click()")
        self.make(f"window.location = {ArvRegisterLocators.BALANCE_REGISTER}.attr('href')")
        sleep(2)
        # Проерка имеется ли строка с необходимым лекарством в остатках
        for i in (ArvRegisters.party_id_for_child, ArvRegisters.party_id_for_adult):
            if i:
                assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.id_drug_party === {i}).length"), "Medicine in Balance register is absent"

            # assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.id_drug_party === {ArvRegisters.party_id_for_child}).length"), "Medicine for child in Balance register is absent"
            # assert self.browser.execute_script(f"return $('#gridContainer').dxDataGrid('instance').getDataSource().items().filter((e) => e.id_drug_party === {ArvRegisters.party_id_for_adult}).length"), "Medicine for adult in Balance register is absent"

    def fill_perinatal_registration_tab(self):
        self.make(f"{PatientCardLocators.ARV_PROPHYLAXIS}.dropdown('set selected', '{arv_proph_choice}');")
        self.make(f"{PatientCardLocators.ARV_START_DATE}.val('{eighty_days_ago}');")
        # self.make(f"{PatientCardLocators.ARV_END_DATE}.calendar('set date', '{fifty_days_ago}');")
        self.make(f"{PatientCardLocators.ARV_MEDICATION}.dropdown('set selected', '20');")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME}.click();")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_NAME_CHOICE}.click();")
        sleep(3)
        self.make(f"$('#{ArvRegisters.party_id_for_child} .blue.button').click();")
        sleep(1)
        self.make(f"{PatientCardLocators.ARV_RECIPE_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.ARV_DAY_NUM}.val('30');")
        self.make(f"{PatientCardLocators.ARV_MEDICINE_PER_DAY}.val('1');")
        self.make(f"{PatientCardLocators.ARV_NEXT_DATE}.val('{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.ARV_MEDICATION_SAVE}.click();")
        sleep(1)
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_SAVE}.click();")
        sleep(1)
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.val('{fifty_days_ago}');")
        self.make(f"{PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.val('{thirty_days_ago}');")
        self.make(f"{PatientCardLocators.HIV_STATUS_P_TAB}.dropdown('set selected', '{arv_hiv_choice}');")
        self.make(f"{PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.val('{fifty_days_ago}');")

    def check_arv_prophylaxis_perinatal_registration_tab(self):
        sleep(1)
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_PROPHYLAXIS}.length"), "The ARV Prophylaxis object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_PROPHYLAXIS}.dropdown('get value')") == arv_proph_choice, "The ARV Prophylaxis object in Perinatal registration tab doesn't take a value"

    def check_arv_start_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_START_DATE}.length"), "The ARV start date object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_START_DATE}.val()") == eighty_days_ago, "The ARV start date object in Perinatal registration tab doesn't take a value"

    def check_arv_medication_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION}.length"), "The Medication object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_MEDICATION}.dropdown('get value')") == '20', "The Medication object in Perinatal registration tab doesn't take a value"

    def check_medication_issuanse_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_ISSUANCE}.length"), "The Issuanse object in Perinatal registration tab is not accessible"
        self.make(f"{PatientCardLocators.ARV_ISSUANCE}.click();")

    def check_medication_name_in_medication_issuanse_registration_tab(self):
        assert self.browser.execute_script(f"return $('#add-row-preparat-art-table tr:eq(0) td:eq()').attr('data-field')") == 'Ретровир', "Medication in Medication issuanse modal in Perinatal registration tab wasn't preserved"

    def check_cancel_button_in_medication_issuanse_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ARV_ISSUANCE_CANCEL}.length"), "Cancel button in Medication issuanse modal in Perinatal registration tab is not accessible"
        self.make(f"{PatientCardLocators.ARV_ISSUANCE_CANCEL}.click();")
        sleep(3)

    def check_pcp_prophylaxis_start_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.length"), "The PCP Prophylaxis start date object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_START_DATE}.val()") == fifty_days_ago, "The PCP Prophylaxis start date object in Perinatal registration tab doesn't take a value"

    def check_pcp_prophylaxis_end_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.length"), "The PCP Prophylaxis end date object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PCP_PROPHYLAXIS_END_DATE}.val()") == thirty_days_ago, "The PCP Prophylaxis end date in Perinatal registration tab doesn't take a value"

    def check_hiv_status_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STATUS_P_TAB}.length"), "The HIV Status object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_STATUS_P_TAB}.dropdown('get value')") == arv_hiv_choice, "The HIV Status object in Perinatal registration tab doesn't take a value"

    def check_hiv_determination_date_perinatal_registration_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.length"), "The HIV Determination date object in Perinatal registration tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.HIV_DETERMINATION_DATE_P_TAB}.val()") == fifty_days_ago, "The HIV Determination date object in Perinatal registration tab doesn't take a value"


    def fill_pregnancy_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.CHILDREN_PREGNANCY}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_ADD}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY}.dropdown('set selected', '{pregnancy_choice}');")
        self.make(f"{PatientCardLocators.PREG_SEX_PARTNER}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.PREG_PARTNER_HIV_STATUS}.dropdown('set selected', '{hiv_status_choice}');")
        self.make(f"{PatientCardLocators.OGC_REGIS_DATE}.val('{regis_date}');")
        self.make(f"{PatientCardLocators.OGC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.ANTENATAL_CLINIC_REGIS_DATE}.val('{regis_date}');")
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.PREGNANCY_EDIT}.click();")
        self.make(f"{PatientCardLocators.AC_PREGNANCY_WEEKS}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT}.dropdown('set selected', '{preg_res_choice}');")
        self.make(f"{PatientCardLocators.PREGNANCY_RESULT_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPHILAXYS}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_START_DATE}.val('{twenty_days_ago}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_START}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_PROPH_END_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.PREGNANCY_WEEKS_ARV_END}.dropdown('set selected', '{preg_weeks_choice}');")
        self.make(f"{PatientCardLocators.PREG_ARV_MEDICATIONS}.dropdown('set selected', '20');") #28
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE}.click();")
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_TABLE_ADD}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME}.click();")
        # self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_NAME_CHOICE}.click();")
        sleep(3)
        self.make(f"$('#{ArvRegisters.party_id_for_adult} .blue.button').click();")
        sleep(2)
        self.make(f"{PatientCardLocators.PREG_ARV_RECIPE_NUM}.val('{numbers4}');")
        # self.make(f"{PatientCardLocators.ARV_DAY_NUM}.val('30');")
        # self.make(f"{PatientCardLocators.ARV_MEDICINE_PER_DAY}.val('1');")
        # self.make(f"{PatientCardLocators.ARV_NEXT_DATE}.val('{thirty_days_forward}');")
        self.make(f"{PatientCardLocators.PREG_ARV_MEDICATION_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")

    def check_add_button_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_ADD}.length"), "Add button in Pregnancy modal is not accessible"

    def check_edit_button_pregnancy_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_EDIT}.length"), "Edit button in Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREGNANCY_EDIT}.click();")

    def check_pregnancy_in_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY}.length"), "The Pregnancy object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY}.dropdown('get value')") == pregnancy_choice, "The Pregnancy object in Pregnancy modal doesn't take a value"

    def check_sex_partner_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_SEX_PARTNER}.length"), "The Sex partner object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_SEX_PARTNER}.dropdown('get value')") == three_choice, "The Sex partner object in Pregnancy doesn't take a value"

    def check_hiv_status_of_partner_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_PARTNER_HIV_STATUS}.length"), "The HIV Status of partner object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_PARTNER_HIV_STATUS}.dropdown('get value')") == hiv_status_choice, "The HIV Status of partner object in Pregnancy doesn't take a value"

    def check_ogc_registration_date_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OGC_REGIS_DATE}.length"), "The OGC Registration date object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OGC_REGIS_DATE}.val()") == regis_date, "The OGC Registration date object in Pregnancy modal doesn't take a value"

    def check_ogc_pregnancy_weeks_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.OGC_PREGNANCY_WEEKS}.length"), "The OGC Pregnancy weeks object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.OGC_PREGNANCY_WEEKS}.dropdown('get value')") == preg_weeks_choice, "The OGC Pregnancy weeks object in Pregnancy doesn't take a value"

    def check_antenatal_clinic_registration_date_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ANTENATAL_CLINIC_REGIS_DATE}.length"), "The Antenatal clinic registration date object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ANTENATAL_CLINIC_REGIS_DATE}.val()") == regis_date, "The Antenatal clinic registration date object in Pregnancy modal doesn't take a value"

    def check_wc_pregnancy_weeks_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.AC_PREGNANCY_WEEKS}.length"), "The AC Pregnancy weeks object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.AC_PREGNANCY_WEEKS}.dropdown('get value')") == preg_weeks_choice, "The AC Pregnancy weeks object in Pregnancy doesn't take a value"

    def check_pregnancy_result_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_RESULT}.length"), "The Pregnancy result object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_RESULT}.dropdown('get value')") == preg_res_choice, "The Pregnancy result object in Pregnancy doesn't take a value"

    def check_pregnancy_result_date_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_RESULT_DATE}.length"), "The Pregnancy result date object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_RESULT_DATE}.val()") == today, "The Pregnancy result date object in Pregnancy modal doesn't take a value"

    def check_arv_prophylaxys_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPHILAXYS}.length"), "The ARV Prophylaxys object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPHILAXYS}.dropdown('get value')") == '1', "The ARV Prophylaxys object in Pregnancy doesn't take a value"

    def check_arv_prophylaxys_start_date_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPH_START_DATE}.length"), "The ARV Prophylaxys start date object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPH_START_DATE}.val()") == twenty_days_ago, "The ARV Prophylaxys start date object in Pregnancy modal doesn't take a value"

    def check_pregnancy_weeks_arv_start_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_WEEKS_ARV_START}.length"), "The Pregnancy weeks ARV start object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_WEEKS_ARV_START}.dropdown('get value')") == preg_weeks_choice, "The Pregnancy weeks ARV start object in Pregnancy doesn't take a value"

    def check_arv_prophylaxys_end_date_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPH_END_DATE}.length"), "The ARV Prophylaxys end date object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_PROPH_END_DATE}.val()") == today, "The ARV Prophylaxys end date object in Pregnancy modal doesn't take a value"

    def check_pregnancy_weeks_arv_end_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_WEEKS_ARV_END}.length"), "The Pregnancy weeks ARV end object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_WEEKS_ARV_END}.dropdown('get value')") == preg_weeks_choice, "The Pregnancy weeks ARV end object in Pregnancy modal doesn't take a value"

    def check_arv_medication_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_MEDICATIONS}.length"), "The ARV Medication object in Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_MEDICATIONS}.dropdown('get value')") == '20', "The ARV Medication  object in Pregnancy modal doesn't take a value"

    def check_medication_issuance_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE}.length"), "The Medication Issuance object of Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE}.click();")

    def check_medication_name_medication_issuance_pregnancy_modal(self):
        assert self.browser.execute_script(f"return $('#add-row-preparat-art-table td:first').attr('data-field')") == 'Ретровир', "The Medication name object in Medication Issuance table of Pregnancy modal doesn't take a value"

    def check_add_button_medication_issuance_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_TABLE_ADD}.length"), "Add button in Medication Issuance table of Pregnancy modal is not accessible"

    def check_edit_button_medication_issuance_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_TABLE_EDIT}.length"), "Edit button in Medication Issuance table of Pregnancy modal is not accessible"

    def check_cancel_button_medication_issuance_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_CANCEL}.length"), "Edit button in Medication Issuance table of Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CANCEL}.click();")

    def check_cancel_button_pregnancy_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_CANCEL}.length"), "Cancel button in Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREGNANCY_CANCEL}.click();")

    def fill_children_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        # self.make(f"{PatientCardLocators.CHILDREN_PREGNANCY}.click();")
        self.make(f"{PatientCardLocators.PREGNANCY_EDIT}.click();")
        sleep(1)
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CHILD}.click();")
        sleep(1)
        self.make(f"{PatientCardLocators.CHILD_ARV_ISSUANCE_ADD}.click();")
        sleep(1)
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_NAME}.click();")
        sleep(2)
        self.make(f"$('#{ArvRegisters.party_id_for_child} .blue.button').click();")
        sleep(1)
        self.make(f"{PatientCardLocators.CHILD_ARV_RECIPE_NUM}.val('{numbers5}');")
        self.make(f"{PatientCardLocators.CHILD_ARV_MEDICATION_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.CHILD_ARV_ISSUANCE_SAVE}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_ADD}.click();")
        self.make(f"{PatientCardLocators.ALIVE_CHILD}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.CHILDS_SURNAME}.val('{surname}');")
        self.make(f"{PatientCardLocators.CHILDS_NAME}.val('{name}');")
        self.make(f"{PatientCardLocators.CHILDS_MIDNAME}.val('{midname}');")
        self.make(f"{PatientCardLocators.CHILDS_BIRTHDAY}.val('{today}');")
        self.make(f"{PatientCardLocators.CHILDS_GENDER}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.PATHALOGY_AT_BIRTH}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_FEEDING}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.FULL_TERM_CHILD}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.CHILDS_DEATH_DATE}.val('{today}');")
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_SAVE}.click();")

    def check_save_button_children_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREGNANCY_SAVE}.length"), "Save button in Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREGNANCY_SAVE}.click();")

    def check_medication_issuance_for_child_pregnancy_modal(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_CHILD}.length"), "The Medication issuance for future child object in Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CHILD}.click();")

    def check_medication_name_medication_issuance_for_future_child_modal(self):
        sleep(3)
        assert self.browser.execute_script(f"return $('#add-row-preparat-art-future-table td:first').attr('data-field')") == 'Ретровир', "The Medication name object in Medication Issuance for future child table in Pregnancy modal doesn't take a value"

    def check_cancel_button_medication_issuance_for_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_CHILD_CANCEL}.length"), "Cancel button in Medication issuance for future child table in Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CHILD_CANCEL}.click();")

    # def check_cancel_button_medication_issuance_for_child_pregnancy_modal(self):
    #     assert self.browser.execute_script(f"return {PatientCardLocators.PREG_ARV_ISSUANCE_CHILD_CANCEL}.length"), "Cancel button in Medication issuance for future child table in Pregnancy modal is not accessible"
    #     self.make(f"{PatientCardLocators.PREG_ARV_ISSUANCE_CHILD_CANCEL}.click();")

    def check_edit_button_child_pregnancy_modal(self):
        sleep(3)
        assert self.browser.execute_script(f"return {PatientCardLocators.INFORMATION_CHILDREN_EDIT}.length"), "Edit button in Information about children table of Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_EDIT}.click();")

    def check_alive_child_in_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ALIVE_CHILD}.length"), "The Alive child object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ALIVE_CHILD}.dropdown('get value')") == '1', "The Alive child object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_surname_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_SURNAME}.length"), "The Child's surname object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_SURNAME}.val()") == surname, "The Child's surname object in Information about children modal of Pregnancy doesn't take a value"

    def check_childs_name_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_NAME}.length"), "The Child's name object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_NAME}.val()") == name, "The Child's name object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_middle_name_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_MIDNAME}.length"), "The Child's middle name object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_MIDNAME}.val()") == midname, "The Child's middle name object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_birth_date_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_BIRTHDAY}.length"), "The Child's birth date object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_BIRTHDAY}.val()") == today, "The Child's birth date object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_gender_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_GENDER}.length"), "The Child's gender object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_GENDER}.dropdown('get value')") == two_choice, "The Child's gender object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_pathalogy_at_birth_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PATHALOGY_AT_BIRTH}.length"), "The Pathalogy at birth object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PATHALOGY_AT_BIRTH}.dropdown('get value')") == two_choice, "The Pathalogy at birth in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_feeding_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_FEEDING}.length"), "The Child's feeding object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_FEEDING}.dropdown('get value')") == three_choice, "The Child's feeding object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_full_term_child_in_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.FULL_TERM_CHILD}.length"), "The Full term child object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.FULL_TERM_CHILD}.dropdown('get value')") == two_choice, "The Full term child object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_childs_death_date_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_DEATH_DATE}.length"), "The Child's death date object in Information about children modal of Pregnancy modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CHILDS_DEATH_DATE}.val()") == today, "The Child's death date object in Information about children modal of Pregnancy modal doesn't take a value"

    def check_cancel_button_child_pregnancy_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.INFORMATION_CHILDREN_CANCEL}.length"), "Cancel button in Information about children modal of Pregnancy modal is not accessible"
        self.make(f"{PatientCardLocators.INFORMATION_CHILDREN_CANCEL}.click();")

    def fill_art_information_modal(self):
        self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        self.make(f"{PatientCardLocators.ART}.click();")
        sleep(2)
        self.make(f"{PatientCardLocators.ART_REASONS_DEFINE_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_READINESS_DEFINE_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.WRITTEN_CONSENT}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_START_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_ROW}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.ART_SCHEME}.dropdown('set selected', '28');")
        self.make(f"{PatientCardLocators.ART_MED_ORG}.dropdown('set selected', '{three_choice}');")
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")
        self.make(f"{PatientCardLocators.ART_INFORMATION_EDIT}.click();")
        self.make(f"{PatientCardLocators.ART_ISSUANCE_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_MEDICATION_NAME}.click();")
        sleep(2)
        # if PatientCardLocators.ART_MEDICATION_NAME_CHOICE:
        self.make(f"$('#{ArvRegisters.party_id_for_art_adult} .blue.button').click();")
        self.make(f"{PatientCardLocators.ART_RECIPE_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.ART_ISSUANCE_SAVE}.click();")
        # else:
        #     self.make(f"{PatientCardLocators.ART_MEDICATION_NAME_DENY}.click();")
        #     self.make(f"{PatientCardLocators.ART_ISSUANCE_DENY}.click();")
        #     print(f"Medicines are not available")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGED_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_TYPE}.dropdown('set selected', '1');")
        self.make(f"{PatientCardLocators.ART_SCHEME_CHANGE_REASON}.dropdown('set selected', '{art_change_choice}');")

    def check_save_button_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_INFORMATION_SAVE}.length"), "Save button in Art Information modal is not accessible"
        self.make(f"{PatientCardLocators.ART_INFORMATION_SAVE}.click();")

    def check_art_reasons_define_date_art_tab(self):
        sleep(2)
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_REASONS_DEFINE_DATE}.length"), "The Art reasons define date in Art tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_REASONS_DEFINE_DATE}.val()") == today, "The Art reasons define date object in Art tab doesn't take a value"

    def check_art_readiness_define_date_art_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_READINESS_DEFINE_DATE}.length"), "The Art readiness define date in Art tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_READINESS_DEFINE_DATE}.val()") == today, "The Art readiness define date object in Art tab doesn't take a value"

    def check_written_consent_art_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.WRITTEN_CONSENT}.length"), "The Written consent object in Art tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.WRITTEN_CONSENT}.dropdown('get value')") == '1', "The Written consent object in Art tab doesn't take a value"

    def check_add_button_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_INFORMATION_ADD}.length"), "Add button in Art Information modal is not accessible"

    def check_edit_button_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_INFORMATION_EDIT}.length"), "Edit button in Art Information modal is not accessible"
        self.make(f"{PatientCardLocators.ART_INFORMATION_EDIT}.click();")

    def check_art_start_date_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_START_DATE}.length"), "The Art start date in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_START_DATE}.val()") == today, "The Art start date object in Art Information modal doesn't take a value"

    def check_art_row_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ROW}.length"), "The Art row object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ROW}.dropdown('get value')") == three_choice, "The Art row object in Art Information modal doesn't take a value"

    def check_art_scheme_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME}.length"), "The Art scheme object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME}.dropdown('get value')") == '28', "The Art scheme object in Art Information modal doesn't take a value"

    def check_art_medical_organization_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_MED_ORG}.length"), "The Art held by object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_MED_ORG}.dropdown('get value')") == three_choice, "The Art held by object in Art Information modal doesn't take a value"

    def check_edit_button_art_issuance_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ISSUANCE_EDIT}.length"), "Edit button in Art Issuance modal is not accessible"

    def check_art_medication_name_art_issuance_modal(self):
        assert self.browser.execute_script(f"return $('#add-row-preparat-art-table td:first').attr('data-field')") == 'Ретровир', "The Art medication name object in Art Issuance table doesn't take a value"

    def check_art_scheme_change_date_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGED_DATE}.length"), "The Art scheme change date object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGED_DATE}.val()") == today, "The Art scheme change date object in Art Information modal doesn't take a value"

    def check_art_scheme_change_type_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGE_TYPE}.length"), "The Art scheme change type object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGE_TYPE}.dropdown('get value')") == '1', "The Art scheme change type object in Art Information modal doesn't take a value"

    def check_art_scheme_change_reason_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGE_REASON}.length"), "The Art scheme change reason object in Art Information modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_SCHEME_CHANGE_REASON}.dropdown('get value')") == art_change_choice, "The Art scheme change reason object in Art Information modal doesn't take a value"

    def check_cancel_button_art_information_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_INFORMATION_CANCEL}.length"), "Cancel button in Art Information modal is not accessible"
        self.make(f"{PatientCardLocators.ART_INFORMATION_CANCEL}.click();")

    def fill_art_adherence_level_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        # self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_ADHERENCE_SUPPORT}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_ADD}.click();")
        self.make(f"{PatientCardLocators.ART_ADHER_YEAR}.val('2021');")
        self.make(f"{PatientCardLocators.ART_ADHER_QUARTER}.dropdown('set selected', '{four_choice}');")
        self.make(f"{PatientCardLocators.ART_ADHERENCE}.dropdown('set selected', '{three_choice}');")
        if three_choice == "3":
            self.make(f"{PatientCardLocators.ART_ADHER_LOW_REASONS}.dropdown('set selected', '{adher_reas_choice}');")
        self.make(f"{PatientCardLocators.SIDE_EFFECTS}.dropdown('set selected', '{side_effect_choice}');")

    def check_art_adherence_support_art_tab(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHERENCE_SUPPORT}.length"), "The Quater object in Art tab is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHERENCE_SUPPORT}.dropdown('get value')") == two_choice, "The Quater object in Art tab doesn't take a value"

    def check_save_button_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LEVEL_SAVE}.length"), "Save button in Art Adherence modal is not accessible"
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_SAVE}.click();")

    def check_add_button_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LEVEL_ADD}.length"), "Add button in Art Adherence modal is not accessible"

    def check_edit_button_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LEVEL_EDIT}.length"), "Edit button in Art Adherence modal is not accessible"
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_EDIT}.click();")

    def check_year_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_YEAR}.length"), "The Year object in Art Adherence modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_YEAR}.val()") == '2021', "The Year object in Art Adherence modal doesn't take a value"

    def check_quater_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_QUARTER}.length"), "The Quater object in Art Adherence modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_QUARTER}.dropdown('get value')") == four_choice, "The Quater object in Art Adherence modal doesn't take a value"

    def check_art_adherence_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHERENCE}.length"), "The Art adherence object in Art Adherence modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHERENCE}.dropdown('get value')") == three_choice, "The Art adherence object in Art Adherence modal doesn't take a value"

    def check_art_adherence_low_reasons_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LOW_REASONS}.length"), "The Art adherence low reasons object in Art Adherence modal is not accessible"
        if three_choice == "3":
            assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LOW_REASONS}.dropdown('get value')") == adher_reas_choice, "The Art adherence low reasons object in Art Adherence modal doesn't take a value"

    def check_side_effects_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SIDE_EFFECTS}.length"), "The Side effects object in Art Adherence modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SIDE_EFFECTS}.dropdown('get value')") == side_effect_choice, "The Side effects object in Art Adherence modal doesn't take a value"

    def check_cancel_button_art_adherence_level_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_ADHER_LEVEL_CANCEL}.length"), "Cancel button in Art Adherence modal is not accessible"
        self.make(f"{PatientCardLocators.ART_ADHER_LEVEL_CANCEL}.click();")


    def fill_recipe_modal(self):
        # self.make(f"{PatientCardLocators.OPEN_PATIENT_MENU}.sidebar('show')")  # Развернули карту пациента
        # self.make(f"{PatientCardLocators.DISP_OBSERVATION}.click();")  # Выбрали Диспансерное наблюдение
        # self.make(f"{PatientCardLocators.ART}.click();")
        self.make(f"{PatientCardLocators.ART_RECIPE_ADD}.click();")
        self.make(f"{PatientCardLocators.RECIPE_NUM}.val('{numbers4}');")
        self.make(f"{PatientCardLocators.RECIPE_DATE}.val('{today}')")
        self.make(f"{PatientCardLocators.ART_MEDICATION}.dropdown('set selected', '{art_med_choice}');")
        self.make(f"{PatientCardLocators.DOSE}.val('1 таблетка');")
        self.make(f"{PatientCardLocators.DOSE_CODE}.dropdown('set selected', '{two_choice}');")
        self.make(f"{PatientCardLocators.CONCENTRATION}.val('1');")
        self.make(f"{PatientCardLocators.PACKING}.val('1');")
        self.make(f"{PatientCardLocators.QUANTITY}.val('30');")
        self.make(f"{PatientCardLocators.UNPACKING_SIGNS}.dropdown('set selected', '{unpacking_choice}');")
        self.make(f"{PatientCardLocators.SIGNATURE}.val('{smth_random}');")

    def check_save_button_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_RECIPE_SAVE}.length"), "Save button in Recipe modal is not accessible"
        self.make(f"{PatientCardLocators.ART_RECIPE_SAVE}.click();")

    def check_add_button_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_RECIPE_ADD}.length"), "Add button in Recipe modal is not accessible"

    def check_edit_button_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_RECIPE_EDIT}.length"), "Edit button in Recipe modal is not accessible"
        self.make(f"{PatientCardLocators.ART_RECIPE_EDIT}.click();")

    def check_recipe_number_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECIPE_NUM}.length"), "The Recipe number object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RECIPE_NUM}.val()") == numbers4, "The Recipe number object in Recipe modal doesn't take a value"

    def check_recipe_date_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.RECIPE_DATE}.length"), "The Recipe date object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.RECIPE_DATE}.val()") == today, "The Recipe date object in Recipe doesn't take a value"

    def check_art_medication_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_MEDICATION}.length"), "The ART Medication object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_MEDICATION}.dropdown('get value')") == art_med_choice, "The ART Medication object in Recipe doesn't take a value"

    def check_dose_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DOSE}.length"), "The Dose object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DOSE}.val()") == '1 таблетка', "The Dose object in Recipe doesn't take a value"

    def check_dose_code_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.DOSE_CODE}.length"), "The Dose code object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.DOSE_CODE}.dropdown('get value')") == two_choice, "The Dose code object in Recipe doesn't take a value"

    def check_concentration_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.CONCENTRATION}.length"), "The Concentration object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.CONCENTRATION}.val()") == '1', "The Concentration object in Recipe doesn't take a value"

    def check_packing_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.PACKING}.length"), "The Packing object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.PACKING}.val()") == '1', "The Packing object in Recipe modal doesn't take a value"

    def check_quatity_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.QUANTITY}.length"), "The Quatity object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.QUANTITY}.val()") == '30', "The Treatment end date object in Recipe modal doesn't take a value"

    def check_unpacking_signs_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.UNPACKING_SIGNS}.length"), "The Unpacking object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.UNPACKING_SIGNS}.dropdown('get value')") == unpacking_choice, "The Unpacking object in Recipe doesn't take a value"

    def check_signiture_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.SIGNATURE}.length"), "The Signiture object in Recipe modal is not accessible"
        assert self.browser.execute_script(f"return {PatientCardLocators.SIGNATURE}.val()") == smth_random, "The Signiture object in Recipe modal doesn't take a value"

    def check_cancel_button_recipe_modal(self):
        assert self.browser.execute_script(f"return {PatientCardLocators.ART_RECIPE_CANCEL}.length"), "Cancel button in Recipe modal is not accessible"
        self.make(f"{PatientCardLocators.ART_RECIPE_CANCEL}.click();")
