"""This module keeps basic configuration utilities used
   to operate pytest.ini file.
"""


from uiautomationtests.configure_framework.framework_config_utils import get_projects_root_dir_path
from uiautomationtests.configure_framework.framework_config_utils import CONFIG_PARSER

__CONFIG = CONFIG_PARSER


def get_pytest_config_path():
    """This method returns pytest.ini configuration file path used across all projects. """

    return get_projects_root_dir_path() + '/pytest.ini'


def get_pytest_config_parser():
    """This method returns a config parser variable used to access pytest.ini file. """
    __CONFIG.read(get_pytest_config_path())
    return __CONFIG
