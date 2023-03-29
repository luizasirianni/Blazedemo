import time

from behave import given, when, then
from selenium import webdriver
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
def step_impl(context):
    context.driver.get('https://www.blazedemo.com/')
    print('Passo 1 - Acessou o site Blazedemo')

@when(u'seleciono a cidade "Sao Paolo" na cidade de origem')
def step_impl(context):
    #Mapear o dropdown (combo)
    dropdown_from = context.driver.find_element(By.NAME, 'fromPort')
    print('Passo 2 - Selecionou a cidade de origem')

    #Cria um objeto para permitir selecionar as opções
    objeto_origem = Select(dropdown_from)

    #Seleciona o elemento no dropdown
    objeto_origem.select_by_value('São Paolo')

@when(u'seleciono a cidade "Rome" na cidade de destino')
def step_impl(context):
    dropdown_to = context.driver.find_element(By.NAME, 'toPort')
    to = Select(dropdown_to).select_by_value('Rome')
    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico no botao "Find Flights"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'body > div.container > form > div > input').click()
    print('Passo 4 - Apertou o botão Find Flights')

@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    titulo = context.driver.find_element(By.CSS_SELECTOR, 'body > div.container')
    assert titulo.text == 'Flights from São Paolo to Buenos Aires: '
    print('Passo 5 - Foi direcionado para a página de seleção de voos')

@when(u'seleciono o primeiro voo')
def step_impl(context):
    print('Passo 5 - Foi selecionado o primeiro voo da lista')

@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    print('Passo 6 - Foi direcionado para a página de pagamento')

@when(u'preencho os dados para pagamento')
def step_impl(context):
    print('Passo 7 - Foi preenchido os dados para pagamento')

@when(u'clico no botao "Purchase Flight"')
def step_impl(context):
    print('Passo 8 - Clicou no botão Purchase Flight')

@then(u'sou direcionado a pagina de confirmacao')
def step_impl(context):
    print('Passo 9 - Foi direcionado a pagina de confirmação de compra')

@when(u'seleciono de "Sao Paolo" para "Rome"')
def step_impl(context):
    print('Passo 2(C) - Selecionou a cidade de origem e destino')