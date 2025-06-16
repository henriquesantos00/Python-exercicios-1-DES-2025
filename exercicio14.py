#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

Compras = float(input("digite o valor da compra:"))

if Compras >= 500:
    print("você tem 10% de desconto")
elif Compras <= 300:
    print("você não tem desconto.")
else:
    print("você tem  5% de desconto.")
