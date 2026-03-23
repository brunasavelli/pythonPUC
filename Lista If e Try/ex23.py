try:
    ladoQuadrado = float(input("Digite o lado do quadrado desejado: "))
except ValueError:
    print("O campo deve ser digitado numericamente.")
else:
    area = ladoQuadrado * ladoQuadrado
    print(f"A área do quadrado é {area}")