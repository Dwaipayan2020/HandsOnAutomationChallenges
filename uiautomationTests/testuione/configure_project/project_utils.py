"""Project Utils module takes care of project level utility functions
   to work with pytest.ini file .
"""
import os

from datetime import datetime

from uiautomationtests.testuione.configure_project.config_utils import get_config_parser_current_project
from uiautomationtests.testuione.configure_project.config_utils import PARENT_DIR
from uiautomationtests.testuione.configure_project.config_utils import get_pytest_config_path

__CFG_PARSER_DICT = get_config_parser_current_project()
__DEFAULT_HTML_REPORT_PATH = PARENT_DIR+'\\reports\\'
__DEFAULT_ALLURE_REPORT_PATH = PARENT_DIR+'\\allure_reports\\'
__REPORT_ALL_FLAG = '-rA'
__DEFAULT_HTML_FLAG = '--html='
__DEFAULT_ALLURE_FLAG = ' alluredir='
__VERBOSE_FLAG = ' -v '
__K_FLAG = ' -k '
__STD_OUTPUT_FLAG = '-s'
__MARKER_FLAG = ' -m '
__DEFAULT_HTML_REPORT_NAME = 'test_results.html'
__IS_DYNAMIC_REPORT = True
CURRENT_TIME_STAMP = datetime.now().strftime("%d%m%Y%H%M")


def __add_new_key_value(section, key, val):
    """Adds a new key, value inside a given section present in pytest.ini file"""

    try:
        if not __CFG_PARSER_DICT.has_option(section, key):
            __CFG_PARSER_DICT.set(section, key, val)
            with open(get_pytest_config_path(), 'w', encoding='utf-8') as file:
                __CFG_PARSER_DICT.write(file)
        else:
            __update_value_of_key(section, key, val)

    except KeyError as key_error:
        print(f'{section} does not exist')
        print(key_error)


def __get_value_of_key(section, key):
    """Fetches the value for requested key of a particular section in pytest.ini file
       of current project.
    """
    return __CFG_PARSER_DICT[section][key]


def __update_value_of_key(section, key, val):
    """Updates the value for requested key of a particular section in pytest.ini file
       of current project.
       It performs update only when the new value is not present in old value
       of the key in update.
    """

    old_val = ''
    if __CFG_PARSER_DICT.has_option(section, key):
        old_val = __CFG_PARSER_DICT[section][key]
    try:
        if not __is_exist_already(section, key, old_val, val):
            __CFG_PARSER_DICT.set(section, key, val)
            with open(get_pytest_config_path(), 'w', encoding='utf-8') as file:
                __CFG_PARSER_DICT.write(file)
                return True
        return False

    except KeyError as key_error:
        print("Requested key does not exist.")
        print(key_error)


def __is_exist_already(section, key, old_val, new_val):
    """Checks if any new value is present in the old value of a given key
    of any section in pytest.ini file.

    :param section: String, section in pytest.ini file
    :param key: String, key in section
    :param old_val: String, old_val of key
    :param new_val: String, new_val to key
    :return: Boolean
    """
    if __CFG_PARSER_DICT.has_option(section, key):
        if new_val in old_val:
            return True
        return False


def __del_value_of_key(section, key):
    """ Deletes an existing key of any existing section in pytest.ini file.
    :param section: String, section in pytest.ini file
    :param key: String, key in section
    """

    try:
        if __CFG_PARSER_DICT.has_option(section, key):
            __CFG_PARSER_DICT.remove_option(section, key)
            with open(get_pytest_config_path(), 'w', encoding='utf-8') as file:
                __CFG_PARSER_DICT.write(file)
        else:
            pass
    except KeyError as key_error:
        print("Requested key does not exist.")
        print(key_error)


def __get_markers():
    """Returns markers field value under pytest in pytest.ini file."""

    return __get_value_of_key('pytest', 'markers')


def __add_markers(marker_data):
    """Adds or updates a new marker to markers field under pytest."""

    new_marker_desc = __get_markers() + '\n' + marker_data + \
        ' : This marker was collected from \'marker_flag_change\'.\n '
    __update_value_of_key('pytest', 'markers', new_marker_desc)


def __update_markers(marker_flag_change_val):
    """Updates markers value in markers field under pytest."""

    marker_val = __get_markers()
    if not __is_exist_already('pytest', 'markers',
                              marker_val, marker_flag_change_val):
        __add_markers(marker_flag_change_val)


def create_new_markers():
    """Deletes existing markers field and creates a new markers field
       with default value in pytest.
    """

    __del_value_of_key('pytest', 'markers')
    __add_new_key_value('pytest', 'markers', __get_default_marker())


