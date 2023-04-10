from behave import when, then
from selenium import *
from selenium.webdriver.common.by import By
@when(u'clico em "check out our destination of the week"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'destination of the week! The Beach!').click()
    print('Passo 2: clicou no link do destino da semana')

@then(u'visualizo o destino da semana')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '//body/div[2]').text == 'Destination of the week: Hawaii !'
    assert context.driver.find_element(By.XPATH, '//body/div[2]/img[1]')