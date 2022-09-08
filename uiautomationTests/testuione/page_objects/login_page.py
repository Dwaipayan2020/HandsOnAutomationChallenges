"""This module contains LoginPage class, has reference to web elements
   and their operations of Login page
"""

from uiautomationtests.testuione.page_objects.locators import Locators


class LoginPage(Locators):
    """LoginPage is a PageObject class that uses driver as constructor argument.
        This class is inherited from Locators class.Most of the getter methods are written
        to specially invoke concurrent web elements of Login Page. All types of sub activities
        (page methods) under Login Page category should be defined only here.
        Programmer needs to create Login Page object to invoke Login page methods
        into test case classes.
    """

    def __init__(self, driver):
        self.__driver = driver

    def get_sign_in_button(self):
        """Returns sign in button element in launched page to navigate to Login Page"""

        return self.__driver.find_element_by_xpath(self.sign_in_login_page_button)

    def get_user_name_login_text(self):
        """Returns username text box element of Login Page"""

        return self.__driver.find_element_by_xpath(self.user_name_login_page_text)

    def get_password_login_text(self):
        """Returns password text box element of Login Page"""

        return self.__driver.find_element_by_xpath(self.password_login_page_text)

    def get_login_button(self):
        """Returns submit login button element of Login Page"""

        return self.__driver.find_element_by_xpath(self.login_submit_sign_in_button)

    def __get_driver(self):  # pylint: disable= W0238
        """Returns driver/browser element. For optional use"""

        return self.__driver
