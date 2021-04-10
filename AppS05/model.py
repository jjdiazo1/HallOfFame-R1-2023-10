"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from datetime import datetime
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sha
from DISClib.Algorithms.Sorting import insertionsort as ia
from DISClib.Algorithms.Sorting import selectionsort as sa
from DISClib.Algorithms.Sorting import quicksort as qk
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(estructura):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'id_category':None}

    catalog['videos'] = lt.newList(estructura)
    catalog['id_category'] = lt.newList(estructura)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    
    dic = {}
    dic ["video_id"] = video ["video_id"]
    dic ["trending_date"] = datetime.strptime (video ["trending_date"], "%y.%d.%m").date ()
    dic ["title"] = video ["title"]
    dic ["channel_title"] = video ["channel_title"]
    dic ["category_id"] = int (video ["category_id"])
    dic ["publish_time"] = datetime.strptime (video ["publish_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    dic ["tags"] = video ["tags"]
    dic ["views"] = int (video ["views"])
    dic ["likes"] = int (video ["likes"])
    dic ["dislikes"] = int (video ["dislikes"])
    dic ["country"] = video ["country"]

    lt.addLast(catalog['videos'], dic)



def addCategory(catalog, category):

    lista = category["id\tname"].split()

    info = {}
    info ["id"] = int (lista [0])

    info ["category"] = " ".join(lista[1:len(lista)])

    lt.addLast(catalog['id_category'], info)

  
# Funciones para creacion de datos

# Funciones de consulta
def crearSubList(lista, tamanhoMuestra):

   return lt.subList(lista, 1, tamanhoMuestra)

def consultar_id(lista, categoria):

    id = -1

    for pos in range(lt.size(lista) + 1):
        elemento = lt.getElement(lista, pos)

        if elemento["category"] == categoria:
            id = elemento["id"]
            pos = lt.size(lista) + 1

    return id

def filtrar_req1(lista, sublista, id, pais):

    for pos in range(1, lt.size(lista) + 1):
        elemento = lt.getElement(lista, pos)

        if (elemento ["country"] == pais) and (elemento ["category_id"] == id): lt.addLast(sublista, elemento)
    
    quickSort(sublista, cmpVideosByViewsMayor)

def filtrar_req2(lista, sublista, pais):

    for pos in range(1, lt.size(lista) + 1):
        elemento = lt.getElement(lista, pos)

        if elemento ["country"] == pais: lt.addLast(sublista, elemento)

    quickSort(sublista, cmpVideosByID)

    fechas= lt.newList(datastructure="ARRAY_LIST")
    id= None
    masDiastrending = 0
    diastrending = 0
    video = None
    videoMastrending = None

    for pos in range(1, lt.size(sublista) + 1):
        elemento = lt.getElement(sublista, pos)

        if id != elemento["video_id"]:

            if diastrending > masDiastrending:
                videoMastrending = video
                masDiastrending = diastrending
 

            video = (elemento["title"], elemento["channel_title"], elemento["country"])
            id = elemento["video_id"]
            fechas = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(fechas, elemento["trending_date"])
            diastrending = 1 

        elif lt.isPresent(fechas, elemento["trending_date"]) == 0:

            lt.addLast(fechas, elemento["trending_date"])
            diastrending += 1

    return (videoMastrending, masDiastrending)

def filtrar_req3(lista, sublista, id):

    for pos in range(1, lt.size(lista) + 1):
        elemento = lt.getElement(lista, pos)

        if elemento ["category_id"] == id: lt.addLast(sublista, elemento)

    mergeSort(sublista, cmpVideosByID)

    fechas= lt.newList(datastructure="ARRAY_LIST")
    ID= None
    masDiastrending = 0
    diastrending = 0
    video = None
    videoMastrending = None

    for pos in range(1, lt.size(sublista) + 1):
        elemento = lt.getElement(sublista, pos)

        if ID != elemento["video_id"]:

            if diastrending > masDiastrending:
                videoMastrending = video
                masDiastrending = diastrending
 

            video = (elemento["title"], elemento["channel_title"], elemento["category_id"])
            ID = elemento["video_id"]
            fechas = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(fechas, elemento["trending_date"])
            diastrending = 1 

        elif lt.isPresent(fechas, elemento["trending_date"]) == 0:

            lt.addLast(fechas, elemento["trending_date"])
            diastrending += 1

    return (videoMastrending, masDiastrending)

def filtrar_req4(lista, sublista, tag, pais):
    for pos in range(1, lt.size(lista) + 1):
        elemento = lt.getElement(lista, pos)

        if (tag in elemento ["tags"]) and (pais == elemento ["country"]): lt.addLast(sublista, elemento)

    quickSort(sublista, cmpVideosByLikes)
    

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):

    valor= None
    if video1["views"] < video2["views"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByViewsMayor(video1, video2):

    valor= None
    if video1["views"] > video2["views"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByID(video1, video2):

    valor= None
    if video1["video_id"] > video2["video_id"]:
        valor= True
    
    else:
        valor= False

    return valor

def cmpVideosByLikes(video1, video2):

    valor= None
    if video1["likes"] > video2["likes"]:
        valor= True
    
    else:
        valor= False

    return valor
# Funciones de ordenamiento

def insertionSort(sublista, cmpfunction):
    
    ia.sort(sublista, cmpfunction)

def selectionSort(sublista, cmpfunction):

    sa.sort(sublista, cmpfunction)

def shellSort(sublista, cmpfunction):

    sha.sort(sublista, cmpfunction)

def quickSort(sublista, cmpfunction):

    qk.sort(sublista, cmpfunction)

def mergeSort(sublista, cmpfunction):

    mg.sort(sublista, cmpfunction)
