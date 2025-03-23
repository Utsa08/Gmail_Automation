import time
import pytest
from pageObjects.ComposePage import ComposePage
from pageObjects.DraftPage import DraftPage
from pageObjects.FilterPage import FilterPage
from pageObjects.LabelPage import LabelPage
from pageObjects.LoginPage import LoginPage
from pageObjects.LogoutPage import LogoutPage
from pageObjects.MessagePage import MessagePage
from pageObjects.SearchPage import SearchPage
from pageObjects.SettingsPage import SettingsPage
from pageObjects.SpamPage import SpamPage
from pageObjects.TrashPage import TrashPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class Test_Main(BaseClass):

    #Argument
    @pytest.fixture(scope="function")
    def get_Data(self,request):
        email = request.config.getoption("--email")
        return email

    #Tests the login Functionality and Asserts
    @pytest.mark.run(order=1)
    def test_login(self):
        loginpage=LoginPage(self.driver)
        loginpage.getGmailImg()

    #Tests the compose mail Functionality and Asserts
    @pytest.mark.compose
    @pytest.mark.run(order=2)
    def test_composeMail(self,get_Data):
        email = get_Data
        composeMail = ComposePage(self.driver)
        composeMail.getCompose()
        composeMail.getTO(email)
        composeMail.getSubject()
        composeMail.getDescription()
        composeMail.getSend()
        composeMail.getMessageSend()

    #Tests if the message sent through the mail is same and Asserts
    @pytest.mark.message
    @pytest.mark.run(order=3)
    def test_message(self):
        messagePage = MessagePage(self.driver)
        messagePage.getSentButton()
        messagePage.getMessageSubject()

    #Tests if the search function is working and Asserts
    @pytest.mark.search
    @pytest.mark.run(order=4)
    def test_search(self):
        searchPage = SearchPage(self.driver)
        searchPage.getSearch()
        searchPage.getSearchButton()
        searchPage.getSearchMessage()

    #Tests the label function and Asserts
    @pytest.mark.label
    @pytest.mark.run(order=5)
    def test_label(self):
        labelPage = LabelPage(self.driver)
        labelPage.getLabel()

    #Tests the settings function and changes the settings
    @pytest.mark.settings
    @pytest.mark.run(order=6)
    def test_settings(self):
        settingsPage = SettingsPage(self.driver)
        settingsPage.getSettings()

    #Tests if the filter function works and checks the message
    @pytest.mark.filter
    @pytest.mark.run(order=7)
    def test_filter(self):
        filterPage= FilterPage(self.driver)
        filterPage.getFilter()

    #Tests if there is any messages in draft
    @pytest.mark.draft
    @pytest.mark.run(order=8)
    def test_draft(self):
        draftPage = DraftPage(self.driver)
        draftPage.getDraft()
        draftPage.getDraftMail()

    #Tests if there is any message in the trash and if exists deletes the mails
    @pytest.mark.trash
    @pytest.mark.run(order=9)
    def test_trash(self):
        trashPage = TrashPage(self.driver)
        trashPage.getMore()
        trashPage.getTrash()
        trashPage.getCheckbox()

    @pytest.mark.spam
    @pytest.mark.run(order=10)
    def test_spam(self):
        spamPage = SpamPage(self.driver)
        spamPage.getSpam()
        spamPage.getSpamCheck()
        time.sleep(2)

    #Tests the logout Function
    @pytest.mark.logout
    @pytest.mark.run(order=11)
    def test_logout(self):
        logoutPage = LogoutPage(self.driver)
        logoutPage.getLogout()