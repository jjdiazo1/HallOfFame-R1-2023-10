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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import shellsort as she
from DISClib.Algorithms.Sorting import quicksort as qui
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
                'categories': None}
    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = lt.newList('ARRAY_LIST', cmpfunction=comparecatnames)
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """Agrega un video al final del catalogo
    Parametros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.

        video: diccionario con la informacion
        del video 
    """
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    """Agrega un video al final de la lista de categorias en el catalogo
    Parametros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.

        categoria: diccionario con la informacion
        de la categoria 
    """
    c = newCategory(category['name'], category['id'])
    lt.addLast(catalog['categories'], c)

# Funciones para creacion de datos

def newCategory(category_name, category_id):
    """Se crea un nuevo diccionario para cada categoria en el cual se guarda el id y el nombre de la categoria
    Return:
        Un diccionario con la informacion de la categoria.
    """
    category = {'category_name': '', 'category_id': ''}
    category['category_name'] = category_name.lower()
    category['category_id'] = category_id
    return category

# Funciones de consulta/filtrado

def filtrado_pais(catalog, pais):
    """ Filtra los datos y hace una lista nueva
    con los datos del pais ingresado.

    Parámetros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.
        
        pais: el país ingresado por el usuario.
    
    Return:
        Una lista con la información del pais
        ingresado.
    """
    lista_pais = lt.newList("ARRAY_LIST")
    for video in lt.iterator(catalog["videos"]):
        if video["country"] == pais:
            lt.addLast(lista_pais, video)
    return lista_pais

def filtrado_categoria(lista, categoria):
    """ Filtra los datos y hace una lista nueva
    con los datos de la categoría ingresada.

    Parámetros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.
        
        categoria: la categoría ingresada por el usuario.
    
    Return:
        Una lista con la información de la categoría
        ingresada.
    """
    lista_filt_cat= lt.newList("ARRAY_LIST")
    for video in lt.iterator(lista):
        if video["category_id"] == categoria:
            lt.addLast(lista_filt_cat,video)
    return lista_filt_cat

def filtrado_tags(lista, tag):
    """ Filtra los datos y hace una lista nueva
    con los datos del pais y del tag ingreado.

    Parámetros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.

        tag: el tag ingresado por el usuario.
        
        pais: el país ingresado por el usuario.
    
    Return:
        Una lista con la información del pais y
        del tag ingresado.
    """
    lista_tags_y_pais = lt.newList('ARRAY_LIST')
    for video in lt.iterator(lista):
        tags = video['tags']
        if (tag in tags):
            lt.addLast(lista_tags_y_pais, video)
    return lista_tags_y_pais

def idCat(catalog,categoria):
    """
    Encuentra el id de la categoria que entra por parametro
    Parámetros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.
        
        categoria: nombre de la categoria en la cual el usuario desea hacer su busqueda
    Return:
        el int que corresponde a la categoria ingresada por parametro.

        """
    num_cat = None
    for kategorien in lt.iterator(catalog["categories"]):
        if categoria == kategorien["category_name"]:
            num_cat = kategorien["category_id"]
    return num_cat

def trending(videos_ordenados):
    """ Recorre la lista ordenada y cuenta cuántas
        veces se repite un id. La condición: si se 
        encuentran dos videos con el mismo id, 
        el contador aumenta, sino, no.

    Parámetros:
        videos_ordenados: es la lista ordenada que 
        se va a recorer.
    
    Return:
        Una tupla en la que la primera posición
        es las veces que apareció en la lista
        (días en trending) y la segunda posisición
        es el video que estuvo más días en trending.
    """    
    posicion = 0
    veces = 1
    mayor = 1
    size = lt.size(videos_ordenados)
    i = 0
    while i < size:
        if i != size:
            id_video = lt.getElement(videos_ordenados, i)
            id_video_2 = lt.getElement(videos_ordenados, i + 1)
            
            if (id_video['title'] == id_video_2['title']) :
                if (id_video['trending_date'] != id_video_2['trending_date']):
                    veces += 1
            else: 
                if veces > mayor:
                    mayor = veces
                    posicion = i
                veces = 1
            i += 1
        else:
            if i == size:
                break
    
    video = lt.getElement(videos_ordenados, posicion)
    return (mayor, video)

def trending_2(videos_ordenados):
    """ Recorre la lista ordenada y cuenta cuántas
        veces se repite un id. La condición: si se 
        encuentran dos videos con el mismo id, 
        el contador aumenta, sino, no.

    Parámetros:
        videos_ordenados: es la lista ordenada que 
        se va a recorer.
    
    Return:
        Una tupla en la que la primera posición
        es las veces que apareció en la lista
        (días en trending) y la segunda posisición
        es el video que estuvo más días en trending.
    """    
    posicion = 0
    veces = 1
    mayor = 1
    size = lt.size(videos_ordenados)
    i = 0
    while i < size:
        if i != size:
            id_video = lt.getElement(videos_ordenados, i)
            id_video_2 = lt.getElement(videos_ordenados, i + 1)
            
            if (id_video['video_id'] == id_video_2['video_id']):
                    veces += 1
            else: 
                if veces > mayor:
                    mayor = veces
                    posicion = i
                veces = 1
            i += 1
        else:
            if i == size:
                break
    
    video = lt.getElement(videos_ordenados, posicion)
    return (mayor, video)

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecatnames(category_name, category):
    """ Compara el nombre de la categoria 
        que entra por parámetro con uno de los
        que ya se encuentran en el catálogo.

    Parámetros:
        category_name: nombre del categoría.

        category: el catálogo.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si category_name
        es igual a la categoría en el catálogo).
    """
    return (category_name == category['category_name'])
 
