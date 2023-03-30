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
import string
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


def new_data_structs(struc):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }
    
    data_structs["data"] = lt.newList(datastructure=struc,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], d)
    
    return data_structs


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
    for e in lt.iterator(data_structs["data"]):
        if int(e["id"]) == int(id):
            return e


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])

def purgar_codigo(codigos):
    cod_final = ""
    for numero in codigos:
        if numero in string.digits:
            cod_final += numero
        else:
            return cod_final

def req_1(catalog):
    """
    Función que soluciona el requerimiento 1
    """
    tamaño = lt.size(catalog["data"])
    año_inferior = int(lt.getElement(catalog["data"],1)["info"]["Año"])
    año_superior = int(lt.getElement(catalog["data"],tamaño)["info"]["Año"])
    
    quk.sort(catalog["data"], req1_sort_criteria)
    
    lista_final = lt.newList("ARRAY_LIST", año_sort_criteria)
    for año in range(año_inferior, año_superior+1):
        paso_año = False
        for elemento in lt.iterator(catalog["data"]):
            if int(elemento["info"]["Año"]) == año and not(paso_año):
                lt.addLast(lista_final, elemento["info"])
                paso_año = True  
    return(data_tabulate(filtro_al(lista_final["elements"])["elements"]))
    
def req_2(catalog):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    tamaño = lt.size(catalog["data"])
    año_inferior = int(lt.getElement(catalog["data"],1)["info"]["Año"])
    año_superior = int(lt.getElement(catalog["data"],tamaño)["info"]["Año"])
    
    quk.sort(catalog["data"], req2_sort_criteria)
    
    lista_final = lt.newList("ARRAY_LIST", año_sort_criteria)
    for año in range(año_inferior, año_superior+1):
        paso_año = False
        for elemento in lt.iterator(catalog["data"]):
            if int(elemento["info"]["Año"]) == año and not(paso_año):
                lt.addLast(lista_final, elemento["info"])
                paso_año = True  
    return(data_tabulate(filtro_al(lista_final["elements"])["elements"]))


def req_3(catalog):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista_final = req3_creacion_listas(catalog)
    lista_años = lt.newList("ARRAY_LIST")
    lista_todos = lt.newList("ARRAY_LIST")
    for tupla in lista_final:
        lt.addLast(lista_años, tupla[0])
        lt.addLast(lista_todos, tupla[1])
        
    headers1 = ["Año", 
               "Código Sector Economico", 
               "Nombre Sector Economico", 
               "Código Subsector Economico", 
               "Nombre Subector Economico",
               "Total de retenciones del subsector económico",
               "Total ingresos netos del subsector económico",
               "Total costos y gastos del subsector económico",
               "Total saldo a pagar del subsector economico",
               "Total Saldo a favor del subsector económico"]
    headers2 = ["Código Sector Economico", 
               "Nombre Sector Economico", 
               "Total retenciones",
               "Total ingresos netos",
               "Total costos y gastos",
               "Total saldo a pagar",
               "Total Saldo a favor"]
    
    return lista_años["elements"], lista_todos["elements"], headers1, headers2
    
def req3_creacion_listas(catalog):
    tamaño = lt.size(catalog["data"])
    año_previo = -1
    pos_inicial = 1
    año_final = lt.getElement(catalog["data"], tamaño)["info"]["Año"]
    lista_final = lt.newList("ARRAY_LIST")
    
    for i in range(1, tamaño + 1):
        año_actual = lt.getElement(catalog["data"], i)["info"]["Año"]   
        if año_actual != año_previo and año_previo != -1:
            lista_año = lt.subList(catalog["data"], pos_inicial, (i-pos_inicial))
            año_procesado = procesar_año(lista_año, año_previo)
            pos_inicial = i 
            año_previo = año_actual
            lt.addLast(lista_final, año_procesado) 
        
        elif año_actual == año_final:
            lista_año = lt.subList(catalog["data"], pos_inicial, (tamaño-pos_inicial)+1)
            año_procesado = procesar_año(lista_año, año_final)
            lt.addLast(lista_final, año_procesado)
            return lista_final["elements"]
        
        else:
            año_previo = año_actual

