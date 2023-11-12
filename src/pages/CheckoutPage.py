from ssqamytest.src.SeleniumExtended import SeleniumExtended
from ssqamytest.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from ssqamytest.src.helpers.generic_helpers import generate_random_email


class CheckoutPage(CheckoutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_checkout_page(self):
        pass

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'TestFirstName'
        return self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'TestLastName'
        return self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address(self, address1=None):
        address1 = address1 if address1 else '123 Main-test st.'
        return self.sl.wait_and_input_text(self.BILLING_ADDRESS_FIELD, address1)

    def input_billing_city(self, city=None):
        city = 'Sacramento' if not city else city
        return self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def input_billing_zip(self, zip_num=None):
        zip_num = '90210' if not zip_num else zip_num
        return self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zip_num)

    def input_phone_number(self, ph_num=None):
        ph_num = '0123456789' if not ph_num else ph_num
        return self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, ph_num)

    def input_email(self):
        rand_email = generate_random_email()
        rand_email = rand_email if not rand_email else rand_email
        return self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, rand_email)

    def fill_in_billing_information(self, f_name=None, l_name=None, street1=None, city=None, zip_num=None, ph_num=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip(zip_num=zip_num)
        self.input_phone_number(ph_num=ph_num)
        self.input_email()
        return self

    def click_on_place_order_button(self):
        return self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)