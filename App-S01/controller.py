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


csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(data_type):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(data_type)
    return control


# Funciones para la carga de datos

def load_data(control,load_table):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    filename = cf.data_dir + 'Salida_agregados_renta_juridicos_AG-large.csv'
    input_file = csv.DictReader(open(filename, encoding = 'utf-8'))
    
    if load_table:
        d_table = new_controller("ARRAY_LIST")
        table = []
        headers = ["Año", "Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico", "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]

        for data in input_file:
            datos = model.add_data(control["model"], data)
            datas = model.add_data(d_table["model"], data)

        model.sort(datas)
        size = model.data_size(control["model"])
        sublista1 = model.sublistas(datas["data"], 1, 3)
        sublista2 = model.sublistas(datas["data"], datas["data"]["size"] - 4, 3)
       
        add_array(table, sublista1, headers)
        add_array(table, sublista2, headers)
        
        return datas, size, table, headers
    else:
        for data in input_file:
            datos = model.add_data(control["model"], data)
        return datos


def add_array(table, list, header):
    for element in list["elements"]:
        row = []
        for key in element:
            if key in header:  
                row.append(element[key]) 
        table.append(row)
    return table
    
        

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

    
    req_1 = model.req_1(control)

    start_time = get_time()
    model.req_1(control)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    
    return req_1, delta_t
    


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2 = model.req_2(control)

    start_time = get_time()
    model.req_2(control)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

    return req_2, delta_t
    


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req_3, tableanios = model.req_3(control)

    
    start_time = get_time()
    model.req_3(control)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

   
    return tableanios, req_3, delta_t


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req_4, tableanios = model.req_4(control)
    start_time = get_time()
    model.req_4(control)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

    return req_4, tableanios, delta_t

def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    req_5, tableanios = model.req_5(control)
    start_time = get_time()
    model.req_5(control)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

    return req_5, tableanios, delta_t


def req_6(control, year):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    sector, max_subsector, min_subsector, max_actividad, min_actividad = model.req_6(control, year)

    start_time = get_time()
    model.req_6(control,year)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)


    
    return sector, max_subsector, min_subsector, max_actividad, min_actividad, delta_t
   

def req_7(control,n,anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    
    req_7 = model.req_7(control,n,anio_inicial,anio_final)


    start_time = get_time()
    model.req_7(control,n,anio_inicial,anio_final)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)


    return req_7, delta_t


def req_8(control,n,anio_inicial,anio_final):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8

    req_8 = model.req_8(control,n,anio_inicial,anio_final)

    start_time = get_time()
    model.req_8(control,n,anio_inicial,anio_final)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)

    
    return req_8, delta_t


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    Devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    Devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
