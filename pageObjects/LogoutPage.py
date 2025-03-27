from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests the logout function of the email
class LogoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getLogout(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.profileIcon))
        self.driver.find_element(*self.locator.profileIcon).click()