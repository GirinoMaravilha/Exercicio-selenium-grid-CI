from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


GRID_URL = "http://localhost:4444/wd/hub"


@pytest.fixture
def driver():

    opcoes = ChromeOptions()
    opcoes.add_argument("--headless")
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(command_executor=GRID_URL, options=opcoes)
    yield driver
    driver.quit()

