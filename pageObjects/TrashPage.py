from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests if there exists any mail in the trash and deletes it
class TrashPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getMore(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.more))
        self.driver.find_element(*self.locator.more).click()

    def getTrash(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.trash))
        self.driver.find_element(*self.locator.trash).click()

    def getCheckbox(self):
        try:
            msg = self.driver.find_element(*self.locator.trashCheck).text
            assert "No conversations" in msg, "Mail in Trash"

        except:
            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located(self.locator.fromTrash))
            self.driver.find_element(*self.locator.checkbox).click()

            wait = WebDriverWait(self.driver, 20)
            wait.until(expected_conditions.presence_of_element_located(self.locator.delete))
            self.driver.find_element(*self.locator.delete).click()