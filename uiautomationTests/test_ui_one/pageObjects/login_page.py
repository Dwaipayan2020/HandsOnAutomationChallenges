from uiautomationTests.TestUIOne.pageObjects.locators import Locators


class LoginPage(Locators):

    def __init__(self, driver):
        self.__driver = driver

    def get_sign_in_button(self):
        return self.__driver.find_element_by_xpath(self.sign_in_login_page_button)

    def get_user_name_login_text(self):
        return self.__driver.find_element_by_xpath(self.user_name_login_page_text)

    def get_password_login_text(self):
        return self.__driver.find_element_by_xpath(self.password_login_page_text)

    def get_login_button(self):
        return self.__driver.find_element_by_xpath(self.login_submit_sign_in_button)

    def __get_driver(self):
        return self.__driver
