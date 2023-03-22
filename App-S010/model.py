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


def new_data_structs(list_type:int):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {
    }
    if list_type == 1:
        catalog["data"] = lt.newList(datastructure="SINGLE_LINKED",
                                     )
    elif list_type == 2:
        catalog["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     )

    return catalog


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs, data)

    return data_structs

def present(data_structs, element):
    
    x = lt.isPresent(data_structs, element)
    
    return x



# Funciones de consulta
def get_data_by_pos(data_structs, pos:int):
    """
    Consigue un elemento según su posición
    """
    data = lt.getElement(data_structs,pos)
    return data


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])

def data_by_quantity(sorted_list, control, cantidad:int, sentido):
    """ 
    Funcion que consigue x cantidad de datos segun el sentido
    
    """
    
    if sentido == "adelante":
        i = 1
        
        while i < cantidad:
            
            info = get_data_by_pos(sorted_list, i)
            respuesta = lt.addLast(control, info)
            i += 1
    
    elif sentido == "atras":
        total = data_size(sorted_list)
        i = total - cantidad
            
        while i < total:
            info = get_data_by_pos(sorted_list, i)
            respuesta = lt.addLast(control, info)
            i += 1
    
    return respuesta

def join_lists(data1, data2):
    size = data_size(data2)
    
    for i in range (0, size):
        element = get_data_by_pos(data2, i)
        data1 = add_data(data1["data"], element)
    
    return data1

def insert_element(datastructs,element, pos):
    respuesta = lt.insertElement(datastructs,element, pos)
    
    return respuesta

def elementos_unicos(data_structs, aspecto):
    size = lt.size(data_structs)
    respuesta = new_data_structs(2)
    for i in range(1, size+1):
        x = get_data_by_pos(data_structs, i)
        present = lt.isPresent(respuesta["data"], x[aspecto])
        if present == 0:
            respuesta["data"] = add_data(respuesta["data"], x[aspecto])
    
    return respuesta

def elementos_segun_aspecto(data_structs, aspecto, valor):
    size = lt.size(data_structs)
    respuesta = new_data_structs(2)
    for i in range(1, size+1):
        x = get_data_by_pos(data_structs, i)
        if x[aspecto] == valor:
            respuesta["data"] = add_data(respuesta["data"], x)
    
    return respuesta

def lista_by_aspecto(datastructs, aspecto):
    elementos = elementos_unicos(datastructs, aspecto)
    respuesta = new_data_structs(2)
    size = data_size(elementos)
    
    for i in range(1, size+1):
        valor = get_data_by_pos(elementos["data"], i)
        x = elementos_segun_aspecto(datastructs, aspecto, valor)
        respuesta["data"] = add_data(respuesta["data"], x)
    
    return elementos, respuesta

# Funciones que solucionan el requerimiento 1


def actividades_por_saldo(lista):
    """
    Función que soluciona el requerimiento 1
    """

    datos = lista["data"]
    respuesta = quk.sort(datos, cmp_saldo)
    element = get_data_by_pos(respuesta, 1)
    
    a = {
        "Año": element["Año"],
        "Código actividad económica": element["Código actividad económica"],
        "Nombre actividad económica": element["Nombre actividad económica"],
        "Código sector económico": element["Código sector económico"],
        "Nombre sector económico": element["Nombre sector económico"],
        "Código subsector económico": element["Código subsector económico"],
        "Nombre subsector económico": element["Nombre subsector económico"],
        "Total ingresos netos": element["Total ingresos netos"],
        "Total costos y gastos": element["Total costos y gastos"],
        "Total saldo a pagar": element["Total saldo a pagar"],
        "Total saldo a favor": element["Total saldo a favor"]
    }
    
    return a


# FUNCIONES PARA SOLUCIONAR EL REQUERIMIENTO 3

