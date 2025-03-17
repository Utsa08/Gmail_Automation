import time
from logging import getLogger

import pytest

from pageObjects.ComposeMailPage import ComposeMailPage
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.LogoutPage import LogoutPage
from pageObjects.MessagePage import MessagePage
from utilities.BaseClass import BaseClass

class TestLogin(BaseClass):

    @pytest.fixture(scope="class")
    def get_data(self, request):
        email = request.config.getoption("--email")
        passwords = request.config.getoption("--passwords")
        toemail = request.config.getoption("--toemail")
        subjects = request.config.getoption("--subjects")
        desc = request.config.getoption("--desc")
        return email, passwords, toemail, subjects, desc

    @pytest.mark.run(order=1)
    def test_login(self, get_data):
        email, passwords, toemail, subjects, desc = get_data
        log = self.get_logger()

        # loginPage
        loginPage = LoginPage(self.driver)
        loginPage.getEmail(email)
        log.info("My Email: " + email)
        loginPage.getNext1()
        loginPage.getPassword(passwords)
        log.info("My Password: " + passwords)
        loginPage.getNext2()

        # ComposeMailPage
        composeMailPage = ComposeMailPage(self.driver)
        composeMailPage.getCompose()
        composeMailPage.getTO(toemail)
        log.info("To Email: " + toemail)
        composeMailPage.getSubject(subjects)
        log.info("Subject :" + subjects)
        composeMailPage.getDescription(desc)
        log.info("Description :" + desc)
        composeMailPage.getSend()
        time.sleep(5)

    @pytest.mark.run(order=2)
    def test_chat(self):
        log = self.get_logger()
        homepage=HomePage(self.driver)
        homepage.getChat()
        log.info("Chat Opened")
        time.sleep(5)

    @pytest.mark.run(order=3)
    def test_meet(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.getMeet()
        log.info("Meet Opened")
        time.sleep(5)

    @pytest.mark.run(order=4)
    def test_search(self):
        log = self.get_logger()
        homePage=HomePage(self.driver)
        homePage.getSearch()
        log.info("Searched Mail")
        time.sleep(5)

    @pytest.mark.run(order=5)
    def test_Sent(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.getSent()
        log.info("Sent Opened")
        time.sleep(5)

    @pytest.mark.run(order=6)
    def test_Starred(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.getStarred()
        log.info("Starred Opened")
        time.sleep(5)

    @pytest.mark.run(order = 7)
    def test_Message(self):
        log = self.get_logger()

        #MessagePage
        messagePage =MessagePage(self.driver)
        messagePage.getMail()
        time.sleep(5)
        messagePage.getText()
        log.info("Msg Asserted")
        log.info("Mail Deleted")
        time.sleep(5)

    @pytest.mark.run(order=8)
    def test_Label(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.getLabel()
        log.info("Added Label")
        time.sleep(5)

    @pytest.mark.run(order=9)
    def test_Settings(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.getSettings()
        log.info("Settings Changed")
        time.sleep(5)

    @pytest.mark.run(order=10)
    def test_Filter(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.getFilter()
        log.info("Filter Added")
        time.sleep(5)

    @pytest.mark.run(order=11)
    def test_Draft(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.getDraft()
        log.info("Draft Opened")
        time.sleep(5)

    @pytest.mark.run(order=12)
    def test_Logout(self):
        log = self.get_logger()
        logoutPage = LogoutPage(self.driver)
        logoutPage.getLogout()
        log.info("Logged Out")
        time.sleep(5)
