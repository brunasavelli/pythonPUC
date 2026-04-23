chave_triangulo = True

while chave_triangulo:
    try:
        qntBolinhas = int(input("Digite um número para o seu triângulo: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
    else:
        if qntBolinhas < 2:
            print("Quantidade mínima de bolinhas não atingida")
        else:
            for i in range(qntBolinhas):
                print(" " * (qntBolinhas - i - 1) + "O" * (2 * i + 1))
            continuar = input("Deseja criar outro triângulo? (S/N)")
            if continuar.upper() != "S":
                chave_triangulo = False
                print("Programa encerrado!")
