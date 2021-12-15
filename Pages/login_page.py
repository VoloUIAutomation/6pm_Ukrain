from Pages.base_page import *

LOCATOR_EMAIL_INPUT = ()
LOCATOR_PSW_INPUT = ()
LOCATOR_SIGN_IN_BTN = ()


class LoginPageHelper(BasePageHelper):

    def login(self, email, psw):
        self.find_element(self.driver, LOCATOR_EMAIL_INPUT).send_keys(email)
        self.find_element(self.driver, LOCATOR_PSW_INPUT).send_keys(psw)
        self.find_element(self.driver, LOCATOR_SIGN_IN_BTN).click()