#################### ATIVIDADE DE AULA 01 ####################
# def discMaiorNota(L):
#     posicao_maior_nota = 0
#     posicao_atual = 1

#     while posicao_atual<len(L):
#         if L[posicao_atual][1] > L[posicao_maior_nota][1]: posicao_maior_nota = posicao_atual
#         posicao_atual += 1
    
#     return L[posicao_maior_nota][0]

# lista=[["APPC", 7.5, 0.75], ["EPBD", 8.0, 0.85], ["TEO", 5.0, 0.95]]
# print(discMaiorNota(lista))


#################### ATIVIDADE DE AULA 02 ####################
def media_das_notas(L):
    media_listinha1 = (L[0][1] + L[0][2]) / 2
    media_listinha2 = (L[1][1] + L[1][2]) / 2
    media_listinha3 = (L[2][1] + L[2][2]) / 2

    media_total = (media_listinha1 + media_listinha2 + media_listinha3) / 3

    return media_total

lista=[["APPC", 7.5, 0.75], ["EPBD", 8.0, 0.85], ["TEO", 5.0, 0.95]]
print(media_das_notas(lista))