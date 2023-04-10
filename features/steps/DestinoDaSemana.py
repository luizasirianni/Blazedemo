from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
@when(u'clico em "check out our destination of the week"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'destination of the week! The Beach!').click()
    print('Passo 2: clicou no link do destino da semana')

@then(u'visualizo o destino da semana')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '//body/div[2]').text == 'Destination of the week: Hawaii !'
    print('Passo 3.1: Visualizo o nome do destino')
    assert context.driver.find_element(By.XPATH, '/html/body/div[2]/img').get_attribute('src') == 'https://www.blazedemo.com/assets/vacation.jpg'
    print('Passo 3.2: Visualizo a imagem do destino')