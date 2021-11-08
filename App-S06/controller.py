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
def initCatalogA():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalogA()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)


def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtists(catalog, artist)
        model.addArtists_Artworks(catalog, artist)
    catalog['Artists_Artworks']=model.sortAux(catalog['Artists_Artworks'])


def loadArtworks(catalog):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    
    arti = model.sortIDArtists(catalog)
    for work in input_file:
        model.addArtworks(catalog, work)
        model.addObject(catalog,work)
        model.addNationArt(catalog, work, arti)


def funcionReqUno(catalog,minimo,maximo):
    return model.funcionReqUno(catalog,minimo,maximo)

def funcionReqDos(catalog, minimo, maximo):
    return model.funcionReqDos(catalog, minimo, maximo)
    
def funcionReqTres(catalog, nombre):
    return model.funcionReqTres(catalog, nombre)

def funcionReqCuatro(catalog):
    return model.funcionReqCuatro(catalog)

def funcionReqCin(catalog, nombre):
    return model.funcionReqCin(catalog, nombre)

def obrasUnicas(top):
    return model.obrasUnicas(top) 

def purchased(lista_f):
    return model.purchased(lista_f)
