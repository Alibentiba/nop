from pageObjects.LoginPage import Login_page
from pageObjects.customer import customer_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from TestData.Email import generate_email
import pytest
class Test_002:
    userName = 'admin@yourstore.com'
    PssWord = 'admin'
    basUrl = 'https://admin-demo.nopcommerce.com'
    random_email = generate_email()

    #logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_costumer(self, setup):
        self.driver = setup
        self.driver.get(Test_002.basUrl)
        lp = Login_page(self.driver)
        lp.setUserName(Test_002.userName)
        lp.setPassword(Test_002.PssWord)
        lp.ClickSubmit()
        New_Customer=customer_page(self.driver)
        New_Customer.go_To_Customer_page()
        New_Customer.setEmail(Test_002.random_email)
        New_Customer.setPassword(Test_002.random_email)
        New_Customer.setFirstName('Ali')
        New_Customer.setFirstName('Bentiba')
        New_Customer.setgander('mal')
        New_Customer.setDatBirthDay('5/9/2023')
        New_Customer.setCompanyName('G22')
        New_Customer.setIsTax()
       # New_Customer.setRole()
        New_Customer.save()
        msg = self.driver.find_element(By.TAG_NAME,'body').text
        if "The new customer has been added successfully." in msg:
            self.driver.save_screenshot("ScreenShots/test.png")
            assert True
        else:
            self.driver.save_screenshot("ScreenShots/testFaile.png")
            assert False
   
        self.driver.close()
      
    

        


     
       
