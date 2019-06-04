class TestHomepage:

    def __init__(self, driver):
        self.driver = driver

        self.Logout_link_id = "ctl00_HozMenu1_ucLogout_cmdLogout"

    def verifylogoutlink(self):
        self.driver.find_element_by_id(self.Logout_link_id).click()




