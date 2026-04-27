chave_circulo = True

while chave_circulo:
    try:
        raio = float(input("Digite o raio do círculo: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    else:
        if raio <= 0:
            print("O raio deve ser um número positivo. Tente novamente.")
        else:    
            perimetro = 2 * 3.1415 * raio
            print(f"O perímetro do círculo é de {perimetro:.2f} cm")
            continuar = input("Deseja calcular o perímetro de outro círculo? (S/N): ")
            if continuar.upper() != "S":
                chave_circulo = False
                print("Programa encerrado!")