# chave_triangulo = True

# while chave_triangulo:
#     try:
#         qntBolinhas = int(input("Digite um número para o seu triângulo: "))
#     except ValueError:
#         print("Entrada inválida. Por favor, digite um número inteiro.")
#     else:
#         if qntBolinhas < 2:
#             print("Quantidade mínima de bolinhas não atingida")
#         else:
#             for i in range(qntBolinhas):
#                 print(" " * (qntBolinhas - i - 1) + "O" * (2 * i + 1))
#             continuar = input("Deseja criar outro triângulo? (S/N)")
#             if continuar.upper() != "S":
#                 chave_triangulo = False
#                 print("Programa encerrado!")


#################### RESOLUÇÃO MALIGNO ###################
def escreva (qual_caractere, qts_vezes, salta_linha = True):
    qnt_escrita = 0
    while qnt_escrita < qts_vezes:
        print(qual_caractere, end="")
        # print("" * (qts_vezes - 1), qual_caractere, end="", sep="")
        qnt_escrita += 1
    if salta_linha:
        print()

def triangulo (qts_linhas):
    qtd_esps_inic = qts_linhas - 1

    escreva(qual_caractere=" ", qts_vezes=qtd_esps_inic, salta_linha=False)
    print("O")
    qtd_esps_inic -= 1

    qtd_esps_meio = 1
    linhas_escritas = 1

    while linhas_escritas < qts_linhas - 1:
        escreva(qual_caractere=" ", qts_vezes=qtd_esps_inic, salta_linha=False)
        print("O", end="")
        escreva(qual_caractere=" ", qts_vezes=qtd_esps_inic, salta_linha=False)
        print("O")
        linhas_escritas += 1
        qtd_esps_inic -= 1
        qtd_esps_meio += 2

    escreva(qual_caractere=" ", qts_vezes=qtd_esps_inic, salta_linha=False)

# escreva("O", 1)
triangulo(15)