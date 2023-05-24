from pageObjects.LoginPage import Login_page
from pageObjects.customer import customer_page
from pageObjects.search_customers import search_customers
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
class Test_003:
    userName = 'admin@yourstore.com'
    PssWord = 'admin'
    basUrl = 'https://admin-demo.nopcommerce.com'

    #logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_searchcustomers(self, setup):
        self.driver = setup
        self.driver.get(Test_003.basUrl)
        lp = Login_page(self.driver)
        lp.setUserName(Test_003.userName)
        lp.setPassword(Test_003.PssWord)
        lp.ClickSubmit()

        searching_customers=search_customers(self.driver)
        searching_customers.goTosearchPage()
        searching_customers.setemailSearch('kiyjcycyhjc676008@gmail.com')
        searching_customers.clickSearch()
        time.sleep(10)
        status=searching_customers.searchCustomer_By_Email('kiyjcycyhjc676008@gmail.com')
        assert True==status
        self.driver.close()
      
    

        


     
       
