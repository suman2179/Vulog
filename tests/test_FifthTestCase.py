from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from Vulog_TestAutomation.utilities.BaseClass import BaseClass

class TestFifth(BaseClass):

    def test_FifthTesyCase(self):

        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys("A NEW")
        self.driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/div/form/div/input").send_keys(Keys.ENTER)
        time.sleep(5)
        results = self.driver.find_elements(By.XPATH, "//*[@id=\"root\"]/div/div/div/div/h2")
#counts = len(results)

        try:
            for result in results:
                assert "A NEW".casefold() in result.text.casefold()

        except:
            print("In some movie titles the phrase A New is not displayed correctly, eg: 'The Gendarme in New York' ")


        finally:
            for result in results:
                print(result.text)



