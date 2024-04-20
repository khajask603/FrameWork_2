import os
from datetime import datetime

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver=None                                                     #Declare Globally

def pytest_addoption(parser):
    # parser.addoption("--browser", action="store")
    parser.addoption("--headless", action="store")
    parser.addoption("--browser", action="store",default="chrome")     #Ign   oring as i kept chrome as default browser

@pytest.fixture(scope="class")
def setup(request):
    browser=request.config.getoption("--browser")
    headless = request.config.getoption("--headless")  # Check if headless option is passed from Jenkins

    global driver                                                #Declare Globally
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("------------Launching Firefox Browser----------------")

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
            options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        print("------------Launching Edge Browser----------------")
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        print("------------Launching Chrome Browser----------------")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver  # Assign the driver to the class attribute
    yield driver
    driver.quit()

@pytest.hookimpl()
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "RS AngularPractise"
    config.stash[metadata_key]["Module Name"] = "Ecomerce Website"
    config.stash[metadata_key]["Tester Name"] = "Sk Khaja Mohiddin"
    # Set the HTML report path
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

#To Take screenshot if failed
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)




#---------------------Pavan Sir Notes ----------for Comparsion
# # --------To invoke browser from comand line for browser
# # 1)This will get the value from CLI
# def pytest_addoption(parser):
#     parser.addoption("--browser")
# # 2)--------These Below fixture will take it from from top-----------
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")

#-------------Single Browser--------


# @pytest.fixture(scope="class")
# def setup(request):
#     global driver                                                #Declare Globally
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=ops)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     request.cls.driver = driver  # Assign the driver to the class attribute
#     yield driver
#     driver.quit()