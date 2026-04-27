'''
Faça um programa em Python que converte temperaturas expressas em graus Fahrenheit para 
graus Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (F). A relação 
entre graus Celsius e graus Fahrenheit é C = 1.8 * (F -32). A menor temperatura possível em graus 
Fahrenheit é -459.67 em em graus Celsius é -273.15.
'''

temperatura_fahrenheit = float(input("Temperatura em Fahrenheit: "))

temperatura_celsius = (temperatura_fahrenheit - 32) / 1.8

print(f"{temperatura_fahrenheit}º F é igual a {temperatura_celsius}º C")