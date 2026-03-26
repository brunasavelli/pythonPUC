chave_digitacao_ligada = True

while chave_digitacao_ligada:
    try:
        m = float(input("Digite o lado paralelo menor do trapézio: "))
    except ValueError:
        print("O campo deve ser preenchido com números.")
    else:
        if m <= 0:
            print("Números negativos não são aceitos.")
        else:
            try:
                M = float(input("Digite o lado paralelo maior do trapézio: "))
            except ValueError:
                print("O campo deve ser preenchido com números.")
            else:
                if M <= 0:
                    print("Números negativos não são aceitos.")
                else:
                    try:
                        O = float(input("Digite outro lado do trapézio: "))
                    except ValueError:
                        print("O campo deve ser preenchido com números.")
                    else:
                        if O <= 0:
                            print("Números negativos não são aceitos.")
                        else:
                            chave_digitacao_ligada = False

perimetro = m + M + (O + O)
print(f"O perímetro do seu trapézio é de {perimetro} cm")