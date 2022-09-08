"""This module keeps basic configuration utilities used across current project level operations. """

import os

from configparser import ConfigParser

__CURR_DIR = os.path.dirname(os.path.realpath(__file__))
__CONFIG = ConfigParser()
PARENT_DIR = os.path.abspath(os.path.join(__CURR_DIR, os.pardir))


def get_pytest_config_path():
    """This method returns pytest.ini configuration file path used across current project. """

    return get_project_utils_path() + '/pytest.ini'


def get_project_utils_path():
    """This method returns configure_project directory path in a current project. """
    return __CURR_DIR


def get_config_parser_current_project():
    """This method returns a config parser variable used inside current project utilities. """
    __CONFIG.read(get_pytest_config_path())
    return __CONFIG
