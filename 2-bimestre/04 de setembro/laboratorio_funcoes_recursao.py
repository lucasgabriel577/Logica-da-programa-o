TAXA_PROCESSAMENTO = 2.00


def calcular_frete(valor_compra, peso_kg):
    taxa_base = peso_kg * 5.00
    if valor_compra >= 200:
        taxa_base = taxa_base * 0.5
    return taxa_base


def aplicar_cupom(valor_item, cupom_desconto):
    valor_com_desconto = valor_item - (valor_item * cupom_desconto / 100)
    preco_final = valor_com_desconto + TAXA_PROCESSAMENTO
    return preco_final


def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return
    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")
    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)


if __name__ == "__main__":
    print("=== TESTE PARTE 1: CALCULADORA DE FRETE ===", end=" ")
    frete = calcular_frete(150, 2)
    print(f"Frete Final Esperado (10.0): {frete}")

    print()
    print("=== TESTE PARTE 2: CUPOM E TAXAS DE ESCOPO ===", end=" ")
    preco = aplicar_cupom(100, 10)
    print(f"Preço Final Esperado (92.0): {preco}")

    print()
    print("=== TESTE PARTE 3: CRONOGRAMA RECURSIVO ===")
    exibir_cronograma_regressivo(3, 150.0)