def compareviews(video1, video2):
    """ Compara el número de 'views' que tiene
        un video.

    Parámetros:
        video1: es una lista de videos de donde se 
        ven los views para comparar.

        video2: es una lista de videos de donde se 
        ven los views para comparar.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si las 'views'
        del video1 son mayores que las del video2).
    """
    result = (video1["views"] > video2["views"])
    return result

def comparetitle(video1, video2):
    """ Compara el 'title' que tiene un video.

    Parámetros:
        video1: es una lista de videos de donde se 
        ve el título para comparar.

        video2: es una lista de videos de donde se 
        ve el título para comparar.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si el 'título'
        del video1 es 'mayor' al del video2).
    """
    result = (video1['title'] > video2['title'])
    return result

def comparedates(video1, video2):
    """ Compara la fecha de trending que tiene un video.

    Parámetros:
        video1: es una lista de videos de donde se 
        ve la fecha para comparar.

        video2: es una lista de videos de donde se 
        ve la fecha para comparar.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si la fecha
        del video1 es menor que la del video2).
    """
    result = video1['trending_date'] < video2['trending_date']
    return result

def comparelikes(video1, video2):
    """ Compara el número de 'likes' que tiene
        un video.

    Parámetros:
        video1: es una lista de videos de donde se 
        ven los likes para comparar.

        video2: es una lista de videos de donde se 
        ven los likes para comparar.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si los 'likes'
        del video1 son mayores que los del video2).
    """
    result = (int(video1['likes']) > int(video2['likes']))
    return result

def compareids(video1, video2):
    """ Compara el id que tiene un video.

    Parámetros:
        video1: es una lista de videos de donde se 
        ve el id para comparar.

        video2: es una lista de videos de donde se 
        ve el id para comparar.
    
    Return:
        Un booleano que indica si sí se cumple la
        condición (en este caso, True si el id
        del video1 es mayor que el del video2).
    """
    result = video1['video_id'] > video2['video_id']
    return result

def lista(catalog):
    """ Retorna la lista de los videos
    
    Parámetros:
        catalog: el catálogo principal creado
        en la función 'newCatalog()'.

    Return: 
        La lista de los videos que se encuentra dentro del catalogo
    """
    lista = catalog["videos"]
    return lista

# Funciones de ordenamiento

def sortVideos(lista):
    """ Función sort para ordenar los videos con
        las condiciones de la cmpfunction. En este
        caso, la función de comparación es:
                    compareviews().

    Parámetros:
        lista: es la lista que se va a ordenar.
    
    Return:
        Una tupla en la que la primera posición
        es el tiempo que tarde la función en ordenar
        y la segunda posición es la lista ordenada.
    """
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = mer.sort(sub_list, compareviews)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortVideosReq2(lista):
    """ Función sort para ordenar los videos con
        las condiciones de la cmpfunction. En este
        caso, la función de comparación es:
                    compareids().

    Parámetros:
        lista: es la lista que se va a ordenar.
    
    Return:
        Una tupla en la que la primera posición
        es el tiempo que tarde la función en ordenar
        y la segunda posición es la lista ordenada.
    """
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = mer.sort(sub_list, compareids)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortVideosReq3(lista):
    """ Función sort para ordenar los videos con
        las condiciones de la cmpfunction. En este
        caso, la función de comparación es:
                    comparetitle().

    Parámetros:
        lista: es la lista que se va a ordenar.
    
    Return:
        Una tupla en la que la primera posición
        es el tiempo que tarde la función en ordenar
        y la segunda posición es la lista ordenada.
    """
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = mer.sort(sub_list, comparetitle)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortDate(lista):
    """ Función sort para ordenar los videos con
        las condiciones de la cmpfunction. En este
        caso, la función de comparación es:
                    comparedates().

    Parámetros:
        lista: es la lista que se va a ordenar.
    
    Return:
        Una tupla en la que la primera posición
        es el tiempo que tarde la función en ordenar
        y la segunda posición es la lista ordenada.
    """
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = mer.sort(sub_list, comparedates)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def sortVideosReq4(lista):
    """ Función sort para ordenar los videos con
        las condiciones de la cmpfunction. En este
        caso, la función de comparación es:
                    comparelikes().

    Parámetros:
        lista: es la lista que se va a ordenar.
    
    Return:
        Una tupla en la que la primera posición
        es el tiempo que tarde la función en ordenar
        y la segunda posición es la lista ordenada.
    """
    size = lt.size(lista)
    sub_list = lt.subList(lista,0,size)
    sub_list = sub_list.copy()
    t1 = time.process_time()
    sorted_list = qui.sort(sub_list, comparelikes)
    t2 = time.process_time()
    tiempo_ms = (t2-t1)*1000
    sub_list = None
    return (tiempo_ms, sorted_list)

def limpieza(lista):
    """ Esta funcion recibe como parametro cualquier
        tipo de dato que es requerido temporalmente
        y lo retorna none para evitar que se llene
        la memoria RAM
    """
    lista = None
    return lista