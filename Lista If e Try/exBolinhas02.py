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
            print(" " * (qntBolinhas - 1) + "O")
            for i in range(1, qntBolinhas - 1):
                print(" " * (qntBolinhas - i - 1) + "O" + " " * (i * 2 - 1) + "O")
            print("O" * (qntBolinhas * 2 - 1))
            continuar = input("Deseja criar outro triângulo? (S/N)")
            if continuar.upper() != "S":
                chave_triangulo = False
                print("Programa encerrado!")