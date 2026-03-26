calcular_area = True

while calcular_area:
    chave_digitacao = True
    while chave_digitacao:
        try:
            Q = float(input("Digite a quantidade de lados do seu poligno: "))
        except ValueError:
            print("O campo deve ser preenchido numericamente. Tente novamente.")
        else:
            if Q < 3:
                print("Não existe polígonos com menos de 3 lados. Tente novamente.")
            else:
                try:
                    medidaLados = float(input("Digite a medida dos lados do polígono:"))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if medidaLados <= 0:
                        print("A medida doa lados não pode ser negativa ou zero. Tente novamente.")
                    else:
                        chave_digitacao = False

    perimetro = Q * medidaLados
    print(f"O perímetro do seu polígono é de {perimetro} cm")

    chave_resposta = True
    while chave_resposta:
        resposta = input("Deseja calcular a área de outro polígono? (S/N): ")
        resposta = resposta.upper()
        if resposta != 'S' and resposta != 'N':
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        else:
            chave_resposta = False
    if resposta == 'N': calcular_area = False

print("Programa encerrado!")