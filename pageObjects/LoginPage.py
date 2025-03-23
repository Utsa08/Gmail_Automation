from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Login Page for logging into the gmail
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getEmail(self,email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.emailID))
        self.driver.find_element(*self.locator.emailID).send_keys(email)

    def getNext1(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.next1))
        self.driver.find_element(*self.locator.next1).click()

    def getPassword(self,password):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.password))
        self.driver.find_element(*self.locator.password).send_keys(password)

    def getNext2(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.password))
        self.driver.find_element(*self.locator.next2).click()

    def getGmailImg(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(expected_conditions.presence_of_element_located(self.locator.gmailImg))
        assert element.is_displayed(), "Login Failed"