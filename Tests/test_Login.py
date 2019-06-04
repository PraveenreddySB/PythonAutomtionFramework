from selenium import webdriver
import time
import pytest
from PageObjects.test_loginpage import TestLoginPage
from PageObjects.test_homepage import TestHomepage
import xlrd
import xlwt
from TestData.test_XLUtility import TestXLUtility
import allure
from allure_commons.types import AttachmentType

@pytest.mark.usefixtures('test_setup')
class TestLogin:

    global path
    path="C://Users/pbangari/PycharmProjects/AutomationFramework/TestData/test_DataFile.xlsx"

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/pbangari/PycharmProjects/SeleniumFramework/Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://uat.admin.firstamericannavigator.com")
        allure.attach(driver.get_screenshot_as_png(), name="LoginScreen", attachment_type=AttachmentType.PNG)
        yield
        driver.close()
        driver.quit()

    allure.step('Verify the valid title is matched')
    def test_login_valid(self, test_setup):

        login = TestLoginPage(driver)

        rows = TestXLUtility.getRowCount(path,'ValidCredentials')

        for r in range(2,rows+1):
            username = TestXLUtility.readData(path,"ValidCredentials", r, 1)
            password = TestXLUtility.readData(path,"ValidCredentials", r, 2)

            login.enter_username(username)
            login.enter_password(password)
            login.click_login()
            time.sleep(10)

            homepage = TestHomepage(driver)

            if driver.title == "First American Navigator":
                print("Test is PASSED")
                allure.attach(driver.get_screenshot_as_png(),name="test_login_valid", attachment_type=AttachmentType.PNG)
                TestXLUtility.writeData(path,"ValidCredentials",r,3,"Test PASSED")
                homepage.verifylogoutlink()
            else:
                print("Test is FAILED")
                login.get_invalidmessage()
                TestXLUtility.writeData(path,"ValidCredentials",r,3,"Test is FAILED")

    allure.step('Verify the title is not matched')
    def test_login_invalid(self, test_setup):

        login = TestLoginPage(driver)

        rows = TestXLUtility.getRowCount(path, 'InvalidCredentials')

        for r in range(2, rows + 1):
            username = TestXLUtility.readData(path, "InvalidCredentials", r, 1)
            password = TestXLUtility.readData(path, "InvalidCredentials", r, 2)

            login.enter_username(username)
            login.enter_password(password)
            login.click_login()
            time.sleep(10)

            homepage = TestHomepage(driver)

            if driver.title == "First American Navigator":
                print("Test is PASSED")
                TestXLUtility.writeData(path, "InvalidCredentials", r, 3, "Test PASSED")
                allure.attach(driver.get_screenshot_as_png(),name="Screenshot", attachment_type=AttachmentType.PNG)
                homepage.verifylogoutlink()
            else:
                print("Test is FAILED")
                allure.attach(driver.get_screenshot_as_png(),name="Screenshot1", attachment_type=AttachmentType.PNG)
                login.get_invalidmessage()
                TestXLUtility.writeData(path, "InvalidCredentials", r, 3, "Test is FAILED")






