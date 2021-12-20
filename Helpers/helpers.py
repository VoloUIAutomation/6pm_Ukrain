import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import pathlib


def page_load(url, driver):
    driver.get(url)


def get_data(*keys):
    with open(f"{pathlib.Path(__file__).parent.parent.resolve()}\TestData\data.json", "r") as datafile:
        x = json.load(datafile)
    for k in keys:
        x = x[k]
    return x


def get_config(*keys):
    with open(f"{pathlib.Path(__file__).parent.resolve()}\config.json", "r") as datafile:
        x = json.load(datafile)
    for k in keys:
        x = x[k]
    return x


def wait_for_elements(element, driver):
    the_wait = webdriver.support.ui.WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(element))
    return the_wait


def wait_for_element(element, driver):
    the_wait = webdriver.support.ui.WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
    return the_wait


def hover_and_click(menuLocator, buttonLocator, driver):
    menu = wait_for_element(menuLocator, driver)
    the_chain = ActionChains(driver).move_to_element(
        menu).pause(1).click(driver.find_element(*buttonLocator))
    the_chain.perform()
