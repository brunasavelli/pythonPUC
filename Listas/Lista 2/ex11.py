try:
    kelvin = float(input("Temperatura em Kelvin: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")
else:
    if kelvin < 0:
        print("A temperatura em Kelvin não pode ser menor que 0. Digite novamente.")
    else:
        fahrenheit = ((kelvin - 273.15) * 1.8) + 32
        print(f"{kelvin} K é igual a {fahrenheit}º F")