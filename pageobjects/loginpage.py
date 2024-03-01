import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ornageHRM_login:
    Text_username_XP=(By.XPATH,"//input[@placeholder='Username']")
    Text_password_XP=(By.XPATH,"//input[@placeholder='Password']")
    Click_on_login_XP=(By.CSS_SELECTOR,"button[type='submit']")
    Click_menu_xp=(By.XPATH,"//img[@class='oxd-userdropdown-img']")
    Click_on_logout_XP=(By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver=driver
        self.wait= WebDriverWait(self.driver,10)


    def Enter_username(self,uname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_username_XP))
        self.driver.find_element(*ornageHRM_login.Text_username_XP).send_keys(uname)


    def Enter_password(self,pas):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_password_XP))
        self.driver.find_element(*ornageHRM_login.Text_password_XP).send_keys(pas)


    def Click_login(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_on_login_XP))
        self.driver.find_element(*ornageHRM_login.Click_on_login_XP).click()



    def Click_menu(self):
        self.driver.find_element(*ornageHRM_login.Click_menu_xp).click()

    def Click_logout(self):
        self.driver.find_element(*ornageHRM_login.Click_on_logout_XP).click()

    def Login_status(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_menu_xp))
        try:
            self.driver.find_element(*ornageHRM_login.Click_menu_xp)

            return True
        except:
            return False




