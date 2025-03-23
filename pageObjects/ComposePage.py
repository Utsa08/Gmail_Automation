from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Compose Page for sending the mail
class ComposePage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getCompose(self):
        self.driver.find_element(*self.locator.compose).click()

    def getTO(self,email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.to))
        self.driver.find_element(*self.locator.to).send_keys(email)

    def getSubject(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.subject))
        self.driver.find_element(*self.locator.subject).send_keys("Email Automation")

    def getDescription(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.description))
        self.driver.find_element(*self.locator.description).send_keys("Python Gmail Automation")

    def getSend(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.send))
        self.driver.find_element(*self.locator.send).click()

    def getMessageSend(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located(self.locator.messageSent))
        element = self.driver.find_element(*self.locator.messageSent).text
        assert element == 'Message sent', "Mail is not send"