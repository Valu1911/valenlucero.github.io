usuario = input("Ingresa tu nombre de usuario: ")
vidas = int(input("Ingrese el número de vidas: "))
if vidas >= 5:
    print("Entrando al modo fácil")
elif vidas <=4 and vidas >= 3:
 print("Entrando al modo intermedio")
elif vidas <= 2 and vidas >= 1:
 print("Entrando al modo difícil")
else:
 print("No tienes vidas, fin del juego")