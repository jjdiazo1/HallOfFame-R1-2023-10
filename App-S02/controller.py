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


def new_controller(list_type):
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {'model': None}
    control['model'] = model.new_data_structs(list_type)
    return control



# Funciones para la carga de datos

def load_data(control, filename,sort_type):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    catalog = control['model']
    contentfile = cf.data_dir + filename
    input_file = csv.DictReader(open(contentfile, encoding = 'utf-8'))
    for content in input_file:
        model.add_data(catalog,content)
        
    delta_t , sorted_file = sort(catalog,sort_type)
    size = int(sorted_file["size"])
    control["model"] = sorted_file
    return size, model.first_and_last3(sorted_file), delta_t


# Funciones de ordenamiento

def sort(control,sort_type):
    """
    Ordena los datos del modelo
    """ 
    start_time = get_time()
    file_org = model.sort(control,sort_type)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, file_org


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
    start_time = get_time()
    req_1 = model.req_1(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_1,delta_t


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    req_2 = model.req_2(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_2,delta_t


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    req_3 = model.req_3(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_3,delta_t


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    req_4 = model.req_4(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_4,delta_t


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    req_5,tabla_anios = model.req_5(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_5,tabla_anios,delta_t


def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    req_6 = model.req_6(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_6,delta_t


def req_7(control,topN,anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    req_7 = model.req_7(control["model"],topN,anio_inicial,anio_final)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_7,delta_t


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
