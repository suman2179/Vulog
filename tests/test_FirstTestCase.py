from selenium.webdriver.common.by import By

#@pytest.mark.usefixtures("setup")
from Vulog_TestAutomation.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_FirstTestCase(self):
        results = self.driver.find_elements(By.CSS_SELECTOR, ".movies .movie-card")

        for result in results:
            assert result.is_displayed() == True

        Movies_Count = len(results)
        assert Movies_Count > 1


