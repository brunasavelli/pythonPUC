disciplinas = [
    {"disciplina": "Matemática", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Física", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Química", "nota": 9.0, "frequencia": 95}
]

def materia_menor_freq(disciplinas):
    if len(disciplinas) == 0:
        return None
    
    menor_frequencia = disciplinas[0]["frequencia"]
    materia = disciplinas[0]["disciplina"]

    for disciplina in disciplinas:
        if disciplina["frequencia"] < menor_frequencia:
            menor_frequencia = disciplina["frequencia"]
            materia = disciplina["disciplina"]

    return materia

print(materia_menor_freq(disciplinas))