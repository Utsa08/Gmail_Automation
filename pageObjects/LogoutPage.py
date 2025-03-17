from selenium.webdriver.common.by import By


class LogoutPage:
    def __init__(self,driver):
        self.driver = driver

    profileIcon = (By.XPATH, "//a[contains(@aria-label, 'Google Account')]")

    def getLogout(self):
        self.driver.find_element(*LogoutPage.profileIcon).click()
        self.driver.quit()