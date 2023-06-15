import time
from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

@given(u'Chrome Browser is opened')
def openBrowser(context):
    context.driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')


@when(u'I open url http://localhost:3000/')
def openMetaBase(context):
    context.driver.maximize_window()
    try:
        context.driver.get("http://localhost:3000/")
    except WebDriverException:
        context.driver.close()
        print("Cannot Open Metabase")
    time.sleep(1)

@when(u'I Enter email {Email}')
def enterEmail(context, Email):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="formField-username"]/div[2]/div/input').send_keys(Email)
    except:
        print("Cannot write email")
    time.sleep(1)

@when(u'I Enter password {Password}')
def enterPass(context, Password):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="formField-password"]/div[2]/div/input').send_keys(Password)
    except:
        print("Cannot write pass")
    time.sleep(1)

@when(u'I click Login Button')
def button(context):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button').click()
    except:
        print("Cannot click button")
    time.sleep(4)

@then(u'I am logged in')
def loggedIn(context):
    try:
        check = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/nav/div/div/ul/div/div').text
    except:
        context.driver.close()
        assert False, "Test Failed, Invalid"
    #if check == "DATA":
     #   assert True, "Test Passed"
     assert check == "DATA"
     return True, "Test Passed"

@given(u'Collections section is visible')
def collectionVisible(context):
    try:
        check = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/nav/div/div/div[2]/div/h4').text
    except:
        context.driver.close()
        print ("Collections not visible")
    if check == "COLLECTIONS":
        print("Collections visible")
    time.sleep(1)


@when(u'I Click menu button')
def clickMenu(context):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/nav/div/div/div[2]/div/button').click()
    except:
        print("Cannot click collections button")
    time.sleep(2)


@when(u'I click new collection')
def clickNewCollection(context):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="tippy-4"]/div/div/div/div/ul/li[1]/button').click()
    except:
        print("Cannot click new collection button")
    time.sleep(2)


@when(u'I Enter name {name}')
def enterName(context, name):
    try:
        context.driver.find_element(By.XPATH, '// *[ @ id = "formField-name"] / div[2] / div / input').send_keys(name)
    except:
        print("Cannot write name")
    time.sleep(1)


@when(u'I Enter Description {description}')
def enterDescription(context, description):
    try:
        context.driver.find_element(By.XPATH, '//*[@id="formField-description"]/div[2]/textarea').send_keys(description)
    except:
        print("Cannot write description")
    time.sleep(1)


@when(u'I Click create button')
def clickCreate(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, 'body > div.ModalContainer > div > div > div > div > div > div.ModalBody.px4 > div > form > div.css-1rw7jxi.etf22zm0 > button:nth-child(1)').click()
    except:
        print("Cannot click create button")
    time.sleep(3)


@then(u'New collection is added')
def collectionAdded(context):
    try:
        check = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div/div[3]/div/div[1]').text
    except:
        context.driver.close()
        print("Collections not added")
    assert (check == "This collection is empty":)
    return print("Collections visible")
    time.sleep(1)
