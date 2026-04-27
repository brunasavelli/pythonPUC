'''
Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus 
Rankine. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Rankine é R = C*1.8 + 491.67. A menor temperatura possível em graus 
Celsius é -273.15 e em graus Rankine é 0.
'''

try:
    celsius = float(input("Temperatura em Celsius: "))
except ValueError:
    print("A temperatura deve ser um número. Digite novamente.")
else:
    if celsius < -273.15:
        print("A temperatura em Celsius não pode ser menor que -273.15. Digite novamente.")
    else:
        rankine = (celsius * 1.8) + 491.67
        print(f"{celsius}º C é igual a {rankine} R")