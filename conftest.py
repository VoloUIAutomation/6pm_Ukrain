import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import json


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture
def test_data():
    with open(os.path.join(os.path.dirname(__file__), 'TestData', 'data.json')) as f:
        return json.load(f)


@pytest.fixture
def config_data():
    with open(os.path.join(os.path.dirname(__file__), 'TestData', 'config.json')) as f:
        return json.load(f)