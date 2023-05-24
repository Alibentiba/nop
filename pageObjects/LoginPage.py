from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_page:
    # elements xpaths
    username_input = "//input[@id='Email']"
    passwors_input = "//input[@id='Password']"
    submit_button = "//button[@type='submit']"
    Logout_text = "//a[normalize-space()='Logout']"

    #     Action LMethods

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName):
        # self.driver=webdriver.Chrome()
        self.driver.find_element(By.XPATH, Login_page.username_input).clear()
        self.driver.find_element(By.XPATH, Login_page.username_input).send_keys(userName)

    def setPassword(self, Password):
        # self.driver = webdriver.Chrome()
        self.driver.find_element(By.XPATH, Login_page.passwors_input).clear()
        self.driver.find_element(By.XPATH, Login_page.passwors_input).send_keys(Password)

    def ClickSubmit(self):
        # self.driver = webdriver.Chrome()
        self.driver.find_element(By.XPATH, Login_page.submit_button).click()

    def ClickLogOut(self):
        # self.driver = webdriver.Chrome()
        self.driver.find_element(By.XPATH, Login_page.Logout_text).click()