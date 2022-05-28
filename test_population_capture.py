import datetime
import os
import time
import pytest
from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TestCapture:

    # Method to scoll through webelement
    def scrollPage(self,driver, webElement):
        # self.driver = webdriver.Edge(executable_path="D:\\EdgeDriver\\msedgedriver.exe")
        driver.execute_script("arguments[0].scrollIntoView(true);", webElement)

    def test_capture_population(self):
        # Drivers set up
        driver_path = os.path.dirname(os.path.realpath(__file__))+ "\Drivers\msedgedriver.exe"
        self.driver = webdriver.Edge(executable_path=driver_path)
        # Launch the URL
        self.driver.get("https://www.worldometers.info/world-population/")
        self.driver.maximize_window()
        time.sleep(10)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable(By.XPATH, ".//div[contains(@class,'cc-bottom')]//div[@class='cc-compliance']/a")).click()
        cookie_got_it = self.driver.find_element_by_xpath(".//div[contains(@class,'cc-bottom')]//div[@class='cc-compliance']/a")
        action = ActionChains(self.driver)
        action.move_to_element(cookie_got_it).click().perform()

        active_breadcrumb_elem = self.driver.find_element_by_xpath("(.//div[@id='maincounter-wrap']//parent::*)/ul/li[@class='active']")
        assert str(active_breadcrumb_elem.text) == "World Population"
        population_count_before20secs = self.driver.find_element_by_xpath(".//div[@class='maincounter-number']/span").text
        print("Population Count Before 20s is : " + population_count_before20secs)

        # Keep getting the count of: - Current World Population
        counter = 0
        # Declaring lists for different categories.
        birth_counts_today_20s_interval_sampled_data = list()
        birth_counts_this_year_20s_interval_sampled_data = list()
        death_counts_today_20s_interval_sampled_data = list()
        death_counts_this_year_20s_interval_sampled_data = list()
        population_growth_counts_today_20s_interval_sampled_data = list()
        population_growth_counts_this_year_20s_interval_sampled_data = list()
        counter_categories = ["Births today", "Births this year", "Deaths today", "Deaths this year",
                              "Population Growth today", "Population Growth this year"]
        while counter < 20:

            for category in counter_categories:
                if str(category) == 'Births today':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'"+str(category)+"')]//parent::div[@class='sec-box']//div[@class='sec-counter']/span"
                    today_birth_count_elem = self.driver.find_element_by_xpath(str(xpath_locator))
                    today_birth_count = today_birth_count_elem.text
                    birth_counts_today_20s_interval_sampled_data.append(today_birth_count)

                elif str(category) == 'Births this year':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'"+str(category)+"')]//parent::div[@class='sec-box']//div[@class='sec-counter']/span"
                    this_year_birth_count_elem = self.driver.find_element_by_xpath(xpath_locator)
                    this_year_birth_count = this_year_birth_count_elem.text
                    birth_counts_this_year_20s_interval_sampled_data.append(this_year_birth_count)

                elif str(category) == 'Deaths today':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'" + str(
                        category) + "')]//parent::div[@class='sec-box']//div[@class='sec-counter']/span"
                    today_death_count_elem = self.driver.find_element_by_xpath(xpath_locator)
                    today_death_count = today_death_count_elem.text
                    death_counts_today_20s_interval_sampled_data.append(today_death_count)

                elif str(category) == 'Deaths this year':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'" + str(
                        category) + "')]//parent::div[@class='sec-box']//div[@class='sec-counter']/span"
                    this_year_death_count_elem = self.driver.find_element_by_xpath(xpath_locator)
                    this_year_death_count = this_year_death_count_elem.text
                    death_counts_this_year_20s_interval_sampled_data.append(this_year_death_count)

                elif str(category) == 'Population Growth today':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'" + str(
                        category) + "')]//parent::div[@class='sec-box-last']//div[@class='sec-counter']/span"
                    today_population_growth_count_elem = self.driver.find_element_by_xpath(xpath_locator)
                    today_population_growth_count = today_population_growth_count_elem.text
                    population_growth_counts_today_20s_interval_sampled_data.append(today_population_growth_count)

                elif str(category) == 'Population Growth this year':
                    xpath_locator = ".//div[@class='sec-text'][contains(.,'" + str(
                        category) + "')]//parent::div[@class='sec-box-last']//div[@class='sec-counter']/span"
                    this_year_population_growth_count_elem = self.driver.find_element_by_xpath(xpath_locator)
                    self.scrollPage(self.driver, this_year_population_growth_count_elem)
                    this_year_population_growth_count = this_year_population_growth_count_elem.text
                    population_growth_counts_this_year_20s_interval_sampled_data.append(
                        this_year_population_growth_count)

            # print(f'value of counter {counter}')
            counter += 1
        self.scrollPage(self.driver, self.driver.find_element_by_xpath(".//div[@id='maincounter-wrap']"))
        population_count_after_20s = self.driver.find_element_by_xpath(".//div[@class='maincounter-number']/span").text
        print("Population Count after 20s is : " + population_count_after_20s)

        print(" Printing Desired Result/ Output as asked in th assignment.")
        # Printing data for 'Births Today'
        print("length of each list item "+str(len(birth_counts_today_20s_interval_sampled_data)))
        print(
            f'Printing sample data  for "Births Today" collected at each second for 20 seconds{birth_counts_today_20s_interval_sampled_data}')
        print()
        print(" *********************************** Next *********************************************************")
        print()
        # Printing data for 'Deaths Today'
        print(
            f'Printing sample data  for "Deaths Today" collected at each second for 20 seconds{death_counts_today_20s_interval_sampled_data}')

        print()
        print(" *********************************** Next *********************************************************")
        print()
        # Printing data for 'Population Growth Today'
        print(
            f'Printing sample data  for "Population Growth Today" collected at each second for 20 seconds{population_growth_counts_today_20s_interval_sampled_data}')

        print()
        print(" *********************************** Next *********************************************************")
        print()
        # Printing data for 'Births this year'
        print(
            f'Printing sample data  for "Births this year" collected at each second for 20 seconds{birth_counts_this_year_20s_interval_sampled_data}')

        print()
        print(" *********************************** Next *********************************************************")
        print()
        # Printing data for 'Deaths this year'
        print(
            f'Printing sample data  for "Deaths this year" collected at each second for 20 seconds{death_counts_this_year_20s_interval_sampled_data}')

        print()
        print(" *********************************** Next *********************************************************")
        print()

        # Printing data for 'Population Growth this year'
        print(
            f'Printing sample data  for "Population Growth this year" collected at each second for 20 seconds{population_growth_counts_this_year_20s_interval_sampled_data}')
        now = datetime.datetime.now()
        screenshot_file_name = "ScreenshotFile "+str(now.strftime('%Y-%m-%d %H%M%S'))+".jpeg"
        target_dir_file = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')+ "/screenshots/"+ screenshot_file_name
        self.driver.save_screenshot(target_dir_file)