def subsector_menor_retenciones(lista):
    comparar = new_data_structs(2)
    subsector, data = lista_by_aspecto(lista["data"], "Código subsector económico")   
    size = data_size(subsector)
    for k in range(1, size+1):
        subsector_elements = lt.getElement(data["data"], k)
        names = lt.firstElement(subsector_elements["data"])
        size2 = data_size(subsector_elements)
        a = {
            "Año":names["Año"],
            "Código sector económico": names["Código sector económico"],
            "Nombre sector económico": names["Nombre sector económico"],
            "Código subsector económico": names["Código subsector económico"],
            "Nombre subsector económico": names["Nombre subsector económico"],
            "Total retenciones": int(names["Total retenciones"]),
            "Total ingresos netos": int(names["Total ingresos netos"]),
            "Total costos y gastos": int(names["Total costos y gastos"]),
            "Total saldo a pagar": int(names["Total saldo a pagar"]),
            "Total saldo a favor": int(names["Total saldo a favor"])
        }
            
        for j in range(2, size2+1):
            adition = lt.getElement(subsector_elements["data"], j)
            a["Total retenciones"] += int(adition["Total retenciones"])
            a["Total ingresos netos"] += int(adition["Total ingresos netos"])
            a["Total costos y gastos"] += int(adition["Total costos y gastos"])
            a["Total saldo a pagar"] += int(adition["Total saldo a pagar"])
            a["Total saldo a favor"] += int(adition["Total saldo a favor"])
            
        comparar["data"] = add_data(comparar["data"], a)
        
    comparar["data"] = se.sort(comparar["data"], cmp_sub_menor_retencion)
    subsector_data = lt.firstElement(comparar["data"])
    subsector_index = lt.isPresent(subsector["data"], subsector_data["Código sector económico"])
    activities = lt.getElement(data["data"], subsector_index)
    activities_size = data_size(activities)
    activities = quk.sort(activities["data"], cmp_sub_menor_retencion)
    
    
    if activities_size < 6:
        return subsector_data, activities
    else:
        a = primeros_ultimos(activities, 3, "adelante")
        b = primeros_ultimos(activities, 3, "atras")
        bsize = data_size(b)
        for i in range(1, bsize):
            x = get_data_by_pos(activities, i)
            a = add_data(a, x)
            
        return subsector_data, a

# FUNCIONES PARA SOLUCIONAR EL REQUERIMIENTO 5

def cmp_descuentos_tributarios(data1, data2):
    if int(data1["Descuentos tributarios"]) > int(data2["Descuentos tributarios"]):
        return True
    else:
        return False

def primeros_ultimos(datastructs, cantidad, sentido:str):
    """
    Agarra la cantidad indicada de elementos en el sentido indicado, "adelante" ir de adelante
    a atras y "atras" para ir de atras a adelante  
    """
    size = data_size(datastructs)
    respuesta = new_data_structs(2)
    if sentido == "adelante":
        x = 1
        y = cantidad
    elif sentido == "atras": 
        x = size - cantidad
        y = size
    
    for i in range(x, y):
        a = get_data_by_pos(datastructs["data"], i)
        respuesta["data"] = add_data(respuesta["data"], a)
    
    return respuesta

def calculos_subsector_req_5(datastructs):
    """
    Función que soluciona el requerimiento 5
    """
    
    comparar = new_data_structs(2)
    subsector, data = lista_by_aspecto(datastructs["data"], "Código subsector económico")   
    size = data_size(subsector)
    for k in range(1, size+1):
        subsector_elements = lt.getElement(data["data"], k)
        names = lt.firstElement(subsector_elements["data"])
        size2 = data_size(subsector_elements)
        a = {
            "Año":names["Año"],
            "Código sector económico": names["Código sector económico"],
            "Nombre sector económico": names["Nombre sector económico"],
            "Código subsector económico": names["Código subsector económico"],
            "Nombre subsector económico": names["Nombre subsector económico"],
            "Descuentos tributarios": int(names["Descuentos tributarios"]),
            "Total ingresos netos": int(names["Total ingresos netos"]),
            "Total costos y gastos": int(names["Total costos y gastos"]),
            "Total saldo a pagar": int(names["Total saldo a pagar"]),
            "Total saldo a favor": int(names["Total saldo a favor"])
        }
            
        for j in range(2, size2+1):
            adition = lt.getElement(subsector_elements["data"], j)
            a["Descuentos tributarios"] += int(adition["Descuentos tributarios"])
            a["Total ingresos netos"] += int(adition["Total ingresos netos"])
            a["Total costos y gastos"] += int(adition["Total costos y gastos"])
            a["Total saldo a pagar"] += int(adition["Total saldo a pagar"])
            a["Total saldo a favor"] += int(adition["Total saldo a favor"])
            
        comparar["data"] = add_data(comparar["data"], a)
        
    comparar["data"] = se.sort(comparar["data"], cmp_descuentos_tributarios)
    subsector_data = lt.firstElement(comparar["data"])
    subsector_index = lt.isPresent(subsector["data"], subsector_data["Código sector económico"])
    activities = lt.getElement(data["data"], subsector_index)
    activities_size = data_size(activities)
    activities["data"] = quk.sort(activities["data"], cmp_descuentos_tributarios)
    
    if activities_size < 6:
        return subsector_data, activities
    else:
        a = primeros_ultimos(activities, 3, "adelante")
        b = primeros_ultimos(activities, 3, "atras")
        bsize = data_size(b)
        for i in range(1, bsize):
            x = get_data_by_pos(activities["data"], i)
            a["data"] = add_data(a["data"], x)
        
        return subsector_data, a
        
    
