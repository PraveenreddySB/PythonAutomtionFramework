class TestLoginPage:
#test
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "ctl00_cpMain_UcLogin1_LoginC_UserName"
        self.password_textbox_id = "ctl00_cpMain_UcLogin1_LoginC_Password"
        self.login_button_id = "ctl00_cpMain_UcLogin1_LoginC_cmdSubmit"
        self.login_errormessage_id = "ctl00_cpMain_UcLogin1_LoginC_lblError"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def get_invalidmessage(self):
        if self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again.":
            print("Invalid test case is PASSED")
            assert self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again."
        else:
            print("Invalid test case is FAILED")
            assert self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again."







