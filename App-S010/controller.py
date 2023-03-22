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
 """

import config as cf
import model
import time
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

csv.field_size_limit(2147483647)


def new_controller(list_type:int):
    """
    Crea una instancia del modelo
    
    list_type: Numero entero para identificar el tipo de lista a usar
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(list_type)
    return control


# Funciones para la carga de datos

def load_data(control, pct):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    archivo = "Data\Salida_agregados_renta_juridicos_AG-{0}.csv"
    filename = ""
    if pct == 1:
        filename = archivo.format("small")
    elif pct == 2:
        filename = archivo.format("5pct")
    elif pct == 3:
        filename = archivo.format("10pct")
    elif pct == 4:
        filename = archivo.format("20pct")
    elif pct == 5:
        filename = archivo.format("30pct")
    elif pct == 6:
        filename = archivo.format("50pct")
    elif pct == 7:
        filename = archivo.format("80pct")
    elif pct == 8:
        filename = archivo.format("large")
    data = control["model"]
    with open(filename, "r", encoding = "utf-8") as info:
        datos = csv.DictReader(info)
        
        for i in datos:
            data["data"] = model.add_data(data["data"], i)
        control["model"] = data
    
    return control["model"]["data"]


# Funciones de ordenamiento

def sort(control,type_sort:int):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    sorted_list = model.sort(control,type_sort)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, sorted_list


# Funciones de consulta sobre el catálogo
def conseguir_datos(sorted_list,control, cantidad:int, sentido):
    """
    Agarra x cantidad de datos segun parametro y sentido, adelante hacia atras o atras hacia adelante

    """
    
    
    if sentido == "ambos":
        respuesta1 = model.data_by_quantity(sorted_list, control, cantidad, "adelante")
        respuesta2 = model.data_by_quantity(sorted_list, control, cantidad, "atras")
        rta = model.join_lists(respuesta1, respuesta2)
    else:
        rta = model.data_by_quantity(sorted_list, control, cantidad, sentido)
        
    return rta
        
            

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def listas_aspecto(control, aspecto):
    """
    Retorna una tupla de arraylist segun un aspecto, la primera lista esta conformada
    por los datos que se utilizaron para organizar, la segunda por los elementos con ese dato
    """
    aspectos, elementos = model.lista_by_aspecto(control, aspecto)
    return aspectos, elementos
    
# Funciones que s0lucionan el Requerimiento 1

def organizar_actividades_por_saldo_a_pagar(data):
    
    año, elements = listas_aspecto(data, "Año")
    a = model.data_size(año)
    x = []
    for i in range(1, a+1):
        year = model.get_data_by_pos(elements["data"], i)
        data = model.actividades_por_saldo(year)
        x.append(data)
    
    return x


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2 = model.req_2(control["model"])
    return req_2

# Funciones que solucionan el Requerimiento 3


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    año, elementos = listas_aspecto(control, "Año")
    size = model.data_size(año)
    respuesta1 = new_controller(2)
    respuesta2 = new_controller(2)
    for i in range(1, size+1):
        data = model.get_data_by_pos(elementos["data"], i)
        x, y = model.subsector_menor_retenciones(data)
        respuesta1["model"]["data"] = model.add_data(respuesta1["model"]["data"], x)
        respuesta2["model"]["data"] = model.add_data(respuesta2["model"]["data"], y)
    
    return respuesta1["model"]["data"]["elements"], respuesta2["model"]["data"]["elements"]

def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    año, elementos = listas_aspecto(control, "Año")
    size = model.data_size(año)
    respuesta1 = new_controller(2)
    respuesta2 = new_controller(2)
    for i in range(1, size+1):
        data = model.get_data_by_pos(elementos["data"], i)
        x, y = model.calculos_subsector_req_5(data)
        respuesta1["model"]["data"] = model.add_data(respuesta1["model"]["data"], x)
        respuesta2["model"]["data"] = model.add_data(respuesta2["model"]["data"], y)
    
    return respuesta1["model"]["data"]["elements"], respuesta2["model"]["data"]["elements"]
        


def req_6(control, año):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    respuesta = new_controller(2)
    respuesta2 = new_controller(2)
    respuesta3 = new_controller(2)
    años, data = listas_aspecto(control["model"]["data"], "Año")
    a = model.present(años["data"], año)
    info = model.get_data_by_pos(data["data"], a)
    sector, data2 = listas_aspecto(info["data"], "Código sector económico")
    size = model.data_size(sector)
    for i in range(1, size + 1):
        element = model.get_data_by_pos(data2["data"], i)
        sectorx, subsectors1, subsectors2 = model.req_6(element)
        respuesta["model"]["data"] = model.add_data(respuesta["model"]["data"], sectorx)
        respuesta2["model"]["data"] = model.add_data(respuesta2["model"]["data"], subsectors1)
        respuesta3["model"]["data"] = model.add_data(respuesta3["model"]["data"], subsectors2)
    
    elected = model.pick_first_sector(respuesta["model"])
    elected2 = new_controller(2)
    elected3 = new_controller(2)
    size2 = model.data_size(elected)
    for i in range(1, size2+1):
        x = model.get_data_by_pos(elected["data"], i)
        codigo = x["Código sector económico"]
        present = model.present(sector["data"], codigo)
        y = model.get_data_by_pos(respuesta2["model"]["data"], present)
        z = model.get_data_by_pos(respuesta3["model"]["data"], present)
        elected2["model"]["data"] = model.add_data(elected2["model"]["data"], y)
        elected3["model"]["data"] = model.add_data(elected3["model"]["data"], z)
    
    j = elected["data"]["elements"]
    k = elected2["model"]["data"]["elements"]
    l = elected3["model"]["data"]["elements"]
    
    return j, k, l


def req_7(control, añoi, añof, cantidad):
    """
    Retorna el resultado del requerimiento 7
    """
    i = int(añoi)
    años = new_controller(2)
    while i <= int(añof):
        años["model"]["data"] = model.add_data(años["model"]["data"], i)
        i += 1
    
    respuesta = model.req_7(control, años["model"], cantidad)
        
    
    req_7 = model.req_7(control, años["model"], cantidad)
    return req_7["data"]["elements"]


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
