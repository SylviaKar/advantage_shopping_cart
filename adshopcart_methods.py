from typing import Any

import datetime
from time import sleep
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select  # <--- add this import for drop down lists
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
#

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


def tearDown():
    if driver is not None:
        print(f'-------------------------~*~--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


def sign_up():
    print(f'-------------------------~*~--------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, 'a.create-new-account').click()
    sleep(1.5)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenum1)
    sleep(0.5)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.5)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.5)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.5)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.5)
    print(f'*** New account is successfully created. ***')

def check_full_name():
    print(f'-------------------------~*~--------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_account"]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
        sleep(0.5)
        print(f'--- {locators.full_name} is found.---')
    else:
        print(f"Something went wrong, please check your code and try again.")
    sleep(0.25)

def check_orders():
    print(f'-------------------------~*~--------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(0.5)

    assert driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    sleep(0.5)
    no_order = driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    if no_order == True:
        print(f"---No orders placed.---")
    else:
        print(f'Something went wrong, please check your code.')


def log_out():
    print(f'-------------------------~*~--------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="Sign_out"]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, '//span[contains(@class,"containMiniTitle")]').text == '':
        sleep(0.5)
        print(f' user {locators.new_username} is signed out successfully')
    else:
        sleep(0.5)
        print(f' user {locators.new_username} is not signed out successfully')
    sleep(2)


def log_in():
    print(f'-----------------------------------------------------')
    if driver.current_url == locators.Advantage_Shopping_Cart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(0.5)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.5)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)
        print(f' --- Login is successful. {locators.app}. ')
    else:
        print('Please check your code and try again.')


def delete_test_account():
    print(f'------------------DELETE---------------------')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(2)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(0.5)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(1)
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(2.5)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
    sleep(1.5)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(1.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    if driver.find_element(By.ID, 'signInResultMessage').is_displayed():
        print(f'incorrect username and password is displayed!')
        print(f'---Test passed and account successfully deleted-----')
    else:
        print(f'Something went wrong.')


# setUp()
# sign_up()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# tearDown()