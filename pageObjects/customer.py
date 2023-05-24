from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class customer_page:
    # elements xpaths
    Customer_Menu="//a[@href='#']//p[contains(text(),'Customers')]"
    Customer_Sub_Menu="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Add_New_Button="//a[@class='btn btn-primary']"
    Email="//input[@id='Email']"
    Password="//input[@id='Password']"
    First_name="//input[@id='FirstName']"
    Last_name="//input[@id='LastName']"
    Male="//input[@id='Gender_Male']"
    Female="//input[@id='Gender_Female']"
    Date_of_birth="//input[@id='DateOfBirth']"
    Company_name="//input[@id='Company']"
    Is_tax_exempt="//input[@id='IsTaxExempt']"
    Newsletter="//div[@class='k-widget k-multiselect k-multiselect-clearable k-state-hover k-state-focused k-state-border-down']//div[@role='listbox']"
    TestStore="//li[normalize-space()='Test store 2']"
    list_Customer_roles="/html[1]/body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"
    Moderators_Rol="//li[normalize-space()='Forum Moderators']"
    Guests_Rol="//li[normalize-space()='Guests']"
    Registered_Rol="//li[normalize-space()='Registered']"
    Vendor_Rol="//li[@id='8765f268-3cce-4e57-a666-d5e421d3d139']"
    Manager_of_vendor="//select[@id='VendorId']"
    Active="//input[@id='Active']"
    Admin_comment="//textarea[@id='AdminComment']"
    #save_button="//button[@name='save']"
    #driver = webdriver.Chrome(r'/Users/air2015/Downloads/chromedriver_mac64 (1)/chromedriver')


    txtcustomer_Roles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"

    def __init__(self, driver):
        self.driver = driver

    def go_To_Customer_page(self):
        self.driver.find_element(By.XPATH,customer_page.Customer_Menu).click()
        self.driver.find_element(By.XPATH,customer_page.Customer_Sub_Menu).click()
        self.driver.find_element(By.XPATH,customer_page.Add_New_Button).click()

    def setEmail(self,email):
                self.driver.find_element(By.XPATH,customer_page.Email).send_keys(email)

    def setPassword(self,password):
                self.driver.find_element(By.XPATH,customer_page.Password).send_keys(password)

    def setFirstName(self,firstName):
                self.driver.find_element(By.XPATH,customer_page.First_name).send_keys(firstName)
            
            
    def setLastName(self,LastName):
                self.driver.find_element(By.XPATH,customer_page.Last_name).send_keys(LastName)
            
    def setgander(self,gander):
                if gander=='mal':
                  self.driver.find_element(By.XPATH,customer_page.Male).click()
                elif gander=="femal":
                    self.driver.find_element(By.XPATH,customer_page.Female).click()
                else:
                    self.driver.find_element(By.XPATH,customer_page.Male).click()
  
             
    def setDatBirthDay(self,birthday):
                self.driver.find_element(By.XPATH,customer_page.Date_of_birth).send_keys(birthday)

    def setCompanyName(self,CompanyName):
                self.driver.find_element(By.XPATH,customer_page.Company_name).send_keys(CompanyName)

    def setIsTax(self):
                self.driver.find_element(By.XPATH,customer_page.Is_tax_exempt).click()

    #def setRole(self, role):
     #   self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
      #  elem = self.driver.find_element(By.XPATH,customer_page.list_Customer_roles)
       # if role == 'Registered' or role == 'Guests' or role == 'Vendors' or role == 'Forum Moderators' or role == 'Administrators':
        #    elem.clear()
         #   elem.send_keys(role)
          #  elem.send_keys(Keys.ENTER)
        #else:
         #   print("Invalid role provided.")


    
           

    def save(self):
            self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]").click()
            
  
                 
               
                 




      
  


