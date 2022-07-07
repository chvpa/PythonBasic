
def run():
    for i in range(1000):
        if i % 2 != 0:
            continue
        print(i)

    # i = 500
    # for i in range(500):
    #     print(i)
    #     if i == 1:
    #         break

    # texto = input('Ingrese una frase: ')
    # for letra in texto:
    #     if letra == 'l':
    #         break
    #     print(letra)

    # print('Adivina la palabra secreta. \n tienes 5 intentos. >:)')

    # intentos_rev = 5
    # while intentos_rev > 0:
    #     palabra = input('¿Cual es la palabra secreta?: ')
    #     intentos_rev -= 1
    #     if palabra != 'Soy el mejor':
    #         print('Te quedan ' + str(intentos_rev) + ' intentos.')
    #     else:
    #         print('Cierto. Eres el mejor.')
    #         break
    #     if intentos_rev == 1:
    #         print('¡Ultimo intento!')
    #     if intentos_rev == 0:
    #         print('Fallaste.')



if __name__ == '__main__':
    run()