disciplinas = [
    {"disciplina": "Matemática", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Física", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Química", "nota": 9.0, "frequencia": 95}
]

def media_arit_notas(disciplinas):
    if len(disciplinas) == 0:
        return None
    
    soma = 0

    for disciplina in disciplinas:
        soma += disciplina["nota"]
        media = soma / len(disciplinas)

    return media

print(media_arit_notas(disciplinas))