#On the search box without putting any data if we type enter the screen is going blank.


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestBugOne(BaseClass):

    def test_Bug_1(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.close()