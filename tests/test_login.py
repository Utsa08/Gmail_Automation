import time
from logging import getLogger

import pytest
from pageObjects.ComposeMailPage import ComposeMailPage
from pageObjects.LoginPage import LoginPage
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

    @pytest.mark.run(order = 1)
    def test_login(self,get_data):
        email, passwords, toemail, subjects, desc = get_data
        log = self.get_logger()

        #loginPage
        loginPage = LoginPage(self.driver)
        loginPage.getEmail(email)
        log.info("My Email: "+email)
        loginPage.getNext1()
        loginPage.getPassword(passwords)
        log.info("My Password: "+passwords)
        loginPage.getNext2()

        #ComposeMailPage
        composeMailPage = ComposeMailPage(self.driver)
        composeMailPage.getCompose()
        composeMailPage.getTO(toemail)
        log.info("To Email: "+toemail)
        composeMailPage.getSubject(subjects)
        log.info("Subject :"+subjects)
        composeMailPage.getDescription(desc)
        log.info("Description :"+desc)
        composeMailPage.getSend()
        time.sleep(5)

    @pytest.mark.run(order = 2)
    def test_Message(self):
        log = self.get_logger()

        #MessagePage
        messagePage =MessagePage(self.driver)
        messagePage.getMail()
        time.sleep(5)
        messagePage.getText()
        log.info("Msg Asserted")





