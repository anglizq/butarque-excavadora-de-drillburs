"""
ajustes.py
Valores del juego «Excavación en el Estanque de Tormentas».
El grupo pone sus propios valores en el bloque VUESTRO JUEGO.

Grupo: Grupo Nº 2 - 2º SMR B          
Componentes: Enzo Guerrero Gala, Hugo Lucio Pereyra y Angel Izquierdo 
Fecha: 28/10/2026
Módulo: CMO316 Programación en Python
"""

# ============ AJUSTES DE BASE ) ============
ANCHO = 1280               # ancho de la ventana, en píxeles
ALTO = 720                 # alto de la ventana, en píxeles
FPS = 60                   # imágenes por segundo
CASILLA = 52               # lado de cada cuadradito en la pantalla, en píxeles
REJILLA_X = 56             # dónde empieza la cuadrícula, desde la izquierda
REJILLA_Y = 118            # dónde empieza la cuadrícula, desde arriba
VER_FOSILES = False        # truco: con True se ven los huesos sin excavar

# ============ VUESTRO JUEGO ============

# --- VARIABLES ---
TITULO = "Excavación en el Estanque de Tormentas"   # str: título del juego, se ve arriba
SUBTITULO = "Encuentra los fósiles antes de quedarte sin presupuesto"  # str: frase bajo el título
FILAS = 7                  # int: filas de la cuadrícula (entre 6 y 9)
COLUMNAS = 11              # int: columnas de la cuadrícula (entre 10 y 14)
PRESUPUESTO = 300          # int: euros disponibles para la excavación
EUROS_POR_FALLO = 15.75    # float: euros que cuesta cada casilla excavada sin hueso

# --- ENTRADA ---
# int: cuántos fósiles quiere buscar el jugador (entre 2 y 10); input() devuelve texto, por eso int()
FOSILES_A_BUSCAR = int(input("¿Cuántos fósiles quieres buscar? (de 2 a 10): "))

# --- OPERACIONES ---
ZONAS = FILAS * COLUMNAS                           # casillas excavables: filas por columnas
FOSILES_SORTEADOS = FOSILES_A_BUSCAR - 1           # el colmillo sale siempre, el resto se sortea
FALLOS_PERMITIDOS = int(PRESUPUESTO / EUROS_POR_FALLO)   # fallos que caben en el presupuesto, sin decimales

# --- SALIDA ---
print("Zonas excavables:", ZONAS)
print("Fósiles que buscar:", FOSILES_A_BUSCAR)
print("Fósiles a sortear (sin contar el colmillo):", FOSILES_SORTEADOS)
print("Presupuesto:", PRESUPUESTO, "€")
print("Coste de cada fallo:", EUROS_POR_FALLO, "€")
print("Fallos permitidos:", FALLOS_PERMITIDOS)

# ============ COLORES (rojo, verde, azul, de 0 a 255 · ya están hechos) ============
FONDO = (43, 38, 32)
PAPEL = (243, 234, 216)
TINTA = (45, 38, 30)
OCRE = (217, 164, 65)
GRIS = (140, 128, 112)
VERDE = (91, 154, 91)
ROJO = (196, 85, 63)
TIERRA = [(112, 84, 58), (104, 78, 54)]
TIERRA_EXCAVADA = (196, 170, 130)
HUESO = (236, 226, 200)
HUESO_OSCURO = (176, 160, 128)
COLOR_PISTA = {1: (52, 92, 140), 2: (46, 112, 64), 3: (160, 64, 44), 4: (110, 52, 130)}
