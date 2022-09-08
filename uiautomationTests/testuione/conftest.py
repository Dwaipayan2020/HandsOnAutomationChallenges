import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from uiautomationtests.configure_framework.browser_actions import close_current_window
from uiautomationtests.configure_framework.browser_actions import exit_current_session
from uiautomationtests.configure_framework.browser_actions import take_screenshot
from uiautomationtests.configure_framework.framework_config_utils import get_driver_path
from uiautomationtests.testuione.configure_project.project_utils import create_new_markers
from uiautomationtests.testuione.configure_project.project_utils import update_addopts

DRIVER = None
REPORTER = None


def pytest_addoption(parser):
    """Directly creates command line arguments with default values and stores them inside request.config """
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
    parser.addoption(
        "--reporter", action="store", default="html"
    )


@pytest.fixture(scope="session")
def setup(request):
    """For browser set up which runs iteratively based on given scope
    param request: For using command line arguments request fixture is invoked here as argument
    :return: returns None but yields the driver or browser to supply across the all the classes
    """
    global DRIVER
    global REPORTER

    REPORTER = request.config.getoption("reporter")
    # set_execution_flags(REPORTER)
    print("inside set up")
    browser_name = request.config.getoption("browser")

    """Selecting driver or browser based on the default browser name"""
    if browser_name == "chrome":
        DRIVER = webdriver.Chrome(ChromeDriverManager().install())
    if browser_name == "edge":
        DRIVER = webdriver.Edge(executable_path=get_driver_path("edgeDriver"))
        """Not recommended to use the following line when the scope is at "session" level
          
          # request.cls.browser = DRIVER
          
          Only use when the scope is at "class" level
        """

    yield DRIVER
    print("\nsession level execution is completed.\n")
    close_current_window(DRIVER)
    exit_current_session(DRIVER)


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call" or report.when == "setup":
#         # always add url to report
#         file_name = os.path.join('C://Users/Dwaipayan_Das/PycharmProjects/HandsOnAutomationChallenges'
#                                  '/uiautomationtests/testuione/reports/', report.nodeid.replace("::", "_") + ".png")
#         # destination_file = os.path.join(report_directory, file_name)
#         capture_screenshot(file_name)
#         if file_name:
#             html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
#         extra.append(pytest_html.extras.html(html))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#             pass
#         report.extra = extra


def pytest_html_report_title(report):
    """Generates custom report title inside the generated html reports."""
    report.title = "UI Automation Tests Report"


def capture_screenshot(destination_file):
    """Captures screenshot and stores them inside the given file path"""
    take_screenshot(DRIVER, destination_file)


def set_execution_flags(reporter_name):
    """Creates two important keys inside pytest.ini file which triggers the execution as requested.
    Firstly it creates a markers key, value to store all default/custom markers used across the test cases.
    Secondly it creates addopts key, value to set commonly used important command line flags
    """
    create_new_markers()
    update_addopts(True, reporter_name)
