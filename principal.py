import os
from logica import*
os.system('cls')
print('Bienvendo al juego Piedra papel o tijera.')
print('1. A continuacion jugara con la computadora, donde se definira un ganador.') 
print('2. EL usuario puede ingresar hasta cuantas rondas jugar.')

#Puntuacion
rondas = int(input("Dijite las rondas para jugar: "))

while rondas > 0:
    iniciarJuego()
    rondas -= 1