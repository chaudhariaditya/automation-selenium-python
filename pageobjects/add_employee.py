from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_Emp:
    Click_PIM_XP=(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    Click_Add_button_Xp=(By.XPATH,"//button[normalize-space()='Add']")
    Enter_Emp_FName_XP=(By.XPATH,"//input[@placeholder='First Name']")
    Enter_Emp_MName_XP = (By.XPATH, "//input[@placeholder='Middle Name']")
    Enter_Emp_LName_XP = (By.XPATH, "//input[@placeholder='Last Name']")
    Upload_Image_XP=(By.XPATH,"//img[@class='employee-image']")
    Click_Save_button_Xp=(By.XPATH,"//button[@type='submit']")



    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)



    def PIM_Click(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_PIM_XP))
        self.driver.find_element(*Add_Emp.Click_PIM_XP).click()
    def Add(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Add_button_Xp))
        self.driver.find_element(*Add_Emp.Click_Add_button_Xp).click()


    def First_Name(self,Fname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Enter_Emp_FName_XP))

        self.driver.find_element(*Add_Emp.Enter_Emp_FName_XP).send_keys(Fname)


    def Middel_Name(self,Mname):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Enter_Emp_MName_XP))
        self.driver.find_element(*Add_Emp.Enter_Emp_MName_XP).send_keys(Mname)


    def Last_Name(self,Lname):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.Enter_Emp_LName_XP))
        self.driver.find_element(*Add_Emp.Enter_Emp_LName_XP).send_keys(Lname)


    def Upload_Image(self,path):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Upload_Image_XP))
        self.driver.find_element(*Add_Emp.Upload_Image_XP).click().send_keys(path)


    def Click_Save(self):

        self.driver.find_element(*Add_Emp.Click_Save_button_Xp).click()

