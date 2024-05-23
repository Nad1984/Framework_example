from time import sleep

import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):

        print("*******")
        print("TEST LOGIN NON EXISTING USER")
        print("*******")
        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username('blabla-car123')
        # type password
        my_account.input_login_password('Pas327483479hsdjfh')
        # click login
        my_account.click_login_btn()
        # sleep(5)
        # verify error message
        exp_error_message = 'Error: The username blabla-car123 is not registered on this site. If you are unsure of your username, try your email address instead.'
        exp2 = 'Unknown email address. Check again or try your username.'

        my_account.wait_until_error_is_displayed(exp2)