# FUNCIONES PARA SOLUCIONAR EL REQUERIMIENTO 6

def cmp_ingresos_netos(data1, data2):
    if int(data1["Total ingresos netos"]) > int(data2["Total ingresos netos"]):
        return True
    else:
        return False

def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    respuesta = new_data_structs(2)
    subsector, data = lista_by_aspecto(data_structs["data"], "Código subsector económico")
    size = data_size(subsector)
    for i in range(1, size+1):
        info = get_data_by_pos(data["data"], i)
        info["data"] = quk.sort(info["data"], cmp_ingresos_netos)
        mayor = lt.firstElement(info["data"])
        menor = lt.lastElement(info["data"])
        size2 = data_size(info)
        a = {
            "Código sector económico": mayor["Código sector económico"],
            "Nombre sector económico": mayor["Nombre sector económico"],
            "Código subsector económico": mayor["Código subsector económico"],
            "Nombre subsector económico": mayor["Nombre subsector económico"],
            "Total ingresos netos": int(mayor["Total ingresos netos"]),
            "Total costos y gastos" : int(mayor["Total costos y gastos"]),
            "Total saldo a pagar" : int(mayor["Total saldo a pagar"]),
            "Total saldo a favor" : int(mayor["Total saldo a favor"])
        }
        for j in range(2, size2+1):
            x = get_data_by_pos(info["data"], j)
            a["Total costos y gastos"] += int(x["Total costos y gastos"])
            a["Total saldo a pagar"] += int(x["Total saldo a pagar"])
            a["Total saldo a favor"] += int(x["Total saldo a favor"])
        
        a["Actividad económica que más aportó"] = {
            "Código actividad económica" : mayor["Código actividad económica"],
            "Nombre actividad económica" : mayor["Nombre actividad económica"],
            "Total ingresos netos": mayor["Total ingresos netos"],
            "Total costos y gastos" : mayor["Total costos y gastos"],
            "Total saldo a pagar" : mayor["Total saldo a pagar"],
            "Total saldo a favor" : mayor["Total saldo a favor"]
        }
        a["Actividad económica que menos aportó"] = {
            "Código actividad económica" : menor["Código actividad económica"],
            "Nombre actividad económica" : menor["Nombre actividad económica"],
            "Total ingresos netos": menor["Total ingresos netos"],
            "Total costos y gastos" : menor["Total costos y gastos"],
            "Total saldo a pagar" : menor["Total saldo a pagar"],
            "Total saldo a favor" : menor["Total saldo a favor"]
        }
        respuesta["data"] = add_data(respuesta["data"],a)
    sortedlist = quk.sort(respuesta["data"], cmp_ingresos_netos)
    size3 = lt.size(sortedlist)
    first = lt.firstElement(sortedlist)
    last = lt.lastElement(sortedlist)
    sector = {
        "Código sector económico": first["Código sector económico"],
        "Nombre sector económico": first["Nombre sector económico"],
        "Total ingresos netos" : int(first["Total ingresos netos"]),
        "Total costos y gastos": int(first["Total costos y gastos"]),
        "Total saldo a pagar" : int(first["Total saldo a pagar"]),
        "Total saldo a favor" : int(first["Total saldo a favor"]),
        "Subsector económico que más aportó": first["Código subsector económico"],
        "Subsector económico que menos aportó": last["Código subsector económico"]
    }
    for i in range(2, size3+1):
        x = get_data_by_pos(sortedlist, i)
        sector["Total ingresos netos"] += int(x["Total ingresos netos"])
        sector["Total costos y gastos"] += int(x["Total costos y gastos"])
        sector["Total saldo a pagar"] += int(x["Total saldo a pagar"])
        sector["Total saldo a favor"] += int(x["Total saldo a favor"])
    
    return sector, first, last

