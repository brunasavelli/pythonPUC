# # exemplo com números
# lista=[2,3,5,7,11]
# print(lista)
# print(id(lista)) # id de memória da lista
# lista.append(13) # adiciona um elemento no final da lista
# print(lista)
# print(id(lista)) # id de memória não muda pq a lista é mutável, ou seja, pode ser modificada sem criar uma nova lista, ela apenas é atualizada
# print(lista[1:3])

# exemplo com strings - lista de caracteres (textos)
# texto="PUC-CAMPINAS"
# print(texto[-2])
# print(len(texto))

# textos são inalteráveis, ou seja, não é possível modificar um texto depois de criado
# não pode usar 'insert', 'append', 'remove', 'del' ou qualquer outra atribuição direta para modificar um texto
# texto[3]='#' # isso não é possível, vai gerar um erro
# texto.append("Pontifícia Universidade Católica de Campinas") # isso também não é possível, vai gerar um erro

# string vazia:
# texto_vazio=""
# print(len(texto_vazio)) #vai imprimir 0, pois o texto está vazio

# input retorna uma string, um texto
# strip retorna sem espaços em branco iniciais e finais, sem as tabulações e sem as quebras de linha
# texto="   Pontifícia   Universidadede   Católica   de   Campinas   "
# print(texto)
# print(texto+ '#')
# print(texto.strip())

# IN verifica se um texto está contido em outro texto, retorna True ou False
# print("PUC" in texto)
# print("ande" in texto)
# print("de" not in texto)

# método find
# print(texto.find("de")) # retorna a posição onde começa a palavra "de" dentro do texto, ou seja, a posição do d de de
# print(texto[26])

# método split
# print(texto.split("de")) # retorna uma lista de palavras, separando o texto pelos espaços em branco

# método replace
# print(texto.replace("dede", "de")) # retorna um novo texto, substituindo todas as ocorrências de "dede" por "de"
# print(texto) #O TEXTO NÃO FOI ALTERADO, APENAS O RETORNO REPLACE
# print(id(texto)) #id de memória do texto

# texto=texto.replace("dede", "de") # retorna um novo texto, substituindo todas as ocorrências de "dede" por "de"
# print(id(texto)) # O id do texto mudou, pois o replace retornou um novo texto

# exemplo de endereços de memória (id)
# nome="Bruna"
# print(nome)
# print(id(nome))

# nome=nome+" Savelli" # pegou o id antigo e adicionou um texto, se tornando um novo texto, assim salvando em um novo endereço de memória
# print(nome)
# print(id(nome))

# método list
# nome="Bruna"
# lista=list(nome)
# print(lista) # retorna uma lista de caracteres, ou seja, cada letra do nome é um elemento da lista
# novonome="#".join(lista) #junta os elementos da lista em um texto, separando por "#". caso o separador for vazio (""), junta os elementos da lista sem espaços entre eles
# print(novonome) # retorna um texto, juntando os elementos da lista em um texto, sem espaços entre eles


# TUPLAS são como listas, mas são imutáveis, e são delimitadas por parênteses
# tupla=(2,3,5)
# print(tupla)
# tupla[1]=33 # isso não é possível, vai gerar um erro, pois as tuplas são imutáveis
# () é uma tupla vazia
# (2,3,4,5) é uma tupla com 4 elementos
# (2) é apenas um número entre parênteses, não é uma tupla
# (2,) é uma tupla com 1 elemento, é necessário colocar a vírgula para indicar que é uma tupla, caso contrário, seria apenas um número entre parênteses

# tupla=(2,)
# # tupla=(2) # vira apenas um número, não é uma tupla
# print(len(tupla))

# DICIONARIOS são mapas que associam chaves a valores, são delimitados por chaves
nota={"ana":"10", "bruna":"9.5", "joao":"5"}
print(nota["bruna"]) # retorna o valor associado à chave "bruna", ou seja, 9.5
nota["maria"]="5"
print(nota["maria"]) # retorna o valor associado à chave "maria", ou seja, 5
print(nota)

# atualizando o valor associado à chave "ana"
nota["ana"]="5"
print(nota["ana"])