from Pages.base_page import *
from selenium.webdriver.common.by import By

LOCATOR_EMAIL_INPUT = (By.ID, 'ap_email')
LOCATOR_PSW_INPUT = (By.ID, 'ap_password')
LOCATOR_SIGN_IN_BTN = (By.ID, 'signInSubmit')
LOCATOR_SIGNED_MESSAGE = (By.XPATH, '//div/h2[text()="Your Primary Account Information"]')


class LoginPageHelper(BasePageHelper):

    def login(self, email, psw):
        self.find_element(self.driver, LOCATOR_EMAIL_INPUT).send_keys(email)
        self.find_element(self.driver, LOCATOR_PSW_INPUT).send_keys(psw)
        self.find_element(self.driver, LOCATOR_SIGN_IN_BTN).click()
        self.find_element(self.driver, LOCATOR_SIGNED_MESSAGE)
