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
from DISClib.Algorithms.Sorting import mergesort 

assert cf


# Construccion de modelos

def newCatalog(list_type = "ARRAY_LIST"):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """

    catalog={"videos":None,
            "categories": None}

    catalog["videos"]=lt.newList()
    catalog["categories"]=lt.newList(list_type,None)
    catalog["countries"]=lt.newList(list_type,None)
    return catalog



# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """Añade un video al catalogo principal."""
    
    # Se modifica el video antes de que este sea añadido al catalogo principal
    #Esto con el objetivo de añadirle una columna que indique el nombre de su categoría
    video = addVideoCategory(catalog, video)

    # Se adiciona el video modificado a la lista de videos
    lt.addLast(catalog['videos'], video)

    #Se agrega el pais una vez a la lista countries
    country = video["country"]

    if lt.isPresent(catalog["countries"], country) == 0:
        lt.addLast(catalog["countries"], country)


def addCategory(catalog, category):
    """
    Adiciona unas category a la lista de categories dentro del catalogo principal.
    """
    t=newCategory(category["name"], category["id"])
    lt.addLast(catalog["categories"], t)

def addVideoCategory(catalog, video):
    """Relaciona el nombre de una categoría con un ID y lo agrega el nombre como una nueva columna al video."""

    video_category = newVideoCategory(catalog["categories"], video)
    video["category_name"] = video_category
    return video



# Funciones para creacion de datos

def newCategory(name, id):
    """
    Esta estructura almancena las categories utilizadas para marcar videos.
    """

    category={}
    category["name"]=name
    category["category_id"]=id
    return category


def newVideoCategory(catalog_category, video):
    """
    Esta estructura crea una relación entre un tag y
    los videos """

    category_id = video["category_id"]

    for category_dict in lt.iterator(catalog_category):
        
        if category_dict["category_id"] == category_id:

            category_name = category_dict["name"]

    return  category_name

def newUniqueCatalog(catalog):

    """Genera un nuevo catálogo en el que cada video (por título invidual) solo se incluye una vez."""

    unique_dict = {"videos": None}
    unique_dict["videos"] = {}
    unique_catalog = lt.newList("ARRAY_LIST")
    pos = 0
    for video in lt.iterator(catalog):
        pos += 1
        try:    
            video_info = unique_dict["videos"][video["title"]]
            new_day = lt.getElement(video_info, 1) + 1
            lt.changeInfo(video_info, 1, new_day)
        except Exception: 
            
            unique_dict["videos"][video["title"]] = lt.newList("ARRAY_LIST")
            lt.addLast(unique_dict["videos"][video["title"]], 1)
            lt.addLast(unique_dict["videos"][video["title"]], pos)
            lt.addLast(unique_dict["videos"][video["title"]], video)

    for i in unique_dict["videos"]:
        lt.addLast(unique_catalog, unique_dict["videos"][i]["elements"])


    return unique_catalog



# Funciones de consulta

def filterCatalog(catalog, column_1, value_1, column_2=None, value_2=None):
    """Filtra el catalogo dejando solo los videos con el valor especificado para máximo 2 columnas.
        determinadas."""


    filtered_catalog = lt.newList("ARRAY_LIST")
    filtered_catalog["videos"] = lt.newList("ARRAY_LIST")

    for video in lt.iterator(catalog['videos']):
        
        if column_2 is not None:  
            
            if video[column_1] == " "+value_1 and video[column_2] == value_2:
    
                lt.addLast(filtered_catalog["videos"], video)
        else:
            if video[column_1] == value_1:
                lt.addLast(filtered_catalog["videos"], video)
          
   
    return filtered_catalog


def filterTag(catalog, tag):
    """Filtra el catalogo obteniendo uno reducido en el que solo se incluyan los videos que
       contengan el tag especificado."""

    filter_tags=lt.newList("ARRAY_LIST")
    filter_tags["videos"]=lt.newList("ARRAY_LIST")

    for video in lt.iterator(catalog['videos']):

        video_tags=video["tags"]
        
        if tag in video_tags:
            lt.addLast(filter_tags["videos"], video)
               

    return filter_tags




# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) > float(video2['views']))

def cmpVideosByDays(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor de dias en la posición 0 
    video2: informacion del segundo video que incluye su valor de dias en la posición 0 
    """
    return (float(video1[0]) > float(video2[0]))

def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'LIKES' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'LIKES'
    video2: informacion del segundo video que incluye su valor 'LIKES'
    """
    return (float(video1["likes"]) > float(video2["likes"]))

# Funciones de ordenamiento

def sortVideos(catalog, size, cmpFunction):
    """Función que organiza una lista mediante Merge Sort. 

    Parametros:
        catalog: Catalogo a organizar
        size: Tamaño del sub-catalogo que será organizado
        cmpFunction: Nombre de la función de comparación a utilizar."""


    if cmpFunction == "sortByViews":
        sub_list = lt.subList(catalog['videos'], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list = mergesort.sort(sub_list, cmpVideosByViews)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

    elif cmpFunction == "sortByDays":
        sub_list = lt.subList(catalog, 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list = mergesort.sort(sub_list, cmpVideosByDays)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

    elif cmpFunction == "sortByLikes":

        sub_list = lt.subList(catalog['videos'], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list = mergesort.sort(sub_list, cmpVideosByLikes)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list    
