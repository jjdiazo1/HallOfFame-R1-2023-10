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


from DISClib.DataStructures.arraylist import newList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qui
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf
import datetime as dt
import time
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo de Obras de arte.
    """
    catalog = {'Artwork': None,
               'Artist': None}

    catalog['Artwork'] = lt.newList(tipo)
    catalog['Artist'] = lt.newList(tipo,
                                    cmpfunction=compareartist)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    a = newArtwork(artwork['ObjectID'],artwork['Title'],artwork['ConstituentID'],
                    artwork['Date'],artwork['Medium'],artwork['Dimensions'],
                    artwork['CreditLine'],artwork['AccessionNumber'],artwork['Classification'],
                    artwork['Department'],artwork['DateAcquired'],artwork['Cataloged'],
                    artwork['URL'],artwork['Circumference (cm)'],artwork['Depth (cm)'],
                    artwork['Diameter (cm)'],artwork['Height (cm)'],artwork['Length (cm)'],
                    artwork['Weight (kg)'],artwork['Width (cm)'],artwork['Seat Height (cm)'],
                    artwork['Duration (sec.)'])

    lt.addLast(catalog['Artwork'], a)


def addArtist(catalog, artist):
    a = newArtist(artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'],
                    artist['Nationality'], artist['Gender'], artist['BeginDate'], 
                    artist['EndDate'], artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['Artist'], a)


# Funciones para creacion de datos

def newArtist(ConstituentID, DisplayName, ArtistBio, Nationality, Gender,
                BeginDate, EndDate, WikiQID, ULAN):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {}
    artist['ConstituentID'] = int(ConstituentID)
    artist['DisplayName'] = DisplayName
    artist['ArtistBio'] = ArtistBio
    artist['Nationality'] = Nationality
    if Nationality == "":
        artist['Nationality'] = "Unknown"
    artist['Gender'] = Gender
    if Gender == "":
        artist['Gender'] = "Unknown"
    artist['BeginDate'] = int(BeginDate)
    artist['EndDate'] = int(EndDate)
    artist['Wiki QID'] = WikiQID
    if WikiQID == "":
        artist['Wiki QID'] = "Unknown"
    artist['ULAN'] = ULAN
    if ULAN == "":
        artist['ULAN'] = "Unknown"
    
    return artist

def newArtwork (ObjectID, Title, ConstituentID, Date, Medium, Dimensions, CreditLine,
                AccessionNumber, Classification, Department, DateAcquired, Cataloged,
                URL, Circumference, Depth, Diameter, Height, Length, Weight, Width,
                SeatHeight, Duration):
        
    constID_str = ConstituentID.replace('[', '').replace(']','').split(",")
    constID_int = [int(x) for x in constID_str]

    artwork = {}
    artwork['ObjectID'] = int(ObjectID.replace('[', '').replace(']',''))
    artwork['Title'] = Title
    artwork['ConstituentID'] = constID_int
    if Date == "":
        artwork['Date'] = 5000
    else:
        artwork['Date'] = int(Date)
    artwork['Medium'] = Medium
    if Medium == "":
        artwork['Medium'] = "Unknown"
    artwork['Dimensions'] = Dimensions
    if Dimensions == "":
        artwork['Dimensions'] = "Unknown"
    artwork['CreditLine'] = CreditLine
    artwork['AccessionNumber'] = AccessionNumber
    artwork['Classification'] = Classification
    artwork['Department'] = Department
    if DateAcquired != "":
        date = DateAcquired.split("-")
        artwork['Date Acquired'] = dt.date(int(date[0]),int(date[1]),int(date[2]))
    else:
        artwork['Date Acquired'] = dt.date.today()
    artwork['Cataloged'] = Cataloged
    artwork['URL'] = URL
    if URL == "":
        artwork['URL'] = "Unknown"
    artwork['Circumference'] = Circumference
    if Circumference == "":
        artwork['Circumference'] = 0
    artwork['Depth'] = Depth
    if Depth == "":
        artwork['Depth'] = 0
    if Diameter == "":
        artwork['Diameter'] = 0
    else:
        artwork['Diameter'] = float(Diameter)
    artwork['Height'] = Height
    if Height == "":
        artwork['Height'] = 0
    artwork['Length'] = Length
    if Length == "":
        artwork['Length'] = 0
    artwork['Weight'] = Weight
    if Weight == "":
        artwork['Weight'] = 0
    artwork['Width'] = Width
    if Width == "":
        artwork['Width'] = 0
    artwork['SeatHeight'] = SeatHeight
    if SeatHeight == "":
        artwork['SeatHeight'] = "Unknown"
    artwork['Duration'] = Duration
    if Duration == "":
        artwork['Duration'] = "Unknown"
    return artwork

def addArea(catalog):
    Artwork = catalog['Artwork']

    for i in lt.iterator(Artwork):
        Height = float(i['Height'])
        Width = float(i['Width'])
        Radius = float(i['Diameter'] / 2) / 100
        ArtworkArea = (Height*Width)/10000
        if i['Diameter'] != 0:
            ArtworkArea = math.pi * (Radius**2)
        i['Area'] = round(ArtworkArea,5)

# Funciones de consulta
def getFirts(catalog, num):
    """
    Retorna los primeros num elementos de una lista
    """
    first = lt.newList('ARRAY_LIST')
    rangmax = num +1
    for i in range(1, rangmax):
        element = lt.getElement(catalog, i)
        lt.addLast(first, element)
    return first

def getLast(catalog, num):
    """
    Retorna los ultimos num elementos de una lista
    """
    last = lt.newList('ARRAY_LIST')
    rangmin = num-1
    for i in range((lt.size(catalog)-rangmin),lt.size(catalog)+1):
        element = lt.getElement(catalog, i)
        lt.addLast(last, element)
    return last

def getCronologicalArtist (sortedArtist_BDate, beginDate, endDate):
    """
    Req 1
    Retorna la lista de los artistas nacidos entre beginDate y endDate
    """
    BornInRange = lt.newList('ARRAY_LIST')
    for artista in lt.iterator(sortedArtist_BDate):
        if beginDate <= artista['BeginDate'] and endDate >= artista['BeginDate']:
            lt.addLast(BornInRange, artista)
    return BornInRange

def getCronologicalArtwork (sortedArtwork_Date, beginDate, endDate):
    """
    Req 2
    Retorna la lista de las obras que fueron adquiridas entre beginDate y endDate
    """
    AcquiredInRange = lt.newList('ARRAY_LIST')
    for artwork in lt.iterator(sortedArtwork_Date):
        if beginDate <= artwork['Date Acquired'] and endDate >= artwork['Date Acquired']:
            lt.addLast(AcquiredInRange, artwork)
    
    return AcquiredInRange

def getArtworksPurchased (catalog):
    """
    Req 2
    Retorna el numero de obras que fueron adquiridas por compra ('purchase')
    """
    purchased = 0
    for item in lt.iterator(catalog):
        if "purchase" in item['CreditLine'].lower():
            purchased += 1
    return purchased

def getArtistInfo(catalog, artistName):
    """
    Req 3
    Retorna una el diccionario del artista a examinar
    Si no se encuentra el artista se retorna None
    """
    artist = catalog['Artist']
    info = None
    for i in lt.iterator(artist):
        if i['DisplayName'].lower() == artistName.lower():
            info = i
            break
    return info

def getArtistsArtwork(catalog, artistID):
    """
    Req 3
    Retorna una TAD lista con todas las obras del artista
    """
    artwork = catalog['Artwork']
    ArtistsArtwork = lt.newList('ARRAY_LIST')
    for i in lt.iterator(artwork):
        if artistID in i['ConstituentID']:
            lt.addLast(ArtistsArtwork, i)
    return ArtistsArtwork

def getArtistTechnique(catalog):
    """
    Req 3
    Retorna una tupla: 
        1. Diccionario con todas las tecnicas de el artista
        como llaves y la cantidad respectivas de obras como valores
        2. La tecnica mas usada
    """
    Technique = {}
    top1 = 0
    topMedium = None
    for i in lt.iterator(catalog):
        medium = i["Medium"]
                
        veces = Technique.get(medium,0)
                
        Technique[medium] = veces +1                
        if Technique[medium] > top1:
            top1 = Technique[medium]
            topMedium = medium

    return Technique, topMedium

def getArtworkNationality(catalog):

    """
    Req 4.
    Retorna:
        1. La lista del top 10 nacionalidades, con su respectivo numero de obras
        2. Las obras de la nacionalidad que se encuentra en la primera posicion de la lista

    """
    obras = {'Unknown': []} 
    artistas = {} 
    autores = {}

    for artist in lt.iterator(catalog['Artist']):
        artistas[str(artist['ConstituentID'])] = artist
    
    for artwork in lt.iterator(catalog['Artwork']):
        stringIDs = str(artwork['ConstituentID'])
        artistIDs = stringIDs[1:-1].replace(" ", "").split(",")
        if len(artistIDs) == 0:
            obras['Unknown'].append(artwork)
        
        for id in artistIDs:
            artist = artistas[id]
            if artwork['ObjectID'] in autores:
                autores[artwork['ObjectID']].append(artist['DisplayName'])
            else:
                autores[artwork['ObjectID']] = [artist['DisplayName']]
            nacionalidad = artist['Nationality']
            if nacionalidad == 'Nationality unknown':
                obras['Unknown'].append(artwork)
            elif nacionalidad in obras:
                obras[nacionalidad].append(artwork)
            else:
                obras[nacionalidad] = [artwork]

    sorted_list = lt.newList('ARRAY_LIST')
    for key in obras:
        lt.addLast(sorted_list, {'Longitud':len(obras[key]), 'Nacionalidad': key})

    mer.sort(sorted_list, cmpArtistbyNationality)
    lista = lt.subList(sorted_list, 1, 10)
    
    return lista, obras[lt.getElement(lista, 1)['Nacionalidad']], autores


def getArworkByDepartment (catalog, department):
    """
    Req 5
    Retorna la lista de las obras que pertenecen al departamento dado
    """
    art = lt.newList('ARRAY_LIST')
    for i in lt.iterator(catalog):
        if i['Department'].lower() == department.lower():
            lt.addLast(art, i)
    return art

def getTransportationCost(catalog):
    """
    Req 5
    Se calcula el costo para transportar cada obra del catalogo dado y
    se añade a su respectivo diccionario el calculo mas costoso multiplicado 
    por 72; si no hay informacion suficiente para el calculo se deduce que 
    el costo es de 48 USD.

    Retorna una tupla:
        1. El catalogo actualizado .
        2. La suma estimada de los costos de transporte de las obra.
        3. La suma estimada del peso de las obras.
    """
    for i in lt.iterator(catalog):
        Weight = float(i['Weight'])
        Length = float(i['Length'])
        Width = float(i['Width'])
        Height = float(i['Height'])
        Radius = float(i['Diameter'] / 2) / 100

        m2 = (Height*Width)/10000
        m3 = (Height*Width*Length)/1000000
        m2_v2 = math.pi * (Radius**2)
        m3_v2 =  (4/3)*(math.pi)*(Radius**3)

        mayor = max(m2,m3,m2_v2,m3_v2,Weight)
        cost = 48
        if mayor != 0:
            cost = round(72*mayor, 3)
        
        i['TransCost'] = cost

    return catalog


def getArtworkTotal_CostWeight(catalog):
    """
    Req 5
    Retorna una tupla:
        1. La suma estimada de los costos de transporte de las obra.
        2. La suma estimada del peso de las obras.
    """
    Totalcost = 0
    TotalWeight = 0
    for i in lt.iterator(catalog):
        Totalcost += i['TransCost']
        TotalWeight += float(i['Weight'])
    return round(Totalcost,3) ,  round(TotalWeight,3)


def createNewDisplay(catalog,beginYear, finalYear, area):
    Artwork = catalog['Artwork']
    display = lt.newList('ARRAY_LIST')

    totalArtworks = 0
    artArea = 0
    areaUsed = 0
    for i in lt.iterator(Artwork):
        if (beginYear <= i['Date'] and finalYear >= i['Date']) and (i['Area'] <= area):
            totalArtworks +=1
            if (i['Classification'] == 'Painting' or i['Classification'] == 'Photograph' \
                or i['Classification'] == 'Print' or i['Classification'] == 'Drawing') and (i['Area'] != 0):

                artArea += i['Area']
                if area < artArea:
                    continue
                else:
                    areaUsed = artArea
                    lt.addLast(display, i)
    
    return display, areaUsed, totalArtworks
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartist (authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def cmpArtistByBeginDate(Artist1, Artist2):
    return (int(Artist1['BeginDate']) < int(Artist2['BeginDate']))


def cmpArtworkByDateAcquired(artwork1, artwork2): 
    return artwork1['Date Acquired'] < artwork2['Date Acquired']

def cmpArtworkByTransCost (cost1, cost2):
    return cost1['TransCost'] > cost2['TransCost']

def cmpArtworkByDate(artwork1, artwork2): 
    return artwork1['Date'] < artwork2['Date']

def cmpArtistbyNationality(artist1, artist2):
    return artist1['Longitud'] > artist2['Longitud']



# Funciones de ordenamiento

def sortArtworkCatalogByDateAcquired(catalog, size, Sort_Type):
    sub_list = lt.subList(catalog, 1, size)
    sub_list = sub_list.copy()
    sorted = None
    start = time.process_time()
    if Sort_Type == 1:
        sorted = qui.sort(sub_list, cmpArtworkByDateAcquired)
    elif Sort_Type == 2:
        sorted = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif Sort_Type == 3:
        sorted = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif Sort_Type == 4:
        sorted = mer.sort(sub_list, cmpArtworkByDateAcquired)
    end = time.process_time()
    time_mseg = (end - start)*1000
    return time_mseg, sorted

def sortArtistCatalogByBeginDate(catalog, size, Sort_Type):
    sub_list = lt.subList(catalog, 1, size)
    sub_list = sub_list.copy()
    sorted = None
    start = time.process_time()
    if Sort_Type == 1:
        sorted = qui.sort(sub_list, cmpArtistByBeginDate)
    elif Sort_Type == 2:
        sorted = ins.sort(sub_list, cmpArtistByBeginDate)
    elif Sort_Type == 3:
        sorted = sa.sort(sub_list, cmpArtistByBeginDate)
    elif Sort_Type == 4:
        sorted = mer.sort(sub_list, cmpArtistByBeginDate)
    end = time.process_time()
    time_mseg = (end - start)*1000
    return time_mseg, sorted

def sortArtworkCatalogByDate(catalog, size, Sort_Type):
    sub_list = lt.subList(catalog, 1, size)
    sub_list = sub_list.copy()
    sorted = None
    start = time.process_time()
    if Sort_Type == 1:
        sorted = qui.sort(sub_list, cmpArtworkByDate)
    elif Sort_Type == 2:
        sorted = ins.sort(sub_list, cmpArtworkByDate)
    elif Sort_Type == 3:
        sorted = sa.sort(sub_list, cmpArtworkByDate)
    elif Sort_Type == 4:
        sorted = mer.sort(sub_list, cmpArtworkByDate)
    end = time.process_time()
    time_mseg = (end - start)*1000
    return time_mseg, sorted

def sortArtworkCatalogByTransCost(catalog):
    return mer.sort(catalog, cmpArtworkByTransCost)
    