aluno=[[26001620, "Bruna Savelli", 19995206934, "bruna@puccampinas.edu.br"],
       [26002548, "Ana de Souza", 1999634875, "ana@puccampinas.edu.br"],
       ...
      ]

disciplina=[[123, "APPC", 4], [234, "EPBD", 2], ...]

resultado=[[26001620, 123, 1, 2026, 7.5, 0.85],
           [26001620, 234, 1, 2026, 6.5, 0.75],
           [26002548, 123, 1, 2025, 3.0, 0.80],
           [26002548, 234, 1, 2026, 7.0, 0.85],
           ...
          ]

def nomeAlunoMaiorNota(alu, res):
       resMaiorNota=res[0] # estou SUPONDO que o aluno da posição 0 tem a maior nota
       posicao=1 # procurar da posição em diante para achar uma nota maior
       while posicao < len(res):
              if res[posicao][4]>resMaiorNota[4]: # pegando cada listinha, 'alu' é 'listonha'
                     resMaiorNota=res[posicao]
              posicao+=1
       raAluMaiorNota=resMaiorNota[0] # ra do aluno com maior nota.
       posicao=0
       while posicao<len(alu):
              if raAluMaiorNota==alu[posicao][0]:
                     return alu[posicao][1]
print(nomeAlunoMaiorNota(aluno,resultado)) # o que está programado para fazer com 'alu' será feito com 'aluno' e o que esta programado para fazer com 'res', será feito com 'resultado'.
