'''
Faça um programa em Python que solicite a digitação de dois valores quaisquer, informando-os, 
em seguida, em ordem crescente.
'''

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 > n2:
    print(f"Ordem crescente: {n2}, {n1}")
elif n1 < n2:
    print(f"Ordem crescente: {n1}, {n2}")
else:
    print("Os números são iguais.")