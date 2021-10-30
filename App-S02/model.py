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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

from DISClib.DataStructures.arraylist import getElement, iterator, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf
import time
from datetime import date, datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá 
dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """

    """
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtworks)
    catalog['artists'] = lt.newList('ARRAY_LIST', cmpfunction=compareArtists)

    return catalog


# Funciones para agregar informacion al catalogo

def addArtwork(catalog, title, dateAcquired, lstmedium, dimensions, lstconstituentid,
               objectid, creditline, date, classification, height, width, department, length, weight):

    dictArtwork = newArtwork(title)
    dictArtwork['DateAcquired'] = dateAcquired
    dictArtwork['Dimensions'] = dimensions
    dictArtwork['Medium'] = lstmedium
    dictArtwork['ObjectID'] = objectid
    dictArtwork['ArtistsID'] = lstconstituentid
    dictArtwork['CreditLine'] = creditline
    dictArtwork['Date'] = date
    dictArtwork['Classification'] = classification
    dictArtwork['Height (cm)'] = height
    dictArtwork['Width (cm)'] = width
    dictArtwork['Department'] = department
    dictArtwork['Length (cm)'] = length
    dictArtwork['Weight (kg)'] = weight
    lt.addLast(catalog['artworks'], dictArtwork)

    for cID in lstconstituentid:
        addArtist(catalog, cID, dictArtwork)


def addArtist(catalog, constituentid, artwork):

    artists = catalog['artists']
    posartist = lt.isPresent(artists, constituentid)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(constituentid)
        lt.addLast(catalog['artists'], artist)
    lt.addLast(artist['artworks'], artwork)


def addInfoArtist(catalog, name, constituentid, nationality, begindate,enddate,gender):

    posartists = lt.isPresent(catalog['artists'], constituentid)
    if posartists > 0:
        artist = lt.getElement(catalog['artists'], posartists)
        artist['name'] = name
        artist['Nationality'] = nationality
        artist['BeginDate'] = begindate
        artist['EndDate'] = enddate
        artist['Gender'] = gender

    else:
        dictArtist = newArtist(constituentid)
        dictArtist['name'] = name
        dictArtist['Nationality'] = nationality
        dictArtist['BeginDate'] = begindate
        dictArtist['EndDate'] = enddate
        dictArtist['Gender'] = gender

    posartwork = lt.isPresent(catalog['artworks'], constituentid)
    if posartwork > 0:
        artwork = lt.getElement(catalog['artworks'], posartwork)
        artwork['Artists'].append(name)


# Funciones para creacion de datos

def newArtist(constituentid):

    artist = {'name': "", 'ConstituentID': "", 'Nationality': "", "artworks": None,'BeginDate':0, 'EndDate':0,'Gender':""}
    artist['ConstituentID'] = constituentid
    artist['artworks'] = lt.newList('ARRAY_LIST')

    return artist


def newArtwork(title):
    artwork = {'Title': "", 'DateAcquired': 0, 'ArtistsID': None, 'Medium': None,
               'Dimensions': "", 'ObjectID': 0, "CreditLine": "", "Artists": [], 'Date': "",
               'Classification': "", 'Height (cm)': 0, 'Width (cm)': 0, 'Department': "", 'Length (cm)': 0, 'Weight (kg)': 0}
    artwork['Title'] = title

    return artwork


# Funciones de consulta


def sortArtworks(catalog, ltsize, a1, a2):

    dt_objectI1 = datetime.strptime(a1, '%Y-%m-%d').date()
    dt_objectI2 = datetime.strptime(a2, '%Y-%m-%d').date()
    sub_list = lt.subList(catalog['artworks'], 1, ltsize)
    sub_list = sub_list.copy()
    sorted_list = None
    sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)
    listFinal = lt.newList('ARRAY_LIST')
    purchasedArtworks = 0
    totalArtworks = 0
    for value in lt.iterator(sorted_list):
        dictT = {}
        if len(value['DateAcquired']) > 1:
            dt_object1 = datetime.strptime(value['DateAcquired'], '%Y-%m-%d').date()
            if ((dt_object1 >= dt_objectI1) and (dt_object1 <= dt_objectI2)):
                dictT['Title'] = value['Title']
                dictT['DateAcquired'] = value['DateAcquired']
                dictT['Date'] = value['Date']
                dictT['Artists'] = value['Artists']
                dictT['Medium'] = value['Medium']
                dictT['Dimensions'] = value['Dimensions']
                lt.addLast(listFinal, dictT)

                totalArtworks += 1
                if 'Purchase' in value['CreditLine']:
                    purchasedArtworks += 1
            else:
                pass

    return listFinal, totalArtworks, purchasedArtworks



def sortArtists(catalog,ltsize,a1,a2):
    sub_list = lt.subList(catalog['artists'],1,ltsize)
    sub_list = sub_list.copy()
    sorted_list = None
    sorted_list = ms.sort(sub_list,cmpArtistbyBirthDate)
    listFinal=[]
    totalArtists=0
    for value in lt.iterator(sorted_list):
        if (int(value['BeginDate']))>1:
            año1=int(value['BeginDate'])
            if ((año1 >= a1) and (año1 <= a2)):
                listFinal.append(value)
                totalArtists += 1
            else:
                pass
    return listFinal,totalArtists

