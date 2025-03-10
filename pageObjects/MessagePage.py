from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MessagePage:
    def __init__(self,driver):
        self.driver = driver

    mail = (By.XPATH," //tbody/tr[1]/td[4]")
    text = (By.XPATH,"//div/div[@dir='ltr']")
    delete =(By.XPATH,"//div[contains(@class,'T-I J-J5-Ji nX T-I-ax7 T-I-Js-Gs mA')]")

    def getMail(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of_element_located(MessagePage.mail))
        self.driver.find_element(*MessagePage.mail).click()

    def getText(self):
        msg = self.driver.find_element(*MessagePage.text).text
        assert "Python" in msg , "Automation Passed"
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.element_to_be_clickable(MessagePage.delete))
        self.driver.find_element(*MessagePage.delete).click()


