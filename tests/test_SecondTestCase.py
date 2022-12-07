from selenium.webdriver.common.by import By
import time
from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_SecondTestCase(self):
        #movies = driver.find_elements(By.XPATH, "//div[@class='movies']/div/div/h2")
        movies = self.driver.find_elements(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/h2")


        for movie in movies:

            if movie.text == 'The Shawshank Redemption':
                self.driver.find_element(By.XPATH, "//div[@class='movies']/div[2]/div[3]/button").click()
                ReleaseDate = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/input").get_attribute("value")
                print(ReleaseDate)
                assert "1994-09-23" in ReleaseDate
                time.sleep(2)
                self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/button/span[1]").click()


# #driver.find_element(By.XPATH, "//div[@class='movies']/div[3]/div[3]/button").click()
# driver.find_element(By.XPATH, "//div[@class='movies']/div[2]/div[3]/button").click()
# ReleaseDate = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/input").get_attribute("value")
# assert "1994-09-23" in ReleaseDate