# ==============================================================================
# PROVA PRÁTICA AV1 - 3º BIMESTRE
# ARQUIVO: av1_saneamento_dados.py
# Nome do Aluno: lucas Gabriel ferraz de carvalho
# Data: 28/08/2026
# ============================================================================== 

cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# TODO: 
for i in range(len(cadastros_brutos)):
   split_cadastro = cadastros_brutos[i].strip().split(";")
   split_cadastro[0] = split_cadastro[0].title()
   split_cadastro[1] = split_cadastro[1].strip()
   ddd = split_cadastro[1][0:2]
   print(f"Funcionário {i+1}: Nome: {split_cadastro[0]}, DDD: {ddd}, Telefone: {split_cadastro[1]}")

   
   pass

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")
