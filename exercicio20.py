# Simule um login com nome de usuário "admin" e senha "1234"
# Caso os dados estejam corretos, exiba "Acesso concedido", senão "Acesso negado"

nome_de_usuario = (input("Digite o nome do usuário: "))
senha = (input("Digite sua senha: "))

if senha == ("1234") and nome_de_usuario ==("admin"):
    print("Acesso concedido.")
else:
    print("Acesso negado.")