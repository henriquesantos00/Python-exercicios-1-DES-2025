# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = float(input("digite a distancia percorrida:"))
tempo = float(input("digite o tempo gasto:"))

velocidade_media = distancia/tempo
if velocidade_media < 5:
    print("velocidade lenta.")
elif velocidade_media >= 5 <= 10:
    print("velocidade moderada.")
else:
    print("velocidade rapida.")