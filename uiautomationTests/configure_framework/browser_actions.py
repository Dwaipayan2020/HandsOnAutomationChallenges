"""This module is created to prototype selenium webdriver actions on any browser
   used across different test suits.
"""


def take_screenshot(driver, file_name):
    """Takes screenshot on current webpage

    :param driver: accepts driver object of any browser
    :param file_name: screenshot file name with target destination.
    """

    driver.get_screenshot_as_file(file_name)


def close_current_window(driver):
    """Closes a single tab or an opened current window

    :param driver: accepts driver object of any browser
    """
    driver.close()


def exit_current_session(driver):
    """Closes all opened tabs or opened windows.
       Quits the current session.

    :param driver: accepts driver object of any browser
    """
    driver.quit()


def launch_application(driver, url):
    """Hits the given url and launches the application

    :param driver: accepts driver object of any browser
    :param url: accepts url address of any web application
    """
    driver.get(url)
    driver.maximize_window()
    driver.refresh()
