primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
terceiro_numero = float(input("Digite o terceiro número: "))

lista = [primeiro_numero, segundo_numero, terceiro_numero]

tamanho_lista = len(lista)
houve_troca = True

while houve_troca:
    houve_troca = False
    posicao = 0
    while posicao < tamanho_lista - 1:
        if lista[posicao] > lista[posicao+1]:
            lista[posicao], lista[posicao+1] = lista[posicao+1], lista[posicao]
            houve_troca = True
        posicao += 1
    tamanho_lista -= 1

print(f"Lista em ordem crescente: {lista}")
