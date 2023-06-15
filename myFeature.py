import time
from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@given(u'Chrome Browser is Opened')
def OpenBrowser(context):
    context.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

@when(u'open url http://localhost:3000/')
def OpenUrl(context):
    context.driver.maximize_window()
    try:
        context.driver.get("http://localhost:3000/")
    except WebDriverException:
          context.driver.close()
          print("Cannot open metabase")
    time.sleep(1)

@when(u'enter email "{email}" and password "{pwd}" and click on login button')
def Login(context, email, pwd):
    context.driver.find_element(By.XPATH, '//*[@id="formField-username"]/div[2]/div/input').send_keys(email)
    context.driver.find_element(By.XPATH, '//*[@id="formField-password"]/div[2]/div/input').send_keys(pwd)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div/div[2]/div/form/div[4]/button/div').click()
    time.sleep(5)
    try:
        check = context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/aside/nav/div/div/ul/div/div').text
    except:
            context.driver.close()
            assert False, "Test Failed: invalid"
    if check == "DATA":
        assert True, "Test Passed"

@when(u'I click on settings icon')
def ClickSettings(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[2]/div[3]/div/div/button').click()

@when(u'I go to admin settings')
def ClickAdminSettings(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '/html/body/span[1]/span/div/div/div/ol/li[2]/a/div/span').click()


@when(u'I click on people')
def clickPeople(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/nav/div[2]/ul/li[4]/a').click()


@when(u'I click on groups')
def clickGroups(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[1]/ul/li[2]/a').click()


@when(u'I click on create a group button')
def groupButton(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/section/div/button/div/div').click()


@when(u'I enter name "{name}"')
def groupName(context, name):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/input').send_keys(name)


@when(u'I click on add button')
def clickAdd(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/table/tbody/tr[1]/td/div/button').click()


@then(u'the group with name "{name}" is created')
def verifyName(context, name):
    time.sleep(3)
    names = context.driver.find_elements(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/table/tbody')
    #if any(name in i.text for i in names):
    #    assert True, "Passed"
    #else:
    #    assert False, "Failed"
    assert any(name in i.text for i in names)
    return True, "Passed"


@when(u'I click on invite someone button')
def inviteSomeone(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/section[1]/div/a/button').click()


@when(u'I enter first name "{firstname}"')
def enterName(context, firstname):
    time.sleep(1)
    context.driver.find_element(By.XPATH,'//*[@id="formField-first_name"]/div[2]/div/input').send_keys(firstname)


@when(u'I enter first last name "{lastname}"')
def enterLastName(context, lastname):
    time.sleep(1)
    context.driver.find_element(By.XPATH,'//*[@id="formField-last_name"]/div[2]/div/input').send_keys(lastname)


@when(u'I enter email "{email}"')
def enterEmail(context, email):
    time.sleep(1)
    context.driver.find_element(By.XPATH,'//*[@id="formField-email"]/div[2]/div/input').send_keys(email)



@when(u'I click on create button')
def createButton(context):
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR,'body > div.ModalContainer > div > div > div > div > div > div.ModalBody.px4 > div > form > div.css-1rw7jxi.etf22zm0 > button.Button.Button.eyw0xx60.Button--primary.css-1sur1e6.emiw9oj2').click()
    time.sleep(3)

@then(u'the person with the name {firstName} is created')
def step_impl(context, firstname):
    time.sleep(3)
    names = context.driver.find_elements(By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div/section[2]/table')
    #if any(firstname in i.text for i in names):
    #    assert True, "Passed"
    #else:
    #    assert False, "Failed"
    assert any(firstname in i.text for i in names)
    return True,"Passed"
