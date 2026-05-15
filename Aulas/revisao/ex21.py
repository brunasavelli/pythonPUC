aluno = [[26001620, "Bruna Savelli", 19995206934, "bruna@puccampinas.edu.br"], [26002548, "Ana de Souza", 1999634875, "ana@puccampinas.edu.br"]]

disciplina = [[123, "APPC", 4],[234, "EPBD", 2]]

resultado = [[26001620, 123, 1, 2026, 7.5, 0.85], [26001620, 234, 1, 2026, 6.5, 0.75], [26002548, 123, 1, 2025, 3.0, 0.80], [26002548, 234, 1, 2026, 7.0, 0.85]]

def nomeAlunoMaiorNota(alu, res):
       resMaiorNota = res[0] ## Assume inicialmente que o primeiro registro tem a maior nota

       # Percorre a lista de resultados para encontrar a maior nota
       posicao = 1
       while posicao < len(res):

       # Compara a nota atual (índice 4) com a maior encontrada
              if res[posicao][4] > resMaiorNota[4]:
                     resMaiorNota = res[posicao]
              posicao += 1  # incrementa para não travar o loop
       raAluMaiorNota = resMaiorNota[0] ## Pega o RA do aluno que tem a maior nota

       # Agora busca o nome do aluno com esse RA
       posicao = 0
       while posicao < len(alu):
              if raAluMaiorNota == alu[posicao][0]:
                     return alu[posicao][1]
              posicao += 1
print(nomeAlunoMaiorNota(aluno, resultado))