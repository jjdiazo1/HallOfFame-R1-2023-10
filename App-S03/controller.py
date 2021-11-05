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
import copy
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtworks(catalog):
    worksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(worksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadArtists(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def getLast3Artists(catalog):
    sublista = model.getLast3Artists(catalog)
    return sublista
    

def getLast3Artworks(catalog):
    sublista = model.lastThreeArtworks(catalog)
    return sublista


# Funciones para la carga de datos

# Funciones de ordenamiento
def sortArtworksDateAcquired(catalog, anio1, anio2, mes1, mes2, dia1, dia2):
    """
    Ordena los libros por average_rating
    """
    return model.sortArtworksDateAcquired(catalog, anio1, anio2, mes1, mes2, dia1, dia2)

# Funciones de consulta sobre el catálogo

#Funciones Req 1
def sublistaRangoArtistas(catalog, year1, year2):
    return model.sublistaRangoArtistas(catalog, year1, year2)

def ArtistasNacimientoPrimeros3(lista):
    return model.ArtistasNacimientoPrimeros3(lista)

def ArtistasNacimientoUltimos3(lista):
    return model.ArtistasNacimientoUltimos3(lista)

#Funciones Req 3
def buscar_artista_constituentID(catalog, nombre):
    return model.buscar_artista_constituentID(catalog, nombre)

def total_obras(catalog, nombre):
    return model.total_obras(catalog,nombre)

def lista_total_tecnicas(catalog, nombre):
    return model.lista_total_tecnicas(catalog, nombre)

def tecnica_mas_utilizada(lista):
    return model.tecnica_mas_utilizada(lista)

def lista_tecnicas_mas_usadas(lista, tecnica):
    return model.lista_tecnicas_mas_usadas(lista, tecnica)


#Funciones Req 5
def ListaPorDepto(catalog, depto):
    return model.ListaPorDepto(catalog, depto)

def CalcularCostoEnvioObra(obra):
    return model.CalcularCostoEnvioObra(obra)

def CostoTodasObras(lista):
    return model.CostoTodasObras(lista)

def ObrasMasAntiguas(lista):
    return model.ObrasMasAntiguas(lista)

def ObrasMasCaras(lista):
    return model.ObrasMasCaras(lista)

def ArtistaEnObra(catalog, obra):
    return model.ArtistaEnObra(catalog, obra)




def ordenarpaises(catalog):
    paises=catalog['nacionalidades']
    resultado=model.ordenarpaises(paises)
    return resultado

