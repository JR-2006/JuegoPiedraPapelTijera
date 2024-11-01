from random import*


def selectPerson():
    '''
    Pide al usuario que dijite una de las opciones
    '''
    print()
    op = int(input("1. Piedra\n2. Papel\n3. Tijera\nPor favor escoja una de las opciones establecidas: "))
    
    
    return op



def selectCPU():
    '''
    Opciones que escoge la computadora de manera random
    '''

    cpu = choice([1, 2, 3])
    return cpu
