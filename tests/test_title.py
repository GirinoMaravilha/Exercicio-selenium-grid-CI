"""

Docstring do módulo de teste

"""


from selenium import webdriver
from selenium.webdriver.chrome import options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as Ac
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import time


def test_titulo_uol(driver:WebDriver):

    url = "https://www.uol.com.br"
    driver.get(url)
    resp = driver.title
    assert "uol" in resp.lower()


def test_titulo_cnn(driver:WebDriver):

    url = "https://www.cnnbrasil.com.br/"
    driver.get(url)
    assert "CNN" in driver.title


def test_imagem_himiko(driver:WebDriver):
    
    url = "https://br.pinterest.com/pin/52143308181266866/" 
    
    driver.get(url)
    time.sleep(5)
    img = driver.find_element(By.XPATH,"//div[@data-test-id='pin-closeup-image'] //img")
    print(img.get_attribute('src'))
    assert img is not None


def test_imagem_lucy(driver:WebDriver):

    url = "https://br.pinterest.com/pin/110338259620568720/"

    driver.get(url)
    time.sleep(5)
    img = driver.find_element(By.XPATH,"//div[@data-test-id='pin-closeup-image'] //img")
    print(img.get_attribute('src'))
    assert img is not None