def procesar_año(list, año):
    quk.sort(list, req3_sort_criteria)
    
    retenciones_min = -1
    subsector_previo = subsector = int(lt.getElement(list, 1)["info"]["Código subsector económico"]) 
    subsector_min = s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = s_econom = nsu_econom = ns_econom = None
    retenciones_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
    retenciones = ingresos = costos_gastos = saldo_pagar = saldo_favor = 0 
    año_total = lt.newList("ARRAY_LIST")
    
    for elemento in lt.iterator(list):
        subsector = int(elemento["info"]["Código subsector económico"])     
        if subsector != subsector_previo:
            if retenciones_t < retenciones_min or retenciones_min == -1:
                
                #Guardar
                subsector_previo = subsector
                s_econom = s_econom_t
                ns_econom = ns_econom_t
                subsector_min = su_econom_t
                nsu_econom = nsu_econom_t
                retenciones_min = retenciones_t
                retenciones = retenciones_t
                ingresos = ingresos_t
                costos_gastos = costos_gastos_t
                saldo_favor = saldo_favor_t
                saldo_pagar = saldo_pagar_t
                
                #Reiniciar
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                retenciones_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
            
            #Si el valor es el ultimo
            s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
            retenciones_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
            
            retenciones_t += int(elemento["info"]["Total retenciones"])
            ingresos_t += int(elemento["info"]["Total ingresos netos"])
            costos_gastos_t += int(elemento["info"]["Total costos y gastos"])
            saldo_pagar_t += int(elemento["info"]["Total saldo a pagar"])
            saldo_favor_t += int(elemento["info"]["Total saldo a favor"])
            s_econom_t = elemento["info"]["Código sector económico"]
            su_econom_t = elemento["info"]["Código subsector económico"]
            ns_econom_t = elemento["info"]["Nombre sector económico"]
            nsu_econom_t = elemento["info"]["Nombre subsector económico"]
            
            if retenciones_t < retenciones_min:
                
                subsector_previo = subsector
                s_econom = s_econom_t
                ns_econom = ns_econom_t
                subsector_min = su_econom_t
                nsu_econom = nsu_econom_t
                retenciones_min = retenciones_t
                retenciones = retenciones_t
                ingresos = ingresos_t
                costos_gastos = costos_gastos_t
                saldo_favor = saldo_favor_t
                saldo_pagar = saldo_pagar_t
                
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                retenciones_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
                
            else:
                subsector_previo = subsector
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                retenciones_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
                
        
        retenciones_t += int(elemento["info"]["Total retenciones"])
        ingresos_t += int(elemento["info"]["Total ingresos netos"])
        costos_gastos_t += int(elemento["info"]["Total costos y gastos"])
        saldo_pagar_t += int(elemento["info"]["Total saldo a pagar"])
        saldo_favor_t += int(elemento["info"]["Total saldo a favor"])
        s_econom_t = elemento["info"]["Código sector económico"]
        su_econom_t = elemento["info"]["Código subsector económico"]
        ns_econom_t = elemento["info"]["Nombre sector económico"]
        nsu_econom_t = elemento["info"]["Nombre subsector económico"]     
    
    lt.addLast(año_total, año)
    lt.addLast(año_total, s_econom)
    lt.addLast(año_total, ns_econom)
    lt.addLast(año_total, subsector_min)
    lt.addLast(año_total, nsu_econom)           
    lt.addLast(año_total, retenciones)
    lt.addLast(año_total, ingresos) 
    lt.addLast(año_total, costos_gastos)
    lt.addLast(año_total, saldo_pagar)
    lt.addLast(año_total, saldo_favor)
               
    lista_resumen = lt.newList("ARRAY_LIST")
    
    for elemento in lt.iterator(list):
        if elemento["info"]["Código subsector económico"] == subsector_min:
            lt.addLast(lista_resumen, elemento) 
    
    
    return año_total["elements"], lista_resumen      

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    lista_final = req4_creacion_listas(data_structs)
    lista_años = lt.newList("ARRAY_LIST")
    lista_todos = lt.newList("ARRAY_LIST")
    for tupla in lista_final:
        lt.addLast(lista_años, tupla[0])
        lt.addLast(lista_todos, tupla[1])
        
    headers1 = ["Año", 
               "Código Sector Economico", 
               "Nombre Sector Economico", 
               "Código Subsector Economico", 
               "Nombre Subector Economico",
               "Total de costos y gastos nómina del subsector económico",
               "Total ingresos netos del subsector económico",
               "Total costos y gastos del subsector económico",
               "Total saldo por pagar del subsector economico",
               "Total saldo a favor del subsector económico"]
    headers2 = ["Código Sector Economico", 
               "Nombre Sector Economico", 
               "Total costos y gastos de nómina",
               "Total ingresos netos",
               "Total costos y gastos",
               "Total saldo por pagar",
               "Total saldo a favor"]
    
    return lista_años["elements"], lista_todos["elements"], headers1, headers2
    
def req4_creacion_listas(data_structs):
    tamaño = lt.size(data_structs["data"])
    año_previo = -1
    pos_inicial = 1
    año_final = lt.getElement(data_structs["data"], tamaño)["info"]["Año"]
    lista_final = lt.newList("ARRAY_LIST")
    
    for i in range(1, tamaño + 1):
        año_actual = lt.getElement(data_structs["data"], i)["info"]["Año"]   
        if año_actual != año_previo and año_previo != -1:
            lista_año = lt.subList(data_structs["data"], pos_inicial, (i-pos_inicial))
            año_procesado = procesar_año(lista_año, año_previo)
            pos_inicial = i 
            año_previo = año_actual
            lt.addLast(lista_final, año_procesado) 
        
        elif año_actual == año_final:
            lista_año = lt.subList(data_structs["data"], pos_inicial, (tamaño-pos_inicial)+1)
            año_procesado = procesar_año(lista_año, año_final)
            lt.addLast(lista_final, año_procesado)
            return lista_final["elements"]
        
        else:
            año_previo = año_actual

