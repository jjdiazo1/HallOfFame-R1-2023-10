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

from DISClib.ADT import list as lt
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

#######################################################################################################################
# Inicialización del Catálogo de obras
#######################################################################################################################

def initCatalog(data_structure):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(data_structure)
    return catalog

#######################################################################################################################
# Funciones para la carga de datos
#######################################################################################################################

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

#######################################################################################################################

def loadArtists(catalog):
    """
    Carga los artistas del archivo
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

#######################################################################################################################

def loadArtworks(catalog):
    """
    Carga las obras del archivo.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

#######################################################################################################################
# Funciones de ordenamiento
#######################################################################################################################

def SortArtistByBirthYear(lst, sample_size, sorting_method, initial_year_birth, end_year_birth, data_structure):
    sub_list = lt.subList(lst,1,sample_size)
    return model.SortArtistByBirthYear(sub_list, sorting_method, initial_year_birth, end_year_birth, data_structure)

#######################################################################################################################

def SortArtworksAdquisition(lst, sample_size, sorting_method):
    sub_list = lt.subList(lst,1,sample_size)
    return model.SortArtworksAdquisition(sub_list, sorting_method)

#######################################################################################################################

def SortArtworksAdquisitionRange(lst, sample_size, sorting_method, initial_date_adquisition, 
                                                                                end_date_adquisition, data_structure):
    sub_list = lt.subList(lst,1,sample_size)
    return model.SortArtworksAdquisitionRange(sub_list, sorting_method, initial_date_adquisition,
                                                                                end_date_adquisition, data_structure)

#######################################################################################################################

def ClasifyArtistsTechnique(catalog, sample_size, sorting_method, artists_name, data_structure):
    sub_list = lt.subList(catalog['artworks'],1,sample_size)
    lst = catalog['artists']
    return model.ClasifyArtistsTechnique(sub_list, lst, sorting_method, artists_name, data_structure)

#######################################################################################################################

def ClasifyArtworksByNationality(catalog, sample_size, sorting_method, artists_ID_dict, data_structure):
    sub_list = lt.subList(catalog['artworks'],1,sample_size)
    return model.ClasifyArtworksByNationality(sub_list, sorting_method, artists_ID_dict, data_structure)

#######################################################################################################################

def TransportArtworksDepartment(catalog, sample_size, sorting_method, department, data_structure):
    sub_list = lt.subList(catalog['artworks'],1,sample_size)
    return model.TransportArtworksDepartment(sub_list, sorting_method, department, data_structure)

#######################################################################################################################
# Funciones de consulta sobre el catálogo
#######################################################################################################################

def getTheFirstElements(lst, num, data_structure):
    return model.GetTheFirstElements(lst, num, data_structure)

#######################################################################################################################

def getTheLasttElements(lst, num, data_structure):
    return model.GetTheLastElements(lst, num, data_structure)

#######################################################################################################################

def CreationArtistsIDDict(lst):
    return model.CreationArtistsIDDict(lst)

#######################################################################################################################

def GetConstituentIDListArtwork(artwork):
    return model.GetConstituentIDListArtwork(artwork)