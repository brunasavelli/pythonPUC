try:
    n1 = float(input("Digite um número: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")
    
try:
    n2 = float(input("Digite outro número: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")

try:
    n3 = float(input("Digite outro número: "))
except ValueError:
    print("Valor inválido. Por favor, digite um número.")

if n1 <= n2 and n1 <= n3:
    if n2 <= n3:
        print(f"Ordem crescente: {n1}, {n2}, {n3}")
    else:
        print(f"Ordem crescente: {n1}, {n3}, {n2}")
elif n2 <= n1 and n2 <= n3:
    if n1 <= n3:
        print(f"Ordem crescente: {n2}, {n1}, {n3}")
    else:
        print(f"Ordem crescente: {n2}, {n3}, {n1}")
else:
    if n1 <= n2:
        print(f"Ordem crescente: {n3}, {n1}, {n2}")
    else:
        print(f"Ordem crescente: {n3}, {n2}, {n1}") 

