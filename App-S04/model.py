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


import config as cf
import time
import re
import operator
import math
from decimal import Decimal, Rounded
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mst
from DISClib.Algorithms.Sorting import quicksort as qst
from DISClib.Algorithms.Sorting import shellsort as sst
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def crearCatalogo(tipo_lista):
    """
    
    """
    catalogo = {'artistas': None,
                'obras': None,}

    catalogo['artistas'] = lt.newList(tipo_lista)
    catalogo['obras'] = lt.newList(tipo_lista)

    return catalogo


# Funciones para agregar informacion al catalogo

def agregarArtista(catalogo, artista):
    artista = nuevoArtista(artista['ConstituentID'],artista['DisplayName'],artista['BeginDate'],artista['EndDate'],artista['Nationality'], artista['Gender'])
    lt.addLast(catalogo['artistas'], artista)

def agregarObra(catalogo, obra):
    obra=nuevaObra(obra['ConstituentID'], obra['ObjectID'], obra['Title'], obra['Date'], obra['Medium'], obra['Department'], obra['DateAcquired'], obra['Height (cm)'], obra['Width (cm)'], obra['Weight (kg)'], obra['CreditLine'], obra['Dimensions'], obra['Diameter (cm)'], obra['Length (cm)'], obra['Classification'])
    lt.addLast(catalogo['obras'], obra)

# Funciones para creacion de datos

def nuevoArtista(id, nombre, fecha_nacimiento, fecha_muerte, nacionalidad, genero):
    artista={'id':"", 'nombre':"", 'fecha_nacimiento':"", 'fecha_muerte':"", 'nacionalidad':"", 'genero':""}
    artista['id'] = id
    artista['nombre']=nombre
    artista['fecha_nacimiento'] = fecha_nacimiento
    artista['fecha_muerte'] = fecha_muerte
    artista['nacionalidad']=nacionalidad
    artista['genero'] = genero
    #artista['obras']=lt.newList('ARRAY_LIST')
    return artista

def nuevaObra(id, objectId, titulo, fecha, tecnica, departamento, fecha_adquisicion, altura, ancho, peso, linea, dimensiones, diametro, largo, clasificacion):
    
    obra={'id':"", 'objectId':"", 'titulo':"", 'fecha':"", 'tecnica':"", 'departamento':"", 'fecha_adquisicion':"", 'altura':"", 'ancho':"", 'peso':"", 'linea_adquisicion':"", 'dimensiones':"", 'diametro':"", 'largo':""}
    obra['id']=id
    obra['objectId'] = objectId
    obra['titulo']=titulo
    obra['fecha']=fecha
    obra['tecnica']=tecnica
    obra['departamento']=departamento
    obra['fecha_adquisicion']=fecha_adquisicion
    obra['altura']=altura
    obra['ancho']=ancho
    obra['peso']=peso
    obra['linea_adquisicion']=linea
    obra['dimensiones'] = dimensiones
    obra['diametro']=diametro
    obra['largo']=largo
    obra['clasificacion'] = clasificacion
    
    return obra

# Funciones de consulta

def darListaObrasDepartamento(datos, departamento):

    lista_obras = lt.newList('ARRAY_LIST')
    info = datos['obras']

    for i in lt.iterator(info):
        if i['departamento'] == departamento:
            lt.addLast(lista_obras, i)

    return lista_obras

def darPrecioTransporteDepartamento(lista_obras):
    costo_total=0
    for i in lt.iterator(lista_obras):
        costo_total = costo_total + calcularCostoTransporteObra(i)
    
    return costo_total

def darPesoTotalDepartamento(lista_obras):
    pesoTotal = 0
    for i in lt.iterator(lista_obras):
        if not i['peso']:
            pass
        else:
            pesoTotal = Decimal(i['peso']) + pesoTotal

    return pesoTotal  


def compararFechasArtistas(datos, anho_inicial, anho_final, tipo_lista):
    
    #listaArtistas = lt.getElement(datos['artistas'],0)
    #listaArtistas = datos['artistas']['elements']
    listaInfo = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['artistas']):
        
        if (int(i['fecha_nacimiento']) >= anho_inicial and int(i['fecha_nacimiento']) <= anho_final):
            lt.addLast(listaInfo, i)
    
    return listaInfo
            
        
def obrasAdquiridasPorCompra(datos):
    
    contador=0

    for dato in lt.iterator(datos):
        frase=dato['linea_adquisicion']
        if re.search('purchase',frase.lower()):
            contador=contador + 1

    return contador


def consultarId(datos, nombreArtista):
    
    info = datos['artistas']
    idArtista = '0'
    
    for i in lt.iterator(info):
        i['nombre']
        if i['nombre'] == nombreArtista:
            idArtista = i['id']
            
    return idArtista 
        
         

