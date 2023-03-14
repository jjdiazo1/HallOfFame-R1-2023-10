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
from csv import reader
from DISClib.ADT import list as lt
import os

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(data_type, cmpfunction=model.compare):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(data_type, cmpfunction)
    return control


# Funciones para la carga de datos

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    data_struct = control['model']
    data_file = cf.data_dir + filename
    input_file = csv.DictReader(open(data_file, encoding="utf-8"))
    id=0
    for info in input_file:
        model.add_data(data_struct, info, id)
        id+=1
    size = model.data_size(data_struct) 
    model.ordenar_carga_de_datos(data_struct)   
    req1 = model.organizar_por_año(data_struct, size, True)
    req2 = model.organizar_por_año(data_struct, size, True)
    req3 = model.organizar_por_año(data_struct, size, True)
    req4 = model.organizar_por_año(data_struct, size, False)
    req5 = model.organizar_por_año(data_struct, size, False)
    req6 = model.organizar_por_año(data_struct, size, True)
    req7 = model.organizar_por_año(data_struct, size, False)
    req8 = model.organizar_por_año(data_struct, size, True)
    
    control['req1'] = req1
    control['req2'] = req2
    control['req3'] = req3
    control['req4'] = req4
    control['req5'] = req5
    control['req6'] = req6
    control['req7'] = req7
    control['req8'] = req8
    

    return size

def datos_filtrados(data_struct, size, llaves_a_incluir):
    list_values_info = model.datos_filtrados(data_struct, size, llaves_a_incluir)
    return list_values_info

""" 
control = new_controller('ARRAY_LIST')
llaves_a_incluir = ["Año", "Código actividad económica", "Nombre actividad económica", 
                    "Código sector económico", "Nombre sector económico", "Código subsector económico", 
                    "Nombre subsector económico","Total ingresos netos", "Total costos y gastos", 
                    "Total saldo a pagar", "Total saldo a favor"]
filename = "Salida_agregados_renta_juridicos_AG-small.csv"
data_struct, size = load_data(control, filename)
datos = model.datos_filtrados(data_struct, size)
print(datos) """

# Funciones de ordenamiento

def sort(lst, algorithm, cmpfunction=model.compare):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(lst, algorithm, cmpfunction)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t

def sort_1(lst, algorithm, cmpfunction=model.cmp_impuestos_by_anio_CAE):
    """
    Ordena los datos del modelo bajo la funcion de comparación por año y por código de actividad económica
    """
    start_time = get_time()
    model.sort(lst, algorithm, cmpfunction)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t



# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    req_1, size = model.req_1(control)
    return req_1, size


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2, size = model.req_2(control)

    return req_2, size


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req_3 = model.req_3(control)
    return req_3


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req_4 = model.req_4(control)
    return req_4


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    req_5 = model.req_5(control)
    return req_5


def req_6(control, anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req_6 = model.req_6(control, anio)
    return req_6


def req_7(control, n, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req_7 = model.req_7(control, n, anio_inicial, anio_final)
    return req_7

def req_8(control, n, anio_inicial, anio_final):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start_time = get_time()
    req_8 = model.req_8(control, n, anio_inicial, anio_final)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    print(delta_t)
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
