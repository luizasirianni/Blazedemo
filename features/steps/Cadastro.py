from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By


@when(u'clico em "Register"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()
    print('Passo 3: Acessou a pagina de login e clicou em register')

@then(u'visualizo o formulario de cadastro')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, '//div[contains(text(),\'Register\')]')
    print('Passo 4: Acessou a pagina de registro')


@when(u'preencho os dados do cliente: "{name}", "{company}", "{email}", "{password}", "{confirmpassw}"')
def step_impl(context, name, company, email, password, confirmpassw):
    context.driver.find_element(By.ID, 'name').send_keys(name)
    context.driver.find_element(By.ID, 'company').send_keys(company)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'password-confirm').send_keys(confirmpassw)
    print('Passo 5: preencheu os dados')

@when(u'clico no botao \'Register\'')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[2]/form/div[6]/div/button').click()
    print('Passo 6: clicou no botao register')
@then(u'visualizo a pagina 419 page expired')
def step_impl(context):
    assert context.driver.find_element(By.CLASS_NAME, 'code').text == '419'
    assert context.driver.find_element(By.CLASS_NAME, 'message').text == 'Page Expired'
    print('Passo 7: visualizou a pagina 419')
