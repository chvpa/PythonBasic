import random
from re import I

def generar_contrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    minusculas = ['a','b','c','d','e','f','g','h','i']
    simbolos = ['!','"','#','$','%']
    numeros = ['1','2','3','4','5','6','7']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        #  choice elige un caracter al azar y lo guarda en caracteres_random
        caracteres_random = random.choice(caracteres)
        # append para agregar caracteres_random a contrasena
        contrasena.append(caracteres_random)
        # ''.join para convertir contrasena a string
    contrasena = ''.join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Your new password is: " + contrasena)



if __name__ == "__main__":
    run()