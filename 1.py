contador = 0

numero = int(input("digite um número(0 pra parar): "))

while numero != 0:
    if numero % 2 ==0:
        contador = contador + 1
    numero = int(input("digite um número(0 pra parar): "))
print("Quantidade de numeros pares:", contador)