def cmp_sector(data1, data2):
    if int(data1["Código sector económico"]) < int(data2["Código sector económico"]):
        return True
    else:
        return False

def pick_first_sector(datastructs):
    """
    Encuentra el sector con mayores ingresos netos
    """
    datastructs["data"] = merg.sort(datastructs["data"], cmp_sector)

    return datastructs

def cmp_menor_costos_gastos(data1, data2):
    
    if data1["Total costos y gastos"] < data2["Total costos y gastos"]:
        return True
    else:
        return False

def cmp_año_mayor_menor(data1, data2):
    if data1["Año"] > data2["Año"]:
        return True
    elif data1["Año"] == data2["Año"]:
        if data1["Total costos y gastos"] < data2["Total costos y gastos"]:
            return True
        else:
            return False
    else:
        return False

def req_7(data_structs,años, cantidad):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    añox, info = lista_by_aspecto(data_structs, "Año")
    size = data_size(añox)
    datos1 = new_data_structs(2)
    
    respuesta = new_data_structs(2)
    for i in range (1, size+1):
        x = int(lt.getElement(añox["data"], i))
        y = lt.isPresent(años["data"], int(x))
        if y != 0:
            data = lt.getElement(info["data"], i)
            size2 = lt.size(data["data"])
            for j in range(1, size2+1):
                a = lt.getElement(data["data"], j)
                
                agregar = {
                    "Año": int(a["Año"]),
                    "Código actividad económica": a["Código actividad económica"],
                    "Nombre actividad económica": a["Nombre actividad económica"],
                    "Código sector económico": a["Código sector económico"],
                    "Nombre sector económico": a["Nombre sector económico"],
                    "Código subsector económico": a["Código subsector económico"],
                    "Nombre subsector económico": a["Nombre subsector económico"],
                    "Total ingresos netos": int(a["Total ingresos netos"]),
                    "Total costos y gastos": int(a["Total costos y gastos"]),
                    "Total saldo a pagar": int(a["Total saldo a pagar"]),
                }
                datos1["data"] = add_data(datos1["data"], agregar)
                
    datos1["data"] = quk.sort(datos1["data"], cmp_menor_costos_gastos)  
    size3 = lt.size(datos1["data"])
        
    for l in range(1, cantidad + 1):
        elemento = lt.getElement(datos1["data"], l)
        respuesta["data"] = add_data(respuesta["data"], elemento)
    
    respuesta["data"] = merg.sort(respuesta["data"], cmp_año_mayor_menor)
    
    return respuesta

def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0
    
    
def cmp_saldo(data1, data2):
    """
    Compara el saldo a pagar de dos parametros
    """
    if int(data1["Total saldo a pagar"]) > int(data2["Total saldo a pagar"]):
        return True
    else:
        return False
    
def cmp_sub_menor_retencion(data1, data2):
    
    if int((data1["Total retenciones"])) < int((data2["Total retenciones"])):
        return True
    else:
        return False
    
    
def cmp_impuestos_by_anio_CAE(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """

    if int(data_1["Año"]) < int(data_2["Año"]):
        return True
    elif data_1["Año"] == data_2["Año"]:
        if data_1["Código actividad económica"] < data_2["Código actividad económica"]:
            return True
        else:
            return False
    return False


# Funciones de ordenamiento
    
def sort(data_structs,type_sort:int):
    """
    Función encargada de ordenar la lista con los datos
    """
    size = lt.size(data_structs)
    if type_sort == 1:
        sorted_list = se.sort(data_structs, cmp_impuestos_by_anio_CAE)
    elif type_sort == 2:
        sorted_list = ins.sort(data_structs, cmp_impuestos_by_anio_CAE)
    elif type_sort == 3:
        sorted_list = sa.sort(data_structs, cmp_impuestos_by_anio_CAE)
    elif type_sort == 4:
        sorted_list = quk.sort(data_structs, cmp_impuestos_by_anio_CAE)
    elif type_sort == 5:
        sorted_list = merg.sort(data_structs, cmp_impuestos_by_anio_CAE) 
        
    return sorted_list