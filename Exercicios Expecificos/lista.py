'''
Implemente duas novas opções, uma para contar quantas vezes aparece
na lista o número dado, e outra para ordernar os números da lista
pelo Método da Bolha (bubble sort).

Método da Bolha:
pega os dois primeiros e vê se eles estão em order, se não estão, troca
    backup=lista[posicao] # guarda o valor do primeiro elemento na váriavel backup
    lista[posicao]=lista[posicao+1] # substitui o valor do primeiro elemento pelo valor do segundo elemento
    lista[posicao+1]=backup # substitui o valor do segundo elemento pelo valor guardado na variável backup, que é o valor do primeiro elemento

caso ainda não estaja ordenada, pega os próximos dois elementos e repete o processo, e assim por diante, até chegar no final da lista. 
Depois disso, volta para o começo da lista e repete o processo até chegar no final da lista novamente, e assim por diante, até que a lista esteja ordenada.
'''

def opcao_escolhida ():
    print("1) Esvaziar a lista")
    print("2) Incluir número na lista")
    print("3) Excluir número dando o número")
    print("4) Excluir número dando sua posição")
    print("5) Mostrar a lista")
    print("6) Somar tudo da lista")
    print("7) Achar o menor")
    print("8) Achar o maior")
    print("9) Sair do programa")
    
    chave_para_escolher_opcao_ate_acertar_ligada = True
    while chave_para_escolher_opcao_ate_acertar_ligada:
        try:
            opcao = int(input("Opcao? "))
        except ValueError:
            print("Opção inválida; tente novamente!")
        else:
            if opcao < 1 or opcao > 9:
                print("Opção inválida; tente novamente!")
            else:
                chave_para_escolher_opcao_ate_acertar_ligada = False

    return opcao

def esvazia_lista (lista):
    lista.clear()
    print("Esvaziamento realizado com sucesso!")

def numero_digitado (proposito, aceitavel):
    chave_para_digitar_um_numero_ate_acertar_ligada = True
    while chave_para_digitar_um_numero_ate_acertar_ligada:
        try:
            numero = float(input("Qual número deseja " + proposito + "? "))
        except ValueError:
            print("Foi pedido um número para ", proposito, "; tente novamente!", sep="")
        else:
            # a ordem dessas condições é importante, nesse caso, se fosse o contrário, iria dar errado.
            if aceitavel != None and numero not in aceitavel:
                print("Número inaceitável para ", proposito, "; tente novamente!", sep="")
            else:
                chave_para_digitar_um_numero_ate_acertar_ligada = False
    return numero


def incluir_numero (lista):
    numero=numero_digitado(proposito="incluir", aceitavel=None)
    lista.append(numero)
    print("Número incluido com sucesso!")

def excluir_numero_dado_o_numero(lista):
    numero=numero_digitado(proposito="excluir", aceitavel=lista)
    if numero in lista:
        lista.remove(numero)
        print("Número excluido com sucesso!")
    else:
        print("Esse número não existe na lista.")

def excluir_numero_dada_a_posicao(lista):
    chave_para_digitar_uma_posicao_ate_acertar_ligada = True
    while chave_para_digitar_uma_posicao_ate_acertar_ligada:
        try: 
            posicao = int(input("Qual posição deseja excluir? "))
        except ValueError:
            print("Foi pedido uma posição; elas devem ser núemeros inteiros; tente novamente", sep="")
        else:
            if posicao < 0 or posicao >=len(lista):
                print("Número inaceitável; tente novamente!", sep="")
            else:
                chave_para_digitar_uma_posicao_ate_acertar_ligada = False
    del lista[posicao]
    print("Número na posição desejada excluido com sucesso!")

def soma (lista):
    resultado=0
    posicao=0
    while posicao<len(lista):
        # pega cada resultado da lista e soma na variavel 'resultado' até chegar no final da lista (tamanho da lista)
        resultado+=lista[posicao]
        posicao+=1
    return resultado

def mostrar_soma (lista):
    print("A soma vale",soma(lista)) #jeito fácil, não usar na prova

def o_menor (lista):
    menor = lista[0] #estou considerando o primeiro elemento como menor
    posicao=1
    while posicao < len(lista):
        # substitui o valor da variável 'menor' pelo valor do elemento da lista na posição 'posicao' se ele for menor do que o valor atual de 'menor'
        if lista[posicao] < menor:
            menor=lista[posicao]
        # avança para a posiçãao seguinte
        posicao+=1
    # depois desse while terminar encontramos o menor valor
    return menor

def mostrar_o_menor (lista):
    # print("O menor valor é ", min(lista)) #jeito fácil, não usar na prova
    print("O menor valor é ", o_menor(lista)) #jeito fácil, não usar na prova

def o_maior (lista):
    maior = lista[0] #estou considerando o primeiro elemento como maior
    posicao=1
    while posicao < len(lista):
        # se eu achar algo maior na lista, substitui o valor da variável 'maior' pelo valor do elemento da lista na posição 'posicao' se ele for maior do que o valor atual de 'maior'
        if lista[posicao] > maior:
            maior=lista[posicao]
        # avança para a posiçãao seguinte
        posicao+=1
    # depois desse while terminar encontramos o maior valor
    return maior

def mostrar_o_maior (lista):
    # print("O maior valor é ", max(lista)) #jeito fácil, não usar na prova
    print("O maior valor é ", o_maior(lista)) #jeito fácil, não usar na prova

def executar_opcoes (lista):
    chave_para_realizar_operacoes_ate_cansar_ligada=True
    while chave_para_realizar_operacoes_ate_cansar_ligada:
        opcao=opcao_escolhida()

        if opcao==1:
            esvazia_lista(lista)
        elif opcao==2:
            incluir_numero(lista)
        elif opcao==3:
            excluir_numero_dado_o_numero(lista)
        elif opcao==4:
            excluir_numero_dada_a_posicao(lista)
        elif opcao==5:
            print(lista)
        elif opcao==6:
            mostrar_soma (lista)
        elif opcao==7:
            mostrar_o_menor (lista)
        elif opcao==8:
            mostrar_o_maior (lista)
        else: # só sobrou a opcao ser 9
            chave_para_realizar_operacoes_ate_cansar_ligada=False

# DAQUI PARA CIMA DEFINIMOS SUBPROGRAMAS
# DAQUI PARA BAIXO FIZEMOS O PROGRAMA, CHAMANDO NELE OS SUBPROGRAMAS ACIMA

print("PROGRAMA PARA REALIZAR OPERAÇÕES COM LISTAS\n")

lista=[] # lista começa vazia
executar_opcoes (lista)

print("PROGRAMA ENCERRADO!")