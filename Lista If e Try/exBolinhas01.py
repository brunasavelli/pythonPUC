qntBolinhas = int(input("Digite um número para o seu triângulo: "))
if qntBolinhas < 2:
    print("Quantidade mínima de bolinhas não atingida")
else:
    print(" " * (qntBolinhas - 1), "O")
    print(" " * (qntBolinhas - 0), "O" )
    
    print("O", "O", "O")