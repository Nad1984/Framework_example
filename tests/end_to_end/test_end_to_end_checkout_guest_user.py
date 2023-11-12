import time

import pytest
from ssqamytest.src.configs.generic_configs import GenericConfigs
from ssqamytest.src.pages.HomePage import HomePage
from ssqamytest.src.pages.Header import Header
from ssqamytest.src.pages.CartPage import CartPage
from ssqamytest.src.pages.CheckoutPage import CheckoutPage
from ssqamytest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqamytest.src.helpers.database_helpers import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckOutGuestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        order_received_page = OrderReceivedPage(self.driver)
        # go to homepage
        home_page.go_to_home_page()
        # add items to cart

        home_page.click_first_add_to_cart_button()

        # make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)
        # go to cart
        header.click_on_cart_on_right_header()
        product_names = cart_page.get_all_products_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 product in the cart, but got {len(product_names)}"
        # apply a coupon 'ssqa100'
        coupon_code = GenericConfigs.FREE_COUPON_NAD
        cart_page.apply_coupon(coupon_code)
        # select free shipping
        # StaleElementReferenceException if no sleep. Sleep in selenium extended.
        # cart_page.click_local_pickup_radio()
        # click on checkout
        cart_page.click_checkout_button()
        # fill in the form
        checkout_page.fill_in_billing_information()
        # click on place order
        checkout_page.click_on_place_order_button()

        # verify order is received
        text = 'Order received'
        order_received_page.verify_order_received_page_loaded(text)
        # time.sleep(3)
        # verify order is recorded in db (via SQL or via API)
        order_no = order_received_page.get_order_number()

        print('---------------')
        print(order_no)
        print('---------------')

        db_order = get_order_from_db_by_order_no(order_no)
        assert db_order, f"Order wasn't found in DB, order number is: {order_no}"   # if empty record

