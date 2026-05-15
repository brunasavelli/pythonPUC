#################### ATIVIDADE DE AULA 01 ####################
def discMaiorNota(L):
    posicao_maior_nota = 0
    posicao_atual = 1

    while posicao_atual<len(L):
        if L[posicao_atual][1] > L[posicao_maior_nota][1]: posicao_maior_nota = posicao_atual
        posicao_atual += 1
    
    return L[posicao_maior_nota][0]

#################### ATIVIDADE DE AULA 02 ####################
def media_das_notas(L):
    if len(L) == 0:
        return None
    else:
        soma = 0
        posicao = 0
        while posicao < len(L):
            soma += L[posicao][1]
            posicao += 1
        return soma / len(L)

lista=[["APPC", 7.5, 0.75], ["EPBD", 8.0, 0.85], ["TEO", 5.0, 0.95]]
print(discMaiorNota(lista))
print(media_das_notas(lista))