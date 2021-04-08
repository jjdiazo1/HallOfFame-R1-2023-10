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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def initUniqueCatalog(catalog):

    """
    Llama la funcion de inicializacion del catalogo único del modelo.
    """
    unique_catalog = model.newUniqueCatalog(catalog)
    return unique_catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la
    estructura de datos (cateogrias y videos).
    """
    loadCategories(catalog)
    loadVideos(catalog)



def loadCategories(catalog):
    """
    Carga todas los categories del archivo y las agrega a la lista de categories dentro del catalogo.
    """

    category_file=cf.data_dir +"category-id.csv"
    input_file=csv.DictReader(open(category_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


def loadVideos(catalog):
    """
    Carga los videos del archivo CSV.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


# Funciones de ordenamiento

def sortVideos(catalog, size, cmpFunction):
    """
    Ordena los videos por número de views, likes o days.
    """
    return model.sortVideos(catalog, size, cmpFunction)


# Funciones de consulta sobre el catálogo
def filterCatalog(catalog, column_1, value_1, column_2=None, value_2=None):
    """Filtra el catalogo dejando solo los videos con el valor especificado para máximo 2 columnas."""

    filtered_catalog = model.filterCatalog(catalog, column_1, value_1, column_2, value_2)
    return filtered_catalog


def filterTag(catalog, tag):
    """Filtra el catalogo por tag (invoca al model para realizar esto)"""
    return model.filterTag(catalog,tag)
