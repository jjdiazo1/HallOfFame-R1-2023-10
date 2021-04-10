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
import time
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar videos con mas views en un país correspondientes a una categoría")
    print("3- Consultar el video que más días estuvo trending en un país")
    print("4- Consultar el video que más días estuvo trending en una categoría")
    print("5- Consultar los videos con un tag especifico que tienen más likes")
    print("0- Salir")


def initCatalog(estructura):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(estructura)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def crearSubList(lista, tamanhoMuestra):

    return controller.crearSubList(lista, tamanhoMuestra)

def consultar_id(lista, categoria):

    return controller.consultar_id(lista, categoria)

def filtrar_req1(lista, sublista, id, pais):

    return controller.filtrar_req1(lista, sublista, id, pais)

def filtrar_req2(lista, sublista, pais):
    
    return controller.filtrar_req2(lista, sublista, pais)

def filtrar_req3(lista, sublista, id):

    return controller.filtrar_req3(lista, sublista, id)

def filtrar_req4(lista, sublista, tag, pais):

    return controller.filtrar_req4(lista, sublista, tag, pais)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Escoja la estructura de datos que desa utilizar para almacenamiento del repositorio: ")
        print("1. Lista por arreglos")
        print("2. Lista Enlazada")
        estructuraDatos= int(input())

        if estructuraDatos == 1:
            estructura= "ARRAY_LIST"

            print("Cargando información de los archivos ....")
            catalog = initCatalog(estructura)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
            
            videos = catalog['videos']
            video = lt.getElement(videos, 1)
            primero = (video['title'], video['channel_title'], video['trending_date'], 
            video['country'], video['views'], video['likes'], video['dislikes'])
            print("Caracteristicas del primer video cargado: ")
            print("Titulo: " + primero[0])
            print("Canal: " + primero[1])
            print("Fecha en que estuvo Trending: " + str(primero[2]))
            print("País: " + primero[3])
            print("Visitas: " + str (primero[4]))
            print("Likes: " + str (primero[5]))
            print("Dislikes: " + str (primero[6]))
            print("Categorias de videos: ")
            for x in range(1, lt.size(catalog['id_category'])+1):
                elemento= lt.getElement(catalog['id_category'], x)
                print(str (elemento["id"]) + "\t" + elemento["category"])
        
        elif estructuraDatos == 2:
            estructura= "LINKED_LIST"

            print("Cargando información de los archivos ....")
            catalog = initCatalog(estructura)
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
                
            videos = catalog['videos']
            video = lt.getElement(videos, 1)
            primero = (video['title'], video['channel_title'], video['trending_date'], 
            video['country'], video['views'], video['likes'], video['dislikes'])
            print("Caracteristicas del primer video cargado: ")
            print("Titulo: " + primero[0])
            print("Canal: " + primero[1])
            print("Fecha en que estuvo Trending: " + primero[2])
            print("País: " + primero[3])
            print("Visitas: " + primero[4])
            print("Likes: " + primero[5])
            print("Dislikes: " + primero[6])
            print("Categorias de videos: ")
            for x in range(1, lt.size(catalog['id_category'])+1):
                elemento= lt.getElement(catalog['id_category'], x)
                print(str (elemento["id"]) + "\t" + elemento["category"])

        else:
            print("Por favor escoja una opciòn válida")        



    elif int(inputs[0]) == 2:
       
       lista = catalog["videos"]

       sublista = lt.newList(datastructure="ARRAY_LIST")

       num_videos = int (input("Ingrese el número de videos que quiere que se presenten en su ranking-> "))
       if num_videos > lt.size(lista): print("El número ingresado excede el número total de videos")
        
       else:

           categoria = input ("Ingrese la categoría que quiere consultar-> ")
           id = consultar_id(catalog["id_category"], categoria)
           if id == -1: print("Por favor ingrese una categoría válida")
           else:
               pais = input("Ingrese el país que quiere consultar-> ")
               filtrar_req1(lista, sublista, id, pais)
               for pos in range(1, num_videos + 1):
                   elemento = lt.getElement(sublista, pos)

                   print("\n\nvideo " + str(pos))
                   print("trending date: " + str(elemento["trending_date"]))
                   print("title: " + elemento["title"])
                   print("channel title: " + elemento["channel_title"])
                   print("publish time: " + str (elemento["publish_time"]))
                   print("views: " + str(elemento["views"]))
                   print("likes: " + str(elemento["likes"]))
                   print("dislikes: " + str(elemento["dislikes"]))

    elif int(inputs[0]) == 3:
        
        lista = catalog["videos"]
        sublista = lt.newList(datastructure="ARRAY_LIST")

        pais = input("Ingrese el país que desea consultar-> ")
        video = filtrar_req2(lista, sublista, pais)

        print("\n\ntitle: " + str(video[0][0]))
        print("channel title: " + str(video[0][0]))
        print("country: " + str(video[0][2]))
        print("trending days: " + str(video[1]))
    
    elif int(inputs[0]) == 4:

        lista = catalog["videos"]
        sublista = lt.newList(datastructure="ARRAY_LIST")

        categoria = input("Ingrese la categoría que desea consultar-> ")

        id = consultar_id(catalog["id_category"], categoria)
        if id == -1: print("Por favor ingrese una categoría válida")
        else:
            video = filtrar_req3(lista, sublista, id)

            print("\n\ntitle: " + str(video[0][0]))
            print("channel title: " + str(video[0][0]))
            print("category id: " + str(video[0][2]))
            print("trending days: " + str(video[1]))

    elif int(inputs[0]) == 5:

        lista = catalog["videos"]
        sublista = lt.newList(datastructure="ARRAY_LIST")

        num_videos = int(input("Ingrese el numero de videos que desea consultar-> "))
        pais = input("Ingrese el país que desea consultar-> ")
        tag = input("Ingrese el tag que desea consultar-> ")

        filtrar_req4(lista, sublista, tag, pais)

        impresos = lt.newList(datastructure="ARRAY_LIST")
        pos = 1
        num = 1
        while num in range (1, num_videos + 1) and pos in range (1, lt.size(sublista) + 1):
            elemento = lt.getElement(sublista, pos)
            if lt.isPresent(impresos, elemento["title"]) == 0:
                print("\n\nvideo " + str(num))
                print("title: " + elemento["title"])
                print("channel title: " + elemento["channel_title"])
                print("publish time: " + str (elemento["publish_time"]))
                print("views: " + str(elemento["views"]))
                print("likes: " + str(elemento["likes"]))
                print("dislikes: " + str(elemento["dislikes"]))
                print("tags: " + elemento["tags"])
                lt.addLast(impresos, elemento["title"])
                num += 1
            pos += 1


    else: 
        sys.exit(0)
sys.exit(0)
