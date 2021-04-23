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
import sys
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
default_limit=1000
sys.setrecursionlimit(default_limit*1000)
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def new_catalog():
    catalog = {'videos':None,
               'category_names': None,
               'countries':None,
               'categories':None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['category_names'] = lt.newList('ARRAY_LIST')
    catalog['countries']=lt.newList('ARRAY_LIST',cmpfunction=compare_countries)
    catalog['categories']=lt.newList('ARRAY_LIST',cmpfunction=compare_categories)
    return catalog

# Funciones para agregar informacion al catalogo

def add_video(catalog, video):
    lt.addLast(catalog['videos'], video)
    add_video_country(catalog,video['country'],video)
    add_video_category(catalog,video['category_id'],video)


def add_video_country(catalog,country_name,video):
    countries=catalog['countries']
    poscountry = lt.isPresent(countries, country_name)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = new_country(country_name)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)

def add_video_category(catalog,category_id,video):
    categories=catalog['categories']
    poscategory = lt.isPresent(categories, category_id)
    if poscategory > 0:
        category = lt.getElement(categories, poscategory)
    else:
        category = new_category(category_id)
        lt.addLast(categories, category)
    lt.addLast(category['videos'], video)

def add_category_name(catalog, category):
    category=new_category_name(category['name'],category['id'])
    lt.addLast(catalog['category_names'], category)

# Funciones para creacion de datos
def new_country(name):
    country={'name':None,'videos':None}
    country['name']=name
    country['videos']=lt.newList('ARRAY_LIST')
    return country

def new_category(id):
    category={'id':None,'videos':None}
    category['id']=id
    category['videos']=lt.newList('ARRAY_LIST')
    return category

def new_category_name(name,id):  
    return {'name':name,'id':id}

#Funciones de comparación

def cmp_videos_by_views(video1,video2):
    return float(video1['views'])>float(video2['views'])

def cmp_videos_by_likes(video1,video2):
    return float(video1['likes'])>float(video2['likes'])

def compare_countries(country_name,country):
    if country_name == country['name']:
        return 0
    return -1

def compare_videos_by_id(video_id,video):
    if video_id==video['video_id']:
        return 0
    return -1

def compare_videos_by_title(video_title,video):
    if video_title==video['title']:
        return 0
    return -1

def compare_categories(category_id,category):
    if category_id == category['id']:
        return 0
    return -1

#def compare_counter(video1,video2):
 #   return int(video1['counter'])>int(video2['counter'])

# Funciones de ordenamiento


# Funciones de consulta
def get_category_id(catalog,category_name):
    category_id=0
    size=lt.size(catalog['category_names'])
    for i in range(1,size+1):
        category=lt.getElement(catalog['category_names'],i)
        if category_name==category['name']:
            category_id=category['id']
    return category_id

def get_most_view_videos(catalog,country_name,category_name):
    category_id=get_category_id(catalog,category_name)
    videos_country_category=lt.newList('ARRAY_LIST')
    countries=catalog['countries']
    poscountry = lt.isPresent(countries,country_name)
    if category_id==0 or poscountry==0:
        return None
    else:
        country = lt.getElement(countries, poscountry)
        for j in range(1,lt.size(country['videos'])+1):
            video=lt.getElement(country['videos'],j)
            if video['category_id']==category_id:
                 lt.addLast(videos_country_category,video)
        return merge.sort(videos_country_category,cmp_videos_by_views)

def get_most_time_trending_country(catalog,country_name):
    countries=catalog['countries']
    poscountry = lt.isPresent(countries,country_name)
    country = lt.getElement(countries, poscountry)
    country_videos=country['videos']
    trending_counter=lt.newList('ARRAY_LIST', cmpfunction=compare_videos_by_id)
    size=lt.size(country_videos)

    for i in range(1,size+1):
        video=lt.getElement(country_videos,i)
        posvideo=lt.isPresent(trending_counter,video['video_id'])
        if posvideo==0:
            video_trending={'video_id':video['video_id'],'title':video['title'],'counter':1,'channel_title':video['channel_title'],'country':country_name}
            lt.addLast(trending_counter,video_trending)
        else:
            video_trending=lt.getElement(trending_counter,posvideo)
            video_trending['counter']+=1

    x=0
    more_trending=None
    for j in range(1,lt.size(trending_counter)+1):
        video=lt.getElement(trending_counter,j)
        if video['counter']>x:
            x=video['counter']
            more_trending=video
    return more_trending
        
def get_most_time_trending_category(catalog,category_name):
    category_id=get_category_id(catalog,category_name)
    categories=catalog['categories']
    poscategory = lt.isPresent(categories,category_id)
    category = lt.getElement(categories, poscategory)
    category_videos=category['videos']
    trending_counter=lt.newList('ARRAY_LIST', cmpfunction=compare_videos_by_title)
    size=lt.size(category_videos)
    for i in range(1,size+1):
        video=lt.getElement(category_videos,i)
        posvideo=lt.isPresent(trending_counter,video['title'])
        if posvideo==0:
            video_trending={'video_id':video['video_id'],'title':video['title'],'counter':1,'channel_title':video['channel_title'],'category_id':category_id}
            lt.addLast(trending_counter,video_trending)
        else:
            video_trending=lt.getElement(trending_counter,posvideo)
            video_trending['counter']+=1
    x=0
    more_trending=None
    for j in range(1,lt.size(trending_counter)+1):
        video=lt.getElement(trending_counter,j)
        if video['counter']>x:
            x=video['counter']
            more_trending=video
    return more_trending
    
def get_most_likes_tag(catalog,tag,country_name):
    videos=catalog['videos']
    size=lt.size(videos)
    tag_country_videos=lt.newList('ARRAY_LIST')
    for i in range(1,size+1):
        video=lt.getElement(videos,i)
        video_tags=video['tags']
        if tag in video_tags and video['country']==country_name:
            lt.addLast(tag_country_videos,video)
    return merge.sort(tag_country_videos,cmp_videos_by_likes)