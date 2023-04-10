@esqueceu_a_senha
# Created by luiza at 10/04/2023
Feature: Esqueceu a senha

  Scenario Outline: Usuario com cadastro
    Given que acesso o site Blazedemo
    When clico em "Home"
    And clico em "Forgot your password"
    Then sou direcionado a pagina de "Reset password"
    When preencho o "<email>" e clico em "send password reset link"
    Then visualizo a pagina 419 page expired
    Examples:
    | email             |
    | abc@yahoo.com     |
    | efg@gmail.com     |
    | kijh@hotmail.com  |