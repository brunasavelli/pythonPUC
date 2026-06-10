## RESOLUÇÃO MALIGNO:
def expansao(txt):
    tamanho=len(txt)
    posicao=0

    while posicao<tamanho:
        if txt[posicao]=='-' and posicao!=0 and posicao!=tamanho-1 and txt[posicao-1]<txt[posicao+1]:
            meio=""
            inicio=txt[posicao-1]
            final=txt[posicao+1]

            while True:
                inicio=chr(ord(inicio)+1)
                if inicio==final: break
                meio+=inicio
            txt=txt[:posicao]+meio+txt[posicao+1:]
            tamanho+=(len(meio)-1)
            posicao+=(len(meio)+1)
        else:
            posicao+=1

    return txt

print(expansao("-AB-DEF-B-GH-"))
