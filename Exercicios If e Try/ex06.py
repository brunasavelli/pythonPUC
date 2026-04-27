'''
Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus 
Kelvin. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Kelvin é K = C + 273.15. A menor temperatura possível em graus Celsius 
é -273.15 e em graus Kelvin é 0.
'''

celsius = float(input("Temperatura em Celsius: "))
kelvin = celsius + 273.15
print(f"{celsius}º C é igual a {kelvin} K")