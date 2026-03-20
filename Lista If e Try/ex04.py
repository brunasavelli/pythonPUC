'''
Faça um programa em Python que converte temperaturas expressas em graus Celsius para graus 
Fahrenheit. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Fahrenheit é F = C / 1.8 + 32. A menor temperatura possível em graus 
Celsius é -273.15 em em graus Fahrenheit é -459.67
'''

temperatura_celsius = float(input("Temperatura em Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32 

print(f"{temperatura_celsius}º C é igual a {temperatura_fahrenheit}º F")