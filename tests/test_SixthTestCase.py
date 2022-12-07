from selenium.webdriver.common.by import By

from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestSix(BaseClass):

    def test_SixthTestCase(self):

        self.driver.find_element(By.XPATH, "//div[@class=\"movies\"]/div[6]/div[3]/button").click()
        ReleaseDate = self.driver.find_element(By.XPATH, "//div[@role=\"document\"]/div[2]/div[2]/div/input").get_attribute("value")
        assert "1995-10-19" == ReleaseDate
        Popularity = self.driver.find_element(By.XPATH, "//div[@role=\"document\"]/div[2]/div[3]/div/input").get_attribute("value")
        assert "24.651" == Popularity
        vote_average = self.driver.find_element(By.XPATH, "//div[@role=\"document\"]/div[2]/div[4]/div/input").get_attribute("value")
        assert "8.6" == vote_average
        vote_count = self.driver.find_element(By.XPATH, "//div[@role=\"document\"]/div[2]/div[5]/div/input").get_attribute("value")
        assert "3975" == vote_count















# pop_up_window = WebDriverWait(driver, 2)
# pop_up_window.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "body > div.jss87.jss80 > div.jss10.jss36.jss11.jss81.jss83 > div.jss122 > div:nth-child(6) > div > input")))
#
# while True:
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
#     time.sleep(1)







#driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
#element_inside_popup = driver.find_element(By.CSS_SELECTOR, "body > div.jss87.jss80 > div.jss10.jss36.jss11.jss81.jss83 > div.jss122 > div:nth-child(6) > div > input")
#element_inside_popup.send_keys(Keys.END)
#ReleaseDate = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/input").get_attribute("value")
#assert "1994-09-23" in ReleaseDate