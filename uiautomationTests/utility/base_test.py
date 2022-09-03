import os
from configparser import ConfigParser

import pytest

from uiautomationTests.conftest import curr_dir, get_application_url, setup


def get_credentials(section_name):
    config = ConfigParser()
    config.read(curr_dir + './credentials.ini')
    credentials = config[section_name]
    return credentials


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
        self.browser.get(get_application_url())
        self.browser.maximize_window()
        self.browser.refresh()


    @staticmethod
    def get_linked_in_credentials():
        return get_credentials("LinkedIn")["username"], get_credentials("LinkedIn")["password"]
