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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def print_menu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar videos con más vistas por categoría y país")
    print("3- Encontrar video más días en tendencia por país")
    print("4- Encontrar video más días en tendencia por categoría")
    print("5- Encontrar videos con más likes por tag y país")
    print("0- Salir")

def init_catalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.init_catalog()


def load_data(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.load_data(catalog)


def print_results_req1(ord_videos, sample=10):
    if ord_videos==None:
        print('Parece que ingresó algún dato mal, vuelva a intentarlo')
    else:
         size = lt.size(ord_videos)
         if size > sample:
            print("Los primeros ", sample, " videos ordenados son:")
            i=1
            while i <= sample:
                video = lt.getElement(ord_videos,i)
                print('El nombre del video numero '+str(i)+' es "' + video['title'] + '", el canal es "'+video['channel_title']+'", la fecha en la que estuvo en tendencia fue '+video['trending_date']+', la fecha de publicacion fue '+video['publish_time']+', y tuvo '+video['views']+' vistas, '
                +video['likes']+' Likes, y '+video['dislikes']+' dislikes')
                i+=1

def print_results_req4(ord_videos, sample=10):
    if ord_videos==None:
        print('Parece que ingresó algún dato mal, vuelva a intentarlo')
    else:
         size = lt.size(ord_videos)
         if size > sample:
            print("Los primeros ", sample, " videos ordenados son:")
            i=1
            while i <= sample:
                video = lt.getElement(ord_videos,i)
                print('El nombre del video numero '+str(i)+' es "' + video['title'] + '", el canal es "'+video['channel_title']+'", la fecha de publicacion fue '+video['publish_time']+', tuvo '+video['views']+' vistas, '
                +video['likes']+' Likes, y '+video['dislikes']+' dislikes')
                print('')
                print('los tags fueron: '+video['tags'])
                print('________________________________________________')
                i+=1

def print_categories(category_names):
    size=lt.size(category_names)
    for n in range(1,size+1):
        category=lt.getElement(category_names,n)
        print(category['id'],category['name'])

catalog = None

"""
Menu principal
"""
while True:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = init_catalog()
        load_data(catalog)
        print('Se cargaron: ',lt.size(catalog['videos']), ' videos')
        print('El primer video cargado es: ' )
        video=lt.getElement(catalog['videos'],1)
        print('Titulo: ' + video['title'] + ' , Canal: '+video['channel_title']+' , Fecha de tendencia '+str(video['trending_date']))
        print('País: '+video['country'] +' , Vistas: '+str(video['views'])+' , Likes: '+str(video['likes'])
        +' , Dislikes: '+str(video['dislikes']))
        print('Las categorías cargadas son: ')
        print_categories(catalog['category_names'])
    elif int(inputs[0]) == 2:
        country_name=input('Ingrese el nombre del país: ').lower()
        category_name=' '+input('Ingrese el nombre de la categoría: ')
        number=int(input('Buscando los TOP ?: '))
        print_results_req1(controller.get_most_view_videos(catalog,country_name,category_name),number)
    elif int(inputs[0]) == 3:
        country_name=input('Ingrese el nombre del país: ').lower()
        video = controller.get_most_time_trending_country(catalog,country_name)
        print('El titulo del video es '+ video['title']+', el numero de dias en tendencia es '+str(video['counter'])+', el nombre del canal es '+video['channel_title']+' y el pais es '+country_name)
    elif int(inputs[0]) == 4:
        category_name=' '+input('Ingrese el nombre de la categoría: ')
        video = controller.get_most_time_trending_category(catalog,category_name)
        print('El titulo del video es '+ video['title']+', el numero de dias en tendencia es '+str(video['counter'])+', el nombre del canal es '+video['channel_title']+' y el identificador de categoria es '+video['category_id'])

    elif int(inputs[0]) == 5:
        tag=input('Ingrese el tag: ')
        number=int(input('Quiere cononcer el TOP?: '))
        country_name=input('Ingrese el pais: ').lower()
        print_results_req4(controller.get_most_likes_tag(catalog,tag,country_name),number)
    else:
        sys.exit(0)
sys.exit(0)

