'''
Escreva uma função em Python que resulte a posição mais a direita de uma dada subcadeia 
em uma cadeia de caracteres fornecida. Faça um programa em Python para testar sua função
'''

def posicao_direita(cadeia, subcadeia):
    posicao = -1
    for i in range(len(cadeia) - len(subcadeia) + 1):      ## Percorre a cadeia até o ponto onde a subcadeia pode caber 
        for j in range(len(subcadeia)):                    ## Verifica se a subcadeia corresponde à parte da cadeia atual
            if cadeia[i + j] != subcadeia[j]:              ## Se não corresponder, sai do loop interno
                break                                      ## Se o loop interno terminou sem interrupção, significa que encontramos a subcadeia
        else:                                              ## O loop interno terminou sem interrupção, o que significa que encontramos a subcadeia
            posicao = i                                    ## Atualiza a posição mais à direita encontrada
    return posicao                                         ## Retorna a posição mais à direita da subcadeia encontrada, ou -1 se não for encontrada

print(posicao_direita("abcPUCdePUCfghiPUCjk", "PUC"))
