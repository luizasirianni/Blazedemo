@compra_passagem
  # descrição da funcionalidade:
Feature: Compra de passagem aerea
  # cenários de teste E2E - end to end
  # para cada feature temos scenarios (test scenarios)
  Scenario: Trecho de Sao Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciono a cidade "São Paolo" na cidade de origem
    And seleciono a cidade "Rome" na cidade de destino
    And clico no botao "Find Flights"
    Then sou direcionado para a pagina de selecao de voos de "<origem>" para "<destino>"
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao "Purchase Flight"
    Then sou direcionado a pagina de confirmacao

  Scenario: Trecho de Sao Paulo a Roma Compacto
    Given que acesso o site Blazedemo
    When seleciono de "São Paolo" para "Rome"
    Then sou direcionado para a pagina de selecao de voos de "<origem>" para "<destino>"
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao "Purchase Flight"
    Then sou direcionado a pagina de confirmacao

  Scenario Outline: De origem a destino
    Given que acesso o site Blazedemo
    When seleciono de "<origem>" para "<destino>"
    Then sou direcionado para a pagina de selecao de voos de "<origem>" para "<destino>"
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados para pagamento
    And clico no botao "Purchase Flight"
    Then sou direcionado a pagina de confirmacao

    Examples:
      | origem       | destino      |
      | Philadelphia | Buenos Aires |
      | Mexico City  | Cairo        |
      | Paris        | London       |
      | San Diego    | Berlin       |
      | Portland     | New York     |