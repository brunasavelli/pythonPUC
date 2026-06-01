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

## O QUE EU FIZ:
 def expande(txt):
     posicao=0
     resultado=""
     while posicao < len(txt):
         resultado += txt[posicao]
         if posicao < txt[posicao - 1]:
             atual=txt[posicao]
             proxima=txt[posicao + 1]
           
             while atual == '-':
                 resultado+=txt[posicao]
                 posicao+=1
           
             while atual != '-' and proxima != '-':
                 cod_atual=ord(atual)
                 cod_proxima=ord(proxima)
               
                 if cod_atual<cod_proxima:
                     resultado+=chr(cod_atual)
                     resultado+=chr(cod_proxima)
                 posicao+=1


# expande("-AB-DEF-B-GH-")
