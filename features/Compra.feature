  # descrição da funcionalidade:
Feature: Compra de passagem aerea
  # cenários de teste E2E - end to end
  Scenario: Trecho de Sao Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciono a cidade "Sao Paolo" na cidade de origem
    And seleciono a cidade "Rome" na cidade de destino
    And clico no botao "Find Flights"
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao "Purchase Flight"
    Then sou direcionado a pagina de confirmacao

  Scenario: Trecho de Sao Paulo a Roma Compacto
    Given que acesso o site Blazedemo
    When seleciono de "Sao Paolo" para "Rome"
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao "Purchase Flight"
    Then sou direcionado a pagina de confirmacao