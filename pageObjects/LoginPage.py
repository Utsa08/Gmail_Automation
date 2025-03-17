from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    emailID = (By.XPATH,"//input[@id='identifierId']")
    next1 = (By.XPATH,"//span[text()='Next']")
    password = (By.XPATH,"//input[@type='password']")
    next2 = (By.XPATH,"//span[text()='Next']")

    def getEmail(self,email):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(LoginPage.emailID))
        self.driver.find_element(*LoginPage.emailID).send_keys(email)

    def getNext1(self):
        self.driver.find_element(*LoginPage.next1).click()

    def getPassword(self,passwords):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(LoginPage.password))
        self.driver.find_element(*LoginPage.password).send_keys(passwords)

    def getNext2(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(LoginPage.password))
        self.driver.find_element(*LoginPage.next2).click()

