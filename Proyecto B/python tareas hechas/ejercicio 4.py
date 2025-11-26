import random
def jugar_dados(tiradas):
    total = 0
    for i in range(tiradas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
    
        suma = dado1 + dado2
        print(f"Tirada {i+1}: Dado 1 = {dado1}, Dado 2 = {dado2}, Suma = {suma}")
        total += suma
    return total
tiradas = int(input("¿Cuántas veces quieres tirar los dados cada jugador? "))

print("Jugador 1:")
total_jugador1 = jugar_dados(tiradas)
print(f"Total del Jugador 1: {total_jugador1}\n")

print("Jugador 2:")
total_jugador2 = jugar_dados(tiradas)   
print(f"Total del Jugador 2: {total_jugador2}\n")

if total_jugador1 > total_jugador2:
     print("¡Jugador 1 gana!")
elif total_jugador2 > total_jugador1:
     print("¡Jugador 2 gana!")
else:
     print("¡Es un empate!")