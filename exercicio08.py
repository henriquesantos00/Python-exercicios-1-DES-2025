# Talita está simulando o custo de frete para sua loja virtual. O valor depende da distância:

# Até 50 km: R$ 5,00
# De 51 a 150 km: R$ 15,00
# Acima de 150 km: R$ 25,00

distancia = float(input("digite a distancia percorrida:"))
if distancia < 51:
    print(" o valor foi R$ 5,00.")
elif distancia < 150:
    print("o valor foi R$ 15,00.")
else:
    print("o valor foi R$ 25,00.")