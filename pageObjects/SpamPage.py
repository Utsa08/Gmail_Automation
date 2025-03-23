from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


class SpamPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getSpam(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.more))
        self.driver.find_element(*self.locator.more).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.spam))
        self.driver.find_element(*self.locator.spam).click()

    def getSpamCheck(self):
        check = self.driver.find_element(*self.locator.spamCheck).text
        assert "no spam" in check, "Spam Mail Present"