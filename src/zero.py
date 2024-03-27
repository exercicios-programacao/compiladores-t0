# SPDX-License-Identifer: MIT

"""Implementação do exercício zero."""

def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior

def procura_menor(lista):
    # """Procura o menor item na lista."""
    menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item
    
    return menor

def procura_impares(lista):
       # """Retorna os numeros impares de uma lista, utilizando a expressao 
       # lambda que verifica se o numero é impar com os parametros x: x % 2 != 0 """
    return list(filter(lambda x: x % 2 != 0, lista))

def procura_pares(lista):
       # """Retorna os numeros impares de uma lista, utilizando a expressao 
       # lambda que verifica se o numero é pares com os parametros x: x % 2 == 0 """
    return list(filter(lambda x: x % 2 == 0, lista))
