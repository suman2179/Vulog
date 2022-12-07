from selenium.webdriver.common.by import By
import time


from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestThree(BaseClass):

    def test_ThirdTestCase(self):

        url = self.driver.find_element(By.XPATH, "//div[@class='movies']/div[3]/div[1]").value_of_css_property('background-image').split('"')[1]
        print(url)

        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


