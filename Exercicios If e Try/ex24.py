calcular_area = True
while calcular_area:
    chave_digitacao = True
    while chave_digitacao:
        try:
            Q = int(input("Quantos lados tem o seu polígono? "))
        except ValueError:
            print("O campo deve ser preenchido com números inteiros. Tente novamente.")
        else:
            try:
                B = float(input("Qual a medida em cm de sua base? "))
            except ValueError:
                print("O campo deve ser preenchido com números. Tente novamente.")
            else:
                try:
                    A = float(input("Qual é a medida de sua apótema? "))
                except ValueError:
                    print("O campo deve ser preenchido com números. Tente novamente.")
                else:
                    if Q <= 2:
                        print("Um polígono deve ter mais de 2 lados.")
                    elif B <= 0 or A <= 0:
                        print("Utilize números positivos.")
                    else:
                        chave_digitacao = False
        
    area = (Q * B * A) / 2
    print(f"A área do seu polígono é {area} cm²")

    calcular_nova_area = True
    while calcular_nova_area:
        pergunta = input("Deseja calcular outra área de polígono? (S/N): ")
        pertunta = pergunta.upper()
        if pertunta != "S" and pertunta != "N":
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        else:
            calcular_nova_area = False
    if pertunta == "N": calcular_area = False

print("Programa encerrado!")