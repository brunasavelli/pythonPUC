print("COMEÇO DO CÓDIGO")

try:
    horas = int(input("Horas: "))
except ValueError:
    print("A hora deve ser numérica e inteira.")
else:
    if horas > 23:
        print("O campo de 'hora' não pode ser maior que 23")
    else:
        try:
            minutos = int(input("Minutos: "))
        except ValueError:
            print("O minuto deve ser numérico e inteiro. Digite novamente")
        else:
            if minutos > 59:
                print("O campo 'minuto' não pode ser maior que 59")
            try:
                segundos = int(input("Segundos: "))
            except ValueError:
                print("Os segundos devem ser numéricos e inteiros. Digite novamente")
            else:
                if segundos > 59:
                    print("O campo 'segundos' não pode ser maior que 59")
                else:
                    print(f"O horário {horas}:{minutos}:{segundos} é válido")
print("\nPROGRAMA ENCERRADO")