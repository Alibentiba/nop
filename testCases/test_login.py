from pageObjects.LoginPage import Login_page
from selenium import webdriver
#from conftest import setup
import pytest

class Test_001_Login:
    userName = 'admin@yourstore.com'
    PssWord = 'admin'
    basUrl = 'https://admin-demo.nopcommerce.com'
    # logger = LogGen.loggen()
    

    @pytest.mark.sanity
    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(Test_001_Login.basUrl)
        title_page = self.driver.title
        if title_page == 'Your store. Login':
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_homepage.png")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(Test_001_Login.basUrl)
        lp = Login_page(self.driver)
        lp.setUserName(Test_001_Login.userName)
        lp.setPassword(Test_001_Login.PssWord)
        lp.ClickSubmit()
        Hompage_Title = self.driver.title
        if Hompage_Title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_login.png")
            assert False
