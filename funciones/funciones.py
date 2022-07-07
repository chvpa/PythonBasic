#def sirve para declarar una funcion.

# def imprimir_mensaje():
#     print("mensaje especial ")
#     print("aprendiendo a usar funciones ")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

#               Parametros.

# Son variables dentro de la funcion "mensaje" en este caso.

# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estas?')
#     print(mensaje)
# #conversacion(variables de mensaje)
# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1.')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2.')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3.')
# else:
#     print('Escribe la opción correcta.')

def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
   #    return significa: devuelve. Cuando la funccion
   #    se termine de ejecutar, la variable resultado va
   #    a hacer regresar.
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)

