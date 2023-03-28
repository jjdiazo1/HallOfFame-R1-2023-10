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

#Se crea el controlador, este recibe como parametro n, a, al que es la  información enviada por la vista.

def new_controller(n, a, al):
    """
    Crea una instancia del modelo
    """
    listtype = ''
    filesize = ''
    sortingtype = ''
    if n == 1:
        listtype = 'ARRAY_LIST'
        
    elif n == 2:
        listtype = 'SINGLE_LINKED'
    
    if a == 1:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-5pct.csv'
    if a == 2:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-10pct.csv'    
    if a == 3:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-20pct.csv'
    if a == 4:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-30pct.csv'
    if a == 5:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-50pct.csv'
    if a == 6:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-80pct.csv'
    if a == 7:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-large.csv'
    if a == 8:
        filesize = 'DIAN/Salida_agregados_renta_juridicos_AG-small.csv'
        
    if al == 1:
        sortingtype = 'selectionsort'
    if al == 2:
        sortingtype = 'insertionsort'
    if al == 3:
        sortingtype = 'shellsort'
    if al == 4:
        sortingtype = 'mergesort'
    if al == 5:
        sortingtype = 'quicksort'
    
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(listtype)

    return control, filesize, sortingtype


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    catalog =  control['model']
    data = loadDatos(catalog, filename)
    return data

def loadDatos(data_structs, filename):
    id = 0
    tagsfile = cf.data_dir + filename
    print(tagsfile)
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for registro in input_file:
        model.add_register(data_structs, registro)
        id += 1

    return data_structs   

# Funciones de ordenamiento

def sortGeneral(control, tipo):
    """
    Ordena los datos del modelo tomando en cuenta el tipo de ordenamiento y el año
    """
    
    global funcion_ordenamiento 

    if tipo == 'selectionsort':
        funcion_ordenamiento = model.useSelectionSort
    elif tipo == 'insertionsort':
        funcion_ordenamiento = model.useInsertionSort
    elif tipo == 'shellsort':
        funcion_ordenamiento = model.useShellSort
    elif tipo == 'mergesort':
        funcion_ordenamiento = model.useMergeSort
    elif tipo == 'quicksort':
        funcion_ordenamiento = model.useQuickSort

    start_time = get_time()
    x = funcion_ordenamiento(control, tipo)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return  delta_t, x 

#Esta funcion es la que permite recortar las listas de forma linda

def recortarLista(list):
    return model.recortarLista(list)

def listaPorCadaAnio(list):
    return model.listaPorCadaAnio(list)

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
    req_1 = model.req_1(control["model"]['data'])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, req_1


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    req_2 = model.req_2(control["model"]['data'])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, req_2


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start_time = get_time()
    req_3, req_3_pt2 = model.req_3(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, req_3, req_3_pt2


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start_time = get_time()
    req_4 = model.req_4(control["model"])[0]
    req_4_2 = model.req_4(control["model"])[1]
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_4, req_4_2, delta_t


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    req_5= model.req_5(control["model"])[0]
    req_5_pt2 = model.req_5(control["model"])[1]
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t, req_5, req_5_pt2


def req_6(control, n):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    year = ''
    
    if n == 1:
        
        year = '2012'
    if n == 2:
        
        year = '2013'
    if n == 3:
        
        year = '2014'
    if n == 4:
        
        year = '2015' 
    if n == 5:
        
        year = '2016'
    if n == 6:
        
        year = '2017'
    if n == 7:
        
        year = '2018'
    if n == 8:
        
        year = '2019'
    if n == 9:
        
        year = '2020'
    if n == 10:
        
        year = '2021'

    start_time = get_time()
    req_6_1 = model.req_6(control["model"], year)[0]
    req_6_2 = model.req_6(control["model"], year)[1]
    req_6_3 = model.req_6(control["model"], year)[2]
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_6_1, req_6_2, req_6_3, delta_t


def req_7(control, Ain, Afn, TOP):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    req_7 = model.req_7(control["model"],Ain, Afn, TOP)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return req_7, delta_t


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8
#llamat a seguridad:
def seguridad(lista):
    x = model.anos_unq(lista["model"])
    return x

# Funciones para medir tiempos de  ejecucion ""(Mirar)""

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
