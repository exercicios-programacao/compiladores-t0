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
    menor = lista[0]

    for item in lista[1:]:
        if item < menor:
            menor = item

    return menor

def procura_impar(lista):
    elementos_impares = []

    for item in lista:
        if item % 2 != 0:
            elementos_impares.append(item)

    return elementos_impares


def procura_par(lista):
    elementos_pares = []

    for item in lista:
        if item % 2 == 0:
            elementos_pares.append(item)

    return elementos_pares