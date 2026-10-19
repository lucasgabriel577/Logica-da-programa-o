valores = [12, 45, 7, 89, 23]
indice_menor = 0
indice_maior = 0

for i in range(len(valores)):
    if valores[i] < valores[indice_menor]:
        indice_menor = i
    if valores[i] > valores[indice_maior]:
        indice_maior = i

print("=== RELATÓRIO POSICIONAL DETALHADO ===")

for i in range(len(valores)):
    status = ""
    if i == indice_menor:
        status = " <- [MENOR VALOR]"
    elif i == indice_maior:
        status = " <- [MAIOR VALOR]"
    print(f"Índice [{i}]: Valor = {valores[i]}{status}")

print("-" * 38)
print(f"Menor valor: {valores[indice_menor]} (no índice {indice_menor})")
print(f"Maior valor: {valores[indice_maior]} (no índice {indice_maior})")
