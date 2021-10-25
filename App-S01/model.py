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

import time
import math
import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures.arraylist import size, subList
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#######################################################################################################################
# Construccion de modelos
#######################################################################################################################

def newCatalog(data_structure):

    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList(datastructure=data_structure)
    catalog['artworks'] = lt.newList(datastructure=data_structure)

    return catalog

#######################################################################################################################
# Funciones para agregar informacion al catalogo
#######################################################################################################################

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)

#######################################################################################################################

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)

#######################################################################################################################
# Funciones para creacion de datos
#######################################################################################################################
def CreationArtistsIDDict(lst):
    artists_ID_dict = {}

    for artist in lt.iterator(lst):
        artist_ID = artist['ConstituentID']
        artists_ID_dict[artist_ID] = artist

    return artists_ID_dict

#######################################################################################################################

def FilteringArtistsByBirthYear(sub_list, initial_birth_year, end_birth_year, data_structure):
    artists_birth_year_range_list = lt.newList(datastructure=data_structure)

    for artist in lt.iterator(sub_list):
        artists_birth_date = int(artist['BeginDate'])
        initial_birth_year_verification = initial_birth_year <= artists_birth_date 
        end_birth_year_verification = artists_birth_date <= end_birth_year
        if initial_birth_year_verification and end_birth_year_verification:
            lt.addLast(artists_birth_year_range_list, artist)

    return artists_birth_year_range_list

#######################################################################################################################

def FilteringArtworksByAdquisitionDate(sub_list, initial_adquisition_date, end_adquisition_date, data_structure):
    artworks_adquisition_date_range_list = lt.newList(datastructure=data_structure)

    for artwork in lt.iterator(sub_list):
        artwork_adquisition_date = artwork['DateAcquired']
        artwork_adquisition_date_in_days = TransformationDateToDays(artwork_adquisition_date)
        initial_date_adquisition_in_days = TransformationDateToDays(initial_adquisition_date)
        end_date_adquisition_in_days = TransformationDateToDays(end_adquisition_date)

        initial_date_verification = initial_date_adquisition_in_days <= artwork_adquisition_date_in_days
        end_date_verification = artwork_adquisition_date_in_days <= end_date_adquisition_in_days
        if initial_date_verification and end_date_verification:
            lt.addLast(artworks_adquisition_date_range_list, artwork)

    return artworks_adquisition_date_range_list

#######################################################################################################################

def FilteringArtworksByAdquisitionDateAndCreditLine(artworks_adquisition_range_list, data_structure):
    purchased_artworks_list = lt.newList(datastructure=data_structure)

    for artwork in lt.iterator(artworks_adquisition_range_list):
        artwork_credit_line = artwork['CreditLine']
        if 'purchase' in artwork_credit_line.lower():
            lt.addLast(purchased_artworks_list, artwork)

    return purchased_artworks_list

#######################################################################################################################

def GetConstituentIDListArtwork(artwork):
    ID = artwork['ConstituentID']
    artwork_constituent_IDs = ID.strip(ID[0]).strip(ID[-1]).split(', ')
    return artwork_constituent_IDs

#######################################################################################################################

def CreationArtistTechniquesInformation(sub_list, lst, artist_name, data_structure):
    artist_ID = GetArtistConstituentID(lst, artist_name)
    artist_artworks = lt.newList(datastructure=data_structure)
    artist_techniques_dict = {}
    artist_techniques_list = lt.newList(datastructure=data_structure)

    for artwork in lt.iterator(sub_list):
        if artist_ID in GetConstituentIDListArtwork(artwork):
            lt.addLast(artist_artworks, artwork)
            artwork_technique = artwork['Medium']
            if artwork_technique not in artist_techniques_dict:
                artist_techniques_dict[artwork_technique] = lt.newList(datastructure=data_structure)
                lt.addLast(artist_techniques_dict[artwork_technique], artwork)
            else:
                lt.addLast(artist_techniques_dict[artwork_technique], artwork)

    for technique in artist_techniques_dict:
        artworks_technique = artist_techniques_dict[technique]
        lt.addFirst(artist_techniques_list, [technique, artworks_technique])

    return artist_artworks, artist_techniques_list