def __get_default_marker():
    """Retrieves updated default markers value
       from default field in MarkerContent.
    """

    return __get_value_of_key('MarkerContent', 'default')


def __update_default_marker(updated_marker_content):
    """Updates default markers value in default field
       inside MarkerContent of pytest.ini file.
    """

    marker_flag_change_val = __get_value_of_key('ReportingContent',
                                                'marker_flag_change')
    if not (marker_flag_change_val is None or marker_flag_change_val == ''):
        __del_value_of_key('MarkerContent', 'default')
        __update_value_of_key('MarkerContent', 'default', updated_marker_content)


def delete_markers_pytest():
    """Deletes markers field in pytest."""

    __del_value_of_key('pytest', 'markers')


def __get_custom_html_report_path():
    """Retrieves 'html_reporter_changed_path' field value under 'ReportingContent'."""

    return __get_value_of_key('ReportingContent', 'html_reporter_changed_path')


def __get_report_name_html():
    """Retrieves 'report_name_html' field value under 'ReportingContent'."""

    report_name = __get_value_of_key('ReportingContent', 'report_name_html')
    if report_name is None or report_name == '':
        return __DEFAULT_HTML_REPORT_NAME

    return __get_value_of_key('ReportingContent', 'report_name_html')


def __update_new_report_name(is_create_new):
    """Updates 'report_name_html' field value under 'ReportingContent'
       only when 'is_create_new' argument value is passed as True and returns
       a dynamic report name. Else it returns default report name.

     param is_create_new : accepts boolean argument
    :return: String
    """

    if is_create_new:
        new_report_name = f'test_results_{CURRENT_TIME_STAMP}.html'
        __update_value_of_key('ReportingContent', 'report_name_html', new_report_name)
    return __get_report_name_html()


def __get_k_flag_change():
    """Returns -k flag with value available in 'k_flag_change field'
       inside ReportingContent."""

    k_flag_val = __get_value_of_key('ReportingContent', 'k_flag_change')
    if k_flag_val is None or k_flag_val == '':
        return ""
    new_k_flag = __K_FLAG + k_flag_val
    return new_k_flag


def __get_marker_flag_change():
    """Returns -m flag with value available in 'marker_flag_change'
       inside ReportingContent."""

    marker_flag_val = __get_value_of_key('ReportingContent', 'marker_flag_change')
    if marker_flag_val is None or marker_flag_val == '':
        return ""
    __update_markers(marker_flag_val)
    __update_default_marker(__get_markers())
    return __MARKER_FLAG + ' ' + marker_flag_val


def __update_html_reporter_path_change():
    """Returns updated html reporter custom path only if
       'html_reporter_changed_path' field is updated with a custom path value.
       Else, it returns '__DEFAULT_HTML_REPORT_PATH'.
    """

    new_custom_path = __get_custom_html_report_path()
    if new_custom_path is None or new_custom_path == '':
        return __DEFAULT_HTML_REPORT_PATH

    return new_custom_path


def update_addopts(is_update, report_type):
    """Updates the addopts field value automatically inside pytest section.
       The method executes only when is_update argument is passed as True.

    param is_update: accepts boolean argument
    :return: None
    """

    new_addopts_str = ''
    if is_update:
        if report_type.lower() == 'html':
            new_addopts_str = f'{__DEFAULT_HTML_FLAG}.strip() \
                {__update_html_reporter_path_change()}.strip() \
                {__update_new_report_name(__IS_DYNAMIC_REPORT)}.strip() \
                {" "+__REPORT_ALL_FLAG}.strip() \
                {__get_k_flag_change()}.strip() {" "} \
                {__get_marker_flag_change()}.strip() {" "} \
                {__VERBOSE_FLAG}.strip() {" "} \
                {__STD_OUTPUT_FLAG}.strip()'
        elif report_type.lower() == 'allure':
            new_addopts_str = f'{__DEFAULT_ALLURE_FLAG}.strip() \
                            {__DEFAULT_ALLURE_REPORT_PATH}.strip()\
                            {"  " + __REPORT_ALL_FLAG}.strip() \
                            {__get_k_flag_change()}.strip() {"  "} \
                            {__get_marker_flag_change()}.strip() {" "} \
                            {__VERBOSE_FLAG}.strip() {"  "} \
                            {__STD_OUTPUT_FLAG}.strip()'
        if not __CFG_PARSER_DICT.has_option('pytest', 'addopts'):
            __CFG_PARSER_DICT.set('pytest', 'addopts', '')
            with open(get_pytest_config_path(), 'w', encoding='utf-8') as file:
                __CFG_PARSER_DICT.write(file)

        print("addopts=" + new_addopts_str)
        __update_value_of_key('pytest', 'addopts', new_addopts_str)
