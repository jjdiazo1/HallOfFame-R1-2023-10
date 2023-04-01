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


def new_data_structs(list_type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs = {"data": None}
    
    data_structs['data'] = lt.newList(list_type)
    
    return data_structs


# Funciones para agregar informacion al modelo
def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    cod = data["Código actividad económica"]
    if not cod.isdecimal():
        done = False
        index = 0
        lista = lt.newList("ARRAY_LIST")
        while done == False:
            obj = cod[index]
            if not obj.isdecimal():
                num = cod.split(obj)
                lt.addLast(lista,num)
                done = True
            index += 1
        value = lt.firstElement(lista)
        data["Código actividad económica"] = value[0]                 
    lt.addLast(data_structs["data"], data)
    return data_structs

def first_and_last3(data_structs):
    elements = data_structs
    first3 = lt.subList(elements,1,3)
    last3 = lt.subList(elements,lt.size(elements)-2,3)
    for x in lt.iterator(last3):
        lt.addLast(first3,x)
    first_and_last3 = first3
    
    return first_and_last3

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


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
    # TODO: Realizar el requerimiento 1
    lista = lt.newList("ARRAY_LIST")
    param = ["Año","Código actividad económica","Nombre actividad económica",
             "Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total ingresos netos","Total costos y gastos",
             "Total saldo a pagar","Total saldo a favor"]
    lt.addLast(lista,param)
    
    highest = lt.firstElement(data_structs)
    for element in lt.iterator(data_structs):
        if element["Año"] != highest["Año"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
            highest = element   
        elif float(element["Total saldo a pagar"]) > float(highest["Total saldo a pagar"]):
            highest = element       
        elif element == lt.lastElement(data_structs):
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
    return lista["elements"]
    


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    lista = lt.newList("ARRAY_LIST")
    
    param = ["Año","Código actividad económica","Nombre actividad económica",
             "Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total ingresos netos","Total costos y gastos",
             "Total saldo a pagar","Total saldo a favor"]
    lt.addLast(lista,param)
    
    highest = lt.firstElement(data_structs)
    for element in lt.iterator(data_structs):
        if element["Año"] != highest["Año"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
            highest = element   
        elif float(element["Total saldo a favor"]) > float(highest["Total saldo a favor"]):
            highest = element       
        elif element == lt.lastElement(data_structs):
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
    return lista["elements"]


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3 
    
    #creo una copia del data_structs 
    data_structs_aux = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        data = {}
        for key,value in element.items():
            data[str(key)] = value
        lt.addLast(data_structs_aux,data)

        
    # Primera parte
    lista = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs_aux):
        if lt.isEmpty(lista):
            initial = lt.firstElement(data_structs_aux)
            lt.addLast(lista,initial)
        elif not lt.isEmpty(lista):
            if element["Código subsector económico"] == initial["Código subsector económico"]:
                initial["Total retenciones"] = str(int(initial["Total retenciones"])+int(element["Total retenciones"]))
                initial["Total ingresos netos"] = str(int(initial["Total ingresos netos"])+int(element["Total ingresos netos"]))
                initial["Total costos y gastos"] = str(int(initial["Total costos y gastos"])+int(element["Total costos y gastos"]))
                initial["Total saldo a pagar"] = str(int(initial["Total saldo a pagar"])+int(element["Total saldo a pagar"]))
                initial["Total saldo a favor"] = str(int(initial["Total saldo a favor"])+int(element["Total saldo a favor"]))
            elif element["Código subsector económico"] != initial["Código subsector económico"]:
                initial = element
                lt.addLast(lista,initial)
                      
    lista_min = lt.newList("ARRAY_LIST")
    minimum = lt.firstElement(lista)
    for element in lt.iterator(lista):
        if element == lt.lastElement(lista):
            if float(element["Total retenciones"]) < float(minimum["Total retenciones"]):
                minimum = element
            lt.addLast(lista_min,minimum)
        elif element["Año"] == minimum["Año"]:
            if float(element["Total retenciones"]) < float(minimum["Total retenciones"]):
                minimum = element
        elif not element["Año"] == minimum["Año"]:
            lt.addLast(lista_min,minimum)
            minimum = element
            
    param = ["Año","Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total retenciones","Total ingresos netos","Total costos y gastos",
             "Total saldo a pagar","Total saldo a favor"]
    
    lista_tablas_anios = lt.newList("ARRAY_LIST")
    for minimum in lt.iterator(lista_min):
        lista = lista_por_anio_req3(data_structs,minimum)
        lt.addLast(lista_tablas_anios,lista)
        
        
    lista_min_def = lt.newList("ARRAY_LIST")
    for x in lista_min["elements"]:
        lista_min_aux = lt.newList("ARRAY_LIST")
        for i in param:
            lt.addLast(lista_min_aux,x[i])
        lt.addLast(lista_min_def,lista_min_aux["elements"])
    
    param2 = ["Año","Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total retenciones del subsector económico",
             "Total ingresos netos del subsector económico","Total costos y gastos del subsector económico",
             "Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
    lt.addFirst(lista_min_def,param2)
    
    return lista_min_def["elements"], lista_tablas_anios["elements"]
                
        
def lista_por_anio_req3(data_structs,minimum):
    param = ["Código actividad económica","Nombre actividad económica","Total retenciones",
              "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    lista = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        if element["Año"] == minimum["Año"]:
            if element["Código subsector económico"] == minimum["Código subsector económico"]:
                lt.addLast(lista,element)
          
    sorted_list = merg.sort(lista,cmp_total_retenciones)
    lista = lt.newList("ARRAY_LIST")
    lt.addLast(lista,param)
    if lt.size(sorted_list) > 6:
        lista_anio = first_and_last3(sorted_list)
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])
    else:
        lista_anio = sorted_list
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])  
    return lista["elements"]

        
