import time
from lib2to3.pgen2 import driver

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


from pageobjects.loginpage import ornageHRM_login

from utilities.ReadConfig import Readconfig

class Test_login:


    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    def test_titel01(self,setup):
         self.driver=setup

         if self.driver.title == "OrangeHRM":
             time.sleep(3)
             allure.attach(self.driver.get_screenshot_as_png(),name="first", attachment_type= AttachmentType.PNG)

             self.driver.save_screenshot("D:\\class\\orangeHRM\\screenshots\\pass.png")
             assert True
         else:
             time.sleep(3)
             self.driver.save_screenshot("D:\\class\\orangeHRM\\screenshots\\fail.png")

             assert False
    def test_login02(self,setup):
         self.driver=setup
         self.lp=ornageHRM_login(self.driver)
         time.sleep(3)
         self.lp.Enter_username(self.username)
         # time.sleep(2)
         self.lp.Enter_password(self.password)
         # time.sleep(2)
         self.lp.Click_login()
         # time.sleep(2)
         if self.lp.Login_status() == True:
             assert True
             time.sleep(2)
             self.lp.Click_menu()
             self.lp.Click_logout()
         else:
             assert False
         # yield driver
         # driver.quit()










