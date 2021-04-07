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
from DISClib.ADT import list as lt
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog(list_type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(list_type)
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    """
    Carga los videos del archivo.
    """
    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    """
    Carga todas las categorías del archivo y los agrega a la lista de
    categorias
    """
    categoriesfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(
        open(categoriesfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)

# Funciones de ordenamiento


def sortVideos(catalog, size, sort_type, cmp):
    """
    Ordena los videos por el parámetro cmp
    """
    return model.sortVideos(catalog, size, sort_type, cmp)


# Funciones de consulta sobre el catálogo

def getVideosByCategoryAndCountry(catalog, category, country):
    '''
    Retorna los videos dado un país y categoría específicos
    '''
    return model.getVideosByCategoryAndCountry(catalog, category, country)


def getVideosByCountryAndTag(catalog, tag, country):
    '''
    Retorna los videos dado un país y tag específicos
    '''
    return model.getVideosByCountryAndTag(catalog, tag, country)


def getVideoMasTrendingByCategory(catalog, categoria):
    '''
    Retorna el video que fue más tiempo trending por categoría
    '''
    return model.VideoMasTrendingCategoria(catalog, categoria)


def getVideosByCountry(catalog, country):
    '''
    Retorna los videos dado un país específico
    '''
    return model.getVideosByCountry(catalog, country)


def getVideosByCategory(catalog, categoria):
    '''
    Retorna los videos dado una categoría específica
    '''
    return model.getVideosByCategory(catalog, categoria)


def getMostTrendingDays(catalog):
    '''
    Retorna el video que fue más tiempo trending
    '''
    return model.getMostTrendingDaysByTitle(catalog)


# Funciones de los Requerimientos

def Requerimiento_2(catalogo, categoria, pais):
    result1 = model.getVideosByCategoryAndCountry(
                catalogo, categoria, pais)
    result = model.sortVideos(
                result1, lt.size(result1), 'ms', 'cmpVideosByViews')
    return result
