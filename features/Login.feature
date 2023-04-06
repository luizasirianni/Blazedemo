@Login
Feature: Login
  Scenario: Login com sucesso
    Given que acesso o site Blazedemo
    When clico em "Home"
    And preencho "<email>" e "<senha>" e clico no botao "Login"
    Then vejo a mensagem de confirmacao
