import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver


# def pytest_metadata(metadata):
#     metadata["Project Name"] = "sucedemo"
#     metadata["Enivorment"] = "QA"
#     metadata["Tester"] = "Aditya"
