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
from tabulate import tabulate

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(struc):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(struc)
    return control

def load_data(control, arch, alg):
    """
    Carga los datos del reto
    """
    catalog = control["model"]
    csvfile = cf.data_dir + 'Salida_agregados_renta_juridicos_AG-'+arch
    input_file = csv.DictReader(open(csvfile, encoding='utf-8'))
    for row in input_file:
        #limpieza de datos
        if ("/" in row["Código actividad económica"] or "*" in row["Código actividad económica"] or "y" in row["Código actividad económica"] or " " in row["Código actividad económica"]):
            codigo_eco = model.purgar_codigo(row["Código actividad económica"])
            row["Código actividad económica"] = codigo_eco
        else:
            codigo_eco = row["Código actividad económica"] 
        if ("/" in row["Código sector económico"] or "*" in row["Código sector económico"] or "y" in row["Código sector económico"] or " " in row["Código sector económico"]):
            codigo_sececo = model.purgar_codigo(row["Código sector económico"])
            row["Código sector económico"] = codigo_sececo
        if ("/" in row["Código subsector económico"] or "*" in row["Código subsector económico"] or "y" in row["Código subsector económico"] or " " in row["Código subsector económico"]):
            codigo_subsececo = model.purgar_codigo(row["Código subsector económico"])
            row["Código subsector económico"] = codigo_subsececo
        
        row["Nombre actividad económica"] = row["Nombre actividad económica"][0].upper() + row["Nombre actividad económica"][1:].lower()
        row["Nombre sector económico"] = row["Nombre sector económico"][0].upper() + row["Nombre sector económico"][1:].lower()
        row["Nombre subsector económico"] = row["Nombre subsector económico"][0].upper() + row["Nombre subsector económico"][1:].lower()
        
        id = (int(row["Año"])*10000)+int(codigo_eco)
        info = row
        data = { "id": id,
                "info": info}
        model.add_data(catalog, data)
    tiempo = sort(control, alg)
    return model.data_size(catalog), tiempo

def data_carga_resumen(catalog):
    data_carga = model.data_carga_resumen(catalog["model"])
    return data_carga

# Funciones de ordenamiento

def sort(control, alg):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"], alg)
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
    req_1 = model.req_1(control["model"])
    return req_1


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2 = model.req_2(control["model"])
    return req_2


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req_3 = model.req_3(control["model"])
    return req_3


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req_4 = model.req_4(control["model"])
    return req_4


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    req_5 = model.req_5(control["model"])
    return req_5


def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req_6 = model.req_6(control["model"],anio)
    return req_6


def req_7(control,n,bi,bs):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req_7 = model.req_7(control["model"],n,bi,bs)
    return req_7


def req_8(control,bi,bs):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"],bi,bs)
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
    return 
