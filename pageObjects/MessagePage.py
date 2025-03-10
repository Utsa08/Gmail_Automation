from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MessagePage:
    def __init__(self,driver):
        self.driver = driver

    mail = (By.XPATH," //tbody/tr[1]/td[4]")
    text = (By.XPATH,"//div/div[@dir='ltr']")

    def getMail(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(MessagePage.mail))
        self.driver.find_element(*MessagePage.mail).click()

    def getText(self):
        msg = self.driver.find_element(*MessagePage.text).text
        assert "Python" in msg , "Automation Passed"


