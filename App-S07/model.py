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


import config as cf
import datetime as dt
import time
import math 
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def museoArrayList():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    

    museo= {'artistas': None,
            'obras': None}

    

    museo['artistas'] = lt.newList('ARRAY_LIST')
    museo['obras'] = lt.newList('ARRAY_LIST')                     
    return (museo)


# Funciones para agregar informacion al catalogo
def crearArtista(nombre, nacionalidad, genero, ano_nacimiento):
    artista = {'nombre': "",
               'nacionalidad': "",
               'genero': "",
               'ano_nacimiento': 0}
    artista['nombre']=nombre
    artista['nacionalidad'] = lt.newList('ARRAY_LIST')
    artista['nacionalidad']=nacionalidad
    artista['genero']=genero 
    artista['ano_nacimiento']=ano_nacimiento

    
    return artista

def crearObra(titulo, artistas, fecha_creacion, medio, fecha_adquisicion, dimensiones):

    obra= {'titulo': " ",
            'artistas': " ",
            'fecha_creacion': " ",
            'medio': " ",
            'fecha_adquisicion': " ",
            'dimensiones': " "}
    obra['titulo']=titulo
    obra['artistas'] = lt.newList('ARRAY_LIST')
    obra['artistas']=artistas
    obra['fecha_creacion']= fecha_creacion
    obra['medio']=medio
    obra['fecha_adquisicion']= fecha_adquisicion
    obra['dimensiones']= dimensiones
    return obra

def addArtista(museo, artista):
    # Se adiciona el libro a la lista de libros
    lt.addLast(museo['artistas'], artista)
    


def addObra(museo, obra):
    
    lt.addLast(museo['obras'], obra)
# Funciones para creacion de datos

# Funciones de consulta
def darUltimosArtistas(museo):
    b= lt.size(museo)
    listaUltimos= lt.subList(museo, (b-2),3)
    return listaUltimos

def darUltimasObras(museo):
    b= lt.size(museo)
    listaUltimos= lt.subList(museo, (b-2),3)
    return listaUltimos

def darPrimerosArtistas(museo):
    listaUltimos= lt.subList(museo, 1,3)
    return listaUltimos

def darPrimerasObras(museo):

    listaUltimos= lt.subList(museo, 1,3)
    return listaUltimos


def numeroArtistas(museo):
    size= lt.size(museo['artistas'])
    return size

def numeroObras(museo):
    size= lt.size(museo['obras'])
    return size
def obrasPurchase(obras):
    numero=0
    for obra in obras['elements']:
        if obra['CreditLine']== 'Purchase':
             numero +=1
    return numero

#Requisito 6
def fechasRangoObras(lista, fechai, fechaf):
    size=lt.size(lista)
    listaf=lt.newList('ARRAY_LIST')
    a= int(fechai)
    b= int(fechaf)
    for i in range(1, size+1):
        try:
            obra = lt.getElement(lista,i)
            c= int(obra['Date'])
            if c<=b and c>=a:
                lt.addLast(listaf, obra)
            
        except ValueError:
             pass
        
    return listaf

def metrosObras(area, listaf):
    size=lt.size(listaf)
    metrosOcupados=0
    obras= lt.newList('ARRAY_LIST')
    retorno=lt.newList('ARRAY_LIST')
    
    for i in range(1, size+1):
        a=lt.getElement(listaf, i)
        d=a['Diameter (cm)']
        h=a['Height (cm)']
        w=a['Length (cm)']
        depth= a['Depth (cm)']
        l=a['Width (cm)']
        areaO=0
        if (w==''or w=='0') and (depth=='' or depth=='0') and (d=='' or d=='0') and (h!='' and h!='0') and (l!='' and l!='0') :
            areaO= float(h)*float(l)
            areaO=areaO/100
        if d!='' and d!='0':
            areaO= 3.1416592*((float(d)/2)**2)
            areaO= areaO/100
        if metrosOcupados< area and metrosOcupados+areaO< area:
            metrosOcupados+=areaO
            lt.addLast(obras, a)

    lt.addLast(retorno, obras)
    lt.addLast(retorno, metrosOcupados)
    return retorno


