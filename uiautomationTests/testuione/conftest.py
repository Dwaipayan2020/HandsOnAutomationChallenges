import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from uiautomationTests.TestUIOne.configureProject.projectUtils import create_new_markers, update_addopts
from uiautomationTests.configureFramework.browserActions import close_current_window, exit_current_session, \
    take_screenshot
from uiautomationTests.configureFramework.frameworkConfigUtils import get_driver_path

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    set_execution_flags()
    global driver
    print("inside set up")
    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser_name == "edge":
        driver = webdriver.Edge(executable_path=get_driver_path("edgeDriver"))
        """
          Not recommended to use the following line when the scope is at "session" level,
          
          # request.cls.browser = driver
          
          Only use when the scope is at "class" level
        """
        request.cls.browser = driver

    yield driver
    print("\nsession level execution is completed.\n")
    close_current_window(driver)
    exit_current_session(driver)


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call" or report.when == "setup":
#         # always add url to report
#         file_name = os.path.join('C://Users/Dwaipayan_Das/PycharmProjects/HandsOnAutomationChallenges'
#                                  '/uiautomationTests/TestUIOne/reports/', report.nodeid.replace("::", "_") + ".png")
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
    report.title = "UI Automation Tests Report"


def capture_screenshot(destination_file):
    take_screenshot(driver, destination_file)


def set_execution_flags():
    create_new_markers()
    update_addopts(True)
