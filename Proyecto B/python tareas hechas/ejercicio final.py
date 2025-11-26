import pygame
import random

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
AZUL_CLARO = (50, 150, 200)
LILA = (156, 70, 255)

# Dimensiones
ANCHO = 640
ALTO = 480

# Inicialización de Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Dados")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)

#  --- CONFIGURACIÓN DE MÚSICA ---
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Valen\\Desktop\\valen desarrollo videojuegos 2025\\sonidos\\fondo.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
#  --- FIN CONFIGURACIÓN DE MÚSICA ---

# Carga de imágenes de dados
imagenes_dados = [pygame.image.load(f"C:\\Users\\Valen\\Desktop\\valen desarrollo videojuegos 2025\\imagenes\\dados\\dado{i}.png") for i in range(1, 7)]

# mascota
imagen_mascota = pygame.image.load("C:\\Users\\Valen\\Desktop\\valen desarrollo videojuegos 2025\\imgs\\mascota.png")  # Cambia la ruta a la imagen

# Variables del juego
jugador_dados = []
cpu_dados = []
jugador_suma = 0
cpu_suma = 0
turno = "jugador"
resultado = ""

dado_animando = False
tiempo_animacion = 0
dado_random = 1

cpu_animando = False
tiempo_cpu_animacion = 0

def reiniciar_juego():
    global jugador_dados, cpu_dados, jugador_suma, cpu_suma, turno, resultado, dado_animando, tiempo_animacion, cpu_animando, tiempo_cpu_animacion, dado_random
    jugador_dados = []
    cpu_dados = []
    jugador_suma = 0
    cpu_suma = 0
    turno = "jugador"
    resultado = ""
    dado_animando = False
    tiempo_animacion = 0
    cpu_animando = False
    tiempo_cpu_animacion = 0
    dado_random = 1

def tirar_dado():
    return random.randint(1, 6)   # Devuelve un número entre 1 y 6

def turno_jugador():
    global jugador_suma, turno, dado_animando, tiempo_animacion, dado_random, jugador_dados
    if jugador_suma < 10 and not dado_animando:
        valor = tirar_dado()
        jugador_dados.append(valor)
        jugador_suma += valor
        dado_random = valor
        dado_animando = True
        tiempo_animacion = pygame.time.get_ticks()

    if jugador_suma >= 10:
        turno = "cpu"

def turno_cpu():
    global cpu_suma, turno, cpu_animando, tiempo_cpu_animacion, dado_random, cpu_dados
    if not cpu_animando:
        if cpu_suma < 10:
            debe_tirar = False
            if cpu_suma < 6:
                debe_tirar = True
            elif cpu_suma < 9 and jugador_suma > cpu_suma:
                debe_tirar = random.choice([True, False])
            if debe_tirar:
                dado_random = random.randint(1, 6)
                cpu_animando = True
                tiempo_cpu_animacion = pygame.time.get_ticks()
            else:
                evaluar_ronda()
        else:
            evaluar_ronda()
    else:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_cpu_animacion >= 800:
            cpu_dados.append(dado_random)
            cpu_suma += dado_random
            cpu_animando = False
            if cpu_suma >= 10 or len(cpu_dados) >= 10:
                evaluar_ronda()

def evaluar_ronda():
    global resultado, turno, jugador_suma, cpu_suma
    if jugador_suma > 10 and cpu_suma > 10:  
        resultado = "¡Empate! Los dos se pasaron."
    elif jugador_suma > 10:
        resultado = "CPU gana (Te pasaste mal ahi)."
    elif cpu_suma > 10:
        resultado = "Ganaste (CPU se pasó)."
    elif jugador_suma > cpu_suma:
        resultado = "¡Jugador gana!"
    elif cpu_suma > jugador_suma:
        resultado = "CPU gana."
    else:
        resultado = "¡Empate!"
    turno = "fin"

def dibujar_dado(x, y, valor, tamaño=60):
    imagen = pygame.transform.scale(imagenes_dados[valor - 1], (tamaño, tamaño))
    pantalla.blit(imagen, (x, y))

def dibujar_juego():
    pantalla.fill(LILA)

    # Dados jugador
    for i, valor in enumerate(jugador_dados):
        dibujar_dado(50 + i * 70, 100, valor)

    # Dados CPU
    for i, valor in enumerate(cpu_dados):
        dibujar_dado(50 + i * 70, 300, valor)

    # Mostrar animación actual
    if turno == "jugador" and dado_animando:
        dibujar_dado(ANCHO // 2 - 40, 100, dado_random, 80)
    elif turno == "cpu" and cpu_animando:
        dibujar_dado(ANCHO // 2 - 40, 320, dado_random, 80)

    # Mostrar suma
    texto_j = fuente.render(f"Jugador: {jugador_suma}", True, BLANCO)
    texto_c = fuente.render(f"CPU: {cpu_suma}", True, BLANCO)
    pantalla.blit(texto_j, (50, 50))
    pantalla.blit(texto_c, (50, 250))

    # Dibuja la imagen de la mascota 
    imagen_mascota_scaled = pygame.transform.scale(imagen_mascota, (170, 170))  
    pantalla.blit(imagen_mascota_scaled, (400, 90))  
    # Botones
    if turno == "jugador" and jugador_suma < 10 and not dado_animando:
        pygame.draw.rect(pantalla, VERDE, (400, 260, 170, 50))  # Botón TIRAR DADO
        texto = fuente.render("TIRAR DADO", True, BLANCO)
        pantalla.blit(texto, (410, 270))

        pygame.draw.rect(pantalla, ROJO, (400, 330, 170, 50))   # Botón PLANTARSE
        texto = fuente.render("PLANTARSE", True, BLANCO)
        pantalla.blit(texto, (410, 340))

    # Resultado final
    if turno == "fin":
        texto_r = fuente.render(resultado, True, BLANCO)
        pantalla.blit(texto_r, (ANCHO // 2 - texto_r.get_width() // 2, 400))

def manejar_eventos():
    global turno
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if turno == "jugador" and not dado_animando:
                if 400 <= x <= 550 and 260 <= y <= 310:  # Botón TIRAR DADO
                    turno_jugador()
                elif 400 <= x <= 550 and 330 <= y <= 380:  # Botón PLANTARSE
                    turno = "cpu"
            if turno == "fin":
                reiniciar_juego()
    return True

def actualizar():
    global dado_animando, tiempo_animacion, turno
    tiempo_actual = pygame.time.get_ticks()
    if dado_animando and tiempo_actual - tiempo_animacion > 800:
        dado_animando = False
        if jugador_suma >= 10:
            turno = "cpu"
    if turno == "cpu":
        turno_cpu()

# Bucle principal
corriendo = True
while corriendo:
    corriendo = manejar_eventos()
    actualizar()
    dibujar_juego()
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()