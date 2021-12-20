from Helpers import helpers
from selenium.webdriver.common.by import By


email_field = (By.XPATH, '//input[@type="email"]')
password_field = (By.XPATH, '//input[@type="password"]')
sign_in_button = (By.XPATH, '//input[@id="signInSubmit"]')

def sign_in(email, password, driver):
    helpers.wait_for_element(email_field, driver).send_keys(email)
    helpers.wait_for_element(password_field, driver).send_keys(password)
    helpers.wait_for_element(sign_in_button, driver).click()