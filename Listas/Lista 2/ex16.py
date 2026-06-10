try: 
    ladoA = float(input("Lado A em cm: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")
else:
    try:
        ladoB = float(input("Lado B em cm: "))
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
    else:
        try:
            ladoC = float(input("Lado C em cm: "))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
        else:
            perimetro = ladoA + ladoB + ladoC
            print(f"Seu triângulo mede {perimetro} cm")