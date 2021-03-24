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
 """

import config as cf
import model
import csv
from datetime import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def initCatalog():
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    loadCategory(catalog)
    loadVideos(catalog)


def loadVideos(catalog):
    """Crea un diccionario con la informacion del video para que sea posteriormente agregado
    al catalogo en su lista correspondiente"""
    videosfile = cf.data_dir + "videos-small.csv"
    input_file = csv.DictReader(open(videosfile, encoding="utf-8"))
    for video in input_file:
        filtrado = {}
        filtrado["video_id"] = video["video_id"]
        filtrado["trending_date"] = video["trending_date"]
        filtrado["title"] = video["title"]
        filtrado["channel_title"] = video["channel_title"]
        filtrado["category_id"] = int(video["category_id"])
        filtrado["publish_time"] = video["publish_time"]
        filtrado["tags"] = video["tags"]
        filtrado["country"] = video["country"]
        filtrado["views"] = int(video["views"])
        filtrado["likes"] = int(video["likes"])
        filtrado["dislikes"] = int(video["dislikes"])
        filtrado["trending_date"] = video["trending_date"]
        filtrado["publish_time"] = video["publish_time"]
        model.addVideo(catalog, filtrado)


def loadCategory(catalog):
    """Crea un diccionario con la informacion de la categoria
    para que sea posteriormente agregado
    al catalogo en su lista correspondiente"""
    categoriesfile = cf.data_dir + "category-id.csv"
    input_file = csv.DictReader(open(categoriesfile, encoding="utf-8"))
    for category in input_file:
        category_list = category["id\tname"].split("\t")
        category["name"] = category_list[1]
        category["id"] = int(category_list[0])
        model.addCategory(catalog, category)


# Funciones de ordenamiento


def sortVideos(lista):
    """ Llama a la funcion sortVideos() del modelo. """
    return model.sortVideos(lista)


def sortVideosReq2(lista):
    """ Llama a la funcion sortVideosReq2() del modelo. """
    return model.sortVideosReq2(lista)


def sortVideosReq3(lista):
    """ Llama a la funcion sortVideosReq3() del modelo. """
    return model.sortVideosReq3(lista)


def sortDate(lista):
    """ Llama a la funcion sortDate() del modelo. """
    return model.sortDate(lista)


def sortVideosReq4(lista):
    """ Llama a la funcion 'sortVideosReq4()' del modelo. """
    return model.sortVideosReq4(lista)


def limpieza(lista):
    """ Llama a la funcion 'limpieza()' del modelo. """
    return model.limpieza(lista)


# Funciones de consulta sobre el catálogo


def filtrado_pais(catalog, pais):
    """ Llama a la funcion 'filtrado_pais()' del modelo. """
    return model.filtrado_pais(catalog, pais)


def lista(catalog):
    """ Llama a la funcion 'lista()' del modelo. """
    return model.lista(catalog)


def filtrado_categoria(lista, categoria):
    """ Llama a la funcion 'filtrado_categoria()' del modelo. """
    return model.filtrado_categoria(lista, categoria)


def filtrado_tags(catalog, tag):
    """ Llama a la funcion 'filtrado_categoria()' del modelo. """
    return model.filtrado_tags(catalog, tag)


def idCat(catalog, categoria):
    """ Llama a la funcion 'idCat()' del modelo. """
    return model.idCat(catalog, categoria)


def trending(lista):
    """ Llama a la funcion 'trending()' del modelo. """
    return model.trending(lista)


def trending_2(lista):
    """ Llama a la funcion 'trending_2()' del modelo. """
    return model.trending_2(lista)