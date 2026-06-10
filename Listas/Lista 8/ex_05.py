disciplinas = [
    {"disciplina": "Matemática", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Física", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Química", "nota": 9.0, "frequencia": 95}
]

def media_geo_notas(disciplinas):
    if len(disciplinas) == 0:
        return None
    
    produto = 1

    for disciplina in disciplinas:
        produto *= disciplina["nota"]

    return produto ** (1 / len(disciplinas))

print(media_geo_notas(disciplinas))