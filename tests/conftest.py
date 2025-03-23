import time
import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage

driver = None

#Addoption
def pytest_addoption(parser):
    parser.addoption("--email", action="store", help="Email to login")
    parser.addoption("--password", action="store", help="Password for the email")


#browser invocation
@pytest.fixture(scope="function")
def setup(request):
    global driver
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")

    driver = webdriver.Chrome()
    # implicit timing
    driver.implicitly_wait(10)
    driver.get(
        "https://gmail.com/")
    driver.maximize_window()

    loginPage =LoginPage(driver)
    loginPage.getEmail(email)
    loginPage.getNext1()
    loginPage.getPassword(password)
    loginPage.getNext2()
    request.cls.driver = driver
    request.cls.loginPage = loginPage
    yield
    driver.quit()
