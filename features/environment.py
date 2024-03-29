import time
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configReader
from selenium.webdriver.chrome.service import Service


def before_scenario(context, driver):
    if configReader.readConfig("basic info","browser") == "chrome":
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service)
        context.driver.maximize_window()
        time.sleep(2)
    if configReader.readConfig("basic info","browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
