# Un modulo es un paquete de código ya escrito para ejecutar  funciones.
import random

def run():
#       random.randint elige un numero al azar en un rango asignado.
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
#       mientras el numero_elegido sea distinto a numero_aleatorio, seguir.   
    while numero_elegido != numero_aleatorio:        
        if numero_elegido < numero_aleatorio:
            print("Elige un número más grande.")
        else:
            print("Elige un número más pequeño.")
        numero_elegido = int(input("elije otro número: "))
    print("¡Ganaste!")




if __name__ == "__main__":
    run()