#######################################################################################################################

def CreateDictNumPerNationality(sub_list, artists_ID_dict):
        num_artworks_nationalities = {}
        for artwork in lt.iterator(sub_list):
            for artist_ID in GetConstituentIDListArtwork(artwork):
                artist_info = artists_ID_dict[artist_ID]
                artist_info = artists_ID_dict[artist_ID]
                artist_nationality = artist_info['Nationality']
                if artist_nationality not in num_artworks_nationalities:
                    num_artworks_nationalities[artist_nationality] = 1
                else:
                    num_artworks_nationalities[artist_nationality] += 1
        return num_artworks_nationalities
    
#######################################################################################################################

def CreateNationalityNumList(num_artworks_nationalities, data_structure):
        artworks_nationalities_list = lt.newList(datastructure=data_structure)
        for nationality in num_artworks_nationalities:
            num_artworks = num_artworks_nationalities[nationality]
            element = [nationality, num_artworks]
            lt.addLast(artworks_nationalities_list, element)
        return artworks_nationalities_list

#######################################################################################################################

def CalculateCostAndWeight(Weight, Length, Width, Height):
    if Weight != '':
        weight = float(Weight)
    else:
        weight = 0

    if Width != '' and Height != '':
        area = float(Width)*float(Height)/10000
    else:
        area = 0
    
    if Length != '':
        volume = area*float(Length)/100
    else:
        volume = area

    cost_volume = 72*volume
    cost_area = 72*area
    cost_weight = 72*weight

    if cost_volume != 0 or cost_weight != 0 or cost_area != 0:
        if cost_weight <= cost_volume and cost_area <= cost_volume:
            artwork_cost = cost_volume
        elif cost_volume <= cost_area and cost_weight <= cost_area:
            artwork_cost = cost_area
        else:
            artwork_cost = cost_weight
    else:
        artwork_cost = 48

    return artwork_cost, weight

#######################################################################################################################

def CreateArtworkTransportationCostList(sub_list, department, data_structure):
    artworks_by_date = lt.newList(datastructure=data_structure)
    artworks_by_cost = lt.newList(datastructure=data_structure)
    total_cost = 0
    total_weight = 0

    for artwork in lt.iterator(sub_list):
        department_artwork = artwork['Department']
        if department_artwork == department:
            Weight = artwork['Weight (kg)']
            Height = artwork['Height (cm)']
            Length = artwork['Length (cm)']
            Width = artwork['Width (cm)']

            information = CalculateCostAndWeight(Weight, Length, Width, Height)
            artwork_transportaion_cost = information[0]
            artwork_weight = information[1]
            
            total_cost += artwork_transportaion_cost
            total_weight += artwork_weight

            lt.addLast(artworks_by_date, [artwork, artwork_transportaion_cost])
            lt.addLast(artworks_by_cost, [artwork, artwork_transportaion_cost])  

    return artworks_by_date, artworks_by_cost, total_cost, total_weight

#######################################################################################################################

def CreationOrderedListByDate(ArtworksDepartment, SortingMethod):
    sub_list_date = ArtworksDepartment.copy()
    ordered_list_by_date = SortingMethodExecution(SortingMethod, sub_list_date, cmpArtworkByCreationDate)
    oldest_artworks = lt.subList(ordered_list_by_date,1,5)

    return oldest_artworks

#######################################################################################################################

def CreationOrderedListByCost(ArtworksDepartment, SortingMethod):
    sub_list_cost = ArtworksDepartment.copy()
    ordered_list_by_cost = SortingMethodExecution(SortingMethod, sub_list_cost, cmpArtworkBycost)
    most_expensive_artworks = lt.subList(ordered_list_by_cost,1,5)

    return most_expensive_artworks

