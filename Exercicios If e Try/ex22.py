chave_area = True

while chave_area:
    try:
        B = float(input("Digite a base do triângulo em cm: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
    else:
        try:
            A = float(input("Digite a altura do triêngulo em cm: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        else:
            area = (B * A) / 2
            print(f"A área do triângulo é de {area:.2f} cm²")
            continuar = input("Deseja calcular a área de outro triângulo? (S/N): ")
            if continuar.upper() != "S":
                chave_area = False
                print("Programa encerrado!")