def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista = lt.newList("ARRAY_LIST")
    
    titulo = ["Año", "Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Costos y gastos nómina", "Total ingresos netos","Total costos y gastos",
             "Total saldo a pagar","Total saldo a favor"]
    lt.addLast(lista,titulo)
    
    highest = lt.firstElement(data_structs)
    for element in lt.iterator(data_structs):
        if element["Año"] != highest["Año"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in titulo:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
            highest = element   
        elif float(element["Costos y gastos nómina"]) > float(highest["Costos y gastos nómina"]):
            highest = element       
        elif element == lt.lastElement(data_structs):
            lista_aux = lt.newList("ARRAY_LIST")
            for i in titulo:
                lt.addLast(lista_aux,highest[i])
            lt.addLast(lista,lista_aux["elements"])
    lt.removeFirst(lista)
    tit= ["Año","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico",
          "Total de costos y gastos nómina del subsector económico","Total ingresos netos del subsector economico","Total costos y gastos del subsector económico",
          "Total saldo a pagar del subsector económico","Total saldo a favor del subsector económico"]
    lt.addFirst(lista,tit)
    
    anios = ["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
    lista_anios = lt.newList("ARRAY_LIST")
    for anio in anios:
        lista2 = lista_anio_req4(data_structs,anio)
        lt.addLast(lista_anios,lista2)
    return lista["elements"], lista_anios["elements"]

def lista_anio_req4(data_structs,anio):
    tit = ["Código actividad económica","Nombre actividad económica","Costos y gastos nómina",
              "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    lista = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        if element["Año"] == anio:
            lt.addLast(lista,element)
          
    sorted_list = merg.sort(lista,cmp_total_retenciones)
    lista = lt.newList("ARRAY_LIST")
    lt.addLast(lista,tit)
    if lt.size(sorted_list) > 6:
        lista_anio = first_and_last3(sorted_list)
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in tit:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])
    else:
        lista_anio = sorted_list
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in tit:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])  
    return lista["elements"]

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    param2 = ["Año","Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total ingresos netos","Total costos y gastos","Descuentos tributarios",
             "Total saldo a pagar","Total saldo a favor"]
                
    param3 = lt.newList('ARRAY_LIST')
    for i in param2:
        lt.addLast(param3,i)
        
    lst = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        l = lt.newList("ARRAY_LIST")
        for i in element.keys():
            if i in param2:
                lt.addLast(l,element[i])
        if lt.isEmpty(lst):
            lt.addLast(lst,l)
        elif not lt.isEmpty(lst):
            if lt.getElement(l,4) == lt.getElement(lt.lastElement(lst),4):
                Des = str(int(lt.getElement(lt.lastElement(lst),6))+int(lt.getElement(l,6)))
                ing = str(int(lt.getElement(lt.lastElement(lst),7))+int(lt.getElement(l,7)))
                cos_y_gas = str(int(lt.getElement(lt.lastElement(lst),8))+int(lt.getElement(l,8)))
                sal_a_pa = str(int(lt.getElement(lt.lastElement(lst),9))+int(lt.getElement(l,9)))
                sal_a_fa = str(int(lt.getElement(lt.lastElement(lst),10))+int(lt.getElement(l,10)))
                lt.changeInfo(lt.lastElement(lst),6,Des)
                lt.changeInfo(lt.lastElement(lst),7,ing)
                lt.changeInfo(lt.lastElement(lst),8,cos_y_gas)
                lt.changeInfo(lt.lastElement(lst),9,sal_a_pa)
                lt.changeInfo(lt.lastElement(lst),10,sal_a_fa)
            elif lt.getElement(l,4) != lt.getElement(lt.lastElement(lst),4):
                lt.addLast(lst,l)
                      
    lista_max = lt.newList("ARRAY_LIST")
    maximum = lt.firstElement(lst)
    for element in lt.iterator(lst):
        if element == lt.lastElement(lst):
            if float(lt.getElement(element,8)) > float(lt.getElement(maximum,8)):
                maximum = element
            lt.addLast(lista_max,maximum)
        elif lt.getElement(element,1) == lt.getElement(maximum,1):
            if float(lt.getElement(element,8)) > float(lt.getElement(maximum,8)):
                maximum = element
        elif not lt.getElement(element,1) == lt.getElement(maximum,1):
            lt.addLast(lista_max,maximum)
            maximum = element
    
    
    lt.addFirst(lista_max,param3)
    
    lista_tablas_anios = lt.newList("ARRAY_LIST")
    for i in lt.iterator(lista_max):
        if lt.getElement(i,1) != "Año":
            lista = lista_por_anio_req5(data_structs,lt.getElement(i,1),lt.getElement(i,4))
            lt.addLast(lista_tablas_anios,lista)
        
    return lista_max["elements"], lista_tablas_anios["elements"]
                
        
