from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestFour(BaseClass):

    def test_FourthTestCase(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys("star trek")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.ENTER)
        #driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/div/div[7]/div[2]/h2").is_displayed()
        wait = WebDriverWait(self.driver,15)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/div/div[7]/div[2]/h2")))
        #print(driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[7]/div[2]/h2").text)
        assert self.driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/div/div[7]/div[2]/h2").is_displayed() == True
        try:
            element = self.driver.find_element(By.XPATH, "//h2[text()=\"The Shawshank Redemption\"]")
            if element.is_displayed():
                print("The Shawshank Redemption is displayed")
        except:
            print("The Shawshank Redemption is not displayed")


