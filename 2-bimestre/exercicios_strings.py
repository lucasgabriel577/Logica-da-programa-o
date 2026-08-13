telefone = input("Digite o telefone desse jeito (32)99999-9999: ")
ddd = telefone[1:3]
numero = telefone[5:]
print(f"DDD: {ddd}")
print(f"Número sem o DDD: {numero}")

data = input("Digite a data no formato 10/10/2010: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

email = input("Digite o e-mail no formato lucas.ferraz@eaportal.com: ")

primeiro_nome = email.split(".")[0]
dominio = email.split("@")[1].split(".")[0]

print("Primeiro nome:", primeiro_nome)
print("Domínio:", dominio)
