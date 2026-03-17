print("COMEÇO DO CÓDIGO")

try:
    a = float(input("Digite o coeficiente 'a' da sua equação: "))
except ValueError:
    print("O coeficiente deve ser numérico. Digite novamente")
else:
    if a==0:
        print("O coeficiente 'a' não pode ser igual a 0")
    else:
        try:
            b = float(input("Digite o coeficiente 'b' da sua equação: "))
        except ValueError:
            print("O coeficiente deve ser numérico. Digite novamente")
        else:
            try:
                c = float(input("Digite o coeficiente 'c' da sua equação: "))
            except ValueError:
                print("O coeficiente deve ser numérico. Digite novamente")
            else:
                delta = b ** 2 - 4 * a * c
                if delta < 0:
                    print("Essa equação não possui raízes reais")
                elif delta == 0:
                    x = -b / (2 * a)
                    print(f"Essa equação possui uma raíz real: {x}")
                else:
                    x1 = (-b + delta ** 0.5) / (2 * a)
                    x2 = (-b - delta ** 0.5) / (2 * a)
                    print(f"Essa equação possui duas raízes reais: {x1} e {x2}")
                    
print("\nPROGRAMA ENCERRADO")