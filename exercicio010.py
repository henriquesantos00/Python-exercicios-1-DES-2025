# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario = float(input("digite o salario:"))
parcela = float(input("digite o valord da parcela do financiamento:"))

if salario <= 3000:
    print("financiamento negado, salário abaixo do minimo exigido")
elif parcela > salario * 35:
    print("financiamento negado, parcela acima de 35% do salário.")
else:
    print("financiamento aprovado!")