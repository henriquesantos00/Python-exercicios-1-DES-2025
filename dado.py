import random

input("precione o enter para lançar o dado")

resultado = random.randint(1,6)

print(f"O dado rolou : {resultado}");
if resultado > 3:
    print("ual! você é fera!")
elif resultado < 3:
    print("tente novamente.")