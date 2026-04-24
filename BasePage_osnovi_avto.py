import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    SUCCESS_MESSAGE = (By.ID, "success-message")

    def open(self):
        self.driver.get("https://example.com/login")
        return self

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

    def get_message(self):
        message_element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return message_element.text

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # или другой браузер
    yield driver
    driver.quit()

def test_login_success(driver):
    page = LoginPage(driver)
    page.open()
    page.login("admin", "123")
    assert page.get_message() == "Login successful"
