import os

import pytest

from uiautomationTests.conftest import get_application_url
from uiautomationTests.pageObjects.login_page import LoginPage
from uiautomationTests.utility.base_test import BaseClass
from selenium import webdriver



class TestScenario1(BaseClass):
    """
      This class is inherited from BaseClass and kept inside tests package.
      The same rule is applied to all test cases under tests sub-package.
      Todo: Write our test methods falls under TestScenario1
    """

    @pytest.mark.usefixtures("launch_browser_and_application")
    def test_01(self):
        print("Executing test case inside first scenario....")
        self.login_page = LoginPage(self.browser)
        user_name, password = self.get_linked_in_credentials()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_user_name_login_text().send_keys(user_name)
        self.login_page.get_password_login_text().send_keys(password)
        self.login_page.get_login_button().click()

    def test_02(self):
        print("Executing second test case inside first scenario....")
