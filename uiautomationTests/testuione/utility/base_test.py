"""This module contains BaseClass that invokes setup fixture before any test run
   on class, module, function, package and session level.
   All Test Case classes under current project is inherited from this BaseClass.
"""

import pytest

from uiautomationtests.configure_framework.browser_actions import launch_application
from uiautomationtests.configure_framework.framework_config_utils import get_value_of
from uiautomationtests.testuione.testdata.testdata_utils import get_data


@pytest.mark.usefixtures("setup")
class BaseClass:
    """
      This is BaseClass or helpers class is kept inside utility sub package.
      Re-usable setup/tear-down method is invoked here as the commonly used
      fixture from 'conftest.py' and supplies the fixture access across all the test classes.
      All Test Cases resides under the main package or
      test suite called uiautomationtests should be inherited
      from this class.
      Todo: Write some reusable methods.
    """

    @pytest.fixture(autouse=False)
    def launch_browser_and_application(self, setup):
        """Launching browser and launches application base url."""

        print("\ninside launch_browser_and_application\n")
        self.browser = setup
        launch_application(self.browser, get_value_of('applicationURL', 'LinkedIn'))

    @staticmethod
    def get_linked_in_credentials():
        """Returns linkedIn credentials."""

        return get_data('credentials', 'LinkedIn', 'username'), \
            get_data('credentials', 'LinkedIn', 'password')
