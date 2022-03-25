import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.Advantage_Shopping_Cart_url)

    if driver.current_url == locators.Advantage_Shopping_Cart_url and locators.Advantage_Shopping_home_page_title in driver.title:
        print('Bravo! Website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application and try again!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


setUp()
tearDown()

