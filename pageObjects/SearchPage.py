from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests the search option and asserts the mail
class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = AllLocators

    def getSearch(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.search))
        self.driver.find_element(*self.locator.search).send_keys("Email Automation")

    def getSearchButton(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(self.locator.convo))
        self.driver.find_element(*self.locator.searchButton).click()

    def getSearchMessage(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(expected_conditions.presence_of_element_located(self.locator.searchMessage))
        messages = self.driver.find_elements(*self.locator.searchMessage)
        for message in messages:
            if "Automation" in message.text:
                message.click()
                break
        msg = self.driver.find_element(*self.locator.desc).text
        assert "Python" in msg, "Message not found"