from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="class")
def setup(request):
    chrome_options_obj = Options()
    chrome_options_obj.add_experimental_option("detach", True)
    service_obj = Service("C:/Users/suman/chromedriver_win32.exe")
    driver = webdriver.Chrome(options=chrome_options_obj, service=service_obj)
    driver.maximize_window()
    driver.get("https://top-movies-qhyuvdwmzt.now.sh/")
    request.cls.driver = driver
    yield
    driver.close()
