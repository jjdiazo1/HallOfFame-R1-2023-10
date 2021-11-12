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

def initCatalog(tipo):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadArtwork(catalog)
    

def loadArtwork(catalog):
    """
    Carga los archivos de los Artworks y se agrega a la lista de obras de arte
    """
    Artworkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(Artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


def loadArtist(catalog):
    """
    Carga los archivos de los Artist y se agrega a la lista de artistas
    """
    Artistfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def addArea(catalog):
    model.addArea(catalog)

# Funciones de ordenamiento

def sortArtistCatalogByBeginDate(catalog, size, Sort_Type):
    return model.sortArtistCatalogByBeginDate(catalog, size, Sort_Type)

def sortArtworkCatalogByDateAcquired(catalog, size, Sort_Type):
    return model.sortArtworkCatalogByDateAcquired(catalog, size, Sort_Type)

def sortArtworkCatalogByDate(catalog, size, Sort_Type):
    return model.sortArtworkCatalogByDate(catalog, size, Sort_Type)

def sortArtworkCatalogByTransCost(catalog):
    return model.sortArtworkCatalogByTransCost(catalog)


# Funciones de consulta sobre el catálogo
def getLast(catalog, num):
    """
    Retorna los últimos num artistas/obras
    """
    return model.getLast(catalog, num)

def getFirts(catalog, num):
    """
    Retorna los primeros num artistas/obras
    """
    return model.getFirts(catalog, num)

def getCronologicalArtist (sortedArtist_BDate, beginDate, endDate):
    """
    Retorna los artistas de un rango dado en orden cronologico
    """
    return model.getCronologicalArtist (sortedArtist_BDate, beginDate, endDate)

def getCronologicalArtwork (sortedArtwork_Date, beginDate, endDate):
    """
    Retorna las obras adquiridas de un rango dado en orden cronologico
    """
    return model.getCronologicalArtwork (sortedArtwork_Date, beginDate, endDate)

def getArtworksPurchased (catalog):
    """
    Retorna el numero de obras que fueron compradas
    """
    return model.getArtworksPurchased(catalog)

def getArtistsArtwork(catalog, artistId):
    """
    Retorna las obras de un artista por tecnica
    """
    return model.getArtistsArtwork(catalog, artistId)

def getArtistTechnique(catalog):
    return model.getArtistTechnique(catalog)

def getArtworkNationality(catalog):
    """
    Retorna las obras por nacionalidad de los artistas
    """
    return model.getArtworkNationality(catalog)

def getArtistInfo(catalog, artistName):
    return model.getArtistInfo(catalog, artistName)

def getArworkByDepartment(catalog, departamento):
    return model.getArworkByDepartment(catalog, departamento)

def getTransportationCost(catalog):
    return model.getTransportationCost(catalog)

def getArtworkTotal_CostWeight(catalog):
    return model.getArtworkTotal_CostWeight(catalog)

def createNewDisplay(catalog,beginYear, finalYear, area):
    return model.createNewDisplay(catalog,beginYear, finalYear, area)






