#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

tarefaX = int(input("digite o tempo para a tarefaX:"))
tarefaY = int(input("digite o tempo para a tarefaY:"))
tarefaZ = int(input("digite o tempo para a tarefaZ:"))

soma = tarefaX + tarefaY + tarefaZ
if tarefaX > 0 or tarefaY > 0 or tarefaZ > 0 :
    print("Tempo positivo.")
else:
    soma = tarefaX + tarefaY + tarefaZ
    print(f"tempo total do projeto: {soma} tarefa")