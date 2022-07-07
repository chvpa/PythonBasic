# Un diccionario es una estructura de datos de llaves (indice) y valores.
def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    poblacion_paises = {
        "argentina": 4445444,
        "brasil": 45465444,
        "colombia": 15451554,
    }
    # print(poblacion_paises["brasil"])

#       El metodo .keys devuelte el nombre de las llaves
    # for pais in poblacion_paises.keys():
    #     print(pais)

#       El metodo .values devuelve los valores dentro de las llaves.
    # for pais in poblacion_paises.values():
    #     print(pais)

#       El metodo .items devuelve los nombres y valores.
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes.")
if __name__ == "__main__":
    run()