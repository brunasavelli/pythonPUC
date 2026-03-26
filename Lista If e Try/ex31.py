#MENU
try:
    opcao_user = int(input('''Escolha uma opção:
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

    Opção escolhida: '''))
except ValueError:
    print("O campo deve ser preenchido numericamente. Tente novamente.")

if opcao_user == 1:
    celsius = float(input("Temperatura em Celsius: "))
    fahrenheit = (celsius * 1.8) + 32 
    print(f"{celsius}º C é igual a {fahrenheit}º F")

elif opcao_user == 2:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}º F é igual a {celsius}º C")

elif opcao_user == 3:
    celsius = float(input("Temperatura em Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}º C é igual a {kelvin} K")

elif opcao_user == 4:
    kelvin = float(input("Temperatura em Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin} K é igual a {celsius}º C")

elif opcao_user == 5:
    celsius = float(input("Temperatura em Celsius: "))
    rankine = (celsius + 273.15) * 1.8
    print(f"{celsius}º C é igual a {rankine} R")

elif opcao_user == 6:
    rankine = float(input("Temperatura em Rankine: "))
    celsius = (rankine / 1.8) - 273.15
    print(f"{rankine} R é igual a {celsius}º C")

elif opcao_user == 7:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    kelvin = (fahrenheit + 459.67) / 1.8
    print(f"{fahrenheit}º F é igual a {kelvin} K")

elif opcao_user == 8:
    kelvin = float(input("Temperatura em Kelvin: "))
    fahrenheit = (kelvin * 1.8) - 459.67
    print(f"{kelvin} K é igual a {fahrenheit}º F")

elif opcao_user == 9:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
    rankine = fahrenheit + 459.67
    print(f"{fahrenheit}º F é igual a {rankine} R")

elif opcao_user == 10:
    rankine = float(input("Temperatura em Rankine: "))
    fahrenheit = rankine - 459.67
    print(f"{rankine} R é igual a {fahrenheit}º F")

elif opcao_user == 11:
    kelvin = float(input("Temperatura em Kelvin: "))
    rankine = kelvin * 1.8
    print(f"{kelvin} K é igual a {rankine} R")

elif opcao_user == 12:
    rankine = float(input("Temperatura em Rankine: "))
    kelvin = rankine / 1.8
    print(f"{rankine} R é igual a {kelvin} K")

else:
    print("Opção inválida. Por favor, escolha uma opção entre 1 e 12.")