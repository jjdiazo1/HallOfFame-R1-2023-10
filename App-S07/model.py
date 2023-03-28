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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(ds):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=ds,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["data"], data)

    return data_structs


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    diccionario = {}
    # Organiza los datos en un diccionario por año
    
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo añade
        year = elem['Año']
        if year not in diccionario:
            diccionario[year] = lt.newList(datastructure='ARRAY_LIST')
            
        # Guarda la información de cada actividad económica en el año correspondiente
        lt.addLast(diccionario[year], elem)
        
    
    # ordena la información de cada año
    for cada_año in diccionario:
        sort({'data' : diccionario[cada_año]}, orderingAlg='4', sortCriteria=sort_saldoapagar)
    
    return diccionario


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    diccionario = {}
    # Organiza los datos en un diccionario por año
    
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo añade
        year = elem['Año']
        if year not in diccionario:
            diccionario[year] = lt.newList(datastructure='ARRAY_LIST')
            
        # Guarda la información de cada actividad económica en el año correspondiente
        lt.addLast(diccionario[year], elem)
        
    
    # ordena la información de cada año
    for cada_año in diccionario:
        sort({'data' : diccionario[cada_año]}, orderingAlg='4', sortCriteria=sort_saldoafavor)
    
    return diccionario


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    subSectoresEconomicos = {}
    # Organiza los datos en un diccionario por año y subsector económico
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo agrega
        year = elem['Año']
        if year not in subSectoresEconomicos:
            subSectoresEconomicos[year] = {
                                           'subsectors':{},
                                           'subsectorName':''
                                          }
               
        # Verifica que no exista el subsector en el diccionario y en caso de que no, lo agrega
        subsector = elem['Nombre subsector económico']
        if subsector not in subSectoresEconomicos[year]['subsectors']:
            subSectoresEconomicos[year]['subsectors'][subsector] = lt.newList(datastructure='ARRAY_LIST')
            subSectoresEconomicos[year]['subsectors'][subsector]['Total retenciones'] = int(elem['Total retenciones'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total ingresos netos'] = int(elem['Total ingresos netos'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total costos y gastos'] = int(elem['Total costos y gastos'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total saldo a favor'] = int(elem['Total saldo a favor'])
        else:
            subSectoresEconomicos[year]['subsectors'][subsector]['Total retenciones'] += int(elem['Total retenciones'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total ingresos netos'] += int(elem['Total ingresos netos'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total costos y gastos'] += int(elem['Total costos y gastos'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
            subSectoresEconomicos[year]['subsectors'][subsector]['Total saldo a favor'] += int(elem['Total saldo a favor'])
        lt.addLast(subSectoresEconomicos[year]['subsectors'][subsector], elem)  
            
    # Encuentra el subsector económico con el menor total de retenciones para todos los años.
    for year in subSectoresEconomicos:
        subsectorName = ''
        minVal = 0
        for subsector in subSectoresEconomicos[year]['subsectors']:
            totalWithholdings = subSectoresEconomicos[year]['subsectors'][subsector]['Total retenciones']
            if minVal == 0:
                minVal = totalWithholdings
                subsectorName = subsector
            elif totalWithholdings < minVal:
                minVal = totalWithholdings
                subsectorName = subsector
        subSectoresEconomicos[year]['subsectorName'] = subsectorName  
        sort({'data':subSectoresEconomicos[year]['subsectors'][subsectorName]}, sortCriteria=sort_retenciones)
    return subSectoresEconomicos



def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    diccionario = {}
    # Organiza los datos en un diccionario por año y subsector económico
    
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo añade
        year = elem['Año']
        if year not in diccionario:
            diccionario[year] = {'subsectors':{}}
            
        # Verifica que no exista el subsector en el diccionario, y en caso de que no, lo añade
        subsector = elem['Nombre subsector económico']
        if subsector not in diccionario[year]['subsectors']:
            diccionario[year]['subsectors'][subsector] = lt.newList(datastructure='ARRAY_LIST')
            diccionario[year]['subsectors'][subsector]["Código sector económico"] = elem['Código sector económico']
            diccionario[year]['subsectors'][subsector]["Nombre sector económico"] = elem['Nombre sector económico']
            diccionario[year]['subsectors'][subsector]["Código subsector económico"] = elem['Código subsector económico']
            diccionario[year]['subsectors'][subsector]['Costos y gastos nómina'] = 0
            diccionario[year]['subsectors'][subsector]['Total ingresos netos'] = 0
            diccionario[year]['subsectors'][subsector]['Total costos y gastos'] = 0
            diccionario[year]['subsectors'][subsector]['Total saldo a pagar'] = 0
            diccionario[year]['subsectors'][subsector]['Total saldo a favor'] = 0
        # Suma y guarda la información necesaria de cada subsector para cumplir el requerimiento
        diccionario[year]['subsectors'][subsector]['Costos y gastos nómina'] += int(elem['Costos y gastos nómina'])
        diccionario[year]['subsectors'][subsector]['Total ingresos netos'] += int(elem['Total ingresos netos'])
        diccionario[year]['subsectors'][subsector]['Total costos y gastos'] += int(elem['Total costos y gastos'])
        diccionario[year]['subsectors'][subsector]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
        diccionario[year]['subsectors'][subsector]['Total saldo a favor'] += int(elem['Total saldo a favor'])
        lt.addLast(diccionario[year]['subsectors'][subsector], elem)
    #Selecciona y guarda el subsector con más costos y gastos de nómina    
    for cada_año in diccionario:
        Costosygastos = 0
        Subsect = ""
        info = diccionario[cada_año]['subsectors']
        for cada_sub in info:
            if info[cada_sub]['Costos y gastos nómina'] > Costosygastos:
                Costosygastos = info[cada_sub]['Costos y gastos nómina']
                Subsect = cada_sub
        diccionario[cada_año]['noms'] = Subsect
        sort({'data' : diccionario[cada_año]['subsectors'][Subsect]}, orderingAlg='4', sortCriteria=sort_nomina)
    
    return diccionario


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    economicSubSectors = {}

    # Organiza los datos en un diccionario por año y subsector económico
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo añade
        year = elem['Año']
        if year not in economicSubSectors:
            economicSubSectors[year] = {'subsectors':{},
                                        'nameSubsec':''}
            
        # Verifica que no exista el subsector en el diccionario, y en caso de que no, lo añade
        subsector = elem['Nombre subsector económico']
        if subsector not in economicSubSectors[year]['subsectors']:
            elem['withholdings'] = elem['Descuentos tributarios']
            economicSubSectors[year]['subsectors'][subsector] = lt.newList(datastructure='ARRAY_LIST')
            economicSubSectors[year]['subsectors'][subsector]['withholdings'] = int(elem['Descuentos tributarios'])
            economicSubSectors[year]['subsectors'][subsector]['income'] = int(elem['Total ingresos netos'])
            economicSubSectors[year]['subsectors'][subsector]['spending'] = int(elem['Total costos y gastos'])
            economicSubSectors[year]['subsectors'][subsector]['debt'] = int(elem['Total saldo a pagar'])
            economicSubSectors[year]['subsectors'][subsector]['profit'] = int(elem['Total saldo a favor'])
        else:
            economicSubSectors[year]['subsectors'][subsector]['withholdings'] += int(elem['Descuentos tributarios'])
            economicSubSectors[year]['subsectors'][subsector]['income'] += int(elem['Total ingresos netos'])
            economicSubSectors[year]['subsectors'][subsector]['spending'] += int(elem['Total costos y gastos'])
            economicSubSectors[year]['subsectors'][subsector]['debt'] += int(elem['Total saldo a pagar'])
            economicSubSectors[year]['subsectors'][subsector]['profit'] += int(elem['Total saldo a favor'])
        lt.addLast(economicSubSectors[year]['subsectors'][subsector], elem)
        
        
    # Encuentra el subsector económico de mayor descuentos tributarios por cada año
    for year in economicSubSectors:
        maxVal = 0
        nameSubsec = ''
        for subsector in economicSubSectors[year]['subsectors']:
            withholdings = economicSubSectors[year]['subsectors'][subsector]['withholdings']
            if maxVal == 0:
                maxVal = withholdings
                nameSubsec = subsector
            elif withholdings > maxVal:
                maxVal = withholdings
                nameSubsec = subsector
        economicSubSectors[year]['nameSubsec'] = nameSubsec
        sort({'data':economicSubSectors[year]['subsectors'][nameSubsec]}, sortCriteria=sort_withholdings)
    
    return economicSubSectors


def req_6(data_structs, año):
    """
    Función que soluciona el requerimiento 6
    """
    diccionario = {}
    # Organiza los datos en un diccionario por año y subsector económico
    
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        dicc_aux = {}
        dicc_aux2 = {}
        # Verifica que no exista el año en el diccionario, y en caso de que no, lo añade
        year = elem['Año']
        if year not in diccionario:
            diccionario[year] = lt.newList(datastructure='ARRAY_LIST')
        # Guarda el sector económico de cada sector en un diccionario que tiene como llave el nombre y como valor un arraylist donde se guardan subsectores con la misma lógica
        if int(diccionario[year]['size']) == 0:
        #Se guarda la información del sector del primer elemento
            dicc_aux[elem['Nombre sector económico']] = lt.newList(datastructure='ARRAY_LIST')
            dicc_aux2[elem['Nombre subsector económico']] = lt.newList(datastructure='ARRAY_LIST')
            dicc_aux[elem['Nombre sector económico']]['Código sector económico'] = elem['Código sector económico']
            dicc_aux[elem['Nombre sector económico']]['Nombre sector económico'] = elem['Nombre sector económico']
            dicc_aux[elem['Nombre sector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
            dicc_aux[elem['Nombre sector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
            dicc_aux[elem['Nombre sector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
            dicc_aux[elem['Nombre sector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
         #Se guarda la información del subsector del primer elemento
            dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico'] = elem['Código subsector económico']
            dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico'] = elem['Nombre subsector económico']
            dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
            dicc_aux2[elem['Nombre subsector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
            dicc_aux2[elem['Nombre subsector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
            dicc_aux2[elem['Nombre subsector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
        #Se establece la información del subsector que más y menos aportó
            dicc_aux[elem['Nombre sector económico']]['maxsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
            dicc_aux[elem['Nombre sector económico']]['maxsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
            dicc_aux[elem['Nombre sector económico']]['maxsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
            dicc_aux[elem['Nombre sector económico']]['minsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
            dicc_aux[elem['Nombre sector económico']]['minsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
            dicc_aux[elem['Nombre sector económico']]['minsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
            dicc_aux2[elem['Nombre subsector económico']]['maxact'] = int(elem['Total ingresos netos'])
            dicc_aux2[elem['Nombre subsector económico']]['minact'] = int(elem['Total ingresos netos'])
            
            lt.addLast(dicc_aux2[elem['Nombre subsector económico']], elem)
            lt.addLast(dicc_aux[elem['Nombre sector económico']], dicc_aux2)
            lt.addLast(diccionario[year], dicc_aux)
        # Se guarda la información del segundo elemento
        elif int(diccionario[year]['size']) == 1:
            sect_b = lt.getElement(diccionario[year], 1)
        #Verifica si la información del primer elemento ya existe en el arreglo y si no, crea un nuevo arreglo para guardar la información de su sector, subsector y actividades económicas
            if elem['Nombre sector económico'] not in sect_b:
                dicc_aux2[elem['Nombre subsector económico']] = lt.newList(datastructure='ARRAY_LIST')
                dicc_aux[elem['Nombre sector económico']] = lt.newList(datastructure='ARRAY_LIST')
                dicc_aux[elem['Nombre sector económico']]['Código sector económico'] = elem['Código sector económico']
                dicc_aux[elem['Nombre sector económico']]['Nombre sector económico'] = elem['Nombre sector económico']
                dicc_aux[elem['Nombre sector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                dicc_aux[elem['Nombre sector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                dicc_aux[elem['Nombre sector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                dicc_aux[elem['Nombre sector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico'] = elem['Código subsector económico']
                dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico'] = elem['Nombre subsector económico']
                dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                dicc_aux2[elem['Nombre subsector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                dicc_aux2[elem['Nombre subsector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                dicc_aux2[elem['Nombre subsector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                dicc_aux[elem['Nombre sector económico']]['maxsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                dicc_aux[elem['Nombre sector económico']]['maxsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                dicc_aux[elem['Nombre sector económico']]['maxsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                dicc_aux[elem['Nombre sector económico']]['minsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                dicc_aux[elem['Nombre sector económico']]['minsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                dicc_aux[elem['Nombre sector económico']]['minsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                dicc_aux2[elem['Nombre subsector económico']]['maxact'] = int(elem['Total ingresos netos'])
                dicc_aux2[elem['Nombre subsector económico']]['minact'] = int(elem['Total ingresos netos'])
                lt.addLast(dicc_aux2[elem['Nombre subsector económico']], elem)
                lt.addLast(dicc_aux[elem['Nombre sector económico']], dicc_aux2)
                lt.addLast(diccionario[year], dicc_aux)
            #Guarda la información del segundo elemento en caso tal de que el arreglo del sector ya exista en el diccionario 
            else:
                sect_b[elem['Nombre sector económico']]['Total ingresos netos'] += int(elem['Total ingresos netos'])
                sect_b[elem['Nombre sector económico']]['Total costos y gastos'] += int(elem['Total costos y gastos'])
                sect_b[elem['Nombre sector económico']]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
                sect_b[elem['Nombre sector económico']]['Total saldo a favor'] += int(elem['Total saldo a favor'])
                sub_b = lt.getElement(sect_b[elem['Nombre sector económico']], 1)
                # Verifica si ya existe el subsector en el arreglo del sector, si no lo está crea el arreglo y guarda el elemento allí
                if elem['Nombre subsector económico'] not in sub_b:
                  dicc_aux2[elem['Nombre subsector económico']] = lt.newList(datastructure='ARRAY_LIST')
                  dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico'] = elem['Código subsector económico']
                  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico'] = elem['Nombre subsector económico']
                  dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                  dicc_aux2[elem['Nombre subsector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                  dicc_aux2[elem['Nombre subsector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                  dicc_aux2[elem['Nombre subsector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                  #Compara con la información del subsector que más y menos aportó y la modifica en caso de que este sea mayor o menor que lo establecido
                  if int(dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']) > int(sect_b[elem['Nombre sector económico']]['maxsubinf']):
                    sect_b[elem['Nombre sector económico']]['maxsubnom'] = dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                    sect_b[elem['Nombre sector económico']]['maxsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                    sect_b[elem['Nombre sector económico']]['maxsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                  elif int(dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']) < int(sect_b[elem['Nombre sector económico']]['minsubinf']): 
                    sect_b[elem['Nombre sector económico']]['minsubnom'] = dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                    sect_b[elem['Nombre sector económico']]['minsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                    sect_b[elem['Nombre sector económico']]['minsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                  if int(elem['Total ingresos netos']) > sub_b[elem['Nombre actividad económica']]['maxact']:
                    lt.addLast(sub_b[elem['Nombre subsector económico']], elem)
                  elif int(elem['Total ingresos netos']) < sub_b[elem['Nombre actividad económica']]['minact']:
                    lt.addFirst(sub_b[elem['Nombre subsector económico']], elem)
                  lt.addLast(sect_b['Nombre sector económico'], dicc_aux2)  
                else:
                    #Guarda el segundo elemento cuando el arreglo de su subsector también ya existe
                    #Suma los aportes del elemento a los totales del subsector
                    sub_b[elem['Nombre subsector económico']]['Total ingresos netos'] += int(elem['Total ingresos netos'])
                    sub_b[elem['Nombre subsector económico']]['Total costos y gastos'] += int(elem['Total costos y gastos'])
                    sub_b[elem['Nombre subsector económico']]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
                    sub_b[elem['Nombre subsector económico']]['Total saldo a favor'] += int(elem['Total saldo a favor'])
                    #Compara con la información del subsector que más y menos aportó y la modifica en caso de que este sea mayor o menor que lo establecido
                    if int(sub_b[elem['Nombre subsector económico']]['Total ingresos netos']) > int(sect_b[elem['Nombre sector económico']]['maxsubinf']):
                        sect_b[elem['Nombre sector económico']]['maxsubnom'] = sub_b[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsub'] = sub_b[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsubinf'] = sub_b[elem['Nombre subsector económico']]['Total ingresos netos']
                    elif int(sub_b[elem['Nombre subsector económico']]['Total ingresos netos']) < int(sect_b[elem['Nombre sector económico']]['minsubinf']): 
                        sect_b[elem['Nombre sector económico']]['minsubnom'] = sub_b[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsub'] = sub_b[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsubinf'] = sub_b[elem['Nombre subsector económico']]['Total ingresos netos']
                    if int(elem['Total ingresos netos']) > sub_b[elem['Nombre subsector económico']]['maxact']:
                        lt.addLast(sub_b[elem['Nombre subsector económico']], elem)
                    elif int(elem['Total ingresos netos']) < sub_b[elem['Nombre subsector económico']]['minact']:
                        lt.addFirst(sub_b[elem['Nombre subsector económico']], elem)
        #Guarda la información para todos los demás elementos
        else:
            centinela = False
            index = 0
            #Verifica si el sector económico del elemento ya existe en el arreglo del año
            for ind in range (1, int(diccionario[year]['size'])+1):
                sect_b = lt.getElement(diccionario[year], ind)
                if elem['Nombre sector económico'] in sect_b:
                    centinela = True
                    index = ind
            #Si no existe el sector económico en el arreglo, lo añade como nuevo elemento y guarda su información en un nuevo arreglo
            if centinela == False:
                dicc_aux2[elem['Nombre subsector económico']] = lt.newList(datastructure='ARRAY_LIST')
                dicc_aux[elem['Nombre sector económico']] = lt.newList(datastructure='ARRAY_LIST')
                dicc_aux[elem['Nombre sector económico']] = lt.newList(datastructure='ARRAY_LIST')
                dicc_aux[elem['Nombre sector económico']]['Código sector económico'] = elem['Código sector económico']
                dicc_aux[elem['Nombre sector económico']]['Nombre sector económico'] = elem['Nombre sector económico']
                dicc_aux[elem['Nombre sector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                dicc_aux[elem['Nombre sector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                dicc_aux[elem['Nombre sector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                dicc_aux[elem['Nombre sector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico'] = elem['Código subsector económico']
                dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico'] = elem['Nombre subsector económico']
                dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                dicc_aux2[elem['Nombre subsector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                dicc_aux2[elem['Nombre subsector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                dicc_aux2[elem['Nombre subsector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                dicc_aux[elem['Nombre sector económico']]['maxsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                dicc_aux[elem['Nombre sector económico']]['maxsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                dicc_aux[elem['Nombre sector económico']]['maxsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                dicc_aux[elem['Nombre sector económico']]['minsubnom'] =  dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                dicc_aux[elem['Nombre sector económico']]['minsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                dicc_aux[elem['Nombre sector económico']]['minsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                dicc_aux2[elem['Nombre subsector económico']]['maxact'] = int(elem['Total ingresos netos'])
                dicc_aux2[elem['Nombre subsector económico']]['minact'] = int(elem['Total ingresos netos'])
                lt.addLast(dicc_aux2[elem['Nombre subsector económico']], elem)
                lt.addLast(dicc_aux[elem['Nombre sector económico']], dicc_aux2)
                lt.addLast(diccionario[year], dicc_aux)
            #Si el arreglo del sector del elemento ya existe, suma los aportes del elemento al sector
            else: 
                sect_b = lt.getElement(diccionario[year], index)
                sect_b[elem['Nombre sector económico']]['Nombre sector económico'] += elem['Nombre sector económico']
                sect_b[elem['Nombre sector económico']]['Total ingresos netos'] += int(elem['Total ingresos netos'])
                sect_b[elem['Nombre sector económico']]['Total costos y gastos'] += int(elem['Total costos y gastos'])
                sect_b[elem['Nombre sector económico']]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
                sect_b[elem['Nombre sector económico']]['Total saldo a favor'] += int(elem['Total saldo a favor'])
                centinela2 = False
                subin = 0
                #Verifica si el subsector del elemento ya existe en el arreglo del sector
                for ix in range (1, int(sect_b[elem['Nombre sector económico']]['size'])+1):
                    sub_b = lt.getElement(sect_b[elem['Nombre sector económico']], ix)
                    if elem['Nombre subsector económico'] in sub_b:
                        centinela2 = True
                        subin = ix
                #Si el subsector no existe en el arreglo del sector, crea un nuevo arreglo donde guarda la información del subsector
                if centinela2 == False:
                    dicc_aux2[elem['Nombre subsector económico']] = lt.newList(datastructure='ARRAY_LIST')
                    dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico'] = elem['Código subsector económico']
                    dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico'] = elem['Nombre subsector económico']
                    dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos'] = int(elem['Total ingresos netos'])
                    dicc_aux2[elem['Nombre subsector económico']]['Total costos y gastos'] = int(elem['Total costos y gastos'])
                    dicc_aux2[elem['Nombre subsector económico']]['Total saldo a pagar'] = int(elem['Total saldo a pagar'])
                    dicc_aux2[elem['Nombre subsector económico']]['Total saldo a favor'] = int(elem['Total saldo a favor'])
                    if int(dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']) > int(sect_b[elem['Nombre sector económico']]['maxsubinf']):
                        sect_b[elem['Nombre sector económico']]['maxsubnom'] = dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                    elif int(dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']) < int(sect_b[elem['Nombre sector económico']]['minsubinf']): 
                        sect_b[elem['Nombre sector económico']]['minsubnom'] = dicc_aux2[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsub'] = dicc_aux2[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsubinf'] = dicc_aux2[elem['Nombre subsector económico']]['Total ingresos netos']
                    dicc_aux2[elem['Nombre subsector económico']]['maxact'] = int(elem['Total ingresos netos'])
                    dicc_aux2[elem['Nombre subsector económico']]['minact'] = int(elem['Total ingresos netos'])
                    lt.addLast(dicc_aux2[elem['Nombre subsector económico']], elem)
                    lt.addLast(sect_b[elem['Nombre sector económico']], dicc_aux2)
                else:
                    sub_b = lt.getElement(sect_b[elem['Nombre sector económico']], subin)
                    sub_b[elem['Nombre subsector económico']]['Total ingresos netos'] += int(elem['Total ingresos netos'])
                    sub_b[elem['Nombre subsector económico']]['Total costos y gastos'] += int(elem['Total costos y gastos'])
                    sub_b[elem['Nombre subsector económico']]['Total saldo a pagar'] += int(elem['Total saldo a pagar'])
                    sub_b[elem['Nombre subsector económico']]['Total saldo a favor'] += int(elem['Total saldo a favor'])
                    if int(sub_b[elem['Nombre subsector económico']]['Total ingresos netos']) > int(sect_b[elem['Nombre sector económico']]['maxsubinf']):
                        sect_b[elem['Nombre sector económico']]['maxsubnom'] = sub_b[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsub'] = sub_b[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['maxsubinf'] = sub_b[elem['Nombre subsector económico']]['Total ingresos netos']
                    elif int(sub_b[elem['Nombre subsector económico']]['Total ingresos netos']) < int(sect_b[elem['Nombre sector económico']]['minsubinf']): 
                        sect_b[elem['Nombre sector económico']]['minsubnom'] = sub_b[elem['Nombre subsector económico']]['Nombre subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsub'] = sub_b[elem['Nombre subsector económico']]['Código subsector económico']
                        sect_b[elem['Nombre sector económico']]['minsubinf'] = sub_b[elem['Nombre subsector económico']]['Total ingresos netos']
                    if int(elem['Total ingresos netos']) > sub_b[elem['Nombre subsector económico']]['maxact']:
                        lt.addLast(sub_b[elem['Nombre subsector económico']], elem)
                    elif int(elem['Total ingresos netos']) < sub_b[elem['Nombre subsector económico']]['minact']:
                        lt.addFirst(sub_b[elem['Nombre subsector económico']], elem)

        
    return diccionario[año]



def req_7(data_structs, n, aInicial, aFinal):
    """
    Función que soluciona el requerimiento 7
    """
    compareList = {'data':lt.newList(datastructure='ARRAY_LIST')}
    
    #Añade los datos que estén en el rango de años ingresado por parámetro
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        if (int(elem['Año']) >= aInicial) and (int(elem['Año']) <= aFinal):
            lt.addLast(compareList['data'], elem)
    
    # Organiza los datos de mayor a menor en terminos de los costos y gastos de la entrada
    sort(compareList, sortCriteria=sort_spending)
    
    #Obtiene los elementos con menor valor de costos y gastos para el periodo.
    lst = lt.newList(datastructure='ARRAY_LIST')
    for i in range(1, n + 1):
        lt.addLast(lst, lt.getElement(compareList['data'], i))
    
    # Organiza la lista resultante del top por año de la entrada
    sort({'data':lst}, sortCriteria=sort_year)
    
    return lst


def req_8(data_structs, aInicial, aFinal):
    """
    Función que soluciona el requerimiento 8
    """
    compareList = {}
    
    # Añade los elementos a un diccionario del subsector que cumplan con el rango de años especificado
    for i in range(1, lt.size(data_structs['data']) + 1):
        elem = lt.getElement(data_structs['data'], i)['data']
        if (int(elem['Año']) >= aInicial) and (int(elem['Año']) <= aFinal):
            subsector = elem['Nombre subsector económico']
            if subsector not in compareList:
                compareList[subsector] = lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(compareList[subsector], elem)

    # Crea los totales de diferentes datos para cada subsector económico
    subsectorNames = lt.newList(datastructure='ARRAY_LIST')
    for subsector in compareList:
        sort({'data':compareList[subsector]}, sortCriteria=sort_chargeTaxes)
        lt.addLast(subsectorNames, subsector)
        chargeTaxes = 0
        income = 0
        spending = 0
        debt = 0
        profit = 0
        for entry in compareList[subsector]['elements']:
            chargeTaxes += int(entry['Total Impuesto a cargo'])
            income += int(elem['Total ingresos netos'])
            spending += int(elem['Total costos y gastos'])
            debt += int(elem['Total saldo a pagar'])
            profit += int(elem['Total saldo a favor'])
        compareList[subsector]['chargeTaxes'] = chargeTaxes
        compareList[subsector]['income'] = income
        compareList[subsector]['spending'] = spending
        compareList[subsector]['debt'] = debt
        compareList[subsector]['profit'] = profit
    
    # Organiza los nombres de los subsesctores alfabéticamente
    sort({'data':subsectorNames}, sortCriteria=sort_subsector)
    
    return compareList, subsectorNames
    

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if str(data_1) > data_2['data']["Código actividad económica"]:
        return 1
    elif str(data_1) < data_2['data']["Código actividad económica"]:
        return -1
    else:
        return 0
    
def compareSubsector(data_1, data_2):
    """
    Compara los nombres de los  subsectores existentes en la lista

    Args:
        data_1 (dict): Elemento a comparar
        data_2 (dict): Elemento a comparar

    Returns:
        int: Retorna un número dependiendo del valor de la comparación
    """
    if data_1 > data_2['Nombre subsector económico']:
        return 1
    elif data_1 < data_2['Nombre subsector económico']:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data_1 (dict): Diccionario del dato 1 a comparar
        data_2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    zeros1 = 4 - len(data_1['data']['Código actividad económica'])
    zeros2 = 4 - len(data_2['data']['Código actividad económica'])
    crit_1 = data_1['data']["Año"] + '0' * zeros1 + data_1['data']['Código actividad económica']
    crit_2 = data_2['data']["Año"] + '0' * zeros2 + data_2['data']['Código actividad económica']
    return crit_1 < crit_2


def sort_withholdings(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Descuentos tributarios']) < int(d2['Descuentos tributarios'])


def sort_retenciones(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total retenciones']) < int(d2['Total retenciones'])

def sort_spending(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total costos y gastos']) < int(d2['Total costos y gastos'])

def sort_nomina(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Costos y gastos nómina']) < int(d2['Costos y gastos nómina'])

def sort_saldoapagar(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total saldo a pagar']) < int(d2['Total saldo a pagar'])
def sort_saldoafavor(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total saldo a favor']) < int(d2['Total saldo a favor'])

def sort_subsector(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (str): Nombre del subsector 1 a comparar
        d2 (str): Nombre del subsector 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return d1.lower() < d2.lower()


def sort_year(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Año']) > int(d2['Año'])


def sort_chargeTaxes(d1, d2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        d1 (dict): Diccionario del dato 1 a comparar
        d2 (dict): Diccionario del dato 2 a comparar

    Returns:
        bool: Valor de verdad de si el dato 1 es mayor al 2
    """
    return int(d1['Total Impuesto a cargo']) > int(d2['Total Impuesto a cargo'])


def sort(data_structs, orderingAlg='1', sortCriteria=sort_criteria):
    """
    Función encargada de ordenar la lista con los datos
    """
    if orderingAlg == '1':
        ins.sort(data_structs["data"], sortCriteria)
    elif orderingAlg == '2':
        se.sort(data_structs["data"], sortCriteria)
    elif orderingAlg == '3':
        sa.sort(data_structs["data"], sortCriteria)
    elif orderingAlg == '4':
        merg.sort(data_structs["data"], sortCriteria)
    elif orderingAlg == '5':
        quk.sort(data_structs["data"], sortCriteria)
