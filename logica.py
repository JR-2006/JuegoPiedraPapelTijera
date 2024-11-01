from seleccion import *


def iniciarJuego():
    cpu = selectCPU()
    op = selectPerson()


    #Ganar
    if  op == 1 and cpu == 3:
        print("Computadora esocoje TIJERA")
        print("Gana usuario")

    elif op == 2 and cpu == 1:
        print("Computadora escoge PIEDRA")
        print("Gana usuario")

    elif op == 3 and cpu == 2:
        print("Computadora escoje PAPEL")
        print("Gana usuario")

    #Empate
    elif op == 1 and cpu == 1:
        print("Computadora escoge PIEDRA")
        print("Empate")

    elif op == 2 and cpu == 2:
        print("Computadora escoje PAPEL")
        print("Empate")

    elif op == 3 and cpu == 3:
        print("Computadora esocoje TIJERA")
        print("Empate")


    #Pierde
    elif cpu == 1 and op == 3:
        print("Computadora escoge PIEDRA")
        print("Gana computadora")

    elif cpu == 2 and op == 1:
        print("Computadora escoje PAPEL")
        print("Gana computadora")
    
    elif cpu == 3 and op == 2:
        print("Computadora esocoje TIJERA")
        print("Gana computadora")