def lista_por_anio_req5(data_structs,anio,codigo_subsector):
    param = ["Código actividad económica","Nombre actividad económica","Descuentos tributarios",
              "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    lista = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        if element["Año"] == anio and element["Código subsector económico"] == codigo_subsector:
            lt.addLast(lista,element)
          
    sorted_list = merg.sort(lista,cmp_descuentos_tributarios)
    lista = lt.newList("ARRAY_LIST")
    lt.addLast(lista,param)
    if lt.size(sorted_list) > 6:
        lista_anio = first_and_last3(sorted_list)
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])
    else:
        lista_anio = sorted_list
        for x in lista_anio["elements"]:
            lista_aux = lt.newList("ARRAY_LIST")
            for i in param:
                lt.addLast(lista_aux,x[i])
            lt.addLast(lista,lista_aux["elements"])  
    return lista["elements"]



def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs,topN,anio_inicial,anio_final):
    """
    Función que soluciona el requerimiento 7
    """
     # TODO: Realizar el requerimiento 7
    #tomo los datos pertenecientes al rango de años
    lista = lt.newList("ARRAY_LIST")
    for element in lt.iterator(data_structs):
        if (int(element["Año"]) >= int(anio_inicial)) and (int(element["Año"])<= int(anio_final)):
            lt.addLast(lista,element)
    
    sorted_lista_min = merg.sort(lista,cmp_total_costos_gastos)  
    lista_min = lt.subList(sorted_lista_min,1,int(topN))
    
    lista_min = ins.sort(lista_min,cmp_impuestos_anio_total_costos_gastos)
    param = ["Año","Código actividad económica","Nombre actividad económica",
             "Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total ingresos netos","Total costos y gastos",
             "Total saldo a pagar","Total saldo a favor"]
    param2 = ["Año","Código actividad económica","Nombre actividad económica",
             "Código sector económico","Nombre sector económico","Código subsector económico",
             "Nombre subsector económico","Total ingresos netos consolidados para el periodo",
             "Total costos y gastos consolidados para el periodo",
             "Total saldo a pagar consolidados para el periodo",
             "Total saldo a favor consolidados para el periodo"]
    
    lista_min_tabulate = lt.newList("ARRAY_LIST")
    lt.addLast(lista_min_tabulate,param2)
    for element in lt.iterator(lista_min):
        lista_aux = lt.newList("ARRAY_LIST")
        for i in param:
            lt.addLast(lista_aux,element[i])
        lt.addLast(lista_min_tabulate,lista_aux["elements"])
        
    return lista_min_tabulate["elements"]


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

