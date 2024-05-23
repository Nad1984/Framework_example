from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    COUPON_CODE_FIELD = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    CART_PAGE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.woocommerce-message')
    LOCAL_PICUP_RADIO = (By.ID, 'shipping_method_0_local_pickup3')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')