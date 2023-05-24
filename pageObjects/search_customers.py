from selenium import webdriver
from selenium.webdriver.common.by import By
class search_customers:

    # elements xpaths
    Customer_Menu="//a[@href='#']//p[contains(text(),'Customers')]"
    Customer_Sub_Menu="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    email_xpath="//input[@id='SearchEmail']"
    firstName_Xpath="//input[@id='SearchFirstName']"
    lastName_Xpath="//input[@id='SearchLastName']"
    buttonSearch_xpath="//button[@id='search-customers']//i[@class='fas fa-search']"
    tblSearch_Results_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"
    #driver = webdriver.Chrome(r'/Users/air2015/Downloads/chromedriver_mac64 (1)/chromedriver')

  

    #     Action LMethods
    def __init__(self, driver):
        self.driver = driver
    
    def goTosearchPage(self):
        self.driver.find_element(By.XPATH,search_customers.Customer_Menu).click()
        self.driver.find_element(By.XPATH,search_customers.Customer_Sub_Menu).click()



    def setemailSearch (self,email):
        self.driver.find_element(By.XPATH,search_customers.email_xpath).send_keys(email)

    def setfirstNameSearch (self,firstName):
        self.driver.find_element(By.XPATH,search_customers.firstName_Xpath).send_keys(firstName)

    
    def setLastNameSearch (self,lastName):
        self.driver.find_element(By.XPATH,search_customers.lastName_Xpath).send_keys(lastName)

    def clickSearch (self):
        self.driver.find_element(By.XPATH,search_customers.buttonSearch_xpath).click()
        # Scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def getNoOfRows (self):
            return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))
    
    def getNoOfColumns (self):
            return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))
    
    def searchCustomer_By_Email(self,email):
            flag=False
            for r in range(1, self.getNoOfRows()+1):
             table=self.driver.find_element(By.XPATH, self.table_xpath)
             emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
             if emailid == email:
              flag = True
             break
            return flag

    def searchCustomer_ByName(self, Name):
            flag=False
            for r in range(1, self.getNoOfRows()+1):
             table=self.driver.find_element(By.XPATH, self.table_xpath)
             name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
             if name == Name:
                flag = True
                break
            return flag


                