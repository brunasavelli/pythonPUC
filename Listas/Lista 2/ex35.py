'''
Faça um programa em Python que solicite a digitação de três valores representando, 
respectivamente, as horas, os minutos e os segundos de um horário, verificando, a seguir se os 
mesmos representam ou não um horário válido. Sendo válido o programa deverá solicitar a 
digitação de uma quantidade de segundos, calcular e mostrar na tela o horário que se obtem ao 
adiantar o horário digitado a quantidade de segundo também digitada
'''

try:
    horas = int(input("Horas: "))
except ValueError:
    print("A hora deve ser numérica.")
else:
    if horas < 0 or horas > 23:
        print("Só há hora de 0 a 23!")
    else:
        try:
            minutos = int(input("Minutos: "))
        except ValueError:
            print("O minuto deve ser numérico.")
        else:
            if minutos < 0 or minutos > 59:
                print("Só há minutos de 0 a 59")
            else:
                try:
                    segundos = int(input("Segundos: "))
                except ValueError:
                    print("O segundo deve ser numérico.")
                else:
                    if segundos < 0 or segundos > 59:
                        print("Só há segundos de 0 a 59")
                    else:
                        try:
                            print(f"{horas}:{minutos}:{segundos}")
                            adSegundos = int(input("Adicione os segundos para serem avançados: "))
                        except ValueError:
                            print("Os segundos adicionados devem ser numéricos.")
                        else:
                            if adSegundos <= 0:
                                print("Os segundos não podem ser negativos")
                            else:

                                # CORREÇÃO MALIGNO
                                tempo = segundos + adSegundos
                                segundos = tempo % 60
                                tempo = tempo // 60 + minutos
                                minutos = tempo % 60
                                tempo = tempo // 60 + horas
                                hora = tempo % 24
                                if horas < 10: horas = "0" + str(horas)
                                if minutos < 10: minutos = "0" + str(minutos)
                                if segundos < 10: segundos = "0" + str(segundos)

                                print("Adiantado conforme solicitado, o horário fica: ", horas, ":", minutos, ":", segundos, sep="")


                                # MINHA VERSÃO
                                # segundos += adSegundos
                                # minutos += segundos // 60
                                # segundos = segundos % 60

                                # horas += minutos // 60
                                # minutos = minutos % 60

                                # horas = horas % 24
                                # print(f"Novo horário: {horas}:{minutos}:{segundos}")