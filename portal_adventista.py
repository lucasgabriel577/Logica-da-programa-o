nome = input("Digite seu nome: ")
uniforme = input("Está de uniforme completo? (sim/nao): ")
if uniforme == "sim": print(f" Bem-vindo, {nome}! Siga para o pátio para o culto.") 
else: print(f" {nome}, por favor, dirija-se à Coordenação antes da aula.")

hora = int(input("que horas são?: "))
if hora <= 7:
    print("Bom dia você {nome}!, voce chegou no horario")
else:
    print("Você está atrasado. Por favor, retire sua autorização na secretaria.")