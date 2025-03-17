from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ComposeMailPage:
    def __init__(self,driver):
        self.driver = driver

    compose =(By.XPATH,"//div[contains(text(),'Compose')]")
    to = (By.XPATH,"//input[@aria-label='To recipients']")
    subject = (By.XPATH,"//input[@name='subjectbox']")
    description = (By.XPATH,"//div[@role='textbox']")
    send = (By.XPATH,"//div[@aria-label='Send ‪(Ctrl-Enter)‬']")

    def getCompose(self):
        self.driver.find_element(*ComposeMailPage.compose).click()

    def getTO(self,toemail):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.element_to_be_clickable(ComposeMailPage.to))
        self.driver.find_element(*ComposeMailPage.to).send_keys(toemail)

    def getSubject(self,subjects):
        self.driver.find_element(*ComposeMailPage.subject).send_keys(subjects)

    def getDescription(self,desc):
        self.driver.find_element(*ComposeMailPage.description).send_keys(desc)

    def getSend(self):
        self.driver.find_element(*ComposeMailPage.send).click()


