'''
Faça um programa em Python que converte temperaturas expressas em graus Rankine para graus 
Celsius. Seu programa deve solicitar a digitação do valor a ser convertido (C). A relação entre 
graus Celsius e graus Rankine é C = (R–491.67) /1.8. A menor temperatura possível em graus 
Rankine é 0 e em graus Celsius é -273.15.
'''

try:
    rankine = float(input("Temperatura em Rankine: "))
except ValueError: 
    print("A temperatura deve ser um número. Digite novamente.")
else:
    if rankine < 0:
        print("A temperatura em Rankine não pode ser menor que 0. Digite novamente.")
    else:
        celsius = (rankine - 491.67) / 1.8
        print(f"{rankine} R é igual a {celsius}º C")