lado1 = float(input("Digite o valor do primeiro lado do quadrado/losango: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))
lado4 = float(input("Digite o valor do quarto lado: "))

perimetro = lado1 + lado2 + lado3 + lado4

if lado1 == lado2 == lado3 == lado4:
    print(f"Os lados formam um quadrado/losango. O perímetro é: {perimetro}")
else:
    print(f"Os lados não formam um quadrado/losango. O perímetro é: {perimetro}")