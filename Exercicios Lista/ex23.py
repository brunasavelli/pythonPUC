# def inversao(lista):
#     primeiro_numero_da_lista = 0
#     ultimo_numero_da_lista = len(lista) - 1

#     while primeiro_numero_da_lista < ultimo_numero_da_lista:
#         lista[primeiro_numero_da_lista], lista[ultimo_numero_da_lista] = lista[ultimo_numero_da_lista], lista[primeiro_numero_da_lista]

#         primeiro_numero_da_lista += 1
#         ultimo_numero_da_lista -= 1
#     return lista
# minha_lista = [2,8,0]
# print(inversao(minha_lista))

#################### CORREÇÃO MALIGNO ####################
def inversao(L):
    posicao_inicio = 0
    posiciao_final = len(L) - 1

    while posicao_inicio < posiciao_final:
        backup = L[posicao_inicio]
        L[posicao_inicio] = L[posiciao_final]
        L[posiciao_final] = backup
        posicao_inicio += 1
        posiciao_final -= 1

    return L

print(inversao([2, 4, 6]))



