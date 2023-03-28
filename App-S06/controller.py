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

from tabulate import tabulate
import pandas as pd
import config as cf
import model
import time
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def new_controller(estructura):
    """
    Crea una instancia del modelo.
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(estructura)
    return control


def tamanio_lista(control):
    
    """ Retorna el tamaño de la lista.
    """
    
    tamanio = model.data_size(control["model"])
    
    return tamanio


def load_data(control, filename):
    """
    Carga los datos del reto
    """
    data_structs = control['model']
    dianfiles = cf.data_dir + f'DIAN/Salida_agregados_renta_juridicos_AG-{filename}.csv'
    input_file = csv.DictReader(open(dianfiles, encoding='utf-8'))
    num = 1
    for data in input_file:
        data["id"] = num
        model.add_data(data_structs, data)
        num += 1
        
    lista_grande = data_structs["data"]
    
    return lista_grande


def sort(control, tipoSort):
    """
    Ordena los datos del modelo y retorna el tiempo que tarda en procesar los datos.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_ordenada = model.sort(control["model"],tipoSort)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t , lista_ordenada


def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def req_1(control):
    """
    Retorna el resultado del requerimiento 1 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_req_1 = model.req_1(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return lista_req_1, delta_t
    
    
def req_2(control):
    """
    Retorna el resultado del requerimiento 2 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_req_2 = model.req_2(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return lista_req_2, delta_t


def req_3(control):
    """
    Retorna el resultado del requerimiento 3 y el tiempo de ejecucion.
    """    
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_req3 = model.req_3(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return lista_req3, delta_t

def req_4(control):
    """
    Retorna el resultado del requerimiento 4 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_req4 = model.req_4(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return lista_req4, delta_t


def req_5(control):
    """
    Retorna el resultado del requerimiento 5 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    lista_req5 = model.req_5(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return lista_req5, delta_t


def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    req_6 = model.req_6(control["model"],anio)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_6, delta_t


def req_7(control,top, inicio, final):
    """
    Retorna el resultado del requerimiento 7 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    req_7 = model.req_7(control["model"],top,inicio,final)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_7,delta_t


def req_8(control):
    """
    Retorna el resultado del requerimiento 8 y el tiempo de ejecucion.
    """
    start_time = 0
    end_time = 0
    start_time = get_time()
    req_8 = model.req_8(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_8


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