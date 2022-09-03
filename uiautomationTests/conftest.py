import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser

driver = None
curr_dir = os.path.dirname(os.path.realpath(__file__))
driver_path = curr_dir + "./driver"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="session")
def setup(request):
    global driver
    print("inside set up")
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser_name == "edge":
        driver = webdriver.Edge(executable_path=driver_path + "./msedgedriver.exe")
        """
          Not recommended to use the following line when the scope is at "session" level,
          
          # request.cls.browser = driver
          
          Only use when the scope is at "class" level
        """
        # request.cls.browser = driver

    yield driver
    print("\nsession level execution is completed.\n")
    driver.close()
    driver.quit()


def get_application_url():
    config = ConfigParser()
    config.read(curr_dir + './config.ini')
    application_url = config['AUT']['url']
    return application_url


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        report_directory = os.path.dirname(item.config.option.htmlpath)
        file_name = report.nodeid.replace("::", "_") + ".png"
        destination_file = os.path.join(report_directory, file_name)
        # destination_file = os.path.join(report_directory, file_name)
        _take_screenshot(destination_file)
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
        extra.append(pytest_html.extras.html(html))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            pass
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "UI Automation Tests Report"


def _take_screenshot(destinationFile):
    driver.save_screenshot(destinationFile)
