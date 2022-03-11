# AvaliacaoTecnicaPython
Avaliação Técnica em Python (versão 3.10.2) desenvolvida por Giulia Rossatto Rocha.

As respostas da avaliação se encontram em *avaliacao_env/scripts_respostas/*.
A pasta avaliacao_env corresponde a um ambiente virtual criado com o módulo -venv.

## Questão 1:
### Escreva um script Python que recebe como parametro um número n inteiro positivo e imprime no console o n-ésimo valor correspondente da sequencia de Fibonacci.
### Obs.: O problema deve ser resolvido utilizando recursão.

O script que contém a resposta corresponde a **fibonacci_questao1.py** disponível em *avaliacao_env/scripts_respostas/*.

O script recebe a entrada pelo terminal (número n) e calcula o n-ésimo valor correspondente a sequência de fibonacci. Para o cálculo do valor utilizou-se uma função recursiva que realiza outras chamadas da própria função para calcular termos anteriores. Essas chamadas são empilhadas e desempilhadas calculando os termos até atingir 0 e 1 (valores iniciais da sequência).

Exemplo para executá-lo:
> python fibonacci_questao1.py 9

Saída:
> 34

## Questão 2:
### Explique o problema que poderia acontecer com o programa desenvolvido na questão 1 ao passar como entrada n = 50.

A resposta corresponde a questão se encontra em um arquivo texto em **questao2.txt** disponível em *avaliacao_env/scripts_respostas/*.

## Questão 3:
### Utilizando a biblioteca requests do Python, crie um programa que consuma a API https://swapi.dev/ (Star Wars).
### O programa deve:
### - Consultar quais personagens (people) aparecem em 4 filmes ou mais.
### - Consultar quais planetas possuem 5 moradores (residents) ou mais.
### - Escrever os dados encontrados em arquivos JSON na raiz do projeto.

O script que contém a resposta corresponde a **starWars_questao3.py** disponível em *avaliacao_env/Scripts/scripts_questoes/*.

Para realizar a requisição utilizou-se a biblioteca *requests* do Python que oferece a maioria das funcionalidades do protocolo HTTP. As requisições foram feitas a API https://swapi.dev/ que retornaram arquivos JSON. Estes arquivos foram manipulados e as respostas foram armazenadas em outro aquivo JSON denominado 'respostas.json'.

Exemplo para executá-lo:
> python starWars_questao3.py

Saída: criação de um arquivo JSON com as respostas (respostas.json)
