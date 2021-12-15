from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator):
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator),
                                          message=f"Can't find element by locator {locator}")


def find_elements(driver, locator):
    return WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(locator),
                                          message=f"Can't find elements by locator {locator}")


def check_elem_doesnt_present(driver, locator):
    return WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(locator),
                                          message=f"Element is present and visible by locator: {locator}")
