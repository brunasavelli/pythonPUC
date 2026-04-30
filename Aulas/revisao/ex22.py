disciplina=[[123, "APPC", 4], [234, "EPBD", 2]]

resultado=[[26001620, 123, 1, 2026, 7.5, 0.85],
           [26001620, 234, 1, 2026, 6.5, 0.75],
           [26002548, 123, 1, 2025, 3.0, 0.80],
           [26002548, 234, 1, 2026, 7.0, 0.85]]

def desciplinaMenorFrequencia(disc, res):
  resMenorFreq=res[0]
  posicao = 1
  while posicao < len(res):
    if res[posicao][5] < resMenorFreq[5]:
      resMenorFreq=res[posicao]
    posicao += 1
  codDiscMenorFreq = resMenorFreq[1]
  posicao = 0
  while posicao < len(disc):
    if codDiscMenorFreq == disc[posicao][0]:
      return disc[posicao][1]
    posicao += 1
    
print(desciplinaMenorFrequencia(disciplina, resultado))
