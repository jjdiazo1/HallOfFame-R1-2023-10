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

# Inicialización del Catálogo de libros


def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos


def loadData(catalog):

    loadArtworks(catalog)
    loadArtists(catalog)


def loadArtworks(catalog):

    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for row in input_file:
        lstid = (row['ConstituentID'][1:-1]).split(", ")
        lstmedium = row['Medium'].split(",")
        if row['Height (cm)'] == '':
            height = 0
        else:
            height = float(row['Height (cm)'])

        if row['Width (cm)'] == '':
            width = 0
        else:
            width = float(row['Width (cm)'])

        if row['Length (cm)'] == '':
            length = 0
        else:
            length = float(row['Length (cm)'])

        if row['Weight (kg)'] == '':
            weight = 0
        else:
            weight = float(row['Weight (kg)'])

        model.addArtwork(catalog, row['Title'], row['DateAcquired'], lstmedium,
                         row['Dimensions'], lstid, row['ObjectID'], row['CreditLine'], row['Date'],
                         row['Classification'], height, width, row['Department'], length, weight)


def loadArtists(catalog):

    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for row in input_file:
        model.addInfoArtist(catalog, row['DisplayName'], row['ConstituentID'], row['Nationality'], row['BeginDate'], row['EndDate'],row['Gender'])


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def sortArtworks(catalog, ltsize, a1, a2):

    return model.sortArtworks(catalog, ltsize, a1, a2)


def sortArtists(catalog, lstsize, a1, a2):
    return model.sortArtists(catalog, lstsize, a1, a2)


def countArtworksNationality(catalog):

    return model.countArtworksNationality(catalog)


def createNewDisplay(catalog, a1, a2, area):

    return model.createNewDisplay(catalog, a1, a2, area)


def ClassifyArtworksbyTechnique (catalog,artist):

    return model.ClassifyArtworksbyTechnique(catalog,artist)


def moveDepartment(catalog, department):

    return model.moveDepartment(catalog, department)


