"""This Module has Locator class that stores web element locators for all pages
 applicable in current project
"""


class Locators:  # pylint:disable=R0903

    """Initializing locators by id, name, xpath, css_selector, link_text """
    sign_in_login_page_button = ".//a[@class='nav__button-secondary btn-md btn-secondary-emphasis']"
    user_name_login_page_text = ".//input[@id='username']"
    password_login_page_text = ".//input[@id='password']"
    login_submit_sign_in_button = ".//*[@class='btn__primary--large from__button--floating']"
