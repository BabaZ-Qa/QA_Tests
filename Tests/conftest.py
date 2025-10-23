from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.get("https://practicetestautomation.com/practice-test-login/")
    request.cls.driver = driver
    yield
    driver.quit()