def ClassifyArtworksbyTechnique (catalog, artist):
    total_obras = 0
    total_medios = 0
    lista_medios = lt.newList('ARRAY_LIST')
    dictFinal ={}
    for artwork in lt.iterator (catalog['artworks']):
        for name in artwork['ArtistsID']:
            for artista in lt.iterator (catalog['artists']):
                if artista['name'] == artist:
                    if artista['ConstituentID']==name:
                        total_obras += 1
                        for x in artwork['Medium']:
                            lt.addLast(lista_medios,x)
                        if (len(artwork['Medium'])) > 0:
                            if x not in dictFinal:
                                dictFinal[x] = 1
                            else:
                                dictFinal[x] += 1


    lista_sin_repetidos = set(lista_medios['elements'])
    total_medios = len(lista_sin_repetidos)
    lista1 = lt.newList('ARRAY_LIST')
    lista2 = lt.newList('ARRAY_LIST')
    for key in dictFinal:
        dictT = {}
        dictT[key] = dictFinal[key]
        lt.addLast(lista1, dictT[key])
    sorted_list = None
    sorted_list = ms.sort(lista1, cmpCountriesbyArtworks)
    for value in lt.iterator(sorted_list):
        for key in dictFinal:
            dictTF = {}
            if value == dictFinal[key]:
                dictTF[key] = value
                lt.addLast(lista2, dictTF)

    key_list = list(lista2['elements'][0])
    Most_used_technique = key_list[0]
    lista_titulos = []
    for artwork in lt.iterator (catalog['artworks']):
        for name in artwork['ArtistsID']:
            for artista in lt.iterator (catalog['artists']):
                if artista['name'] == artist:
                    if artista['ConstituentID']==name:
                        for x in artwork['Medium']:
                            if x == Most_used_technique:
                                lista_titulos.append(artwork['Title'])


    lista_final = lt.newList('ARRAY_LIST')
    for x in lt.iterator(catalog['artworks']):
        if x['Title'] in lista_titulos and  Most_used_technique in x['Medium']:
            dictObras={}
            dictObras['Título'] = x['Title']
            dictObras['Fecha'] = x['Date']
            dictObras['Medio'] = x['Medium']
            dictObras['Dimensiones'] = x['Dimensions']
            lt.addLast(lista_final,dictObras)

    return (total_obras, total_medios, Most_used_technique,lista_final)
    


def countArtworksNationality(catalog):

    dictFinal = {}
    for artist in lt.iterator(catalog['artists']):
        if (len(artist['Nationality']) > 0 and (artist['Nationality'] != 'Nationality unknown')):
            if artist['Nationality'] not in dictFinal:
                dictFinal[artist['Nationality']] = lt.size(artist['artworks'])
            else:
                dictFinal[artist['Nationality']] += lt.size(artist['artworks'])

    lst = lt.newList('ARRAY_LIST')
    lstf = lt.newList('ARRAY_LIST')
    for key in dictFinal:
        dictT = {}
        dictT[key] = dictFinal[key]
        lt.addLast(lst, dictT[key])
    sorted_list = None
    sorted_list = ms.sort(lst, cmpCountriesbyArtworks)

    for value in lt.iterator(sorted_list):
        for key in dictFinal:
            dictTF = {}
            if value == dictFinal[key]:
                dictTF[key] = value
                lt.addLast(lstf, dictTF)

    # DATOS DE LAS OBRAS DEL TOP 1

    key_list = list(lstf['elements'][0])
    topCountry = key_list[0]

    lstTopCountryArtists = []
    for value in lt.iterator(catalog['artists']):
        if value['Nationality'] == topCountry:
            lstTopCountryArtists.append(value['name'])

    listData = lt.newList('ARRAY_LIST')
    for value in lt.iterator(catalog['artworks']):
        for i in range(len(value['Artists'])):
            dictData = {}
            if value['Artists'][i] in lstTopCountryArtists:
                dictData['Title'] = value['Title']
                dictData['Artists'] = value['Artists']
                dictData['Date'] = value['Date']
                dictData['Medium'] = value['Medium']
                dictData['Dimensions'] = value['Dimensions']
                lt.addLast(listData, dictData)
                break

    return lstf, listData


