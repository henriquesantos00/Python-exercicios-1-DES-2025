#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

nota1 = int(input("digite a nota 1: "))
peso1 = int(input("digite o peso 1: "))
nota2 = int(input("digite a nota 2: "))
peso2 = int(input("digite o peso 2: "))

f = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print(f"Média: {f}")
