#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

temperatura = int(input("digite os graus celsius:"))
Fahrenheit = temperatura * 1.8 + 32

if Fahrenheit:
    print("a temperatura em fahrenheit foi:" , Fahrenheit)