def buscarObrasPorNacionalidad(datos, nacionalidad):
    info_obras = datos['obras']

    lista_obras = lt.newList('ARRAY_LIST')    

    for i in lt.iterator(info_obras):

        x=i['id']
    
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        for j in lista:
            if consultarNacionalidad(datos, int(j)) == nacionalidad:
                lt.addLast(lista_obras, i)

    return lista_obras


    

def consultarNacionalidad(datos, id):

    info_artistas = datos['artistas']
    nacionalidad = ""

    for i in lt.iterator(info_artistas):
        if i['id'] == str(id):
            nacionalidad = i['nacionalidad']
            break
        
    return nacionalidad 

def listaNacionalidades(datos):

    info_obras = datos['obras']
    #info_obras = datos['obras']['elements']

    lista_id_artistas = lt.newList('ARRAY_LIST')
    dic_nacionalidades = {}

    for i in lt.iterator(info_obras):

        x = i['id']
        characters = "[] "

        for s in range(len(characters)):
            x = x.replace(characters[s],"")

        lista = x.split(',')
        #print(lista)
        for a in lista:
            if lt.isPresent(lista_id_artistas, a) == -1 or a == ' ' or a == '':
               pass
            else:
                lt.addLast(lista_id_artistas, a)
    
    for i in lt.iterator(lista_id_artistas):
        
        nacionalidad = consultarNacionalidad(datos, int(i))

        if nacionalidad in dic_nacionalidades:
            dic_nacionalidades[nacionalidad]=dic_nacionalidades[nacionalidad]+1
        else:
            dic_nacionalidades[nacionalidad]=1

    del dic_nacionalidades['']

    nacionalidades_sort = sorted(dic_nacionalidades.items(), key=operator.itemgetter(1), reverse=True)
    
    return nacionalidades_sort


def filtrarObrasPorId(datos, idArtista, tipo_lista):
    
    obrasDelArtista = lt.newList(tipo_lista)
    lista_temp_1 = []
    lista_temp_2 = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['obras']):
        
        tamanho_id = len(i['id'])
        if (str(i['id'][1:(tamanho_id-1)]) == idArtista):
            lt.addLast(obrasDelArtista, i)
            lista_temp_1.append(i['tecnica'])

            if (lt.isPresent(lista_temp_2, i['tecnica']) == 0):
                lt.addLast(lista_temp_2, i['tecnica'])
    
    return obrasDelArtista, lista_temp_1, lista_temp_2


def filtrarFechasObras1(datos):
    
    for i in lt.iterator(datos):
        pass

def filtrarFechasObras(datos):
    for i in lt.iterator(datos):
        
        fecha = i['fecha']
        
        if not(fecha.isnumeric()):
            if fecha.count('(') != 0: 
                if fecha.index("(") == 0 and fecha.index(")") == len(fecha)-1:
                    fecha = fecha[1:-1] 
                elif fecha.index("(") == 0: 
                    fecha = fecha[1:] 
            if fecha.count('.') != 0:
                fecha = fecha.replace('.', '')
            if fecha == 'Unknown':
                i['fecha'] = 0
            elif fecha == 'n.d.':
                i['fecha'] = 0
            elif fecha.count(" ") == 0:  
                if '–' in fecha:
                    fechaLista = fecha.split("–") 
                elif '-' in fecha:
                    fechaLista = fecha.split("-") 
                fechaLista = fecha.split() 
                fechaAnho = encontrarAnho(fechaLista)
                i['fecha'] = fechaAnho[0]
            else:
                fechaLista = fecha.split() 
                fechaAnho = encontrarAnho(fechaLista)
                i['fecha'] = fechaAnho[0] 
        
    return datos
          
    
def obtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista):

    rangoObras = lt.newList(tipo_lista)
    
    for i in lt.iterator(datos['obras']):
              
        if i['fecha'] == '':
            i['fecha'] = 0
                     
        if ((int(i['fecha']) <= anhoFinal) and (int(i['fecha']) >= anhoInicial)):
            alturaObra = i['altura']
            anchoObra = i['ancho']
            
            if alturaObra == "":
                alturaObra = 0
            if anchoObra == "":
                anchoObra = 0
                
            i['areaObra'] = (((float(alturaObra))*(float(anchoObra))))*0.0001
            lt.addLast(rangoObras, i)    
            
    return rangoObras


def agregarArtistaPorId(datos, datosArtistas):
    
    for i in lt.iterator(datos):   
        if len(i['id']) > 8:
            i['artista'] = 'Varios'
            
        else:
            for j in lt.iterator(datosArtistas): 
                if (j['nombre'] != ""):
                    if i['id'][1:-1] == j['id']:
                        i['artista'] = j['nombre']
                else:
                    i['artista'] = 'Unknown'
                
    return datos
    
    #for i in lt.iterator(datos):   
     #   artistas = []
      #  for j in lt.iterator(datosArtistas):
            
       #     if len(i['id']) > 8:
        #        lista = (i['id'][1:-1]).split(',')
         #       print(lista)
                
          #      for n in lista:
           #        if (j['nombre'] != ""):
            #          if n == j['id']:
             #               artistas.append(j['nombre'])
              #  i['artista'] = artistas
               # break
            
            #elif (j['nombre'] != ""):
             #   if i['id'][1:-1] == j['id']:
              #      i['artista'] = j['nombre']
               #     break
            #else:
             #   i['artista'] = 'Unknown'
   
    #return datos
            
    
