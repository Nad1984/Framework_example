import os
# from selenium_driver_updater import DriverUpdater
from pytest_html.extras import image
import pytest_html
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.fixture(scope="class")
def init_driver(request):

    global driver
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']
    # browser = os.environ.get('BROWSER', None)
    browser = 'headlesschrome'
    if not browser:
        browser = 'ch'
        # raise Exception("The environment variable 'BROWSER' must be set.")
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception("Provided browser is not one of the supported."
                        f"Supported are: {supported_browsers}.")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()
    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()
    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser in ('headlessfirefox'):
        firefox_options = FFOptions()
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--headless')
        driver = webdriver.Chrome(options=firefox_options)

    #     setting a class variable
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


### FOR ALLURE report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):

            is_frontend_test = True if 'init_driver' in item.fixturenames else False
            if is_frontend_test:
                # 'RESULTS_DIR=/Users/nadiiapatrusheva/PycharmProjects/DemoVENV/AQA_course/Framework/ssqamytest/results'

                results_dir = os.environ.get("RESULTS_DIR")
                if not results_dir:
                    raise Exception(f"Environment variable 'RESULTS_DIR' must be set.")
                # import pdb; pdb.set_trace()
                screenshot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)




### FOR PYTEST-HTML report
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         # extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#
#             is_frontend_test = True if 'init_driver' in item.fixturenames else False
#             if is_frontend_test:
#                 # 'RESULTS_DIR=/Users/nadiiapatrusheva/PycharmProjects/DemoVENV/AQA_course/Framework/ssqamytest/results'
#
#                 results_dir = os.environ.get("RESULTS_DIR")
#                 if not results_dir:
#                     raise Exception(f"Environment variable 'RESULTS_DIR' must be set.")
#                 # import pdb; pdb.set_trace()
#                 screenshot_path = os.path.join(results_dir, item.name + '.png')
#                 driver_fixture = item.funcargs['request']
#                 driver_fixture.cls.driver.save_screenshot(screenshot_path)
#
#                 # only add additional html on failure
#                 # extras.append(pytest_html.extras.html("<div style='background:orange;'>Additional HTML</div>"))
#                 extras.append(pytest_html.extras.image(screenshot_path))
#         report.extras = extras
