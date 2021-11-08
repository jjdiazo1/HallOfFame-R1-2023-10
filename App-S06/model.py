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
import math
from DISClib.DataStructures.arraylist import getElement
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as sa
import config as cf
assert cf



def newCatalogA():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,
               'Artists_Artworks':None,
               'Nationality_Artworks': None}

    catalog['Artists'] = lt.newList('ARRAY_LIST', cmpfunction = compareArtistID)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', cmpfunction =  compareObjectID)
    catalog['Artists_Artworks'] = lt.newList('ARRAY_LIST')
    catalog['Nationality_Artworks'] = lt.newList('ARRAY_LIST')

    return catalog
# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['Artists'], artist)
    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']


def addArtworks(catalog, artwork):
    # Se adiciona el libro a la lista de libros

    if artwork["Date"] == "":
        artwork["Date"] = "999999"

    obra = {
        'ObjectID':artwork['ObjectID'],
        'ConstituentID':artwork['ConstituentID'],
        'Title':artwork['Title'],
        'Medium':artwork['Medium'],
        'Dimensions':artwork['Dimensions'],
        'CreditLine':artwork['CreditLine'],
        'DateAcquired':artwork['DateAcquired'],
        'Department':artwork['Department'],
        'URL':artwork['URL'],
        'Height (cm)':artwork['Height (cm)'],
        'Length (cm)':artwork['Length (cm)'],
        'Weight (kg)':artwork['Weight (kg)'],
        'Width (cm)':artwork['Width (cm)'],
        'Classification':artwork['Classification'],
        'Depth (cm)':artwork['Depth (cm)'],
        'Diameter (cm)':artwork['Diameter (cm)'],
        'Date':artwork['Date']

    }
    lt.addLast(catalog['Artworks'], obra)

def addArtists_Artworks(catalog, artist):
    artista={
        'ConstituentID':artist['ConstituentID'],
        'DisplayName':artist['DisplayName'],
        'ObjectID':"",
    }
    lt.addLast(catalog['Artists_Artworks'], artista)

#CODIGO DONDE SE AGREGAN LOS OBJETOS A LOS AUTORES!!
def addObject(catalog,work):
    p = work["ConstituentID"]
    byecorchetes = p.replace("[","")
    byecorchetedos = byecorchetes.replace("]","")
    authors = byecorchetedos.split(",")
    for i in authors:
        index = binary_search(catalog['Artists_Artworks'],int(i))
        ele = lt.getElement(catalog['Artists_Artworks'], index)
        viejos = ele["ObjectID"]
        if (viejos == None) or (viejos == ''):
            nuevo = work["ObjectID"]
        else:
            nuevo = viejos+","+work["ObjectID"]
        i_insert={
            'ConstituentID':ele['ConstituentID'],
            'DisplayName':ele['DisplayName'],
            'ObjectID':nuevo,
        }
        lt.changeInfo(catalog['Artists_Artworks'], index, i_insert)
    

def addNationArt(catalog, work, arti):

    artists = work["ConstituentID"].replace("[","").replace("]", "").replace(" ","").split(",")
    for i in artists:
        pos = binary_search(arti, int(i))
        artista = lt.getElement(catalog['Artists'], pos)

        if artista["Nationality"].lower() in (None,"", "unknown"):
            artista["Nationality"] = "nationality unknown"
        
        people = ""
        
        for j in artists:
            po = binary_search(arti, int(j))

            if len(artists) > 1:
                people = people + str(lt.getElement(arti, po)["DisplayName"]) + ", "
            else:
                people = people + str(lt.getElement(arti, po)["DisplayName"]) 


        art = {'ObjectID':work['ObjectID'],
                'ConstituentID': people,
                'Title':work['Title'],
                'Medium':work['Medium'],
                'Date': work['Date'],
                'Dimensions':work['Dimensions'],
                'CreditLine':work['CreditLine'],
                'DateAcquired':work['DateAcquired'],
                'Department':work['Department'],
                'URL':work['URL'],
                'Classification':work['Classification'],
                'Nationality': artista['Nationality'].lower()
            }

        lt.addLast(catalog['Nationality_Artworks'], art)


def sortAux(catalog):
    ordenado = sa.sort(catalog,cmpFunctionIndice)
    return ordenado

def sortIDArtists(catalog):
    p = catalog["Artists"]
    orde = sa.sort(p, cmpIDArtistas)
    return orde

