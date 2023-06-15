@import time
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
    if check == "DATA":
        assert True, "Test Passed"

@given(u'Data section is visible')
def dataVisible(context):
    try:
        check = context.driver.find_element_by_xpath( "//h4[contains(text(),'Data')]").is_displayed();
    except:
        context.driver.close()
        print ("Collections not visible")
    if check == "COLLECTIONS":
        print("Collections visible")
    time.sleep(1)


@when(u'I click on browse data')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on browse data')


@when(u'I select the database "Sample Database"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the database "Sample Database"')


@when(u'click on new button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click on new button')


@when(u'I select new query')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select new query')


@when(u'I enter the new query "<query>"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter the new query "<query>"')


@when(u'i click on run icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i click on run icon')


@then(u'the query is executed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the query is executed')