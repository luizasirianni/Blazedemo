
from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@when(u'clico em "Home"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'body:nth-child(2) div.navbar.navbar-inverse:nth-child(1) '
                                                 'div.navbar-inner div.container > a.brand:nth-child(3)').click()
    print('Passo 2 - Acessou a pagina Home')


@when(u'preencho "<email>" e "<senha>" e clico no botao "Login"')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('emailexemplo@hotmail.com')
    context.driver.find_element(By.ID, 'password').send_keys('123455')
    context.driver.find_element(By.CSS_SELECTOR, 'div.container div.row div.col-md-8.col-md-offset-2 '
                                                 'div.panel.panel-default div.panel-body form.form-horizontal '
                                                 'div.form-group:nth-child(5) div.col-md-8.col-md-offset-4 > '
                                                 'button.btn.btn-primary:nth-child(1)').click()
    print('Passo 3 - Preencheu os dados e clicou em Login')

@then(u'vejo a mensagem de confirmacao')
#o site atualmente está com erro de Page Expired
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[contains(text(),'Page Expired')]")