def procesar_año(list, año):
    merg.sort(list, req4_sort_criteria)
    
    costos_gastos_nom_max = 1
    subsector_previo = subsector = int(lt.getElement(list, 1)["info"]["Código subsector económico"]) 
    subsector_min = s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = s_econom = nsu_econom = ns_econom = None
    costos_gastos_nom_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
    costos_gastos_nom = ingresos = costos_gastos = saldo_pagar = saldo_favor = 0 
    año_total = lt.newList("ARRAY_LIST")
    
    for elemento in lt.iterator(list):
        subsector = int(elemento["info"]["Código subsector económico"])     
        if subsector != subsector_previo:
            if costos_gastos_nom_t > costos_gastos_nom_max or costos_gastos_nom_max == 1:
                
                #Guarda los valores de las variables
                subsector_previo = subsector
                s_econom = s_econom_t
                ns_econom = ns_econom_t
                subsector_min = su_econom_t
                nsu_econom = nsu_econom_t
                costos_gastos_nom_max = costos_gastos_nom_t
                costos_gastos_nom = costos_gastos_nom_t
                ingresos = ingresos_t
                costos_gastos = costos_gastos_t
                saldo_favor = saldo_favor_t
                saldo_pagar = saldo_pagar_t
                
                #Reinicia los valores de las variables
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                costos_gastos_nom_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
            
            #Si el valor es el ultimo
            s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
            costos_gastos_nom_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
            
            costos_gastos_nom_t += int(elemento["info"]["Costos y gastos nómina"])
            ingresos_t += int(elemento["info"]["Total ingresos netos"])
            costos_gastos_t += int(elemento["info"]["Total costos y gastos"])
            saldo_pagar_t += int(elemento["info"]["Total saldo a pagar"])
            saldo_favor_t += int(elemento["info"]["Total saldo a favor"])
            s_econom_t = elemento["info"]["Código sector económico"]
            su_econom_t = elemento["info"]["Código subsector económico"]
            ns_econom_t = elemento["info"]["Nombre sector económico"]
            nsu_econom_t = elemento["info"]["Nombre subsector económico"]
            
            if costos_gastos_nom_t > costos_gastos_nom_max:
                
                subsector_previo = subsector
                s_econom = s_econom_t
                ns_econom = ns_econom_t
                subsector_min = su_econom_t
                nsu_econom = nsu_econom_t
                costos_gastos_nom_max = costos_gastos_nom_t
                costos_gastos_nom = costos_gastos_nom_t
                ingresos = ingresos_t
                costos_gastos = costos_gastos_t
                saldo_favor = saldo_favor_t
                saldo_pagar = saldo_pagar_t
                
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                costos_gastos_nom_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
                
            else:
                subsector_previo = subsector
                s_econom_t = su_econom_t = nsu_econom_t = ns_econom_t = None
                costos_gastos_nom_t = ingresos_t = costos_gastos_t = saldo_pagar_t = saldo_favor_t = 0
                
        
        costos_gastos_nom_t += int(elemento["info"]["Costos y gastos nómina"])
        ingresos_t += int(elemento["info"]["Total ingresos netos"])
        costos_gastos_t += int(elemento["info"]["Total costos y gastos"])
        saldo_pagar_t += int(elemento["info"]["Total saldo a pagar"])
        saldo_favor_t += int(elemento["info"]["Total saldo a favor"])
        s_econom_t = elemento["info"]["Código sector económico"]
        su_econom_t = elemento["info"]["Código subsector económico"]
        ns_econom_t = elemento["info"]["Nombre sector económico"]
        nsu_econom_t = elemento["info"]["Nombre subsector económico"]     
    
    lt.addLast(año_total, año)
    lt.addLast(año_total, s_econom)
    lt.addLast(año_total, ns_econom)
    lt.addLast(año_total, subsector_min)
    lt.addLast(año_total, nsu_econom)           
    lt.addLast(año_total, costos_gastos_nom)
    lt.addLast(año_total, ingresos) 
    lt.addLast(año_total, costos_gastos)
    lt.addLast(año_total, saldo_pagar)
    lt.addLast(año_total, saldo_favor)
               
    lista_resumen = lt.newList("ARRAY_LIST")
    
    for elemento in lt.iterator(list):
        if elemento["info"]["Código subsector económico"] == subsector_min:
            lt.addLast(lista_resumen, elemento) 
    
    
    return año_total["elements"], lista_resumen


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    lista_main = agrupar_datos_req_5(data_structs["data"])
    for i in range(int(lt.size(lista_main))):
        # organiza el año 
        quk.sort(lista_main["elements"][i]["info"], req5_sort_criteria)
        # organiza las actividades para el mayor aporte descuentos de los subsectores
        quk.sort(lista_main["elements"][i]["info"]["elements"][0]["info"]["actividades_list"], req5_sort_criteria2)
    return lista_main
    

