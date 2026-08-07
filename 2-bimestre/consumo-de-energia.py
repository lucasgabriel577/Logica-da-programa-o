total_consumo = 0.0
alertas_alto_consumo = 0

for dia in range(1, 8):
    consumo = float(input(f"Dia {dia}: informe o consumo em kWh: "))
    total_consumo += consumo
    if consumo > 20:
        alertas_alto_consumo += 1

print(f"Consumo total da semana: {total_consumo:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {alertas_alto_consumo}")
