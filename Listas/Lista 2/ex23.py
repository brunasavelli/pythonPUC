#COMANDO REPETITIVO: while

chave_de_claculo_de_area_ligada = True
while chave_de_claculo_de_area_ligada:
    chave_de_digitacao_ligada = True
    while chave_de_digitacao_ligada:
        try:
            lado = float(input("Digite o lado do quadrado desejado em cm: "))
        except ValueError:
            print("O campo deve ser preenchido com números. Tente novamente.")
        else:
            if lado <= 0:
                print("O lado do quadrado deve ser positivo. Tente novamente.")
            else:
                chave_de_digitacao_ligada = False

    area = lado ** 2
    print(f"A área do quadrado de lado {lado} cm é {area} cm²")

    chave_de_digitacao_de_resposta_ligada = True
    while chave_de_digitacao_de_resposta_ligada:
        resposta = input("Deseja calcular a área de outro quadrado? (S/N): ")
        resposta = resposta.upper() #UPPER transforma a 'resposta' minúscula em maiúscula
        if resposta != "S" and resposta != "N":
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        else:
            chave_de_digitacao_de_resposta_ligada = False
    if resposta == "N" : chave_de_claculo_de_area_ligada = False

print("Programa encerrado!")