# Funciones utilizadas para comparar elementos dentro de una lista

def encontrarAnho(lista):
    
    listaNueva = []
    for i in lista:
        if i.isnumeric() and len(i)>3:
            listaNueva.append(i)
            
    return listaNueva
            

def cmpArtworkByDateAcquired(artwork1, artwork2):
    
    if artwork1['fecha_adquisicion'] < artwork2['fecha_adquisicion']:
        return True
    else:
        return False
    
def cmpArtistaPorNacimiento(artista1, artista2):
    
    if int(artista1['fecha_nacimiento']) < int(artista2['fecha_nacimiento']):
        return True
    else:
        return False
    
def cmpObrasPorFecha(obra1, obra2):
    
    if (int(obra1['fecha']) < int(obra2['fecha'])):
        return True
    else:
        return False

def cmpObrasPorCostoTransporte(obra1, obra2):
    
    if (int(obra1['costo_transporte']) < int(obra2['costo_transporte'])):
        return True
    else:
        return False

# Funciones de ordenamiento

def insertion(datos, identificador): 
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = ist.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = ist.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = ist.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = ist.sort(datos, cmpObrasPorCostoTransporte)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def shell(datos, identificador):   
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = sst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = sst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = sst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = sst.sort(datos, cmpObrasPorCostoTransporte)
        
    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def merge(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = mst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = mst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = mst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = mst.sort(datos, cmpObrasPorCostoTransporte)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

def quicksort(datos, identificador):
    tiempo_inicial = time.process_time()
    
    if identificador == 1:
        lista_ordenada = qst.sort(datos, cmpArtistaPorNacimiento)
    elif identificador == 2:
        lista_ordenada = qst.sort(datos, cmpObrasPorFecha)
    elif identificador == 3:
        lista_ordenada = qst.sort(datos, cmpArtworkByDateAcquired)
    elif identificador == 4:
        lista_ordenada = qst.sort(datos, cmpObrasPorCostoTransporte)

    tiempo_final = time.process_time()
    duracion = (tiempo_final - tiempo_inicial)*1000
    
    return duracion, lista_ordenada

#Otras
  
def crearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista):
    
    areaUsada = 0
    i = 0
    info = rangoObrasRequerido['elements']
    nuevaExposicion = lt.newList(tipo_lista)
    
    for i in lt.iterator(rangoObrasRequerido):
        
        if areaUsada <= areaDisponible:
            areaUsada += i['areaObra']
            lt.addLast(nuevaExposicion, i)
        else:
            break
        
    return nuevaExposicion, areaUsada
        

def calcularCostoTransporteObra(obra):

    costo_peso = 0
    costo_area = 0
    costo_volumen = 0

    costo_mayor=0

    costo = 72

    if not obra['altura']:
        altura = 0
    else:
        altura = Decimal(obra['altura'])/100
    if not obra['largo']:
        largo = 0
    else:
        largo = Decimal(obra['largo'])/100
    if not obra['ancho']:
        ancho = 0
    else:
        ancho = Decimal(obra['ancho'])/100
    if not obra['peso']:
        peso = 0
    else:
        peso = Decimal(obra['peso'])
    if not obra['diametro']:
        diametro = 0
    else:
        diametro = int(round(Decimal(obra['diametro'])/100))
    
    #Calculo del peso
    if peso != 0:
        costo_peso=peso*costo

    #Calculo del area
    if diametro != 0:
        costo_area=(math.pi()*((diametro)/2)^2)*costo
    elif largo != 0 and ancho != 0:
        costo_area=(largo*ancho)*costo
    elif altura != 0 and ancho != 0:
        costo_area=(altura*ancho)*costo

    #Calculo del volumen
    if diametro != 0 and altura != 0:
        costo_volumen=(math.pi()*((diametro)/2)^2*altura)*costo
    elif largo != 0 and ancho != 0 and altura != 0:
        costo_volumen=(largo*ancho*altura)*costo

    if costo_area > costo_peso and costo_area > costo_volumen:
        costo_mayor=costo_area
    elif costo_peso > costo_area and costo_peso > costo_volumen:
        costo_mayor=costo_peso
    else:
        costo_mayor=costo_volumen

    if costo_mayor == 0:
        obra['costo_transporte']=48
        return 48
    else:
        obra['costo_transporte']=costo_mayor
        return costo_mayor
    
