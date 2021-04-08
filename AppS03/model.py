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
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.DataStructures import listiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""



# Construccion de modelos



def newCatalog():

    catalog = {"videos" : None, "categories" : None}
    catalog["videos"] = lt.newList("ARRAY_LIST", cmpfunction=comparevideos)
    catalog["categories"] = lt.newList("ARRAY_LIST", cmpfunction=comparecategories)

    return catalog 



# Funciones para agregar informacion al catalogo



def addVideo(catalog, videoname):

    lt.addLast(catalog["videos"], videoname)
    
def addCategory(catalog, category):

    c = newCategory(category["name"], category["id"])
    lt.addLast(catalog["categories"], c)



# Funciones para creacion de datos
    


def newCategory(name, id):

    category = {"category_name": "", "category_id": ""}
    category["category_name"] = name
    category["category_id"] = id
    return category



# Funciones de consulta



def firstVideo (catalog):

    lista = catalog["videos"]
    primer_video = lt.firstElement(lista)
    title = primer_video["title"]
    channel = primer_video["channel_title"]
    trending_date = primer_video["trending_date"]
    country = primer_video["country"]
    views = primer_video["views"]
    likes = primer_video["likes"]
    dislikes = primer_video["dislikes"]

    video = {"title": title, "channel_title": channel, "trending_date": trending_date, "country": country, "views": views, "likes": likes, "dislikes": dislikes}

    return video



# Funciones utilizadas para comparar elementos dentro de una lista



def comparevideos(videotitle1, video):

    if (videotitle1.lower() in video["title"].lower()):
        return -1
    else:
        return 0

def comparecategories(name, category):

    if (name==category["category_name"]):
        return 0
    elif (name<category["category_name"]):
        return -1
    else:
        return 1

def compVideoByViews(video1, video2):

    return (float(video1['views']) > float(video2['views']))

def compVideoByTitle (video1, video2):

    return (str(video1['title']) < str(video2['title']))

def compVideoByLikes(video1, video2):

    return (float(video1['likes']) > float(video2['likes']))



# Funciones de ordenamiento



def sortVideosByViews (catalog, category, country):

    start_time = time.process_time()

    sublistcategories = lt.newList("ARRAY_LIST")

    iterator1 = it.newIterator(catalog["categories"])
    while it.hasNext(iterator1):
        element = it.next(iterator1)
        category_name = (element["category_name"]).lstrip()

        if (category_name.lower()) == (category.lower()):
            category_id = element["category_id"]

    iterator2 = it.newIterator(catalog["videos"])
    while it.hasNext(iterator2):
        element = it.next(iterator2)
        if element["category_id"] == category_id:
            lt.addLast(sublistcategories, element)

    sublistcountries = lt.newList("ARRAY_LIST")

    iterator3 = it.newIterator(sublistcategories)
    while it.hasNext(iterator3):
        element = it.next(iterator3)
        if (element["country"].lower()) == (country.lower()):
            lt.addLast(sublistcountries, element)

    sorted_list = merge.sort(sublistcountries, compVideoByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def sortVideosCountryTrending (catalog, country):

    start_time = time.process_time()

    sublistcountries = lt.newList("ARRAY_LIST")

    iterator1 = it.newIterator(catalog["videos"])
    while it.hasNext(iterator1):
        element = it.next(iterator1)
        if (element["country"].lower()) == (country.lower()):
            lt.addLast(sublistcountries, element)

    sorted_list_titles = merge.sort(sublistcountries, compVideoByTitle)

    video_id = ""
    days = 0
    days_max = 0
    video_id_max = "" 
    channel = ""
    channel_max = ""
    title = ""
    title_max = ""

    iterator2 = it.newIterator(sorted_list_titles)
    while it.hasNext(iterator2):
        element = it.next(iterator2)
        idNumber = element["video_id"]

        if video_id != "#NAME":
            if video_id == idNumber:
                days += 1
            
            else:
                if days > days_max:
                    days_max = days
                    video_id_max = video_id
                    channel_max = channel
                    title_max = title
                video_id = element["video_id"]
                channel = element["channel_title"]
                title = element["title"]
                days = 1

    result = ("Titulo: " + str(title_max) + ", Nombre del canal: " + str(channel_max) + 
    ", País: " + str(country) + ", Días: " + str(days_max) )


    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, result
    


def sortVideosCategoryTrending (catalog, category):

    start_time = time.process_time()

    sublistcategories = lt.newList("ARRAY_LIST")

    iterator1 = it.newIterator(catalog["categories"])
    while it.hasNext(iterator1):
        element = it.next(iterator1)
        category_name = (element["category_name"]).lstrip(" ")

        if (category_name.lower()) == (category.lower()):
            category_id = element["category_id"]


    iterator2 = it.newIterator(catalog["videos"])
    while it.hasNext(iterator2):
        element = it.next(iterator2)
        if element["category_id"] == category_id:
            lt.addLast(sublistcategories, element)

    sorted_list = merge.sort(sublistcategories,compVideoByTitle)

    video_id = ""
    days = 0
    days_max = 0
    video_id_max = "" 
    channel = ""
    channel_max = ""
    title = ""
    title_max = ""

    iterator3 = it.newIterator(sorted_list)
    while it.hasNext(iterator3):
        element = it.next(iterator3)
        idNumber = element["video_id"]

        if video_id == idNumber:
            days += 1
            
        else:
            if days > days_max:
                days_max = days
                video_id_max = video_id
                channel_max = channel
                title_max = title
            video_id = element["video_id"]
            channel = element["channel_title"]
            title = element["title"]
            days = 1

    result = ("Titulo: " + str(title_max) + ", Nombre del canal: " + str(channel_max) + 
    ", Id de la categoria: " + str(category_id) + ", Días: " + str(days_max) )

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, result


def sortVideosLikesTag(catalog, tag, country):

    start_time = time.process_time()

    sublist_tags = lt.newList("ARRAY_LIST")


    iterator1 = it.newIterator(catalog["videos"])
    while it.hasNext(iterator1):
        element = it.next(iterator1)
        if str(tag.lower()) in str(element["tags"].lower()):
            lt.addLast(sublist_tags, element)

    sublist_countries = lt.newList("ARRAY_LIST")

    iterator2 = it.newIterator(sublist_tags)
    while it.hasNext(iterator2):
        element = it.next(iterator2)
        if (element["country"].lower()) == (country.lower()):
            lt.addLast(sublist_countries, element)


    sorted_list_likes = merge.sort(sublist_countries, compVideoByLikes)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, sorted_list_likes





    

   


    

    