def agrupar_datos_req_5(data):
    """ 
    Función que agrupa los datos por año, subsector economico, total de descuentos tributarios de un subsector.
    """
    list_base = lt.newList("ARRAY_LIST")
    
    for e in lt.iterator(data):
        ie = e["info"]
        anios_listados = []
        for i in list_base["elements"]:
            anios_listados+=[i["id"]]
        if ie["Año"] in anios_listados:
            codigos_listados = []
            pos_a = anios_listados.index(ie["Año"])
            for i in list_base["elements"][pos_a]["info"]["elements"]:
                codigos_listados+=[i["info"]["Código sector económico"]]
            if ie["Código sector económico"] in codigos_listados:
                # Caso en que el año y sector economico ya se encuentren en la lista
                
                # añadimos a la lista de actividades para ese subsector, la actividad economica
                pos_c = codigos_listados.index(ie["Código sector económico"])
                list_actividades = list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["actividades_list"]
                dict_actividades_en_año = {"Código actividad económica": ie["Código actividad económica"],
                                       "Nombre actividad económica": ie["Nombre actividad económica"],
                                       "Total descuentos tributarios": int(ie["Descuentos tributarios"]),
                                       "Total ingresos netos": int(ie["Total ingresos netos"]),
                                       "Total costos y gastos": int(ie["Total costos y gastos"]),
                                       "Total saldo a pagar": int(ie["Total saldo a pagar"]),
                                       "Total saldo a favor": int(ie["Total saldo a favor"])}
                lt.addLast(list_actividades,{"id": e["id"], "info": dict_actividades_en_año})
                
                # se actualiza los valores del subsector economico para dicho año
                list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["Total de descuentos tributarios del subsector económico"] += int(ie["Descuentos tributarios"])
                list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["Total ingresos netos del subsector económico"] += int(ie["Total ingresos netos"])
                list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["Total costos y gastos del subsector económico"] += int(ie["Total costos y gastos"])
                list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["Total saldo a pagar del subsector económico"] += int(ie["Total saldo a pagar"])
                list_base["elements"][pos_a]["info"]["elements"][pos_c]["info"]["Total saldo a favor del subsector económico"] += int(ie["Total saldo a favor"])
            else:
                # Caso en que solo el año se encuentre en la lista pero no el sector economico
                list_totales_o = list_base["elements"][pos_a]["info"]
                list_actividades = lt.newList("ARRAY_LIST")
                dict_actividades_en_año = {"Código actividad económica": ie["Código actividad económica"],
                                       "Nombre actividad económica": ie["Nombre actividad económica"],
                                       "Total descuentos tributarios": int(ie["Descuentos tributarios"]),
                                       "Total ingresos netos": int(ie["Total ingresos netos"]),
                                       "Total costos y gastos": int(ie["Total costos y gastos"]),
                                       "Total saldo a pagar": int(ie["Total saldo a pagar"]),
                                       "Total saldo a favor": int(ie["Total saldo a favor"])}
                lt.addLast(list_actividades,{"id": e["id"], "info": dict_actividades_en_año})
                
                dict_base = {"Año": ie["Año"],
                         "Código sector económico": ie["Código sector económico"],
                         "Nombre sector económico": ie["Nombre sector económico"],
                         "Código subsector económico": ie["Código subsector económico"],
                         "Nombre subsector económico": ie["Nombre subsector económico"],
                         "Total de descuentos tributarios del subsector económico": int(ie["Descuentos tributarios"]),
                         "Total ingresos netos del subsector económico": int(ie["Total ingresos netos"]),
                         "Total costos y gastos del subsector económico": int(ie["Total costos y gastos"]),
                         "Total saldo a pagar del subsector económico": int(ie["Total saldo a pagar"]),
                         "Total saldo a favor del subsector económico": int(ie["Total saldo a favor"]),
                         "actividades_list": list_actividades}
                codigo_eco = ie["Código sector económico"] 
                id = (int(ie["Año"])*10000)+int(codigo_eco)
                lt.addLast(list_totales_o,{"id": id,"info": dict_base})
                
        else:
            # Caso en el que ni el año ni el sector economico se encuentran en la lista
            list_actividades = lt.newList("ARRAY_LIST")
            dict_actividades_en_año = {"Código actividad económica": ie["Código actividad económica"],
                                       "Nombre actividad económica": ie["Nombre actividad económica"],
                                       "Total descuentos tributarios": int(ie["Descuentos tributarios"]),
                                       "Total ingresos netos": int(ie["Total ingresos netos"]),
                                       "Total costos y gastos": int(ie["Total costos y gastos"]),
                                       "Total saldo a pagar": int(ie["Total saldo a pagar"]),
                                       "Total saldo a favor": int(ie["Total saldo a favor"])}
            lt.addLast(list_actividades,{"id": e["id"], "info": dict_actividades_en_año})
            
            list_totales = lt.newList("ARRAY_LIST")
            dict_base = {"Año": ie["Año"],
                         "Código sector económico": ie["Código sector económico"],
                         "Nombre sector económico": ie["Nombre sector económico"],
                         "Código subsector económico": ie["Código subsector económico"],
                         "Nombre subsector económico": ie["Nombre subsector económico"],
                         "Total de descuentos tributarios del subsector económico": int(ie["Descuentos tributarios"]),
                         "Total ingresos netos del subsector económico": int(ie["Total ingresos netos"]),
                         "Total costos y gastos del subsector económico": int(ie["Total costos y gastos"]),
                         "Total saldo a pagar del subsector económico": int(ie["Total saldo a pagar"]),
                         "Total saldo a favor del subsector económico": int(ie["Total saldo a favor"]),
                         "actividades_list": list_actividades}
            codigo_eco = ie["Código sector económico"] 
            id = (int(ie["Año"])*10000)+int(codigo_eco)
            lt.addLast(list_totales,{"id": id,"info": dict_base})
            lt.addLast(list_base,{"id": ie["Año"], "info": list_totales})
    return list_base

