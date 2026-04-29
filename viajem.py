destino = input("Para onde você vai viajar: ")
reais = int(input("Quantos reais você tem pra viagem: "))
cotação =  float(input("Qual a cotação do dolar hoje?: "))

dolares = reais / cotação

print(f"Planejamento: {destino}")
print(f"Valor em conta: R${reais}")
print(f"cotação usada: U${cotação}")
print(f"Voce terá: U${dolares}")
print(f"BOA VIAGEM")