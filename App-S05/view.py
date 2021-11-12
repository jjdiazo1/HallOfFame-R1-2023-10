"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import datetime as dt
import prettytable
from prettytable import PrettyTable
import time as tm

""" 
Utilizar el siguiente codigo en caso de que se alcance el limite de recursion y mande el 
siguiente error “RecursionError: maximum recursion depth exceeded in 
comparison”
"""
default_limit = 1000 
sys.setrecursionlimit(default_limit*100) 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Organizar el catalogo de artistas por Begin Date")
    print("3- Organizar el catalogo de obras por Date Acquired")
    print("4- Organizar el catalogo de obras por Date")
    print("5- Req 1: Listar cronológicamente los artistas")
    print("6- Req 2: Listar cronológicamente las adquisiciones")
    print("7- Req 3: Clasificar obras de un artista por técnica")
    print("8- Req 4: Clasificar obras por la nacionalidad de sus creadores")
    print("9- Req 5: Transportar obras de un departamento")
    print("10- Req 6: Proponer una nueva exposición en el museo")
    

def initCatalog(tipo):
    """
    Inicializa el catalogo del museo
    """
    return controller.initCatalog(tipo)

def loadData(catalog):
    """
    Carga los datos del mueso en la estructura de datos
    """
    controller.loadData(catalog)

def addArea(catalog):
    controller.addArea(catalog)


def printArtistTable(artist):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["ConstituentID", "DisplayName",
                    "BeginDate", "Nationality", 
                    "Gender", "ArtistBio", 
                    "Wiki QID", "ULAN"]

    x._max_width = {"DisplayName":18}

    for i in lt.iterator(artist):
        x.add_row([ i["ConstituentID"], i["DisplayName"], 
                    i["BeginDate"], i["Nationality"], 
                    i["Gender"], i["ArtistBio"], 
                    i["Wiki QID"], i["ULAN"]])
    x.align = "l"
    x.align["ConstituentID"] = "r"
    x.align["BeginDate"] = "r"
    print(x)

def printArtworkTable(artwork):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID", "Medium", 
                    "Dimensions", "Date", 
                    "DateAcquired", "URL"]

    x._max_width = {"Title":18,"ConstituentID":18, "Medium":18, "Dimensions":18, "URL":15}

    for i in lt.iterator(artwork):
        if i["Date"] == 5000:
            x.add_row([ i["ObjectID"], i["Title"], 
                        i["ConstituentID"], i["Medium"], 
                        i["Dimensions"], "Unknown", 
                        i["Date Acquired"], i["URL"]])
        else:
            x.add_row([ i["ObjectID"], i["Title"], 
                        i["ConstituentID"], i["Medium"], 
                        i["Dimensions"], i["Date"], 
                        i["Date Acquired"], i["URL"]])
    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r" 
    print(x)

def printMediumTable(artwork, medium):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID", "Medium", 
                    "Dimensions", "Date", 
                    "DateAcquired", "URL"]

    x._max_width = {"Title":18,"ConstituentID":18, "Medium":18, "Dimensions":18, "URL":15}

    for i in lt.iterator(artwork):
        if i["Medium"] == medium:
            if i["Date"] == 5000:
                x.add_row([ i["ObjectID"], i["Title"], 
                            i["ConstituentID"], i["Medium"], 
                            i["Dimensions"], "Unknown", 
                            i["Date Acquired"], i["URL"]])
            else:
                x.add_row([ i["ObjectID"], i["Title"], 
                            i["ConstituentID"], i["Medium"], 
                            i["Dimensions"], i["Date"], 
                            i["Date Acquired"], i["URL"]]) 
            
    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r" 
    print(x)

def printTransCostTable(artwork, stop):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID","Classification", "Medium", 
                    "Dimensions", "Date", 
                    "TransCost (USD)", "URL"]

    x._max_width = {"Title":16,"ConstituentID":15, "Medium":17,"Classification":17 , "Dimensions":16, "URL":15}
    contador = 0
    for i in lt.iterator(artwork):
        if stop and contador > 4:
            break
        contador += 1
        if i["Date"] == 5000:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i['Classification'], i["Medium"], 
                    i["Dimensions"], "Unknown", 
                    i["TransCost"], i["URL"]])
        else:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i['Classification'], i["Medium"], 
                    i["Dimensions"], i["Date"], 
                    i["TransCost"], i["URL"]])

    x.align = "l"
    x.align["ObjectID"] = "r"
    x.align["Date"] = "r"
    
    print(x)

