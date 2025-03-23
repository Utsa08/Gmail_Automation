from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests if the message is sent and asserts weather it contains the same description or not.
class MessagePage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = AllLocators

    def getSentButton(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located(self.locator.sentButton))
        self.driver.find_element(*self.locator.sentButton).click()

    def getMessageSubject(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(expected_conditions.presence_of_element_located(self.locator.anytime))
        subjects = self.driver.find_elements(*self.locator.messageSubject)
        for subject in subjects:
             if "me" in subject.text:
                subject.click()
                break
        msg = self.driver.find_element(*self.locator.text).text
        assert "Python" in msg, "Message not found"