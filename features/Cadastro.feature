@Cadastro
# Created by luiza at 10/04/2023
Feature: Cadastro novo cliente
  Scenario Outline: Cadastro com sucesso
    Given que acesso o site Blazedemo
    When clico em "Home"
    And clico em "Register"
    Then visualizo o formulario de cadastro
    When preencho os dados do cliente: "<name>", "<company>", "<email>", "<password>", "<confirmpassw>"
    And clico no botao 'Register'
    Then visualizo a pagina 419 page expired

    Examples:
    |name           |company   |email          |password    |confirmpassw |
    |james bond     |Bond Ind. |jb@yahoo.com   |iamgreat123 |iamgreat123  |
    |scarlet        |Johansenn |sj@hotmail.com |blonde44    |blonde44     |
    |jennifer       |Aniston   |jenny@gmail.com|friends4ever|friends4ever |