def createNewDisplay(catalog, a1, a2, area):

    lstValidArtworks = lt.newList('ARRAY_LIST')
    for artwork in lt.iterator(catalog['artworks']):
        dictInfo = {}
        if ((artwork['Date'] >= a1) and (artwork['Date'] <= a2) and (artwork['Classification'] == 'Painting'
             or artwork['Classification'] == 'Photograph'or artwork['Classification'] == 'Print' or artwork['Classification'] == 'Drawing')):
            height = (artwork['Height (cm)'])/100
            width = (artwork['Width (cm)'])/100
            areaArtwork = height*width
            dictInfo['Title'] = artwork['Title']
            dictInfo['Artists'] = artwork['Artists']
            dictInfo['Date'] = artwork['Date']
            dictInfo['Classification'] = artwork['Classification']
            dictInfo['Medium'] = artwork['Medium']
            dictInfo['Dimensions'] = artwork['Dimensions']
            dictInfo['Area'] = areaArtwork
            lt.addLast(lstValidArtworks, dictInfo)

    areaTemp = 0
    lstExpo = lt.newList('ARRAY_LIST')
    for validArtwork in lt.iterator(lstValidArtworks):
        lt.addLast(lstExpo, validArtwork)
        areaTemp += validArtwork['Area']
        if areaTemp >= area:
            areaTempF = areaTemp-validArtwork['Area']
            break
        else:
            areaTempF = areaTemp
    lt.removeLast(lstExpo)

    return lstExpo, areaTempF


def moveDepartment(catalog, department):

    lstDepartment = lt.newList('ARRAY_LIST')
    totalPrice = 0
    totalWeight = 0
    for artwork in lt.iterator(catalog['artworks']):
        dictDepartment = {}
        area = 0
        volume = 0
        weight = 0
        p1 = 0
        p2 = 0
        p3 = 0
        may = 0
        if artwork['Department'] == department:
            dictDepartment['Title'] = artwork['Title']
            area = (artwork['Height (cm)'] * artwork['Width (cm)'])/10000
            volume = (artwork['Height (cm)'] * artwork['Width (cm)'] * artwork['Length (cm)'])/1000000
            weight = artwork['Weight (kg)']
            p1 = area * 72
            p2 = volume * 72
            p3 = weight * 72

            if p1 > p2:
                may = p1
            else:
                p2 = may

            if p3 > may:
                may = p3

            if may == 0:
                may = 48

            dictDepartment['Price'] = may
            dictDepartment['Artists'] = artwork['Artists']
            dictDepartment['Classification'] = artwork['Classification']
            dictDepartment['Date'] = artwork['Date']
            dictDepartment['Medium'] = artwork['Medium']
            dictDepartment['Dimensions'] = artwork['Dimensions']
            lt.addLast(lstDepartment, dictDepartment)
            totalPrice += may
            totalWeight += weight

    ltsize = lt.size(lstDepartment)
    sub_list = lt.subList(lstDepartment, 1, ltsize)
    sub_list = sub_list.copy()
    sortedDate_list = None
    sortedDate_list = ms.sort(sub_list, cmpArtworkByDate)
    sub_list2 = lt.subList(lstDepartment, 1, ltsize)
    sub_list2 = sub_list2.copy()
    sortedPrice_list = None
    sortedPrice_list = ms.sort(sub_list2, cmpArtworkByPrice)

    return totalPrice, totalWeight, sortedDate_list, sortedPrice_list


# Funciones utilizadas para comparar elementos dentro de una lista


def compareArtists(artistid1, artist):
    if artistid1 == artist['ConstituentID']:
        return 0
    return -1


def compareArtworks(artworkid, artwork):
    if artworkid in artwork['ArtistsID']:
        return 0
    return -1


# Funciones de ordenamiento

def cmpArtworkByDate(artwork1, artwork2):

    if artwork1['Date'] == '':
        date1 = 2021
        artwork1['Date'] = 2021
    else:
        date1 = int(artwork1['Date'])

    if artwork2['Date'] == '':
        date2 = 2021
        artwork2['Date'] = 2021
    else:
        date2 = int(artwork2['Date'])

    if date1 < date2:
        r = True
    else:
        r = False

    return r


def cmpArtworkByPrice(artwork1, artwork2):

    if artwork1['Price'] < artwork2['Price']:
        r = True
    else:
        r = False
    return r


def cmpArtworkByDateAcquired(artwork1, artwork2):
    """ Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
        Args:
            artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
            artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    date1 = artwork1['DateAcquired'].split("-")
    date2 = artwork2['DateAcquired'].split("-")
    r = None
    if (len(date1) < 2):
        date1 = [2021, 10, 20]
        artwork1['DateAcquired'] = '2021-10-02'
    if (len(date2)) < 2:
        date2 = [2021, 10, 20]
        artwork2['DateAcquired'] = '2021-10-02'

    if int(date1[0]) < int(date2[0]):
        r = True
    elif int(date1[0]) > int(date2[0]):
        r = False
    elif int(date1[1]) < int(date2[1]):
        r = True
    elif int(date1[1]) > int(date2[1]):
        r = False
    elif int(date1[2]) < int(date2[2]):
        r = True
    elif int(date1[2]) > int(date2[2]):
        r = False

    return r


def cmpCountriesbyArtworks(country1, country2):

    r = None
    if country1 > country2:
        r = True
    else:
        r = False

    return r


def cmpArtistbyBirthDate(date1, date2):
    birth1 = int(date1['BeginDate'])
    birth2 = int(date2['BeginDate'])
    r = None

    if birth1 > birth2:
        r = True
    else:
        r = False
    return r

def cmpArtistbyTachnique (Medium1, Medium2):
    r = None
    if Medium1 > Medium2:
        r = True
    else:
        r = False
    return r