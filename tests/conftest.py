import time
import pytest
from selenium import webdriver

#browser invocation
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    # implicit timing
    driver.implicitly_wait(10)
    driver.get(
        "https://gmail.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--email", action="store", help="Email to login")
    parser.addoption("--passwords", action="store", help="Password for the email")
    parser.addoption("--toemail", action="store", help="Recipient email")
    parser.addoption("--subjects", action="store", help="Email subject")
    parser.addoption("--desc", action="store", help="Email description")


