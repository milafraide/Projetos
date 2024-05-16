nome = str.upper(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
print(f"Parabéns {nome}, você tem {idade} anos!")
e_mail = str.lower(input("Digite seu e-mail: "))
senha = str.lower(input("Digite sua senha: "))


if e_mail == 'allansmarcelino@icloud.com' and senha == '12345':
    print("Você foi autenticado com sucesso: ")
elif e_mail != 'allansmarcelino@icloud.com' or senha != '12345':
    print("Você errou, tente novamente!")
else:
    print("Você saiu do programa!")