def darPrimerasObras5(museo):

    listaUltimos= lt.subList(museo, 1,5)
    return listaUltimos
            

#Requisito3

def artistaID(museo, nombre):
    lista= museo['artistas']
    size= lt.size(lista)

    for i in range(1, size+1):
        a=lt.getElement(lista, i)
        if nombre==a['DisplayName']:
            id= a['ConstituentID']
         
    return id
def obrasID(museo, id):
    lista= museo['obras']
    size=lt.size(lista)
    listaf=lt.newList('ARRAY_LIST')
    i=1
    while i<=size:
        try:
            a=lt.getElement(lista, i)
            b=str(a['ConstituentID'])
            b = b.replace("[", "")
            b = b.replace("]", "")
            c=b.split(",")
            if id in c:
                lt.addLast(listaf, a)
            i+=1
        except ValueError:
            pass
    return listaf

def clasificarObrasPorTecnica(listaf, tecnica):
    i=1
    size=lt.size(listaf)
    obrasTecnica= lt.newList('ARRAY_LIST')
    while i<=size:
        if lt.getElement(listaf,i)['Medium']==tecnica:
            lt.addLast(obrasTecnica, lt.getElement(listaf,i))
        i+=1
    return obrasTecnica
 
def listarTecnicas(listaf):
    tecnicas=lt.newList('ARRAY_LIST')
    size=lt.size(listaf)
    for i in range(1, size+1):
        try:
            a=lt.getElement(listaf, i)
            b= a['Medium']
            lt.addLast(tecnicas, b)
            
        except ValueError:
            
            pass
    return tecnicas

def contarTecnicas(tecnicas):
    duplas = {}
    for i in range(1, lt.size(tecnicas) + 1):
        tecnica = lt.getElement(tecnicas, i)
        if not tecnica in duplas.keys():
            duplas[tecnica] = 1
        else:
            num = duplas[tecnica]
            duplas[tecnica] = num + 1
    return duplas

def tecnicaMasFrecuente(listaT):
    mayor = 0
    tecnica = ""
    for llave in listaT.keys():
        if listaT[llave] > mayor:
            mayor = listaT[llave]
            tecnica = llave
    retorno = lt.newList('ARRAY_LIST')
    lt.addLast(retorno, tecnica)
    lt.addLast(retorno, mayor) 
    return retorno



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artwork1['DateAcquired']
    b= artwork2['DateAcquired']
    try:
        if a !='' and b!='':
            x= dt.datetime.strptime(a, '%Y-%m-%d')
            y= dt.datetime.strptime(b, '%Y-%m-%d')
            if x<y:
                return True
        else: 
            return False
    except ValueError:
        return False
