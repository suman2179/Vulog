#After clearing the search box the website is not getting back to its original list of movies as it was before searching

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestBugTwo(BaseClass):

    def test_Bug_2(self):

        results1 = self.driver.find_elements(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/h2")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys("The")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.CONTROL+"a")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.DELETE)
        results2 = self.driver.find_elements(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/h2")

        print("After clearing the search box the website is not getting back to its original list of movies as it was before searching")
        assert results1 == results2




