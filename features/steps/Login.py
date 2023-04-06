
from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@when(u'clico em "Home"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico em "Home"')


@when(u'preencho "<email>" e "<senha>" e clico no botao "Login"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When preencho "<email>" e "<senha>" e clico no botao "Login"')


@then(u'vejo a mensagem de confirmacao')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then vejo a mensagem de confirmacao')
