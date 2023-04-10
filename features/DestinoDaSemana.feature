@destino_da_semana
# Created by luiza at 10/04/2023
Feature: Destino da semana
  Scenario: Link do destino da semana OK
    Given que acesso o site Blazedemo
    When clico em "check out our destination of the week"
    Then visualizo o destino da semana