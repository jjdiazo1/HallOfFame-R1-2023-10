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

# Inicialización del Catálogo de libros

def initCatalog():

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):

    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):

    videosfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):

    categoriesfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoriesfile, encoding='utf-8'),delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


# Funciones de ordenamiento

def sortVideosByViews(catalog, category, country):
    
    return model.sortVideosByViews(catalog, category, country)

# Funciones de consulta sobre el catálogo

def firstVideo(catalog):

    firstvideo = model.firstVideo(catalog)

    return firstvideo

def sortVideosCountryTrending (catalog,country):

    return model.sortVideosCountryTrending (catalog, country)


def sortVideosLikesTag(catalog, tag, country):

    return model.sortVideosLikesTag(catalog, tag, country)

def sortVideosCategoryTrending (catalog, category):

    return model.sortVideosCategoryTrending (catalog, category)

