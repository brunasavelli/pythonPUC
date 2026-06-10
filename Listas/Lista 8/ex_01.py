disciplinas = [
    {"disciplina": "Matemática", "nota": 8.5, "frequencia": 90},
    {"disciplina": "Física", "nota": 7.0, "frequencia": 85},
    {"disciplina": "Química", "nota": 9.0, "frequencia": 95}
]

def materia_maior_nota(disciplinas):
    if len(disciplinas) == 0:
        return None
    
    maior_nota = disciplinas[0]["nota"]
    materia = disciplinas[0]["disciplina"]

    for disciplina in disciplinas:
        if disciplina["nota"] > maior_nota:
            maior_nota = disciplina["nota"]
            materia = disciplina["disciplina"]
    
    return materia

print(materia_maior_nota(disciplinas))