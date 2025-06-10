import random

frutas = ("maçãs", "bananas", "laranja", "uva", "manga")
print("lista de frutas:")
for i in range(len(frutas)):
    print(f"{1+1} - {frutas[i]}")

posicao_sorteada = random.randint(1, 5)

palpite = input("Qual fruta você acha que esta na posiçãosorteada?")
fruta_certa = frutas[posicao_sorteada - 1]
if palpite.capitalize() == fruta_certa:
    print("🥳 parabéns! você acertou!")
    print(f"A fruta na posicão {posicao_sorteada} era realmente {fruta_certa}.")
else:
    print("❌ que pena, você errou.")