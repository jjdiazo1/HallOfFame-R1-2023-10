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


def new_controller(ds):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(ds)
    return control


# Funciones para la carga de datos

def load_data(control, filename, orderingAlg):
    """
    Carga los datos del reto
    """

    catalog = control['model']
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for column in input_file:
        register = {'data':column}
        model.add_data(catalog, register)
    t = sort(control, orderingAlg)
    return control, t

def selectPercentage(dataPercentage):
    """
    Retorna el sufijo del archivo al cuál se dese acceder

    Args:
        dataPercentage (str): Número seleccionado por consola para el porcentaje de datos

    Returns:
        str: Sufijo del archivo en cuestión
    """
    suffixes = {'1':'small', '2':'5pct', '3':'10pct', '4':'20pct',
                '5':'30pct', '6':'50pct', '7':'80pct', '8':'large'}
    return suffixes[dataPercentage]

# Funciones de ordenamiento

def sort(control, orderingAlg):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"], orderingAlg)
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
    start = get_time()
    req_1 = model.req_1(control["model"])
    end = get_time()
    delta = delta_time(start, end)
    return req_1, delta


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    start = get_time()
    req_2 = model.req_2(control["model"])
    end = get_time()
    delta = delta_time(start, end)
    return req_2, delta


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    start = get_time()
    req_3 = model.req_3(control["model"])
    end = get_time()
    delta = delta_time(start, end)
    return req_3, delta


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    start = get_time()
    req_4 = model.req_4(control["model"])
    end = get_time()
    delta = delta_time(start, end)
    return req_4, delta


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    start = get_time()
    req_5 = model.req_5(control["model"])
    end = get_time()
    delta = delta_time(start, end)
    return req_5, delta


def req_6(control, año):
    """
    Retorna el resultado del requerimiento 6
    """
    start = get_time()
    req_6 = model.req_6(control["model"], año)
    end = get_time()
    delta = delta_time(start, end)
    return req_6, delta


def req_7(control, n, aInicial, aFinal):
    """
    Retorna el resultado del requerimiento 7
    """
    start = get_time()
    req_7 = model.req_7(control["model"], n, aInicial, aFinal)
    end = get_time()
    delta = delta_time(start, end)
    return req_7, delta


def req_8(control, aInicial, aFinal):
    """
    Retorna el resultado del requerimiento 8
    """
    start = get_time()
    req_8D, req_8N = model.req_8(control["model"], aInicial, aFinal)
    end = get_time()
    delta = delta_time(start, end)
    return req_8D, req_8N, delta


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

