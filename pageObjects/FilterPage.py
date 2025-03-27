from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AllLocators


#Tests if the filter function works properly
class FilterPage:
    def __init__(self,driver):
        self.driver = driver
        self.locator = AllLocators

    def getFilter(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.filter))
        self.driver.find_element(*self.locator.filter).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.filterDate))
        self.driver.find_element(*self.locator.filterDate).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.filterSelectDate))
        self.driver.find_element(*self.locator.filterSelectDate).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.element_to_be_clickable(self.locator.filterSearch))
        self.driver.find_element(*self.locator.filterSearch).click()

        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located(self.locator.filterAssert))
        element = self.driver.find_element(*self.locator.filterAssert)
        assert element.is_displayed(), "Email is not Filtered "
