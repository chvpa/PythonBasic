def palindromo(palabra):
    #  Sacamos todos los espacios
    palabra = palabra.replace(' ', '')
    #  Pasamos todo a minúscula
    palabra = palabra.lower()
    #  Invertimos la palabra
    palabra_invertida = palabra[::-1]
    #  Preguntamos si palabra_invertida es igual a palabra
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__=='__main__':
    run()