def binary_search(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 1
    while low <= high:
        mid = (high + low) // 2
        comp= lt.getElement(arr,mid)
        ahorasi=int(comp["ConstituentID"])
        # If x is greater, ignore left half
        if ahorasi < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif ahorasi > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']
def funcionReqUno(catalog,minimo,maximo):
    ordenado = sa.sort(catalog['Artists'],cmpFunctionRuno)
    indexmin = binary_search_min(ordenado, int(minimo))
    indexmax = binary_search_max(ordenado, int(maximo))
    cant= indexmax-indexmin
    la_lista = lt.subList(ordenado, indexmin,cant+1)
    return la_lista

def binary_search_min(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 1
 
    while low <= high:
 
        mid = (high + low) // 2
        ele=lt.getElement(arr, mid)
        begin=int(ele["BeginDate"])
 
        # If x is greater, ignore left half
        if begin < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif begin > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            while begin==x:
                mid=mid-1
                ele=lt.getElement(arr, mid)
                begin=int(ele["BeginDate"])
            return mid+1
 
    # If we reach here, then the element was not present
    return -1

def binary_search_max(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 1
 
    while low <= high:
 
        mid = (high + low) // 2
        ele=lt.getElement(arr, mid)
        begin=int(ele["BeginDate"])
 
        # If x is greater, ignore left half
        if begin < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif begin > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            while begin==x:
                mid=mid+1
                ele=lt.getElement(arr, mid)
                begin=int(ele["BeginDate"])
            return mid-1
 
    # If we reach here, then the element was not present
    return -1

def funcionReqDos(catalog, minimo, maximo):
    mini= minimo[0:4]+minimo[5:7]+minimo[8:10]
    maxi= maximo[0:4]+maximo[5:7]+maximo[8:10]
    mini = int(mini)
    maxi = int(maxi)
    ordenado = sa.sort(catalog['Artworks'],cmpFunctionRdos)
    indexmin = binary_search_min2(ordenado, int(mini))+1
    indexmax = binary_search_max2(ordenado, int(maxi))
    cant= indexmax-indexmin
    la_lista = lt.subList(ordenado, indexmin,cant+1)
    la_rta= lt.newList("ARRAY_LIST")
    for n in range(1,lt.size(la_lista)+1):
        elemento= lt.getElement(la_lista,n)
        buscar= elemento["ConstituentID"]
        byecorchetes = buscar.replace("[","")
        byecorchetedos = byecorchetes.replace("]","")
        authors = byecorchetedos.split(",")
        autores=""
        for x in authors:
            index = binary_search(catalog['Artists_Artworks'],int(x))
            ele = lt.getElement(catalog['Artists_Artworks'], index)
            autores = autores +"-"+ ele['DisplayName'] + "-"
        agregar = {
            'ObjectID':elemento['ObjectID'],
            'Title':elemento['Title'],
            'Artists':autores,
            'Medium':elemento['Medium'],
            'Dimensions':elemento['Dimensions'],
            'CreditLine':elemento['CreditLine'],
            'DateAcquired':elemento['DateAcquired'],
            'URL':elemento['URL']
        }
        lt.addLast(la_rta,agregar)
    return la_rta

def funcionReqTres(catalog, nombre):
    index = normal_search_nombre(catalog['Artists_Artworks'],nombre)
    if index != (-1):
        autor = lt.getElement(catalog['Artists_Artworks'],index)
        objetos = autor["ObjectID"]
        if (objetos==None) or (objetos==''):
            vacio = "NOHAYOBRAS"
            tupla = vacio,vacio
            return tupla
        else:
            lt_objetos = objetos.split(",")
            ordenado = sa.sort(catalog["Artworks"], cmpobjectid)
            tad_objetos = lt.newList("ARRAY_LIST")
            tad_medios = lt.newList("ARRAY_LIST")
            for i in lt_objetos:
                index = binary_search_id(ordenado, i)
                elemento = lt.getElement(ordenado, index)
                agregar = {
                    'ObjectID':elemento['ObjectID'],
                    'Title':elemento['Title'],
                    'Medium':elemento['Medium'],
                    'Dimensions':elemento['Dimensions'],
                    'DateAcquired':elemento['DateAcquired'],
                    'Department':elemento['Department'],
                    'Classification':elemento['Classification'],
                    'URL':elemento['URL'],
                    'ConstituentID':elemento['ConstituentID']
                }
                lt.addLast(tad_objetos, agregar)
                cambiarTADmedios(tad_medios,elemento)
            sa.sort(tad_medios,cmpcount)
            mediorep = lt.getElement(tad_medios, 1)
            rtafinal= lt.newList("ARRAY_LIST")
            objetos  = lt.size(tad_objetos)
            for ob in range(1,objetos+1):
                objeto=lt.getElement(tad_objetos,ob)
                name = objeto["Medium"]
                if (name == mediorep["Medium"]):
                    lt.addLast(rtafinal, objeto)
            tuplarta= tad_medios,rtafinal
            return tuplarta
            
    else:
        vacio = "NOHAYAUTOR"
        tupla = vacio,vacio
        return tupla


def funcionReqCuatro(catalog):
    data = sa.sort(catalog['Nationality_Artworks'], cmpnationality)
    nat = lt.newList("ARRAY_LIST")
    low = 1
    size = lt.size(data)
    while low <= size:

        if low == size:
            
            temp = lt.subList(data, low, 1)

            pais = {'Nationality': lt.getElement(data, low)['Nationality'],
                        'obras': temp}

            lt.addLast(nat,pais)

            low += 1

        else:

            high = binmax(data, lt.getElement(data, low)["Nationality"])
            temp = lt.subList(data, low, high - low + 1)

            pais = {'Nationality': lt.getElement(data, low)['Nationality'],
                        'obras': temp}

            lt.addLast(nat,pais)

            low = high + 1

    a = sa.sort(nat, cmpsize)

    return a

def funcionReqCin(catalog, nombre):
    ordenado = sa.sort(catalog["Artworks"],cmpdept)
    indexmax = binary_search_maxdept(ordenado,nombre)
    indexmin = binary_search_mindept(ordenado, nombre)
    cant = indexmax-indexmin
    costoretotal=0.0
    pesototal=0.0
    cant+=1
    antiguas = lt.newList("ARRAY_LIST")
    costosas = lt.newList("ARRAY_LIST")
    for i in range(indexmin,indexmax+1):
        costototal=0.0
        ele = lt.getElement(ordenado,i)
        costopeso=0
        if (ele["Weight (kg)"]==None) or (ele["Weight (kg)"]==''):
            costopeso=float(-1)
        else:
            costopeso = float(ele["Weight (kg)"])*72
            pesototal+= float(ele["Weight (kg)"])
        costomedidas=-1
        if (ele["Height (cm)"]!=None) and (ele["Height (cm)"]!=''):
            if (ele["Width (cm)"]!=None) and (ele["Width (cm)"]!=''):
                if (ele['Depth (cm)']!=None) and (ele['Depth (cm)']!=''):
                    if float(ele['Depth (cm)'])>0:
                        depth= float(ele['Depth (cm)'])/100
                        width = float(ele["Width (cm)"])/100
                        height = float(ele["Height (cm)"])/100
                        m3= depth*width*height
                        costomedidas=m3*72
                    else:
                        width = float(ele["Width (cm)"])/100
                        height = float(ele["Height (cm)"])/100
                        m2= width*height
                        costomedidas=m2*72
                else:
                    width = float(ele["Width (cm)"])/100
                    height = float(ele["Height (cm)"])/100
                    m2= width*height
                    costomedidas=m2*72
            elif (ele["Diameter (cm)"]!=None) and (ele["Diameter (cm)"]!=''):
                radio = float(ele["Diameter (cm)"])/200
                height = float(ele["Height (cm)"])/100
                m3= radio*height*radio*math.pi
                costomedidas=m3*72
        elif (ele["Width (cm)"]!=None) and (ele["Width (cm)"]!=''):
            if (ele['Length (cm)']!=None) and (ele['Length (cm)']!=''):
                width = float(ele["Width (cm)"])/100
                lenght = float(ele["Length (cm)"])/100
                m2=width*lenght
                costomedidas=m2*72
        elif (ele["Diameter (cm)"]!=None) and (ele["Diameter (cm)"]!=''):
            radio = float(ele["Diameter (cm)"])/200
            m2= radio*radio*math.pi
            costomedidas=m2*72
        costototal=max(costopeso,costomedidas)
        if costototal<=0:
            costototal=48.0
        buscar= ele["ConstituentID"]
        byecorchetes = buscar.replace("[","")
        byecorchetedos = byecorchetes.replace("]","")
        authors = byecorchetedos.split(",")
        autores=""
        for x in authors:
            index = binary_search(catalog['Artists_Artworks'],int(x))
            elemento = lt.getElement(catalog['Artists_Artworks'], index)
            autores = autores +"-"+ elemento['DisplayName'] + "-"
        agregar = {
            'ObjectID':ele['ObjectID'],
            'Title':ele['Title'],
            'Artists':autores,
            'Medium':ele['Medium'],
            'Dimensions':ele['Dimensions'],
            'DateAcquired':ele['DateAcquired'],
            'Classification':ele['Classification'],
            'TransCost (USD)':str(costototal),
            'URL':ele['URL'],
            'Date':ele['Date']
        }
        lt.addLast(antiguas,agregar)
        lt.addLast(costosas,agregar)
        costoretotal+=costototal
    #AQUI SE SUPONE QUE YA TENEMOS LAS 2 LISTICAS LISTAS:)
    ordenantiguas = sa.sort(antiguas,cmpdate)
    ordencostosas = sa.sort(costosas,cmpcost)
    tuplatriple = costoretotal,ordenantiguas,ordencostosas,pesototal
    return tuplatriple    

def binmax(arr, x):
    low = 0
    high = lt.size(arr)-1
    mid = 0
 
    while low <= high:
 
        mid = low + (high - low) // 2
        ele=lt.getElement(arr, mid+1)
        begin=ele["Nationality"]
 
        # If x is greater, ignore left half
        
        if x < begin:
            high = mid - 1

        elif x > begin:
            low = mid + 1
 
        # means x is present at mid
        else:
            if mid < lt.size(arr)-1:
                while begin==x and mid < lt.size(arr):
                    mid=mid+1
                    ele=lt.getElement(arr, mid)
                    begin=ele["Nationality"]
                return mid
            else:
                return mid+1
    # If we reach here, then the element was not present
    return -1

def binary_search_maxdept(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        ele=lt.getElement(arr, mid)
        begin=ele["Department"]
 
        # If x is greater, ignore left half
        if begin < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif begin > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            if mid < lt.size(arr)-1:
                while begin==x:
                    mid=mid+1
                    ele=lt.getElement(arr, mid)
                    begin=ele["Department"]
                return mid-1
            else:
                return mid
    # If we reach here, then the element was not present
    return -1

def binary_search_mindept(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        ele=lt.getElement(arr, mid)
        begin=ele["Department"]
 
        # If x is greater, ignore left half
        if begin < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif begin > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            if mid < lt.size(arr)-1:
                while begin==x:
                    mid=mid-1
                    ele=lt.getElement(arr, mid)
                    begin=ele["Department"]
                return mid+1
            else:
                return mid
    # If we reach here, then the element was not present
    return -1

def binmaxreqdos(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if m < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif m > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            if mid < lt.size(arr)-1:
                while m==x:
                    mid=mid+1
                    ele=lt.getElement(arr, mid)
                    e = ele["DateAcquired"]
                    m= e[0:4]+e[5:7]+e[8:10]
                    m= int(m)
                return mid-1
            else:
                return mid
    # If we reach here, then the element was not present
    return mid

def binminreqdos(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if m < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif m > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            if mid < lt.size(arr)-1:
                while m==x:
                    mid=mid-1
                    ele=lt.getElement(arr, mid)
                    e = ele["DateAcquired"]
                    m= e[0:4]+e[5:7]+e[8:10]
                    m= int(m)
                return mid+1
            else:
                return mid
    # If we reach here, then the element was not present
    return mid


"""def obrasUnicas(top):

    new = lt.newList("ARRAY_LIST")

    c = sa.sort(top["obras"], cmpunique)

    for i in range(1, lt.size(c)+1):
        b = lt.getElement(c,i)
        present = binaryUnicas(new, int(b["ObjectID"]))
        if present == -1:
            lt.addLast(new, b)
    return new"""

def purchased(lista_f):
    
    cont = 0
    
    for i in range(1, lt.size(lista_f)+1):
        a = lt.getElement(lista_f, i)
        b = a["CreditLine"].lower()
        if "purchase" in b:
            cont+=1
    return cont

def binaryUnicas(arr,x):
    low = 1
    high = lt.size(arr)
    mid = 1
    while low <= high:
        mid = (high + low) // 2
        comp= lt.getElement(arr,mid)
        ahorasi=int(comp["ObjectID"])
        # If x is greater, ignore left half
        if ahorasi < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif ahorasi > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1

def cambiarTADmedios(arr, x):
    pos=0
    final=lt.size(arr)
    for i in range(1,final+1):
        cosa=lt.getElement(arr,i)
        medio= cosa["Medium"]
        if medio==x["Medium"]:
            pos=i
    if pos>0:
        o = lt.getElement(arr,pos)
        coso= int(o["Count"])
        cambio= coso + 1
        cambiodict = {
            'Medium': o["Medium"],
            'Count': str(cambio)
        }
        lt.changeInfo(arr,pos,cambiodict)
    else:
        nuevodict={
            'Medium': x["Medium"],
            'Count': "1"
        }
        lt.addLast(arr,nuevodict)

        

def normal_search_nombre(arr, x):
    largo  = lt.size(arr)
    for artist in range(1,largo+1):
        artista = lt.getElement(arr,artist)
        name = artista["DisplayName"]
        if (name == x):
            return artist
    return -1

def binary_search_max2(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if int(m) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(m) == x:
            rta=mid
            low = mid + 1
        else:
            low = mid + 1
    if rta == 0:
        rta= mid-1
    return rta

def binary_search_min2(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if int(m) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(m) == x:
            rta=mid
            high = mid - 1
        else:
            low = mid + 1
    if rta == 0:
        rta= mid-1
    return rta

def binary_search_id(arr, x):
    low = 1
    high = lt.size(arr)
    mid = 0
    xdepurado = x.replace("'","")
    xdep = xdepurado.replace(" ","")
    xint = int(xdep)
 
    while low <= high:
 
        mid = (high + low) // 2
        comp= lt.getElement(arr,mid)
        ahorasi=int(comp["ObjectID"])
 
        # If x is greater, ignore left half
        if ahorasi < xint:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif ahorasi > xint:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1




def cmpFunctionRuno(anouno, anodos):
    return (int(anouno["BeginDate"]) < int(anodos["BeginDate"]))

def cmpobjectid(iduno, iddos):
    return (int(iduno["ObjectID"]) < int(iddos["ObjectID"]))

def cmpFunctionIndice(artist1, artist2):
    return (int(artist1["ConstituentID"]) < int(artist2["ConstituentID"]))

def cmpcount(countuno, countdos):
    return (int(countuno["Count"])> int(countdos["Count"]))

def cmpFunctionRdos(feuno, fedos):
    fechauno= feuno["DateAcquired"]
    fechados = fedos["DateAcquired"]
    if (fechauno!=None) and (fechauno!=""):
        mini= fechauno[0:4]+fechauno[5:7]+fechauno[8:10]
        mini= int(mini)
    else:
        mini=0
    if (fechados!=None) and (fechados!=""):
        maxi= fechados[0:4]+fechados[5:7]+fechados[8:10]
        maxi= int(maxi)
    else:
        maxi=0
    return (int(mini) < int(maxi))


def cmpnationality(nat1, nat2):
    return nat1["Nationality"] < nat2["Nationality"]

def cmpsize(obras1, obras2):
    return int(lt.size(obras1["obras"])) > int(lt.size(obras2["obras"]))

def compareObjectID(artwork1, artwor2):
    if (artwork1["ObjectID"] == artwor2['ObjectID']):
        return 0
    elif (artwork1["ObjectID"] > artwor2['ObjectID']):
        return 1
    return -1

def compareArtistID(artwork1, artwor2):
    if (artwork1["ConstituentID"] == artwor2['ConstituentID']):
        return 0
    elif (artwork1["ConstituentID"] > artwor2['ConstituentID']):
        return 1
    return -1

def cmpIDArtistas(artista1, artista2):
    return int(artista1["ConstituentID"]) < int(artista2["ConstituentID"])

def cmpunique(obra1, obra2):
    return int(obra1["ObjectID"])<int(obra2["ObjectID"])

def cmpdept(deptuno,deptdos):
    return (deptuno["Department"]<deptdos["Department"])

def cmpdate(dateuno, datedos):
    return (int(dateuno['Date'])<int(datedos['Date']))

def cmpcost(costuno, costdos):
    return (float(costuno['TransCost (USD)'])>float(costdos['TransCost (USD)']))