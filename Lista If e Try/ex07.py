'''
Faça um programa em Python que converte temperaturas expressas em graus Kelvin para graus 
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (K). A relação entre 
graus Celsius e graus Kelvin é C = K – 273.15. A menor temperatura possível em graus Kelvin 
é 0 e em graus Celsius é -273.15.
'''

kelvin = float(input("Temperatura em Kelvin: "))
celsius = kelvin - 273.15
print(f"{kelvin} K é igual a {celsius}º C")