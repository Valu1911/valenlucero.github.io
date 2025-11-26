input("ingrese su nombre de usuario: ")
for i in range(1, 6):
    
    vidas = int(input("Ingrese el número de vidas: "))
    if vidas >= 5:
        print("Entrando al modo fácil")
    elif vidas <=4 and vidas >= 3:
     print("Entrando al modo intermedio")
    elif vidas <= 2 and vidas >= 1:
     print("Entrando al modo difícil")
   