def printNewDisplay(artwork):
    x = PrettyTable(hrules=prettytable.ALL)
    x.field_names = ["ObjectID", "Title", 
                    "ConstituentID","Classification", "Medium", 
                    "Dimensions", "Date", 
                    "EstArea (m^2)","Department", "URL"]

    x._max_width = {"Title":16,"ConstituentID":15, "Medium":17,"Classification":17 ,"Department":13, "Dimensions":16,"EstArea (m^2)": 14, "URL":15}

    for i in lt.iterator(artwork):
        if i["Date"] == 5000:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i['Classification'], i["Medium"], 
                    i["Dimensions"], "Unknown", 
                    i["Area"],i["Department"], i["URL"]])
        else:
            x.add_row([ i["ObjectID"], i["Title"], 
                    i["ConstituentID"], i['Classification'], i["Medium"], 
                    i["Dimensions"], i["Date"], 
                    i["Area"],i["Department"], i["URL"]])
    print(x)

catalog = None
sortedArtwork_DateA = None
sortedArtwork_Date = None
sortedArtist_BDate = None
DepartmentList = lt.newList()
Area = None
   
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        print('Si desea mostrar el catalogo usando un tipo especifico de lista, observe las opciones a continuacion:')
        print('1. Obtener el catalogo utilizando listas tipo SINGLE_LINKED')
        print('2. Obtener el catalogo utilizando listas tipo ARRAY_LIST')

        inp = input('Selecione una opción para continuar: ')
        print("Cargando información de los archivos ....\n")
        if int(inp) == 1:
            catalog = initCatalog('SINGLE_LINKED')
        else:
            catalog = initCatalog('ARRAY_LIST')
        loadData(catalog)
        
        print('Obras de Arte cargadas: ' + str(lt.size(catalog['Artwork'])))
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))

        print("\nLos últimos 3 artistas son: ")
        artist = controller.getLast(catalog['Artist'], 3)
        printArtistTable(artist)

        print("Las últimas 3 obras son: ")
        art = controller.getLast(catalog['Artwork'], 3)
        printArtworkTable(art)

    elif int(inputs) == 2:
        print("Si desea obtener el catalogo de artistas organizado por Begin Date usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort")
        print("2. Organizar la lista usando Insertionsort")
        print("3. Organizar la lista usando Shellsort")
        print("4. Organizar la lista usando Mergesort")
        orden = int(input('Seleccione una opcion: '))
        if orden not in [1,2,3,4]:
            print("La opcion selecionada no es valida")
        else:
            Artist = catalog['Artist']
            time, sortedArtist_BDate = controller.sortArtistCatalogByBeginDate(Artist, lt.size(Artist), orden)
            print("The time it took to sort the artist catalog by Begin Date with the selected algorithm was:", time ,"mseg\n")

    elif int(inputs) == 3:
        print("Si desea obtener la lista de obras organizada por Date Acquired usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort  ")
        print("2. Organizar la lista usando Insertionsort ")
        print("3. Organizar la lista usando Shellsort ")
        print("4. Organizar la lista usando Mergesort ")
        orden = int(input('Seleccione una opcion: '))
        if orden not in [1,2,3,4]:
            print("La opcion selecionada no es valida")
        else:
            Artwork = catalog['Artwork']
            time, sortedArtwork_DateA = controller.sortArtworkCatalogByDateAcquired(Artwork, lt.size(Artwork), orden)
            print("The time it took to sort the artwork catalog by Date Acquired with the selected algorithm was:", time ,"mseg\n")

    elif int(inputs) == 4:
        print("Si desea obtener la lista de obras organizada por Date usando un algoritmo de organizacion, observe las opciones a continuacion:")
        print("1. Organizar la lista usando Quicksort  ")
        print("2. Organizar la lista usando Insertionsort ")
        print("3. Organizar la lista usando Shellsort ")
        print("4. Organizar la lista usando Mergesort ")
        orden = int(input('Seleccione una opcion: '))
        if orden not in [1,2,3,4]:
            print("La opcion selecionada no es valida")
        else:
            Artwork = catalog['Artwork']
            time, sortedArtwork_Date = controller.sortArtworkCatalogByDate(Artwork,lt.size(Artwork), orden)
            print("The time it took to sort the artwork catalog by Date was:", time ,"mseg\n")

    elif int(inputs) == 5:
        #Req 1

        start = tm.process_time()
        if sortedArtist_BDate == None:
            print("Primero tienes que organizar el catalogo de artistas por BeginDate")
        else:
            beginDate = int(input("Ingrese el año inicial: "))
            endDate = int(input("Ingrese el año final: "))

            print("="*15, " Req No. 1 Inputs ", "="*15)
            print("Artist born between" , beginDate, "and" , endDate, "\n")
            print("="*15, " Req No. 1 Answer ", "="*15)
            ArtistasCrono = controller.getCronologicalArtist(sortedArtist_BDate, beginDate, endDate)
            print("There are ", lt.size(ArtistasCrono), " artist born between", beginDate, " and " , endDate,"\n")

            if lt.size(ArtistasCrono) != 0:
                if lt.size(ArtistasCrono) >= 6:
                    print("The first 3 artist in the range are...")
                    first = controller.getFirts(ArtistasCrono, 3)
                    printArtistTable(first)
                    print("\nThe last 3 artist in the range are...")
                    last = controller.getLast(ArtistasCrono, 3)
                    printArtistTable(last)
                else:
                    print("The artist in the range are...")
                    printArtistTable(ArtistasCrono)

        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")

    elif int(inputs) == 6:
        #Req 2
        start = tm.process_time()
        if sortedArtwork_DateA == None:
            print("Primero tienes que organizar el catalogo de obras por Date Acquired")
        else:
            firstY=int(input("Año incial: "))
            firstM=int(input("Mes incial: "))
            firstD=int(input("Dia inicial: "))
            first=dt.date(firstY,firstM,firstD)

            lastY=int(input("Año final: "))
            lastM=int(input("Mes final: "))
            lastD=int(input("Dia final: "))
            last=dt.date(lastY,lastM,lastD)

            print("="*15, " Req No. 2 Inputs ", "="*15)
            print("Artwork aquired between "+ str(first)+" and " +str(last)+ "\n")
            print("="*15, " Req No. 2 Answer ", "="*15)
            ObrasCrono = controller.getCronologicalArtwork(sortedArtwork_DateA, first, last)
            purchased = controller.getArtworksPurchased(ObrasCrono)
            print("The MoMA acquired", lt.size(ObrasCrono), "unique pieces between", first, "and" , last)
            print("Of which", purchased, "were purchased\n")
            if lt.size(ObrasCrono)!= 0:
                if lt.size(ObrasCrono) >= 6:
                    print("The first 3 artworks in the range are...")
                    primeros = controller.getFirts(ObrasCrono, 3)
                    printArtworkTable(primeros)

                    print("\nThe last 3 artworks in the range are...")  
                    ultimos = controller.getLast(ObrasCrono, 3)
                    printArtworkTable(ultimos)  
                else:
                    print("The artworks in the range are...")
                    printArtworkTable(ObrasCrono)  

        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")              

    elif int(inputs) == 7:
        #Req 3
        start = tm.process_time()
        artistName= input("Ingrese el nombre de la/el artista: ")
        artist_info = controller.getArtistInfo(catalog, artistName)
        if artist_info == None:
            print("El artista no se encontro")
        else:
            Id = artist_info['ConstituentID']
            artworksOfArtist = controller.getArtistsArtwork(catalog, Id)
            Technique, topMedium = controller.getArtistTechnique(artworksOfArtist)
            print("="*15, " Req No. 3 Inputs ", "="*15)
            print("Examine the work of the artist named: "+artistName+"\n")
            print("="*15, " Req No. 3 Answer ", "="*15)
            print(artistName, "with MoMA ID",Id, "has",lt.size(artworksOfArtist), "pieces in her/his name at the museum.")
            if lt.size(artworksOfArtist) != 0:
                print("There are" ,len(Technique), "different mediums/techniques in her/his work.\n")                  

                x = PrettyTable(hrules=prettytable.ALL)
                x.field_names = ["Medium Name", "Count"]
                contador = 0
                for i in Technique.keys():
                    x.add_row([i, Technique[i]])
                x.sortby = "Count"
                x.reversesort = True
                x.align["Medium Name"] = "l"
                x.align["Count"] = "r"

                if len(Technique) > 5:
                    print("Her/his top 5 Medium/Technique are")
                    print(x.get_string(start=0, end=5))
                else:
                    print("Her/his Medium/Technique are:")
                    print(x)

                print("\nHis/her most used Medium/Technique is:", topMedium , "with", Technique[topMedium], "pieces.")
                
                print("The",Technique[topMedium],"works of",topMedium,"from the collection are:")
                printMediumTable(artworksOfArtist, topMedium)

        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")

    elif int(inputs) == 8:
        #Req 4
        start = tm.process_time()
        print("="*15, " Req No. 4 Inputs ", "="*15)
        print("Ranking countries by their number of artworks in the MoMA")
        print("="*15, " Req No. 4 Answer ", "="*15)
        print("The TOP 10 Countries in the MoMA are:")
        artworksByCountry = controller.getArtworkNationality(catalog)
        ListofCountries = artworksByCountry[0]
        Popular = artworksByCountry[1]
        Artists = artworksByCountry[2]
        x = PrettyTable(hrules=prettytable.ALL)
        x.field_names = ["Artworks", "Nationality"]
        for value in lt.iterator(ListofCountries):
                x.add_row([value['Longitud'], value['Nacionalidad']])
        print(x)

        items = lt.newList('ARRAY_LIST')
        count = 0
        for i in Popular:
            if count == 3:
                break
            count +=1
            lt.addLast(items, i)

        for j in range (len(Popular)-3, len(Popular)):
            lt.addLast(items, Popular[j])
            print(Popular[j])
        print('The first and last 3 objets in the --- artwork list are:')
        printArtworkTable(items)
        
        
        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")
            
        
        
    elif int(inputs) == 9:
        #Req 5
        start = tm.process_time()
        if sortedArtwork_Date == None:
            print("Primero tienes que organizar el catalogo de obras por Date")
        else:
            departamento = input("Ingrese el nombre del departamento del museo: ")
            ArtworkDepartment = controller.getArworkByDepartment(sortedArtwork_Date, departamento)
            if lt.isPresent(DepartmentList, departamento) == 0:
                ArtworkDepartment = controller.getTransportationCost(ArtworkDepartment)
                lt.addLast(DepartmentList, departamento)
                
            TotalPriece, TotalWeight  = controller.getArtworkTotal_CostWeight(ArtworkDepartment)
        
            print("="*15, " Req No. 5 Inputs ", "="*15)
            print("Estimete the cost to transport all artifacts in " + departamento + " MoMA's Departament")
            print("="*15, " Req No. 5 Answer ", "="*15)
            print("The MoMA is going to transport", lt.size(ArtworkDepartment), "from the",departamento)
            print("REMEMBER! NOT all MoMA's data is complete !!! .... These are estimates.")
            print("Estimated cargo weight (kg):", TotalWeight)
            print("Estimated cargo cost (USD):", TotalPriece)

            print("\nThe TOP 5 oldest items to transport are:")
            printTransCostTable(ArtworkDepartment, True)
                
            sortedArtwork_TransCost = controller.sortArtworkCatalogByTransCost(ArtworkDepartment)
            print("\nThe TOP 5 most expensive items to transport are:")
            printTransCostTable(sortedArtwork_TransCost, True)
                
        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")

    elif int(inputs) == 10:
        #Req 6 (Bono)
        start = tm.process_time()
        if Area == None:
            addArea(catalog)

        beginYear = int(input('Digite el año inicial de las obras que desea exponer: '))
        finalYear = int(input('Digite el año final de las obras que desea exponer: '))
        area = float(input('Area disponible para la exposición en m^2: '))

        newDisplay, areaUsed, totalArtworks = controller.createNewDisplay(catalog,beginYear, finalYear, area)

        print("="*15, " Req No. 6 (BONUS) Inputs ", "="*15)
        print("Searching artworks between", beginYear, "to", finalYear,".")
        print("With an available area of",area,"m^2.")
        print("="*15, " Req No. 6 (BONUS) Answer ", "="*15)
        print("The MoMA is going to exhibit pieces from", beginYear, "to", finalYear,".")
        print("There are",totalArtworks,"possible items in an available area of:",area,"m^2.")
        print("The possible exhibit has", lt.size(newDisplay),"flat items (paintings, photographs, prints, drawings).")
        print("Filling",round(areaUsed,3),"m^2 of the",area,"m^2 available.")

        if lt.size(newDisplay) > 10:
            primeros = controller.getFirts(newDisplay, 5)
            ultimos = controller.getLast(newDisplay, 5)

            print("The first 5 objects in the artwork list are:")
            printNewDisplay(primeros)
            print("The last 5 objects in the artwork list are:")
            printNewDisplay(ultimos)

        else:
            print("The objects in the artwork list are:")
            printNewDisplay(newDisplay)
        end = tm.process_time()
        total_time = (end - start)*1000
        print("The time it took to execute the requirement was:", total_time ,"mseg\n")
    
    else:
        sys.exit(0)
sys.exit(0)
