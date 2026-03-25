'''
Levando em conta as relações entre unidades de temperatura mostradas nos 6 exercícios
anteriores, faça um programa em Python que converte temperaturas expressas em graus 
Fahrenheit para graus Rankine. Seu programa deve solicitar a digitação do valor a ser 
convertido (F). A menor temperatura possível em graus Fahrenheit é -459.67 e em graus Rankine 
é 0.
'''

try:
    fahrenheit = float(input("Temperatura em Fahrenheit: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")
else:
    if fahrenheit < -459.67:
        print("A temperatura em Fahrenheit não pode ser menor que -459.67. Digite novamente.")
    else:
        rankine = fahrenheit + 459.6721
        print(f"{fahrenheit}º F é igual a {rankine} R")