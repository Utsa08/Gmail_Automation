import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    #searching a mail
    search = (By.XPATH, "//input[@aria-label='Search mail']")
    sbutton = (By. CSS_SELECTOR,"button[aria-label='Search mail']")
    smail = (By.XPATH,"(//span[text()='Automation'])[1]")
    chat = (By.XPATH,"//div[@aria-label='Chat, 1 unread message']")
    meet = (By.XPATH,"//div[@aria-label='Meet']")

    #creating a label
    label=(By.XPATH,"//div[@aria-label='Create new label']")
    labelName=(By.XPATH,"//span//input[@type='text']")
    labelCreate = (By.XPATH,"//span[text()='Create']")

    #changing settings
    settings=(By.XPATH,"//a[@aria-label='Settings']")
    settingsRadioButton = (By.XPATH,"//div[text()='Compact']")
    settingsClose=(By.XPATH,"//div/button[@aria-label='Close']")

    #adding filter
    filter=(By.XPATH,"//button[@aria-label='Advanced search options']")
    filterDate=(By.XPATH,"//div[@aria-label='Date within']")
    filterSelectDate = (By.XPATH,"//div[text()='3 days']")
    filterSearch = (By.XPATH,"//div[@aria-label='Search Mail']")

    drafts = (By.XPATH,"//a[@aria-label='Drafts']")

    sent=(By.XPATH,"//a[@aria-label='Sent']")

    starred =(By.XPATH,"//a[@aria-label='Starred']")


    def getChat(self):
        self.driver.find_element(*HomePage.chat).click()
        self.driver.back()

    def getMeet(self):
        self.driver.find_element(*HomePage.meet).click()
        self.driver.back()

    def getSearch(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.search))
        self.driver.find_element(*HomePage.search).send_keys("Gmail Automation")
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.sbutton))
        self.driver.find_element(*HomePage.sbutton).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(HomePage.smail))
        self.driver.find_element(*HomePage.smail).click()
        self.driver.back()
        self.driver.back()

    def getLabel(self):
        self.driver.find_element(*HomePage.label).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.labelName))
        self.driver.find_element(*HomePage.labelName).send_keys("Label1")
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(HomePage.labelCreate))
        self.driver.find_element(*HomePage.labelCreate).click()

    def getSettings(self):
        self.driver.find_element(*HomePage.settings).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.settingsRadioButton))
        self.driver.find_element(*HomePage.settingsRadioButton).click()
        self.driver.find_element(*HomePage.settingsClose).click()

    def getFilter(self):
        self.driver.find_element(*HomePage.filter).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.filterDate))
        self.driver.find_element(*HomePage.filterDate).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.filterSelectDate))
        self.driver.find_element(*HomePage.filterSelectDate).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.visibility_of_element_located(HomePage.filterSearch))
        self.driver.find_element(*HomePage.filterSearch).click()
        time.sleep(2)
        self.driver.back()

    def getDraft(self):
        self.driver.find_element(*HomePage.drafts).click()
        time.sleep(2)
        self.driver.back()

    def getSent(self):
        self.driver.find_element(*HomePage.sent).click()
        time.sleep(2)
        self.driver.back()

    def getStarred(self):
        self.driver.find_element(*HomePage.starred).click()
        time.sleep(2)
        self.driver.back()


