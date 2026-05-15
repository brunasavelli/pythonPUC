calcular_area_circulo = True
while calcular_area_circulo:
    chave_digitacao = True
    while chave_digitacao:
        try:
            R = float(input("Qual é o raio do seu círculo? "))
        except ValueError:
            print("O campo deve ser preenchido com números. Tente novamente.")
        else:
            if R <= 0:
                print("Utilize números positivos.")
            else:
                chave_digitacao = False
    
    area = 3.1415 * R**2
    print(f"A área do seu círculo é {area} cm²")

    calcular_nova_area = True
    while calcular_nova_area:
        pergunta = input("Deseja calcular outra área de círculo? (S/N): ")
        pertunta = pergunta.upper()
        if pertunta != "S" and pertunta != "N":
            print("Resposta inválida. Digite 'S' para sim ou 'N' para não.")
        else:
            calcular_nova_area = False
    if pertunta == "N": calcular_area_circulo = False
print("Programa encerrado!")