"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

no_categorias = [
    1, 2, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24,
    25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36,
    37, 38, 39, 40, 41, 42, 43, 44]


def printMenu():
    """
    La función de PrintMenu() Muestra las cinco opciones que tiene el
    usuario para la busqueda de Videos según los requerimientos
    """
    print("\n_______________________________________________________________")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print(
        "2- Conocer cuáles son los n videos con más views que son "
        + " tendencia en un país, dada una categoría específica."
        )
    print(
        "3- Conocer cuál es el video que más días ha sido" +
        " trending para un país específico.")
    print(
        "4- Cuál es el video que más días ha sido" +
        " trending para una categoría específica.")
    print(
        "5- Conocer cuáles son los n videos diferentes con" +
        " más likes en un país con un tag específico.")
    print("0- Salir")


def initCatalog(list_type):
    """
    La función initCatalog() Inicializa el catalogo de Videos
    retornando la función correspondiente del controller
    """
    return controller.initCatalog(list_type)


def loadData(catalog):
    """
    La función LoadData() carga el catalogo de Videos en la
    estructura de datos escogida retornando la función
    correspondiente del controller
    """
    controller.loadData(catalog)


def printResults(ord_videos, sample):
    """"
    La función de printResults() nos permite imprimir
    los videos según el tamaño del sample
    la usamos para la impresión del primer
    video en la carga del catálogo y para mostrar los
    resultados del primer requerimiento
    """
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i = 1
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print("\n")
            print(
                'Título: ' + str(video.get('title')) + ", " +
                'Nombre del canal: ' + str(video.get('channel_title')) + ", " +
                'Fue tendencia el día: ' + str(video.get('trending_date'))
                + ", " +
                'Visitas: ' + str(video.get('views')) + ", " +
                'Likes: ' + str(video.get('likes')) + ", " +
                'Dislikes: ' + str(video.get('dislikes')) + ", " +
                'Fecha de publicación: ' + str(video.get('dislikes')))
            i += 1


def printResultsv2(ord_videos, sample):
    printlist = []
    i = 1
    while len(printlist) <= (sample - 1):
        element = lt.getElement(ord_videos, i)
        title = str(element.get('title'))
        if title not in printlist:
            printlist.append(title)
            print("\n")
            print(
                'Título: ' + str(element.get('title')) + ", " +
                'Nombre del canal: ' + str(element.get('channel_title'))
                + ", " + 'Visitas: ' + str(element.get('views')) + ", " +
                'Likes: ' + str(element.get('likes')) + ", " +
                'Dislikes: ' + str(element.get('dislikes')) + ", " +
                'Tags: ' + str(element.get('tags')))
        i += 1


def printResultsv3(result):
    print(
            'Título: ' + str(result[0].get('title')) + ", " +
            'Nombre del canal: ' + str(result[0].get('channel_title')) + ", " +
            'País: ' + str(result[0].get('country')) + ", " +
            'No. de días trending: ' + str(result[1]))


"""
Menu principal
"""

while True:
    printMenu()
    print('\n')
    inputs = input('Seleccione una opción para continuar: ')

    if str(inputs[0]) == "1":
        x = 'ARRAY_LIST'
        print("\nCargando información de los archivos ....")
        catalog = initCatalog(x)
        loadData(catalog)
        first = lt.firstElement(catalog['video'])
        primervideo = {
            'Título: ': str(first.get('title')),
            'Nombre del canal: ': str(first.get('channel_title')),
            'Fue tendencia el día: ': str(first.get('trending_date')),
            'Visitas: ': str(first.get('views')),
            'Likes: ': str(first.get('likes')),
            'Dislikes: ': str(first.get('dislikes'))}

        print('\nVideos cargados: ' + str(lt.size(catalog['video'])))
        print('\nDatos del primer video: ')
        for i in primervideo.keys():
            print(str(i) + str(primervideo.get(i)))
        print(
            "\n" + str(lt.size(catalog['category'])) + ' Categorías cargadas: '
            )
        i = 1
        resultadoxy = []
        while i <= int(lt.size(catalog['category'])):
            resultadoxy.append(
                lt.getElement(catalog['category'], i).get('c_id') + ":" +
                lt.getElement(catalog['category'], i).get('name'))
            i += 1
        print(*resultadoxy, sep=' ')

        lista = ''
        for i in range(0, lt.size(catalog['country'])):
            element = lt.getElement(catalog['country'], i)
            pais = str(element.get('country_name'))
            if i < (lt.size(catalog['country'])-1):
                lista += (pais.lower() + ", ")
            else:
                lista += pais.lower()
        print(
            "\n" + str(lt.size(catalog['country'])) + ' Países cargados: ',
            lista)

    elif str(inputs[0]) == "2":
        pais = input("\nIngrese el país de referencia: ")
        if pais.lower() in lista:
            categoria = int(input('Ingrese la categoría de referencia: '))
            if categoria in no_categorias:
                n = int(input(
                    "Ingrese el número de videos que desea imprimir: "))
                print("\nCargando ....")
                resultado = controller.Requerimiento_2(
                    catalog['country'], categoria, pais)
                print(
                    "Para la muestra de",
                    lt.size(catalog['country']),
                    "elementos, el tiempo (mseg) es:",
                    str(resultado[0]))
                print("\n")
                printResults(resultado[1], int(n))

            else:
                print("\n")
                print("No se encontró la Categoría")
        else:
            print("\n")
            print("No se encontró el país")

    elif str(inputs[0]) == "3":
        pais = input("Ingrese el país de referencia: ")
        print("\nCargando ....")
        lista = controller.getVideosByCountry(catalog['country'], pais)
        result = controller.sortVideos(
            lista, lt.size(lista), 'ms', 'comparetitles')[1]
        dias_tendencia = controller.getMostTrendingDays(result)
        print("\n")
        printResultsv3(dias_tendencia)

    elif str(inputs[0]) == "4":
        categoria = int(input('Ingrese la categoría de referencia: '))
        print("\nCargando ....")
        result1 = controller.getVideosByCategory(
            catalog['video'], categoria)
        result = controller.sortVideos(
            result1, lt.size(result1), 'ms', 'comparetitles')[1]

        video_tendencia = controller.getMostTrendingDays(result)
        print("\n")
        printResultsv3(video_tendencia)

    elif str(inputs[0]) == "5":
        pais = input("Ingrese el país de referencia: ")
        tag = input('Ingrese el tag de referencia: ')
        n = int(input("Ingrese el número de videos que desea imprimir: "))
        print("\nCargando ....")

        result = controller.getVideosByCountryAndTag(
             catalog['country'], tag, pais)

        print(
            "Para la muestra de",
            lt.size(catalog['country']),
            "elementos, el tiempo (mseg) es:",
            str(result[0]))

        printResultsv2(result[1], n)

    elif str(inputs[0]) == "0":
        sys.exit(0)
    else:
        print("\n")
        print("Opción No Válida")