def req_6(data_structs,anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    lista_main = agrupar_datos_req_6(data_structs,anio)
    quk.sort(lista_main,req6_sort_criteriaM)
    for s in lista_main["elements"]:
        quk.sort(s["info"]["subsectores_list"],req6_sort_criteria)
        quk.sort(s["info"]["subsectores_list"]["elements"][0]["info"]["actividad_list"],req6_sort_criteria2)
        quk.sort(s["info"]["subsectores_list"]["elements"][-1]["info"]["actividad_list"],req6_sort_criteria2)
    return lista_main

def agrupar_datos_req_6(data,anio):
    """ 
    Función que agrupa los datos por para el requerimiento 6.
    """
    list_filtrada = lt.newList("ARRAY_LIST")
    #filtro para quitar años no deseados a analizar
    for d in lt.iterator(data["data"]):
        if int(d["info"]["Año"]) == int(anio):
            lt.addLast(list_filtrada,d)
    
    list_base = lt.newList("ARRAY_LIST")
    
    for e in lt.iterator(list_filtrada):
        ie = e["info"]
        sector_listado = []
        for i in list_base["elements"]:
            sector_listado+=[i["id"]]
        if int(ie["Código sector económico"]) in sector_listado:
            subsectores_listado = []
            pos_a = sector_listado.index(int(ie["Código sector económico"]))
            for i in list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"]:
                subsectores_listado += [i["id"]]
            if int(ie["Código subsector económico"]) in subsectores_listado:
                # Caso en que el sector y subsector economico ya se encuentren en la lista
                
                # añadimos a la lista de actividades para ese subsector, la actividad economica
                pos_c = subsectores_listado.index(int(ie["Código subsector económico"]))
                list_actividad = list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"][pos_c]["info"]["actividad_list"]
                dict_actividad = {"Código actividad económica": ie["Código actividad económica"],
                                  "Nombre actividad económica": ie["Nombre actividad económica"],
                                  "Total ingresos netos": ie["Total ingresos netos"],
                                  "Total costos y gastos": ie["Total costos y gastos"],
                                  "Total saldo a pagar": ie["Total saldo a pagar"],
                                  "Total saldo a favor": ie["Total saldo a favor"]}
                lt.addLast(list_actividad,{"id": e["id"], "info": dict_actividad})
                
                # se actualiza los valores del subsector
                list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"][pos_c]["info"]["Total ingresos netos del subsector económico"] += int(ie["Total ingresos netos"])
                list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"][pos_c]["info"]["Total costos y gastos del subsector económico"] += int(ie["Total costos y gastos"])
                list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"][pos_c]["info"]["Total saldo a pagar del subsector económico"] += int(ie["Total saldo a pagar"])
                list_base["elements"][pos_a]["info"]["subsectores_list"]["elements"][pos_c]["info"]["Total saldo a favor del subsector económico"] += int(ie["Total saldo a favor"])
                
                # se actualiza los valores del sector economico 
                list_base["elements"][pos_a]["info"]["Total ingresos netos del sector económico"] += int(ie["Total ingresos netos"])
                list_base["elements"][pos_a]["info"]["Total costos y gastos del sector económico"] += int(ie["Total costos y gastos"])
                list_base["elements"][pos_a]["info"]["Total saldo a pagar del sector económico"] += int(ie["Total saldo a pagar"])
                list_base["elements"][pos_a]["info"]["Total saldo a favor del sector económico"] += int(ie["Total saldo a favor"])
                
            else:
                # Caso en que solo el sector se encuentre en la lista pero no el subsector economico
                
                codigo_subeco = ie["Código subsector económico"] 
                idsub = int(codigo_subeco)
                
                list_totales_o = list_base["elements"][pos_a]["info"]["subsectores_list"]
                list_actividad = lt.newList("ARRAY_LIST")
                dict_actividad = {"Código actividad económica": ie["Código actividad económica"],
                                  "Nombre actividad económica": ie["Nombre actividad económica"],
                                  "Total ingresos netos": ie["Total ingresos netos"],
                                  "Total costos y gastos": ie["Total costos y gastos"],
                                  "Total saldo a pagar": ie["Total saldo a pagar"],
                                  "Total saldo a favor": ie["Total saldo a favor"]}
                lt.addLast(list_actividad,{"id": e["id"], "info": dict_actividad})
                
                dict_subsector = {"Código subsector económico": ie["Código subsector económico"],
                                  "Nombre subsector económico": ie["Nombre subsector económico"],
                                  "Total ingresos netos del subsector económico": int(ie["Total ingresos netos"]),
                                  "Total costos y gastos del subsector económico": int(ie["Total costos y gastos"]),
                                  "Total saldo a pagar del subsector económico": int(ie["Total saldo a pagar"]),
                                  "Total saldo a favor del subsector económico": int(ie["Total saldo a favor"]),
                                  "Actividad económica que más aporto":0,
                                  "Actividad económica que menos aporto":0,
                                  "actividad_list": list_actividad}
                
                lt.addLast(list_totales_o,{"id": idsub,"info": dict_subsector})
                
                # se actualizan los valores del sector economico
                list_base["elements"][pos_a]["info"]["Total ingresos netos del sector económico"] += int(ie["Total ingresos netos"])
                list_base["elements"][pos_a]["info"]["Total costos y gastos del sector económico"] += int(ie["Total costos y gastos"])
                list_base["elements"][pos_a]["info"]["Total saldo a pagar del sector económico"] += int(ie["Total saldo a pagar"])
                list_base["elements"][pos_a]["info"]["Total saldo a favor del sector económico"] += int(ie["Total saldo a favor"])
                
        else:
            # Caso en el que ni el sector ni el subsector economico se encuentran en la list
            
            # limpiamos los codigos de subsector y sector economico
            codigo_eco = ie["Código sector económico"] 
            id = int(codigo_eco)
            codigo_subeco = ie["Código subsector económico"] 
            idsub = int(codigo_subeco)
            
            list_actividad = lt.newList("ARRAY_LIST")
            
            dict_actividad = {"Código actividad económica": ie["Código actividad económica"],
                              "Nombre actividad económica": ie["Nombre actividad económica"],
                              "Total ingresos netos": ie["Total ingresos netos"],
                              "Total costos y gastos": ie["Total costos y gastos"],
                              "Total saldo a pagar": ie["Total saldo a pagar"],
                              "Total saldo a favor": ie["Total saldo a favor"]}
            lt.addLast(list_actividad,{"id": e["id"], "info": dict_actividad})
            
            list_subsector = lt.newList("ARRAY_LIST")
            dict_subsector = {"Código subsector económico": ie["Código subsector económico"],
                              "Nombre subsector económico": ie["Nombre subsector económico"],
                              "Total ingresos netos del subsector económico": int(ie["Total ingresos netos"]),
                              "Total costos y gastos del subsector económico": int(ie["Total costos y gastos"]),
                              "Total saldo a pagar del subsector económico": int(ie["Total saldo a pagar"]),
                              "Total saldo a favor del subsector económico": int(ie["Total saldo a favor"]),
                              "Actividad económica que más aporto":0,
                              "Actividad económica que menos aporto":0,
                              "actividad_list": list_actividad}
            lt.addLast(list_subsector,{"id": idsub, "info": dict_subsector})

            dict_base = {"Código sector económico": ie["Código sector económico"],
                         "Nombre sector económico": ie["Nombre sector económico"],
                         "Total ingresos netos del sector económico": int(ie["Total ingresos netos"]),
                         "Total costos y gastos del sector económico": int(ie["Total costos y gastos"]),
                         "Total saldo a pagar del sector económico": int(ie["Total saldo a pagar"]),
                         "Total saldo a favor del sector económico": int(ie["Total saldo a favor"]),
                         "Subsector económico que mas aporto":0,
                         "Subsector económico que menos aporto":0,
                         "subsectores_list": list_subsector}
            
            lt.addLast(list_base,{"id": id, "info": dict_base})
    return list_base

def req_7(data_structs,n,bi,bs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7 
    list_main = agrupar_datos_req_7(data_structs,bi,bs)
    # se ordena de menor a mayor
    quk.sort(list_main,req7_sort_criteria)
    list_final = lt.newList("ARRAY_LIST")
    counter = 0
    while counter < n:
        lt.addLast(list_final,list_main["elements"][counter])
        counter += 1
    merg.sort(list_final,req7_sort_criteria2)
    # ciclo para crear lista de diccionarios que se pueda mostrar en tabulate
    list_tab = []
    counter = 0
    while counter < n:
        e = list_final["elements"][counter]["info"]
        dict_actividad_economica = {"Año": e["Año"],
                                    "Código actividad económica": e["Código actividad económica"],
                                    "Nombre actividad económica": e["Nombre actividad económica"],
                                    "Código sector económico": e["Código sector económico"],
                                    "Nombre sector económico": e["Nombre sector económico"],
                                    "Código subsector económico": e["Código subsector económico"],
                                    "Nombre subsector económico": e["Nombre subsector económico"],
                                    "Total ingresos netos consolidados para el periodo": e["Total ingresos netos"],
                                    "Total costos y gastos consolidados para el periodo":e["Total costos y gastos"],
                                    "Total saldo a pagar consolidados para el periodo":e["Total saldo a pagar"],
                                    "Total saldo a favor consolidados para el periodo":e["Total saldo a favor"]}
        list_tab += [dict_actividad_economica]
        counter += 1
    return list_tab
            

def agrupar_datos_req_7(data,bi,bs):
    """
    Función que agrupa datos por menor costo y gasto total, dependiendo del periodo en años asignado
    """
    list_base = lt.newList("ARRAY_LIST")
    #filtro para quitar años no deseados a analizar
    for d in lt.iterator(data["data"]):
        if int(d["info"]["Año"]) in range(bi,bs+1):
            lt.addLast(list_base,d)
    return list_base


def req_8(data_structs,bi,bs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    list_base = lt.newList("ARRAY_LIST")
    #filtro para quitar años no deseados a analizar
    for d in lt.iterator(data_structs["data"]):
        if int(d["info"]["Año"]) in range(bi,bs+1):
            lt.addLast(list_base,d)
    lista_main = agrupar_datos_req_8(list_base)
    # organiza alfabeticamente por subsector economico
    quk.sort(lista_main,req8_sort_criteria)
    for i in range(int(lista_main["size"])):
        # organiza las actividades por 'Total Impuesto a cargo' 
        quk.sort(lista_main["elements"][i]["info"]["list_actividades_sub"], req8_sort_criteria2)
    return lista_main

def agrupar_datos_req_8(data):
    """ 
    Función que agrupa los datos por sector y subsector economico, total de descuentos tributarios de un subsector.
    """
    list_base = lt.newList("ARRAY_LIST")
    
    for e in lt.iterator(data):
        ie = e["info"]
        codigo_eco = ie["Código sector económico"] 
        codigo_eco_sub = ie["Código subsector económico"]
        # creacion de un id unico para dicho sector y su subsector
        eid = (int(codigo_eco)*10000)+int(codigo_eco_sub)
        sectores_listados = []
        for i in list_base["elements"]:
            sectores_listados += [i["id"]]
        if eid in sectores_listados:
            # Caso en que el sector y subsector economica ya estan en la lista
            pos_c = sectores_listados.index(eid)
            list_actividades_sub = list_base["elements"][pos_c]["info"]["list_actividades_sub"]
            dict_actividad_sub = {"Código actividad económica": ie["Código actividad económica"],
                                       "Nombre actividad económica": ie["Nombre actividad económica"],
                                       "Total Impuesto a cargo": int(ie["Total Impuesto a cargo"]),
                                       "Total ingresos netos": int(ie["Total ingresos netos"]),
                                       "Total costos y gastos": int(ie["Total costos y gastos"]),
                                       "Total saldo a pagar": int(ie["Total saldo a pagar"]),
                                       "Total saldo a favor": int(ie["Total saldo a favor"])}
            lt.addLast(list_actividades_sub,{"id": e["id"], "info": dict_actividad_sub})
            
            # se actualizan los valores para dicho subsector 
            list_base["elements"][pos_c]["info"]["Total de impuestos a cargo para el subsector"] += int(ie["Total Impuesto a cargo"])
            list_base["elements"][pos_c]["info"]["Total ingresos netos para el subsector"] += int(ie["Total ingresos netos"])
            list_base["elements"][pos_c]["info"]["Total costos y gastos para el subsector"] += int(ie["Total costos y gastos"])
            list_base["elements"][pos_c]["info"]["Total saldo a pagar para el subsector"] += int(ie["Total saldo a pagar"])
            list_base["elements"][pos_c]["info"]["Total saldo a favor para el subsector"] += int(ie["Total saldo a favor"])
        else:
            # Caso en que no este el sector y el subsector economico en la lista
            list_actividades_sub = lt.newList("ARRAY_LIST")
            dict_actividad_sub = {"Código actividad económica": ie["Código actividad económica"],
                                  "Nombre actividad económica": ie["Nombre actividad económica"],
                                  "Total Impuesto a cargo": int(ie["Total Impuesto a cargo"]),
                                  "Total ingresos netos": int(ie["Total ingresos netos"]),
                                  "Total costos y gastos": int(ie["Total costos y gastos"]),
                                  "Total saldo a pagar": int(ie["Total saldo a pagar"]),
                                  "Total saldo a favor": int(ie["Total saldo a favor"])}
            lt.addLast(list_actividades_sub,{"id": e["id"], "info": dict_actividad_sub})
            
            dict_base = {"Código sector económico": ie["Código sector económico"],
                         "Nombre sector económico": ie["Nombre sector económico"],
                         "Código subsector económico": ie["Código subsector económico"],
                         "Nombre subsector económico": ie["Nombre subsector económico"],
                         "Total de impuestos a cargo para el subsector": int(ie["Total Impuesto a cargo"]),
                         "Total ingresos netos para el subsector": int(ie["Total ingresos netos"]),
                         "Total costos y gastos para el subsector": int(ie["Total costos y gastos"]),
                         "Total saldo a pagar para el subsector": int(ie["Total saldo a pagar"]),
                         "Total saldo a favor para el subsector": int(ie["Total saldo a favor"]),
                         "list_actividades_sub": list_actividades_sub}
            lt.addLast(list_base,{"id": eid, "info":dict_base})
    return list_base

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
def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    if data_1["info"]["Año"] < data_2["info"]["Año"]:
        return True
    elif data_1["info"]["Año"] > data_2["info"]["Año"]:
        return False
    else:
        if int(data_1["info"]["Código actividad económica"]) < int(data_2["info"]["Código actividad económica"]):
            return True
        elif int(data_1["info"]["Código actividad económica"]) > int(data_2["info"]["Código actividad económica"]):
            return False

def año_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    if int(data_1["info"]["Año"]) < int(data_2["info"]["Año"]):
        return True
    else:
        return False
       
def req1_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    if int(data_1["info"]["Total saldo a pagar"]) < int(data_2["info"]["Total saldo a pagar"]):
        return False
    else:
        return True
    
def req2_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    if int(data_1["info"]["Total saldo a favor"]) < int(data_2["info"]["Total saldo a favor"]):
        return False
    else:
        return True

def req3_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    if int(data_1["info"]["Código subsector económico"]) < int(data_2["info"]["Código subsector económico"]):
        return True
    elif int(data_1["info"]["Código subsector económico"]) > int(data_2["info"]["Código subsector económico"]):
        return False
    else:
        if int(data_1["info"]["Total retenciones"]) < int(data_2["info"]["Total retenciones"]):
            return True
        elif int(data_1["info"]["Total retenciones"]) > int(data_2["info"]["Total retenciones"]):
            return False
        
def req4_sort_criteria(data_1, data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 4, compara por 'Código subsector económico' y 'Costos y gastos nómina'
    """
    if int(data_1["info"]["Código subsector económico"]) < int(data_2["info"]["Código subsector económico"]):
        return True
    elif int(data_1["info"]["Código subsector económico"]) > int(data_2["info"]["Código subsector económico"]):
        return False
    else:
        if int(data_1["info"]["Costos y gastos nómina"]) < int(data_2["info"]["Costos y gastos nómina"]):
            return True
        elif int(data_1["info"]["Costos y gastos nómina"]) > int(data_2["info"]["Costos y gastos nómina"]):
            return False

def req5_sort_criteria(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 5, compara por 'Año', 'Código subsector económico', 'Descuentos tributarios totales'
    """
    if int(data_1["info"]["Total de descuentos tributarios del subsector económico"]) > int(data_2["info"]["Total de descuentos tributarios del subsector económico"]):
        return True
    else:
        return False

def req5_sort_criteria2(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 5, comparacion para 'Año' individual
    """
    if int(data_1["info"]["Total descuentos tributarios"]) > int(data_2["info"]["Total descuentos tributarios"]):
        return True
    else:
        return False

def req6_sort_criteriaM(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 6, comparacion para codigo sector economico
    """
    if int(data_1["info"]["Código sector económico"]) < int(data_2["info"]["Código sector económico"]):
        return True
    else:
        return False

def req6_sort_criteria(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 6, comparacion para subsector economico por aporte
    """
    if int(data_1["info"]["Total ingresos netos del subsector económico"]) > int(data_2["info"]["Total ingresos netos del subsector económico"]):
        return True
    else:
        return False

def req6_sort_criteria2(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 6, comparacion para actividad economica
    """
    if int(data_1["info"]["Total ingresos netos"]) > int(data_2["info"]["Total ingresos netos"]):
        return True
    else:
        return False

def req7_sort_criteria(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 7, comparacion para 'Total costos y gastos'
    """
    if int(data_1["info"]["Total costos y gastos"]) < int(data_2["info"]["Total costos y gastos"]):
        return True
    else:
        return False

def req7_sort_criteria2(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 7, comparacion para 'Año'
    """
    if int(data_1["info"]["Año"]) > int(data_2["info"]["Año"]):
        return True
    else:
        return False

def req8_sort_criteria(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 8, compara por el nombre del subsector economico alfabeticamente
    """
    if data_1["info"]["Nombre subsector económico"] < data_2["info"]["Nombre subsector económico"]:
        return True
    else:
        return False

def req8_sort_criteria2(data_1,data_2):
    """
    sortCriteria criterio de ordenamiento para el requerimiento 8, compara por 'Año', 'Código subsector económico', 'Total Impuesto a cargo'
    """
    if int(data_1["info"]["Total Impuesto a cargo"]) > int(data_2["info"]["Total Impuesto a cargo"]):
        return True
    else:
        return False

def sort(data_structs, alg):
    """
    Función encargada de ordenar la lista con los datos
    """
    if alg == "Selection":
        se.sort(data_structs["data"], sort_criteria)
    elif alg == "Insertion":
        ins.sort(data_structs["data"], sort_criteria)
    elif alg == "Shell":
        sa.sort(data_structs["data"], sort_criteria)
    elif alg == "Merge":
        merg.sort(data_structs["data"], sort_criteria)
    elif alg == "Quick":
        quk.sort(data_structs["data"], sort_criteria)

def data_carga_resumen(catalog):
    tipo = catalog["data"]["type"]
    if tipo == "ARRAY_LIST":
        datos = catalog["data"]["elements"]
        data_carga = [
            filtro_dict(datos[0]["info"]),
            filtro_dict(datos[1]["info"]),
            filtro_dict(datos[2]["info"]),
            filtro_dict(datos[-3]["info"]),
            filtro_dict(datos[-2]["info"]),
            filtro_dict(datos[-1]["info"])]
    elif tipo == "SINGLE_LINKED": 
        tamaño = lt.size(catalog["data"])
        data_carga = [
        filtro_dict((lt.getElement(catalog["data"],1))["info"]),
        filtro_dict((lt.getElement(catalog["data"],2))["info"]),
        filtro_dict((lt.getElement(catalog["data"],3))["info"]),
        filtro_dict((lt.getElement(catalog["data"],tamaño-2))["info"]),
        filtro_dict((lt.getElement(catalog["data"],tamaño-1))["info"]),
        filtro_dict((lt.getElement(catalog["data"],tamaño))["info"])
        ]   
    return data_carga


def data_tabulate(ldic):
    filas = []
    headers = ["Año", "Código actividad económica","Nombre actividad económica", 'Código sector económico','Nombre sector económico','Código subector económico','Nombre subsector económico','Total ingresos netos','Total costos y gastos','Total saldo a pagar','Total saldo a favor']
    for fila in ldic:
        temp = []
        for dato in fila.values():
            temp.append(dato)
        filas.append(temp)
    return filas, headers

def filtro_al(list):
    data_resumen = lt.newList("ARRAY_LIST")
    for dato in list:
        lt.addLast(data_resumen, filtro_dict(dato))
    return data_resumen

def filtro_dict(d):
    llave = ["Año", "Código actividad económica", "Nombre actividad económica", 
            "Código sector económico", "Nombre sector económico", "Código subsector económico", 
            "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", 
            "Total saldo a pagar", "Total saldo a favor"]
    newDict = {}
    k = d.keys()
    for u in k:
        if u in llave:
            newDict[u] = d[u]
    return 
