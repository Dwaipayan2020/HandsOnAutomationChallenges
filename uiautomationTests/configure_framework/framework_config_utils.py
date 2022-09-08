"""Framework config utils module is created to function all framework level
   utility functions.
   It has the methods to access any high-level information
   of any existing projects under uiautomationtests.
   Project's AUT, Project's Title, Project's Path, Driver's Information
   are kept inside config.ini file as properties.
"""
import os

from configparser import ConfigParser

__CURR_DIR = os.path.dirname(os.path.realpath(__file__))
__CONFIG = ConfigParser()


def get_driver_path(driver_name):  # pylint : disable=R1710
    """Returns driver path of specific driver.exe file in the current directory.

    :param driver_name: String : accepts driver name as chrome or edge
    :return: String: returns the value of passed key
    """
    if "chrome" in driver_name.lower():
        pass
    elif "edge" in driver_name.lower():
        return get_value_of('edgeDriver', 'PATH')


def __get_config_path():
    """Returns config.ini file path as String."""

    return get_configure_framework_dir_path() + '/config.ini'


def __get_config_parser():
    """Returns config parser object to operate on config.ini file."""

    __CONFIG.read(__get_config_path())
    return __CONFIG


def get_configure_framework_dir_path():
    """Returns current directory path as String.
       It basically returns the path of configure_framework folder
    """
    return __CURR_DIR


def get_value_of(key, section_name):  # pylint : disable=R1710
    """Returns value of a given key which exists
       inside given section in config.ini file.

    :param key: String: It's a key property of a particular section name dictionary.
    :param section_name: String: Section name is a dictionary that holds keys.
    :return: String: returns the value of passed key
    """
    try:
        parser_dict = __get_config_parser()
        return parser_dict[section_name][key]

    except KeyError as key_error:
        print("Requested Key does not exist.")
        print(key_error)


def add_new_key_value(section, key, val):
    """Adds new 'key' which has value 'val' to dictionary name 'section'

    :param section: String: Section name is a dictionary that holds keys.
    :param key: String: It's a key property of a particular section name dictionary.
    :param val: String: It's value of the given key
    :return: None
    """
    parser_dict = __get_config_parser()
    try:
        parser_dict.set(section, key, val)
        with open(__get_config_path(), 'w', encoding='utf-8') as file:
            parser_dict.write(file)

    except KeyError as key_error:
        print("Requested Key does not exist.")
        print(key_error)


def update_value(section, key, new_value):
    """Updates the current key with a new value

    :param section: String: Section name is a dictionary that holds keys.
    :param key: String: It's a key property of a particular section name dictionary.
    :param new_value: String: It's a new value to be assigned to the given key
    :return: None
    """
    parser_dict = __get_config_parser()
    try:
        if parser_dict.has_option(section, key):
            parser_dict.set(section, key, new_value)
            with open(__get_config_path(), 'w', encoding='utf-8') as file:
                parser_dict.write(file)

    except KeyError as key_error:
        print("Requested key doest not exist")
        print(key_error)


def del_value(section, key):
    """Deletes the key exists in current section

    :param section: String: Section name is a dictionary that holds keys.
    :param key: String: It's a key property of a particular section name dictionary.
    :return: None
    """
    parser_dict = __get_config_parser()
    try:
        if parser_dict.has_option(section, key):
            parser_dict.remove_option(section, key)
            with open(__get_config_path(), 'w', encoding='utf-8') as file:
                parser_dict.write(file)

    except KeyError as key_error:
        print("Requested key not available.")
        print(key_error)


def del_section(section):
    """Deletes the section from the config.ini file.

    :param section: String: Section name is a dictionary that holds keys.
    :return: None
    """
    parser_dict = __get_config_parser()
    try:
        if parser_dict.has_section(section):
            parser_dict.remove_section(section)
            with open(__get_config_path(), 'w', encoding='utf-8') as file:
                parser_dict.write(file)
        else:
            raise KeyError

    except KeyError as key_error:
        print("Requested key not available.")
        print(key_error)
