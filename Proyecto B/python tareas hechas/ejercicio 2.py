import random
contador = 0
suma_total = 0

tiradas = int(input("Ingrese el número de tiradas: "))
while contador < tiradas:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    print(f"Tirada {contador + 1}: Dado 1 = {dado1}, Dado 2 = {dado2}, Suma = {suma}")
    suma_total += suma
    contador += 1
print(f"Suma total de todas las tiradas: {suma_total}")

