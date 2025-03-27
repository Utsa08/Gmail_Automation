from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators
from pageObjects.MessagePage import MessagePage


#Checks the mail and if matched then deletes the mail
class DeletePage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getMessage(self):
        messagePage = MessagePage(self.driver)
        messagePage.getSentButton()

    def getDeleteMessage(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located(self.locator.anytime))
        subjects = self.driver.find_elements(*self.locator.messageSubject)
        for subject in subjects:
            if "me" in subject.text:
                subject.click()
                wait = WebDriverWait(self.driver, 30)
                wait.until(expected_conditions.element_to_be_clickable(self.locator.delete))
                self.driver.find_element(*self.locator.delete).click()
                wait = WebDriverWait(self.driver, 30)
                wait.until(expected_conditions.presence_of_element_located(self.locator.deleteMessage))

                break
        else:
            print("Mail Not Found")