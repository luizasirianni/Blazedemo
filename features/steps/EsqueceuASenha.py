from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
@when(u'clico em "Forgot your password"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Forgot Your Password?').click()
    print('passo 3 - clicou no botao forgot your password')
@then(u'sou direcionado a pagina de "Reset password"')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[contains(text(),'Reset Password')]")


@when(u'preencho o "{email}" e clico em "send password reset link"')
def step_impl(context, email):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.CSS_SELECTOR, '#app > div > div > div > div > div.panel-body > '
                                                 'form > div:nth-child(3) > div > button').click()
