#MENU
chave_menu_ligada = True

while chave_menu_ligada:
    try:
        opcao_user = int(input('''==============================================================\n
Escolha uma opção:
1 - Celsius para Fahrenheit
2 - Fahrenheit para Celsius
3 - Celsius para Kelvin
4 - Kelvin para Celsius
5 - Celsius para Rankine
6 - Rankine para Celsius
7 - Fahrenheit para Kelvin
8 - Kelvin para Fahrenheit
9 - Fahrenheit para Rankine
10 - Rankine para Fahrenheit
11 - Kelvin para Rankine
12 - Rankine para Kelvin
13 - Sair

Opção escolhida: '''))
    except ValueError:
        print("O campo deve ser preenchido numericamente. Tente novamente.")

    else: 
        if opcao_user < 1 or opcao_user > 13:
            print("Opção inválida.")
        else:
            if opcao_user == 1:
                try:
                    celsius = float(input("Temperatura em Celsius: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if celsius < -273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        fahrenheit = (celsius * 1.8) + 32 
                        print(f"{celsius}º C é igual a {fahrenheit}º F\n")

            elif opcao_user == 2:
                try:
                    fahrenheit = float(input("Temperatura em Fahrenheit: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if fahrenheit < -459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        celsius = (fahrenheit - 32) / 1.8
                        print(f"{fahrenheit}º F é igual a {celsius}º C\n")

            elif opcao_user == 3:
                try:
                    celsius = float(input("Temperatura em Celsius: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if celsius < -273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        kelvin = celsius + 273.15
                        print(f"{celsius}º C é igual a {kelvin} K\n")

            elif opcao_user == 4:
                try:
                    kelvin = float(input("Temperatura em Kelvin: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if kelvin < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        celsius = kelvin - 273.15
                        print(f"{kelvin} K é igual a {celsius}º C\n")

            elif opcao_user == 5:
                try:
                    celsius = float(input("Temperatura em Celsius: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if celsius < -273.15:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        rankine = (celsius + 273.15) * 1.8
                        print(f"{celsius}º C é igual a {rankine} R\n")

            elif opcao_user == 6:
                try:
                    rankine = float(input("Temperatura em Rankine: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if rankine < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        celsius = (rankine / 1.8) - 273.15
                        print(f"{rankine} R é igual a {celsius}º C\n")

            elif opcao_user == 7:
                try:
                    fahrenheit = float(input("Temperatura em Fahrenheit: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if fahrenheit < -459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        kelvin = (fahrenheit + 459.67) / 1.8
                        print(f"{fahrenheit}º F é igual a {kelvin} K\n")

            elif opcao_user == 8:
                try:
                    kelvin = float(input("Temperatura em Kelvin: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if kelvin < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        fahrenheit = (kelvin * 1.8) - 459.67
                        print(f"{kelvin} K é igual a {fahrenheit}º F\n")

            elif opcao_user == 9:
                try:
                    fahrenheit = float(input("Temperatura em Fahrenheit: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if fahrenheit < -459.67:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        rankine = fahrenheit + 459.67
                        print(f"{fahrenheit}º F é igual a {rankine} R\n")

            elif opcao_user == 10:
                try:
                    rankine = float(input("Temperatura em Rankine: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if rankine < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        fahrenheit = rankine - 459.67
                        print(f"{rankine} R é igual a {fahrenheit}º F\n")

            elif opcao_user == 11:
                try:
                    kelvin = float(input("Temperatura em Kelvin: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if kelvin < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        rankine = kelvin * 1.8
                        print(f"{kelvin} K é igual a {rankine} R\n")

            elif opcao_user == 12:
                try:
                    rankine = float(input("Temperatura em Rankine: "))
                except ValueError:
                    print("O campo deve ser preenchido numericamente. Tente novamente.")
                else:
                    if rankine < 0:
                        print("Temperatura fornecida abaixo do ZERO ABSOLUTO")
                    else:
                        kelvin = rankine / 1.8
                        print(f"{rankine} R é igual a {kelvin} K\n")

            elif opcao_user == 13:
                chave_menu_ligada = False

            else:
                print("Opção inválida. Por favor, escolha uma opção entre 1 e 12.")

print("VOCÊ SAIU DO PROGRAMA DE CONVERSÃO")