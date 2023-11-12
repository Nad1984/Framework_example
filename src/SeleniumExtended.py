import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_if_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements by '{locator}', " \
                              f"after timeout of {timeout}"
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(err)

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = element.text
        return element_text

    # def find_stale_element(self, locator, timeout=None):
    #     timeout = timeout if timeout else self.default_timeout
    #     ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    #     element = WebDriverWait(self.driver, timeout, ignored_exceptions=ignored_exceptions) \
    #         .until(EC.presence_of_element_located(locator))
    #     return element
    #
    # def click_on_stale_element(self, locator):
    #     self.find_stale_element(locator).click()
