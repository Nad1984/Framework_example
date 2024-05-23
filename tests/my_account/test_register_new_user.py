import time

import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.helpers.generic_helpers import generate_random_email, generate_random_password
from src.pages.MyAccountSignedIn import MyAccountSignedIn


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)

        # go to my account
        my_account_o.go_to_my_account()
        # fill in email
        rand_email = generate_random_email()
        my_account_o.input_register_email(rand_email)
        # fill in password
        rand_password = generate_random_password()
        my_account_o.input_register_password(rand_password)
        # click register
        my_account_o.click_register_btn()
        # verify user is registered
        my_account_i = MyAccountSignedIn(self.driver)
        my_account_i.verify_user_is_signed_in()