#######################################################################################################################
# Funciones de consulta
#######################################################################################################################

def GetTheFirstElements(lst, num, data_structure):

    first_elements = lt.newList(datastructure=data_structure)
    for index in range(1, num + 1):
        element = lt.getElement(lst, index)
        lt.addLast(first_elements, element)

    return first_elements

#######################################################################################################################

def GetTheLastElements(lst, num, data_structure):
    size = lt.size(lst) + 1
    last_elements = lt.newList(datastructure=data_structure)

    for index in range(1, num + 1):
        element = lt.getElement(lst, size - index)
        lt.addLast(last_elements, element)

    return last_elements
    
#######################################################################################################################
# Funciones utilizadas para comparar elementos dentro de una lista
#######################################################################################################################

def cmpArtistByBirthDate(artist1, artist2):
    birth_date_artist1 = int(artist1['BeginDate'])
    birth_date_artist2 = int(artist2['BeginDate'])

    return birth_date_artist1 > birth_date_artist2

#######################################################################################################################

def TransformationDateToDays(date):
    date_information = date.split('-')
    if len(date_information) != 1:
        date_in_days = int(date_information[0])*365 + int(date_information[1])*30 + int(date_information[2])
    else:
        date_in_days = 0
    return date_in_days

#######################################################################################################################

def cmpArtworkByDateAcquired(artwork1, artwork2): 
    """ 
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2 Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired' 
    """
    date_acquired_artwork_1 = TransformationDateToDays(artwork1['DateAcquired'])
    date_acquired_artwork_2 = TransformationDateToDays(artwork2['DateAcquired'])
    return date_acquired_artwork_1 > date_acquired_artwork_2

#######################################################################################################################

def cmpTechniquesBySize(technique1, technique2):
    size_technique1 = lt.size(technique1[1])
    size_technique2 = lt.size(technique2[1])

    return size_technique1 > size_technique2

#######################################################################################################################

def GetArtistConstituentID(lst, artist_name):
    found_artist = False
    index = 1
    while found_artist == False and index <= lt.size(lst):
        artist =lt.getElement(lst, index)
        artist_name_list = artist['DisplayName']
        if artist_name_list.lower() == artist_name.lower():
            artist_ID = artist['ConstituentID']
            found_artist = True
        else:
            index += 1
    return artist_ID

#######################################################################################################################

def cmpNationalitiesBySize(nationality1, nationality2):
    size_nationality1 = nationality1[1]
    size_nationality2 = nationality2[1]

    return size_nationality1 > size_nationality2

#######################################################################################################################

def cmpArtworkByCreationDate(artwork1, artwork2):
    creation_date_artwork1 = artwork1[0]['Date']
    creation_date_artwork2 = artwork2[0]['Date']
    if creation_date_artwork1 != '':
        creation_date_artwork1 = int(creation_date_artwork1)
    else:
        creation_date_artwork1 = 0
    if creation_date_artwork2 != '':
        creation_date_artwork2 = int(creation_date_artwork2)
    else:
        creation_date_artwork2 = 0

    if creation_date_artwork1 != 0 and creation_date_artwork2 != 0:
        result = creation_date_artwork1 < creation_date_artwork2
    elif creation_date_artwork1 == 0 and creation_date_artwork2 != 0:
        result = False
    elif creation_date_artwork1 != 0 and creation_date_artwork2 == 0:
        result = True
    else:
        result = False
    return result

#######################################################################################################################

def cmpArtworkBycost(artwork1, artwork2):
    cost_artwork1 = artwork1[1]
    cost_artwork2 = artwork2[1]

    return cost_artwork1 > cost_artwork2

#######################################################################################################################
# Funciones de ordenamiento
#######################################################################################################################

