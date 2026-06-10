'''
Levando em conta as relações entre unidades de temperatura mostradas nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas expressas em graus 
Fahrenheit para graus Kelvin. Seu programa deve solicitar a digitação do valor a ser 
convertido (F). A menor temperatura possível em graus Fahrenheit é -459.67 e em graus Kelvin 
é 0.
'''
# fahrenheit = (C * 1.8) + 32
# kelvin = C + 273.15

try:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")
else:
    if fahrenheit < -459.67:
        print("A temperatura em Fahrenheit não pode ser menor que -459.67. Digite novamente.")
    else:
        kelvin = ((fahrenheit - 32) / 1.8) + 273.15
        print(f"{fahrenheit}º F é igual a {kelvin} K")