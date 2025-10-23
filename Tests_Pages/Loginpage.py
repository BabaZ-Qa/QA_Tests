import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_page(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    def login_messages(self):
        try:
            mesaj = self.driver.find_element(By.ID, "error").text
            return mesaj
        except:
            mesaj = self.driver.find_element(By.XPATH, "//div/h1").text
            return mesaj
