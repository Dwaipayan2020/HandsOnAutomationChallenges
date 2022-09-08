"""Test_Scenario_01 is first test scenario module has test cases
   referring to Login Page actions
"""

import pytest

from uiautomationtests.testuione.page_objects.login_page import LoginPage
from uiautomationtests.testuione.utility.base_test import BaseClass


class TestScenario1(BaseClass):
    """
      This class is inherited from BaseClass and kept inside tests package.
      The same rule is applied to all test cases under tests sub-package.
      Todo: Write our test methods falls under TestScenario1
    """

    @pytest.mark.usefixtures("launch_browser_and_application")
    def test_01(self):
        """Test case performs login in LinkedIn
        """
        print("Executing test case inside first scenario....")
        self.login_page = LoginPage(self.browser)
        user_name, password = self.get_linked_in_credentials()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_user_name_login_text().send_keys(user_name)
        self.login_page.get_password_login_text().send_keys(password)
        self.login_page.get_login_button().click()

    def test_02(self):
        """This test case is dummy."""

        print("Executing second test case inside first scenario....")
