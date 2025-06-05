# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

umidade = int(input("digite a umidade no local:"))
if umidade < 70:
    print("umidade boa")
elif umidade > 70:
    print("alerta! umidade acima do limite")