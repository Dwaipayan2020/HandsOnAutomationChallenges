"""Testdata utility module keeps all test data configuration methods
   for manipulating existing test data kept inside data properties file like credentials.ini
"""

import os

from configparser import ConfigParser

__CURR_DIR = os.path.dirname(os.path.realpath(__file__))


def get_test_data_config(only_file_name):
    """Initializing config parser to access test data configuration file.
        Example: It can return config parser of 'credentials.ini' file
    """
    config = ConfigParser()
    config.read(get_test_data_file_path(only_file_name))
    return config


def get_test_data_dir_path():
    """Returns current testdata directory path."""

    return __CURR_DIR


def get_test_data_file_path(file_name):
    """Returns current testdata directory path."""

    return get_test_data_dir_path() + './' + file_name + '.ini'


def get_data(file_name, section_name, field):
    """Returns any existing field value of any existing section
       in any existing testdata file.
    """
    return get_test_data_config(file_name)[section_name][field]
