import pytest

from uiautomationTests.configureFramework.browserActions import launch_application
from uiautomationTests.configureFramework.frameworkConfigUtils import get_value_of
from uiautomationTests.TestUIOne.testdata.testdataUtils import get_data


@pytest.mark.usefixtures("setup")
class BaseClass():
    """
      This is BaseClass or helpers class is kept inside utility sub package.
      Re-usuable setup/tear-down method is invoked here as the commonly used
      fixture from conftest.py and supplies the fixture access across all the test classes.
      All Test Cases resides under the main package or test suite called uiautomationTests should be inherited
      from this class.
      Todo: Write some reusable methods.
    """

    @pytest.fixture(autouse=False)
    def launch_browser_and_application(self, setup):
        print("\ninside launch_browser_and_application\n")
        self.browser = setup
        launch_application(self.browser, get_value_of('LinkedIn', 'applicationURL'))

    @staticmethod
    def get_linked_in_credentials():
        return get_data("LinkedIn", "username"), get_data("LinkedIn", "password")
