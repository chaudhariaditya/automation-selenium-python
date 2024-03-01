import time
from lib2to3.pgen2 import driver

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageobjects.loginpage import ornageHRM_login

from pageobjects.add_employee import Add_Emp
from utilities.ReadConfig import Readconfig

class Test_Add_EMP:
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    First=Readconfig.GetFNAME()
    Middle=Readconfig.GetMNAME()
    Last=Readconfig.GetLNAME()
    # Path=Readconfig.GetImage()
    def test_add(self,setup):
         self.driver = setup
         self.lp = ornageHRM_login(self.driver)
         time.sleep(3)
         self.lp.Enter_username(self.username)
        # time.sleep(2)
         self.lp.Enter_password(self.password)
        # time.sleep(2)
         self.lp.Click_login()

         self.cick=Add_Emp(self.driver)
         self.cick.PIM_Click()
         self.ad=Add_Emp(self.driver)
         self.ad.Add()
         time.sleep(5)
         self.AE=Add_Emp(self.driver)
         self.AE.First_Name(self.First)
         time.sleep(5)
         self.AE.Middel_Name(self.Middle)
         time.sleep(3)
         self.AE.Last_Name(self.Last)
         time.sleep(2)
         # self.AE.Upload_Image(self.Path)
         # time.sleep(10)
         self.Save=Add_Emp(self.driver)
         # driver.implicitly_wait(10)
         self.Save.Click_Save()
