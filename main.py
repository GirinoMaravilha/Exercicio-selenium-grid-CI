from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException


class ChromeRemoteDriver():
    
    def __init__(self,browser:str):
        
        self._caps = {

            "browserName":f"{browser}",
            "browserVersion":"stable",
            "selenoid:options":{}

        }

        self.GRID_URL = "http://localhost:4444"

        self.driver = ""
    
    def __enter__(self):

        opcoes = ChromeOptions()
        opcoes.add_argument("--headless")
        self.driver = webdriver.Remote(command_executor=f"{self.GRID_URL}/wd/hub", options=opcoes)
        return self.driver

    def __exit__(self, exc_type, exc, tb):

        self.driver.quit()


def main():
    
    d = ChromeRemoteDriver("Chrome")
    with d as driver:
        driver.get("https://www.uol.com.br")
        print(driver.title)



if __name__ == "__main__":
    main()
        


     