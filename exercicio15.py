#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("digite a sua idade:"))
if idade > 13:
    print("acesso permitido.")
else:
    print("acesso negado.")