def cmpArtistByDateBirth(artista1, artista2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artista1['BeginDate']
    b= artista2['BeginDate']
    x= int(a)
    y= int(b)
    if x<y:
        return True
    else: 
        return False

# Funciones de ordenamiento obras



def sortArrayListMerge(lista):
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListMerge(leftlist)
        sortArrayListMerge(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtworkByDateAcquired(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    
    return lista


def fechasRango(lista, fechai, fechaf):
    
    listaf=lt.newList('ARRAY_LIST')
    a= dt.datetime.strptime(fechai, '%Y-%m-%d')
    b= dt.datetime.strptime(fechaf, '%Y-%m-%d')
    
    
    for i in range(1, lt.size(lista)+1):
        try:
            obra = lt.getElement(lista,i)
            c= dt.datetime.strptime(obra['DateAcquired'], '%Y-%m-%d')
            if c<=b and c>=a:
                lt.addLast(listaf, obra)
            
        except ValueError:
             pass
        
    return listaf


 # Funciones de ordenamiento artistas   

def sortArrayListArtistMerge(lista):
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListArtistMerge(leftlist)
        sortArrayListArtistMerge(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtistByDateBirth(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lista

def fechasRangoArtista(lista, fechai, fechaf):
    
    listaf=lt.newList('ARRAY_LIST')
    a= int(fechai)
    b= int(fechaf)
    for i in range(1,lt.size(lista)+1):
        artista=lt.getElement(lista, i)
        x= artista['BeginDate']
        c= int(x)
        if c<=b and c>=a:
            lt.addLast(listaf, artista)
    return listaf
#Requerimiento 5
def obraDepartamento(museo, departamento):
    lista= museo['obras']
    size=lt.size(lista)
    listaf= lt.newList('ARRAY_LIST')
    for i in range(1, size+1):
        a=lt.getElement(lista, i)
        if a['Department']==departamento:
            lt.addLast(listaf, a)
    return listaf

def precioObra (obras):
    llaves = lt.newList("ARRAY_LIST")
    lt.addLast(llaves, "Circumference (cm)")
    lt.addLast(llaves, "Depth (cm)")
    lt.addLast(llaves, "Diameter (cm)")
    lt.addLast(llaves, "Height (cm)")
    lt.addLast(llaves, "Length (cm)")
    lt.addLast(llaves, "Width (cm)")
    for j in range(1,lt.size(obras)+1):
        obra = lt.getElement(obras, j)
        valores = lt.newList("ARRAY_LIST")
        for i in range(1, lt.size(llaves)+1):
            llave = lt.getElement(llaves, i)
            try: 
                atributo = float(obra[llave])/100
                print(atributo)
            except ValueError:
                atributo = 0.0
            lt.addLast(valores, atributo)
        
        costo = lt.getElement(valores, 1)*math.pi*18

        area_plan = lt.getElement(valores, 4)*lt.getElement(valores, 6)*72
        profundidad = lt.getElement(valores, 2)
        ancho = lt.getElement(valores, 5)
        
        if  ancho != 0 and profundidad == 0:
            area_plan = ancho
        if  profundidad  != 0:
            area_plan *=profundidad
        if area_plan > costo:
           costo = area_plan
        peso = obra["Weight (kg)"]
        if peso != '':
            peso2 = float(peso)*72
            if  peso2 > costo:
                costo = peso2

        if costo == 0:
            costo = 48
        obra["Costo"] = costo



            
def cmpArtworkByDate(artwork1, artwork2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artwork1['Date']
    b= artwork2['Date']
    try:
        if a !='' and b!='':
            x= int(a)
            y= int(b)
            if x<y:
                return True
        else: 
            return False
    except ValueError:
        return False
def sortArrayListMergeDate(lista):
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListMergeDate(leftlist)
        sortArrayListMergeDate(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtworkByDate(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    
    return lista
def darUltimasObras5(museo):
    b= lt.size(museo)
    listaUltimos= lt.subList(museo, (b-4),5)
    return listaUltimos


def cmpArtworkByCost(artwork1, artwork2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artwork1['Costo']
    b= artwork2['Costo']
    try:
        if a !='' and b!='':
            x= float(a)
            y= float(b)
            if x<y:
                return True
        else: 
            return False
    except ValueError:
        return False
def sortArrayListMergeCost(lista):
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListMergeCost(leftlist)
        sortArrayListMergeCost(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtworkByCost(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    
    return lista
def pesoObra(obras):
    cuenta = 0
    for i in range(1, lt.size(obras)+1):
        obra=lt.getElement(obras, i)
        peso=obra["Weight (kg)"]
        if peso!='':
            peso= float(peso)
            cuenta += peso
    return cuenta
def sumaPrecios(obras):
    cuenta = 0
    for i in range(1, lt.size(obras)+1):
        obra=lt.getElement(obras, i)
        cuenta += obra["Costo"]
    return cuenta