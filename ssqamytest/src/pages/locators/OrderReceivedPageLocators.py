from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:
    ORDER_RECEIVED_TITLE = (By.CSS_SELECTOR, 'header h1.entry-title')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')