quantidade_itens = int(input("Quantidade de itens: "))
total_compra = 0

for i in range(quantidade_itens):
    preco_item = float(input(f"Preço do item {i + 1}: "))
    total_compra += preco_item
    
print(f"Total da compra: R$ {total_compra:.2f}")

