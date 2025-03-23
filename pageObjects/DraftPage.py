from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


class DraftPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getDraft(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.draft))
        draft_Button = self.driver.find_element(*self.locator.draft)
        draft_Button.click()

    def getDraftMail(self):
        msg = self.driver.find_element(*self.locator.draftDiv).text
        if "don't have any saved drafts" in msg:
            print("Draft Empty")
        else:
            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.element_to_be_clickable(self.locator.draftCheckbox))
            self.driver.find_element(*self.locator.draftCheckbox).click()

            wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.element_to_be_clickable(self.locator.draftDiscard))
            self.driver.find_element(*self.locator.draftDiscard).click()