# Funciones de ordenamiento


def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2):
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2,
    en caso de que sean iguales tenga en cuenta el código de la actividad económica,
    de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el “Código actividad económica”
    impuesto2: información del segundo registro de impuestos que incluye el “Año” y el “Código actividad económica”
    """  
    if float(impuesto1["Año"]) == float(impuesto2['Año']):
        cod1 = impuesto1['Código actividad económica']
        cod2 = impuesto2['Código actividad económica']
        return float(cod1) <= float(cod2)
         
    else:
        return (float(impuesto1['Año']) < float(impuesto2['Año']))
    
def cmp_total_retenciones(impuesto1, impuesto2):
    return float(impuesto1["Total retenciones"]) < float(impuesto2["Total retenciones"])
        
def cmp_descuentos_tributarios(impuesto1, impuesto2):
    return float(impuesto1["Descuentos tributarios"]) < float(impuesto2["Descuentos tributarios"])

def cmp_total_costos_gastos(impuesto1, impuesto2):
    return float(impuesto1["Total costos y gastos"]) < float(impuesto2["Total costos y gastos"])

def cmp_impuestos_anio_total_costos_gastos(impuesto1, impuesto2):
    if float(impuesto1["Año"]) == float(impuesto2['Año']):
        cod1 = impuesto1['Total costos y gastos']
        cod2 = impuesto2['Total costos y gastos']
        return float(cod1) <= float(cod2)    
    else:
        return (float(impuesto1['Año']) > float(impuesto2['Año']))

def cmp_gastos_nomina(gasto_1, gasto_2):
    return float(gasto_1["Costos y gastos nómina"]) > float(gasto_2["Costos y gastos nómina"])   

def cmp_descuentos_tributarios(impuesto1, impuesto2):
    return float(impuesto1["Descuentos tributarios"]) < float(impuesto2["Descuentos tributarios"])
def sort(data_structs,sort_type):
    """
    Función encargada de ordenar la lista con los datos
    """
    size = data_size(data_structs)
    sort_criteria = cmp_impuestos_by_anio_CAE
    sub_list = lt.subList(data_structs["data"], 1, size)
    if sort_type == "SELECTION_SORT":
        sorted_list = se.sort(sub_list, sort_criteria)
        
    elif sort_type == "INSERTION_SORT":
        sorted_list = ins.sort(sub_list, sort_criteria) 
         
    elif sort_type == "SHELL_SORT":
        sorted_list = sa.sort(sub_list, sort_criteria)
    
    elif sort_type == "MERGE_SORT":
        sorted_list = merg.sort(sub_list, sort_criteria)
    elif sort_type == "QUICK_SORT":
        sorted_list = quk.sort(sub_list, sort_criteria)
        
    control = sorted_list
    return sorted_list

