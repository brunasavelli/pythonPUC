primeiro_numero = float(input("Digite um número: "))
segundo_numero = float(input("Digite outro número: "))

if primeiro_numero < segundo_numero:
    print(f"Ordem crescente: {primeiro_numero}, {segundo_numero}")
else:
    print(f"Ordem crescente: {segundo_numero}, {primeiro_numero}")