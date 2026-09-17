# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: lucas Gabriel Ferraz de Carvalho
# Data: 17/09/2026
# ==============================================================================


dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------


def processar_dados(dados):
    lista_processada = []

    for registro in dados:
        registro = registro.strip()
        partes = registro.split(";")

        nome = partes[0].strip().title()
        cargo = partes[1].strip().title()
        telefone = partes[2].strip()

        pessoa = {
            "nome": nome,
            "cargo": cargo,
            "telefone": telefone
        }

        lista_processada.append(pessoa)

    return lista_processada



def exibir_dados(lista):
    print("\n===== DADOS CADASTRADOS =====")

    for pessoa in lista:
        print("Nome:", pessoa["nome"])
        print("Cargo/Setor:", pessoa["cargo"])
        print("Telefone/CPF:", pessoa["telefone"])
        print("-" * 30)



def buscar_pessoa(lista, nome):
    nome = nome.strip().lower()

    for pessoa in lista:
        if pessoa["nome"].lower() == nome:
            return pessoa

    return None


# ------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

dados_processados = processar_dados(dados_brutos)

exibir_dados(dados_processados)

nome_busca = input("\nDigite o nome para buscar: ")

resultado = buscar_pessoa(dados_processados, nome_busca)

if resultado:
    print("\nPessoa encontrada:")
    print("Nome:", resultado["nome"])
    print("Cargo/Setor:", resultado["cargo"])
    print("Telefone/CPF:", resultado["telefone"])
else:
    print("\nPessoa não encontrada.")
