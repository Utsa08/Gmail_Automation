from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


class LabelPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getLabel(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.label))
        self.driver.find_element(*self.locator.label).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.labelName))
        self.driver.find_element(*self.locator.labelName).send_keys("L1")

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.labelCreate))
        self.driver.find_element(*self.locator.labelCreate).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.label))
        self.driver.find_element(*self.locator.label).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.labelName))
        self.driver.find_element(*self.locator.labelName).send_keys("L1")

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.labelCreate))
        self.driver.find_element(*self.locator.labelCreate).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located(self.locator.labelCheck))
        element = self.driver.find_element(*self.locator.labelCheck)
        assert element.is_displayed(), "Label with same name already exists "