from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests the settings function and changes the settings
class SettingsPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators
 
    def getSettings(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.settings))
        self.driver.find_element(*self.locator.settings).click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.settingsRadioButton))
        self.driver.find_element(*self.locator.settingsRadioButton).click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.settingsClose))
        self.driver.find_element(*self.locator.settingsClose).click()