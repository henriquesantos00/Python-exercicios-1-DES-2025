alunos = ("alice", "bruno", "carla")
dias = ("seg", "ter", "qua", "qui")
reservas = [["ausente" for _ in dias] for _ in alunos]
print ("preencha com 'S' para presença e 'X' para ausência:")

for i, aluno in enumerate(alunos):
    print(f"\nAluno: {aluno}")
    for j, dia in enumerate (dias):
        entrada = input(f" {dia}: ")
        if entrada.upper () == 'S' :
            reservas [i] [j] = "presente"
print(f"\nTabela de reservas:")
print(f"{'Aluno': <10} {' '. join([f'{d:<10}' for d in dias])}")
for i, aluno in enumerate(alunos):
    print(f"{'Aluno': <10} {' '. join([f'{res:<10}' for res in reservas[i]])}")