#Crie um programa que receba um ano e diga se ele é bissexto.
#(Dica: múltiplos de 4, exceto os múltiplos de 100, a menos que também sejam múltiplos de 400)

ano = int(input("digite um ano para saber se é bissexto:"))
bissexto = ano % 4 == 0
if bissexto == 0:
    print("O ano não é bissexto. ")
else:
    print("o ano é bissexto.")
