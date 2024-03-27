# SPDX-License-Identifer: MIT

lista = [23, 30, 100, 89] 


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

def procura_pares(lista):
    """Procura o número par na lista usando procura linear."""
    par = []
    for item in lista:
        if item % 2 == 0 :
            par.append(item)
    return par


def procura_impares(lista):
    """Procura o número impar na lista usando procura linear."""
    impar = []
    for item in lista:
        if item % 2 != 0 :
            impar.append(item)
    return impar



print(procura_maior(lista))
print(procura_menor(lista))
print(procura_pares(lista))
print(procura_impares(lista))