# SPDX-License-Identifer: MIT

"""Implementação do exercício zero."""

numeros = [6, 34, 23, 2, 54, 49, 12, 5, 8, 63]

def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior

def procura_menor(lista):
    """Procura menor item na lista usando procura linear."""
    menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item
    return menor

def procura_impares(lista):
    """Procura numeros impares na lista."""
    impar = []
    for item in lista[0:]:
        if item % 2 == 1:
            impar.append(item)
    return impar

def procura_pares(lista):
    """Procura numeros impares na lista."""
    par = []
    for item in lista[0:]:
        if item % 2 == 0:
            par.append(item)
    return par

print('O maior número é:', procura_maior(numeros))

print('O menor número é:', procura_menor(numeros))

print('Os números ímpares são:', procura_impares(numeros))

print('Os números pares são:', procura_pares(numeros))