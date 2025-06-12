#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = int(input("digite quantos caracteres tem sua senha:"))
if senha > 8:
    print("senha válida.")
else:
    print("senha muito curta.")