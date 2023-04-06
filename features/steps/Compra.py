import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# context = variavel global q se utiliza pra comunicar os dados entre os módulos do behave

#método executado antes da feature para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            #podem ser incluídas outras ações ...
        )
@given(u'que acesso o site Blazedemo')
@given(u'que acesso o portal Blazedemo') #esse bloco vai acessar o endereço por qualquer uma dessas chamadas
def step_impl(context):
    context.driver.get('https://www.blazedemo.com/')
    print('Passo 1 - Acessou o site Blazedemo')
''''''
@when(u'seleciono a cidade "Sao Paolo" na cidade de origem')
def step_impl(context):
    #Mapear o dropdown (combo)
    dropdown_from = context.driver.find_element(By.NAME, 'fromPort')
    #Cria um objeto para permitir selecionar as opções
    objeto_origem = Select(dropdown_from)
    #Seleciona o elemento no dropdown
    objeto_origem.select_by_value('São Paolo')
    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade "Rome" na cidade de destino')
def step_impl(context):
    dropdown_to = context.driver.find_element(By.NAME, 'toPort')
    Select(dropdown_to).select_by_value('Rome')
    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico no botao "Find Flights"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'body > div.container > form > div > input').click()
    print('Passo 4 - Apertou o botão Find Flights')

@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    #assert context.driver.find_element(By.TAG_NAME, 'h3').text() == 'Flights from São Paolo to Rome: '
    assert context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/h3[1]').text == 'Flights from São Paolo to Rome:'
    print('Passo 5 - Foi direcionado para a página de seleção de voos')

@when(u'seleciono o primeiro voo')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr[1]/td[1]/input').click()
    print('Passo 5 - Foi selecionado o primeiro voo da lista')

@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(),'Your flight from TLV to SFO has been reserved.')]")
    print('Passo 6 - Foi direcionado para a página de pagamento')

@when(u'preencho os dados para pagamento')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('James Bond')
    context.driver.find_element(By.ID, 'address').send_keys('Avenida Brasil 123')
    context.driver.find_element(By.ID, 'city').send_keys('Miami')
    context.driver.find_element(By.ID, 'state').send_keys('Florida')
    context.driver.find_element(By.ID, 'zipCode').send_keys('1234567')
    card = context.driver.find_element(By.ID, 'cardType')
    Select(card).select_by_index(1)
    context.driver.find_element(By.ID, 'creditCardNumber').send_keys('5999477789991555')
    context.driver.find_element(By.ID, 'creditCardMonth').send_keys('10')
    context.driver.find_element(By.ID, 'creditCardYear').send_keys('2027')
    context.driver.find_element(By.ID, 'nameOnCard').send_keys('James Bond')
    print('Passo 7 - Foi preenchido os dados para pagamento')

@when(u'clico no botao "Purchase Flight"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'body > div.container > form > div:nth-child(12) > div > input').click()
    print('Passo 8 - Clicou no botão Purchase Flight')

@then(u'sou direcionado a pagina de confirmacao')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1[contains(text(),'Thank you for your purchase today!')]")
    print('Passo 9 - Foi direcionado a pagina de confirmação de compra')

@when(u'seleciono de "Sao Paolo" para "Rome"')
def step_impl(context):

    dropdown_from = context.driver.find_element(By.NAME, 'fromPort')
    objeto_origem = Select(dropdown_from)
    objeto_origem.select_by_value('São Paolo')

    dropdown_to = context.driver.find_element(By.NAME, 'toPort')
    Select(dropdown_to).select_by_value('Rome')

    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

    print('Passo 2(C) - Selecionou a cidade de origem e destino')
