def conversor(tipo_peso, valor_dolar):
    guaranies = input("¿Cuántos " + tipo_peso + " quieres convertir a dólares?: ")
    guaranies = float(guaranies)
    dolares = guaranies / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Entonces, tienes " + dolares + " dólares.")   
menu = """
Bienvenidos al conversor de Monedas de PIPO 😊

1 - Guaranies
2 - Pesos Argentinos
3 - Reales

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("guaranies", 6900)
elif opcion == 2:
    conversor("pesos argentinos", 65)
elif opcion == 3:
    conversor("reales", 4.77)
else:
    print("Ingrese un número correcto: ")