def SortingMethodExecution(sorting_method, sub_list, cmpFunction):
    if sorting_method == 1:
        sorted_list = insertion.sort(sub_list, cmpFunction)
    elif sorting_method == 2:
        sorted_list = shell.sort(sub_list, cmpFunction)
    elif sorting_method == 3:
        sorted_list = merge.sort(sub_list, cmpFunction)
    else:
        sorted_list = quick.sort(sub_list, cmpFunction)

    return sorted_list

#######################################################################################################################

def SortArtistByBirthYear(sub_list, sorting_method, initial_year_birth, end_year_birth, data_structure):
    start_time = time.process_time()

    sub_list = sub_list.copy()
    artists_birth_year_range_list = FilteringArtistsByBirthYear(sub_list, initial_year_birth,
                                                                             end_year_birth, data_structure)
    sorted_list = SortingMethodExecution(sorting_method, artists_birth_year_range_list, cmpArtistByBirthDate)

    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    
    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def SortArtworksAdquisition(sub_list, sorting_method):
    start_time = time.process_time()

    sub_list = sub_list.copy()
    sorted_list = SortingMethodExecution(sorting_method, sub_list, cmpArtworkByDateAcquired)

    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000 

    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def SortArtworksAdquisitionRange(sub_list, sorting_method, initial_date_adquisition, 
                                                                                end_date_adquisition, data_structure):
    start_time = time.process_time()
    sub_list = sub_list.copy()

    artworks_adquisition_date_range_list = FilteringArtworksByAdquisitionDate(sub_list, initial_date_adquisition, 
                                                                                    end_date_adquisition, data_structure)
    purchase_artworks_num = lt.size(FilteringArtworksByAdquisitionDateAndCreditLine(artworks_adquisition_date_range_list,
                                                                                                     data_structure))
    sorted_list_by_date = SortingMethodExecution(sorting_method, artworks_adquisition_date_range_list,
                                                                                             cmpArtworkByDateAcquired)

    stop_time = time.process_time()
    elapsed_time_mseg = elapsed_time_mseg = (stop_time - start_time)*1000  
    
    return elapsed_time_mseg, sorted_list_by_date, purchase_artworks_num

#######################################################################################################################

def ClasifyArtistsTechnique(sub_list, lst, sorting_method, artist_name, data_structure):
    start_time = time.process_time()
    sub_list = sub_list.copy()

    information = CreationArtistTechniquesInformation(sub_list, lst, artist_name, data_structure)
    artist_artworks = information[0]
    artist_techniques = information[1]
    sorted_artist_techniques = SortingMethodExecution(sorting_method, artist_techniques, cmpTechniquesBySize)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return elapsed_time_mseg, artist_artworks, sorted_artist_techniques

#######################################################################################################################

def ClasifyArtworksByNationality(sub_list, sorting_method, artists_ID_dict, data_structure):
    start_time = time.process_time()
    sub_list = sub_list.copy()

    num_artworks_nationalities = CreateDictNumPerNationality(sub_list, artists_ID_dict)
    artworks_nationalities_list = CreateNationalityNumList(num_artworks_nationalities, data_structure)
    sorted_list = SortingMethodExecution(sorting_method, artworks_nationalities_list, cmpNationalitiesBySize)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000  

    return elapsed_time_mseg, sorted_list

#######################################################################################################################

def TransportArtworksDepartment(sub_list, sorting_method, department, data_structure):
    start_time = time.process_time()
    information = CreateArtworkTransportationCostList(sub_list, department, data_structure)
    artworks_by_date = information[0]
    artworks_by_cost = information[1]
    total_cost = information[2]
    total_weight = information[3]           
    oldest_artworks = CreationOrderedListByDate(artworks_by_date, sorting_method)
    most_expensive_artworks = CreationOrderedListByCost(artworks_by_cost, sorting_method)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, artworks_by_date, total_cost, total_weight, most_expensive_artworks, oldest_artworks 