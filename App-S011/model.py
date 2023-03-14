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
import time 
import copy
from tabulate import tabulate

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(data_type, cmpfunction_):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=data_type,
                                     cmpfunction=cmpfunction_)

    return data_structs

# Funciones para creacion de datos

def new_data(id=0, info=""):
    """
    Crea una nueva estructura para modelar los datos
        data["id"] = id
    data["info"] = info
    """
    data = {'id': id, "info": info}

    return data

# Funciones para agregar informacion al modelo

def add_data(data_structs, data, id):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(id, data)
    lt.addLast(data_structs["data"], d)

    return data_structs

# Función para organizar los datos por año

def ordenar_carga_de_datos(data_struct):
    sort(data_struct, 'MergeSort', cmp_impuestos_by_anio_CAE)
    

def organizar_por_año(data_struct, size, modo_ordenamiento):
    """ Organiza por años los datos. Crea un diccionario cuyas llaves son los años 
    registrados en los datos, y cuyos valores corresponden a un nuevo TAD lista 
    (de tipo array) que contiene todos los datos del TAD lista original y que 
    coinciden con el año que está por llave. Si modo_ordenamiento es True, llama a la funcion que ordena de menor a mayor"""
    #data_copy = copy.deepcopy(data_struct) No se puede hacer deepcopy por los modulos:(
    #Ordena por año
    if not modo_ordenamiento:
        dataStructure = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_impuestos_by_anio_mayor_menor)
        for i in range(size):
            data = lt.getElement(data_struct['data'], i+1)
            add_data(dataStructure, data['info'], i)
        sort(dataStructure, 'MergeSort', cmp_impuestos_by_anio_mayor_menor)
        
        datos_filtrados = {}
        for i in range(size):
            data = lt.getElement(dataStructure['data'], i+1)
            if data['info']['Año'] not in datos_filtrados:
                #Toma y añade los datos al nuevo TAD lista correspondiente al año. Utiliza por defecto el tipo ARRAY_LIST.
                datos_filtrados[data['info']['Año']] = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
            data_new = add_data(datos_filtrados[data['info']['Año']], data=data['info'], id=i)
        return datos_filtrados
    
    datos_filtrados = {}    
    for i in range(size):
        data = lt.getElement(data_struct['data'], i+1)
        if data['info']['Año'] not in datos_filtrados:
            #Toma y añade los datos al nuevo TAD lista correspondiente al año. Utiliza por defecto el tipo ARRAY_LIST.
            datos_filtrados[data['info']['Año']] = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
        data_new = add_data(datos_filtrados[data['info']['Año']], data=data['info'], id=i)
    return datos_filtrados

def selector_de_periodo(datos_organizados, anio_inicial, anio_final):
    #Esta función filtra el diccionario retornado por organizar_por_año para un periodo de tiempo en específico.
    anios = list(datos_organizados.keys())
    for anio in anios:
        if int(anio)<int(anio_inicial):
            del datos_organizados[anio]
        elif int(anio)>int(anio_final):
            del datos_organizados[anio]
    return datos_organizados

# Funciones de consulta

def datos_filtrados(data_struct, size, llaves_a_incluir):
    #Organiza por años el data_struct ingresado.
    datos_filtrados_prev = organizar_por_año(data_struct, size, True)
    datos_filtrados = datos_filtrados_prev.copy()
    
    list_values = []
    #Extrae los tres primeros y últimos datos de cada año
    #Ordena los datos de cada año por Código de actividad económica
    for año in datos_filtrados:
        #sort(datos_filtrados[año], 'MergeSort', cmp_impuestos_by_CAE)
        list_complete = []
        first_three = lt.subList(datos_filtrados[año]['data'], 1, 3) 
          
        last_three = lt.subList(datos_filtrados[año]['data'], datos_filtrados[año]['data']['size']-2, 3)
        
        for i in range(3):
            dato = lt.getElement(first_three, i+1)
            list_complete.append(dato)
        
        for i in range(3):
            dato = lt.getElement(last_three, i+1)
            list_complete.append(dato)
        list_values.extend(list_complete)
        
    list_values_info = []
    #Añade en una lista otra lista que contiene la informacion de cada dato. Esto es para usar tabulate en view
    for data in list_values:
        data_copy = data['info'].copy()
        data_copy_2 ={}
        for llave in data_copy:
            if llave in llaves_a_incluir:
                data_copy_2[llave]=data_copy[llave]
        list_data = list(data_copy_2.values())
        list_values_info.append(list_data)
    return list_values_info



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


def req_1(datos_anio):
    """
    Función que soluciona el requerimiento 1
    """
    
    llaves_a_incluir = ['Año',
                        'Código actividad económica', 
                        'Nombre actividad económica', 
                        'Código sector económico',
                        'Nombre sector económico',
                        'Código subsector económico',
                        'Nombre subsector económico',
                        'Total ingresos netos',
                        'Total costos y gastos',
                        'Total saldo a pagar',
                        'Total saldo a favor'] 
    #Organizar por año
    nueva_lista = new_data_structs('ARRAY_LIST', cmpfunction_=compare)  
    for anio in datos_anio:
        total_mayor = 0
        dato_mayor = {}
        size = data_size(datos_anio[anio])
        #encuentra el dato cuyo saldo a pagar es el mayor.
        for i in range(size):
            dato = lt.getElement(datos_anio[anio]['data'],i+1)
            if int(dato['info']['Total saldo a pagar'])>total_mayor:
                total_mayor = int(dato['info']['Total saldo a pagar'])
                dato_mayor = dato
                
        #Descarta las columnas que no se solicitan
        dato_copia_info = dato_mayor['info'].copy()
        for llave in dato_mayor['info']:
            del dato_copia_info[llave] 
        for llave in llaves_a_incluir:
            dato_copia_info[llave]=dato_mayor['info'][llave]
        add_data(nueva_lista, dato_copia_info, anio)
    return nueva_lista, data_size(nueva_lista)

def req_2(datos_anio):
    """
    Función que soluciona el requerimiento 1
    """
    
    llaves_a_incluir = ['Año',
                        'Código actividad económica', 
                        'Nombre actividad económica', 
                        'Código sector económico',
                        'Nombre sector económico',
                        'Código subsector económico',
                        'Nombre subsector económico',
                        'Total ingresos netos',
                        'Total costos y gastos',
                        'Total saldo a pagar',
                        'Total saldo a favor'] 
    #Organizar por año
    nueva_lista = new_data_structs('ARRAY_LIST', cmpfunction_=compare)  
    for anio in datos_anio:
        total_mayor = 0
        dato_mayor = {}
        size = data_size(datos_anio[anio])
        #encuentra el dato cuyo saldo a favor es el mayor.
        for i in range(size):
            dato = lt.getElement(datos_anio[anio]['data'],i+1)
            if int(dato['info']['Total saldo a favor'])>total_mayor:
                total_mayor = int(dato['info']['Total saldo a favor'])
                dato_mayor = dato
                
        #Descarta las columnas que no se solicitan     
        dato_copia_info = dato_mayor['info'].copy()
        for llave in dato_mayor['info']:
            del dato_copia_info[llave] 
        for llave in llaves_a_incluir:
            dato_copia_info[llave]=dato_mayor['info'][llave]
        add_data(nueva_lista, dato_copia_info, anio)
    return nueva_lista, data_size(nueva_lista)



def req_3(datos_anio):
    """
    Función que soluciona el requerimiento 3
    """
    #se retorna un datastructure final que contiene la información para cada año
    data_struct_final = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
    k=0
    for anio in datos_anio:
        sort(datos_anio[anio], "MergeSort", compare)
        size=data_size(datos_anio[anio])
        #Se crea un datastructure que contenga a todos los subsectores como id, y como valor otro datastructure que contiene los datos del subsector
        data_struct_subsectores = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
        add_data(data_struct_final, data_struct_subsectores, anio)
        for i in range(size):
            dato = lt.getElement(datos_anio[anio]['data'], i+1)
            info_data = dato['info']
            data_a_ingresar = new_data(id=info_data['Código subsector económico'], info=info_data)
            #Si el subsector del dato no se encuentra en la el datastructure de subsectores, se crea el datastructure de datos del subsector y se añade el dato
            if lt.isPresent(data_struct_subsectores['data'], data_a_ingresar) == 0:
                data_struct_datos_subsector = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
                #el datastructure de datos tiene como id el subsector, y como info un dato que tiene por id el total de retenciones 
                #que se va sumando a medida que pasan los datos, y como info el datastructure que contendrá todos los datos del subsector
                nueva_data = new_data(id=int(info_data['Total retenciones']), info= data_struct_datos_subsector)
                add_data(data_struct_subsectores, nueva_data, dato['info']['Código subsector económico'])
            else:
                #Se busca el subsector en el datastructure de subsectores para actualizar el total de retenciones
                nueva_data = new_data(info_data['Código subsector económico'], '')
                subsector = get_data(data_struct_subsectores, nueva_data)
                #Se suma el total de retenciones del dato al subsector correspondiente
                subsector['info']['id']+=int(info_data['Total retenciones'])
            #se añade el dato el datastructure de datos del subsector
            add_data(data_struct_datos_subsector, info_data, dato['id'])
        #se ordenan los datos del datastructure de datos del subsector
        sort(data_struct_subsectores, 'MergeSort', cmp_datastuctures_by_retenciones)
        #se toma el primer subsector (que es el menor en total de retenciones porque está ordenado el arreglo)
        subsector_menor = lt.getElement(data_struct_subsectores['data'], 1)
        total_retenciones_menor_subsector = int(subsector_menor['info']['id'])
        total_ingresos_netos_menor_subsector = 0
        total_costos_gastos_menor_subsector = 0
        total_saldo_por_pagar_menor_subsector = 0
        total_saldo_a_favor_menor_subsector = 0
        #se ordenan los datos del datastructure de datos del subsector menor para obtener lass tres primeras y últimas actividades económicas
        sort(subsector_menor['info']['info'], 'MergeSort', cmp_by_retenciones)
        #se van sumando los valores pedidos de cada dato para calcular los totales pedidos del subsector menor
        for i in range(data_size(subsector_menor['info']['info'])):
            dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
            total_ingresos_netos_menor_subsector +=int(dato['info']['Total ingresos netos'])
            total_costos_gastos_menor_subsector +=int(dato['info']['Total costos y gastos'])
            total_saldo_por_pagar_menor_subsector +=int(dato['info']['Total saldo a pagar'])
            total_saldo_a_favor_menor_subsector +=int(dato['info']['Total saldo a favor'])
        
        llaves_a_incluir = ['Código actividad económica', 
                            'Nombre actividad económica', 
                            'Total retenciones', 
                            'Total ingresos netos',
                            'Total costos y gastos',
                            'Total saldo a pagar',
                            'Total saldo a favor']  
        # tomando el primer dato, da igual cual sea, se definen las primeras columnas a mostrar para el menor subsector
        dato_base = lt.getElement(subsector_menor['info']['info']['data'], 1)
        codigo_sector = dato_base['info']['Código sector económico']
        nombre_sector = dato_base['info']['Nombre sector económico']
        codigo_subsector = dato_base['info']['Código subsector económico']
        nombre_subsector = dato_base['info']['Nombre subsector económico']
        #se toman los tres primeros y últimos datos (ordenados) y se descartan las columnas que no se desean. 
        #Si hay menos de 6 actividades en el subsector, devuelve las que hay.
        if data_size(subsector_menor['info']['info'])<6:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_retenciones)
            for i in range(data_size(subsector_menor['info']['info'])):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
        else:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_retenciones)
            i=0
            while i<3:
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i+=1
            i=data_size(subsector_menor['info']['info'])-3
            while i<data_size(subsector_menor['info']['info']):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i-=1
        lista_columnas_a_mostrar = ['Año',
                                    'Código sector económico',
                                    'Nombre sector económico',
                                    'Código subsector económico',
                                    'Nombre subsector económico',
                                    'Total de retenciones del subsector económico',
                                    'Total de ingresos netos del subsector económico',
                                    'Total de costos y gastos del subsector económico',
                                    'Total saldo por pagar del subsector económico',
                                    'Total saldo a favor del subsector económico',
                                    'Actividades a retornar']
        #se crea el datastructure que contiene como datos, en id la columna y en info el valor. 
        #Las columnas están definidas por listas_columnas_a_mostrar
        datos_a_mostrar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_retenciones)
        add_data(datos_a_mostrar, data=anio, id=lista_columnas_a_mostrar[0])
        add_data(datos_a_mostrar, data=codigo_sector, id=lista_columnas_a_mostrar[1])
        add_data(datos_a_mostrar, data=nombre_sector, id=lista_columnas_a_mostrar[2])
        add_data(datos_a_mostrar, data=codigo_subsector, id=lista_columnas_a_mostrar[3])
        add_data(datos_a_mostrar, data=nombre_subsector, id=lista_columnas_a_mostrar[4])
        add_data(datos_a_mostrar, data=total_retenciones_menor_subsector, id=lista_columnas_a_mostrar[5])
        add_data(datos_a_mostrar, data=total_ingresos_netos_menor_subsector, id=lista_columnas_a_mostrar[6])
        add_data(datos_a_mostrar, data=total_costos_gastos_menor_subsector, id=lista_columnas_a_mostrar[7])
        add_data(datos_a_mostrar, data=total_saldo_por_pagar_menor_subsector, id=lista_columnas_a_mostrar[8])
        add_data(datos_a_mostrar, data=total_saldo_a_favor_menor_subsector, id=lista_columnas_a_mostrar[9])
        add_data(datos_a_mostrar, data=actividades_a_retornar, id=lista_columnas_a_mostrar[10])
        
        #Se actualiza el valor del datastructure para el año en cuestión, tal que pueda retornarse al final de forma definitiva.
        data_structure_anio = lt.getElement(data_struct_final['data'], k+1)
        data_structure_anio['info'] = datos_a_mostrar
        k+=1
    return data_struct_final

def req_4(datos_anio):
    """
    Función que soluciona el requerimiento 4
    """
    data_struct_final = new_data_structs('MergeSort', cmpfunction_=compare)
    k=0
    for anio in datos_anio:
        sort(datos_anio[anio], "MergeSort", compare)
        size=data_size(datos_anio[anio])
        #Se crea un datastructure que contenga a todos los subsectores como id, y como valor otro datastructure que contiene los datos del subsector
        data_struct_subsectores = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
        add_data(data_struct_final, data_struct_subsectores, anio)
        for i in range(size):
            dato = lt.getElement(datos_anio[anio]['data'], i+1)
            info_data = dato['info']
            data_a_ingresar = new_data(id=info_data['Código subsector económico'], info=info_data)
            #Si el subsector del dato no se encuentra en la el datastructure de subsectores, se crea el datastructure de datos del subsector y se añade el dato
            if lt.isPresent(data_struct_subsectores['data'], data_a_ingresar) == 0:
                data_struct_datos_subsector = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
                #el datastructure de datos tiene como id el subsector, y como info un dato que tiene por id el total de cyg nómina 
                #que se va sumando a medida que pasan los datos, y como info el datastructure que contendrá todos los datos del subsector
                nueva_data = new_data(id=int(info_data['Costos y gastos nómina']), info= data_struct_datos_subsector)
                add_data(data_struct_subsectores, nueva_data, dato['info']['Código subsector económico'])
            else:
                #Se busca el subsector en el datastructure de subsectores para actualizar el total de cyg nómina
                nueva_data = new_data(info_data['Código subsector económico'], '')
                subsector = get_data(data_struct_subsectores, nueva_data)
                #Se suma el total de CyG nómina del dato al subsector correspondiente
                subsector['info']['id']+=int(info_data['Costos y gastos nómina'])
            #se añade el dato el datastructure de datos del subsector
            add_data(data_struct_datos_subsector, info_data, dato['id'])
        #se ordenan los datos del datastructure de datos del subsector
        sort(data_struct_subsectores, 'MergeSort', cmp_datastuctures_by_Total_CGN)
        #se toma el primer subsector (que es el menor en total de Costs y gastos nomina porque está ordenado el arreglo)
        subsector_menor = lt.getElement(data_struct_subsectores['data'], 1)
        total_cgn_menor_subsector = int(subsector_menor['info']['id'])
        total_ingresos_netos_menor_subsector = 0
        total_costos_gastos_menor_subsector = 0
        total_saldo_por_pagar_menor_subsector = 0
        total_saldo_a_favor_menor_subsector = 0
        #se ordenan los datos del datastructure de datos del subsector menor para obtener lass tres primeras y últimas actividades económicas
        sort(subsector_menor['info']['info'], 'MergeSort', cmp_impuestos_by_Total_CGN)
        #se van sumando los valores pedidos de cada dato para calcular los totales pedidos del subsector menor
        for i in range(data_size(subsector_menor['info']['info'])):
            dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
            total_ingresos_netos_menor_subsector +=int(dato['info']['Total ingresos netos'])
            total_costos_gastos_menor_subsector +=int(dato['info']['Total costos y gastos'])
            total_saldo_por_pagar_menor_subsector +=int(dato['info']['Total saldo a pagar'])
            total_saldo_a_favor_menor_subsector +=int(dato['info']['Total saldo a favor'])
        
        llaves_a_incluir = ['Código actividad económica', 
                            'Nombre actividad económica', 
                            'Costos y gastos nómina', 
                            'Total ingresos netos',
                            'Total costos y gastos',
                            'Total saldo a pagar',
                            'Total saldo a favor']  
        # tomando el primer dato, da igual cual sea, se definen las primeras columnas a mostrar para el menor subsector
        dato_base = lt.getElement(subsector_menor['info']['info']['data'], 1)
        codigo_sector = dato_base['info']['Código sector económico']
        nombre_sector = dato_base['info']['Nombre sector económico']
        codigo_subsector = dato_base['info']['Código subsector económico']
        nombre_subsector = dato_base['info']['Nombre subsector económico']
        #se toman los tres primeros y últimos datos (ordenados) y se descartan las columnas que no se desean. 
        #Si hay menos de 6 actividades en el subsector, devuelve las que hay.
        if data_size(subsector_menor['info']['info'])<6:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_retenciones)
            for i in range(data_size(subsector_menor['info']['info'])):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
        else:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_impuestos_by_Total_CGN)
            i=0
            while i<3:
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i+=1
            i=data_size(subsector_menor['info']['info'])-3
            while i<data_size(subsector_menor['info']['info']):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i+=1
        lista_columnas_a_mostrar = ['Año',
                                    'Código sector económico',
                                    'Nombre sector económico',
                                    'Código subsector económico',
                                    'Nombre subsector económico',
                                    'Total costos y gastos nómina del subsector económico',
                                    'Total de ingresos netos del subsector económico',
                                    'Total de costos y gastos del subsector económico',
                                    'Total saldo por pagar del subsector económico',
                                    'Total saldo a favor del subsector económico',
                                    'Actividades a retornar']
        #se crea el datastructure que contiene como datos, en id la columna y en info el valor. 
        #Las columnas están definidas por listas_columnas_a_mostrar
        datos_a_mostrar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_impuestos_by_Total_CGN)
        add_data(datos_a_mostrar, data=anio, id=lista_columnas_a_mostrar[0])
        add_data(datos_a_mostrar, data=codigo_sector, id=lista_columnas_a_mostrar[1])
        add_data(datos_a_mostrar, data=nombre_sector, id=lista_columnas_a_mostrar[2])
        add_data(datos_a_mostrar, data=codigo_subsector, id=lista_columnas_a_mostrar[3])
        add_data(datos_a_mostrar, data=nombre_subsector, id=lista_columnas_a_mostrar[4])
        add_data(datos_a_mostrar, data=total_cgn_menor_subsector, id=lista_columnas_a_mostrar[5])
        add_data(datos_a_mostrar, data=total_ingresos_netos_menor_subsector, id=lista_columnas_a_mostrar[6])
        add_data(datos_a_mostrar, data=total_costos_gastos_menor_subsector, id=lista_columnas_a_mostrar[7])
        add_data(datos_a_mostrar, data=total_saldo_por_pagar_menor_subsector, id=lista_columnas_a_mostrar[8])
        add_data(datos_a_mostrar, data=total_saldo_a_favor_menor_subsector, id=lista_columnas_a_mostrar[9])
        add_data(datos_a_mostrar, data=actividades_a_retornar, id=lista_columnas_a_mostrar[10])
        
        #Se actualiza el valor del datastructure para el año en cuestión, tal que pueda retornarse al final de forma definitiva.
        data_structure_anio = lt.getElement(data_struct_final['data'], k+1)
        data_structure_anio['info'] = datos_a_mostrar
        k+=1
    return data_struct_final
    
        

def req_5(datos_anio):
    """
    Función que soluciona el requerimiento 4
    """
    data_struct_final = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
    k=0
    for anio in datos_anio:
        sort(datos_anio[anio], "MergeSort", compare)
        size=data_size(datos_anio[anio])
        #Se crea un datastructure que contenga a todos los subsectores como id, y como valor otro datastructure que contiene los datos del subsector
        data_struct_subsectores = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
        add_data(data_struct_final, data_struct_subsectores, anio)
        for i in range(size):
            dato = lt.getElement(datos_anio[anio]['data'], i+1)
            info_data = dato['info']
            data_a_ingresar = new_data(id=info_data['Código subsector económico'], info=info_data)
            #Si el subsector del dato no se encuentra en la el datastructure de subsectores, se crea el datastructure de datos del subsector y se añade el dato
            if lt.isPresent(data_struct_subsectores['data'], data_a_ingresar) == 0:
                data_struct_datos_subsector = new_data_structs('ARRAY_LIST', cmpfunction_=compare)
                #el datastructure de datos tiene como id el subsector, y como info un dato que tiene por id el total de descuentos tributarios
                #que se va sumando a medida que pasan los datos, y como info el datastructure que contendrá todos los datos del subsector
                nueva_data = new_data(id=int(info_data['Descuentos tributarios']), info= data_struct_datos_subsector)
                add_data(data_struct_subsectores, nueva_data, dato['info']['Código subsector económico'])
            else:
                #Se busca el subsector en el datastructure de subsectores para actualizar el total de descuentos tributarios
                nueva_data = new_data(info_data['Código subsector económico'], '')
                subsector = get_data(data_struct_subsectores, nueva_data)
                #Se suma el total de descuentos tributarios del dato al subsector correspondiente
                subsector['info']['id']+=int(info_data['Descuentos tributarios'])
            #se añade el dato el datastructure de datos del subsector
            add_data(data_struct_datos_subsector, info_data, dato['id'])
        #se ordenan los datos del datastructure de datos del subsector
        sort(data_struct_subsectores, 'MergeSort', cmp_datastuctures_by_total_descuentos_tributarios)
        #se toma el primer subsector (que es el menor en total de Costs y gastos nomina porque está ordenado el arreglo)
        subsector_menor = lt.getElement(data_struct_subsectores['data'], 1)
        total_descuentos_menor_subsector = int(subsector_menor['info']['id'])
        total_ingresos_netos_menor_subsector = 0
        total_costos_gastos_menor_subsector = 0
        total_saldo_por_pagar_menor_subsector = 0
        total_saldo_a_favor_menor_subsector = 0
        #se ordenan los datos del datastructure de datos del subsector menor para obtener lass tres primeras y últimas actividades económicas
        sort(subsector_menor['info']['info'], 'MergeSort', cmp_by_descuentos_tributarios_menor_mayor)
        #se van sumando los valores pedidos de cada dato para calcular los totales pedidos del subsector menor
        for i in range(data_size(subsector_menor['info']['info'])):
            dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
            total_ingresos_netos_menor_subsector +=int(dato['info']['Total ingresos netos'])
            total_costos_gastos_menor_subsector +=int(dato['info']['Total costos y gastos'])
            total_saldo_por_pagar_menor_subsector +=int(dato['info']['Total saldo a pagar'])
            total_saldo_a_favor_menor_subsector +=int(dato['info']['Total saldo a favor'])
        
        llaves_a_incluir = ['Código actividad económica', 
                            'Nombre actividad económica', 
                            'Descuentos tributarios', 
                            'Total ingresos netos',
                            'Total costos y gastos',
                            'Total saldo a pagar',
                            'Total saldo a favor']  
        # tomando el primer dato, da igual cual sea, se definen las primeras columnas a mostrar para el menor subsector
        dato_base = lt.getElement(subsector_menor['info']['info']['data'], 1)
        codigo_sector = dato_base['info']['Código sector económico']
        nombre_sector = dato_base['info']['Nombre sector económico']
        codigo_subsector = dato_base['info']['Código subsector económico']
        nombre_subsector = dato_base['info']['Nombre subsector económico']
        #se toman los tres primeros y últimos datos (ordenados) y se descartan las columnas que no se desean. 
        #Si hay menos de 6 actividades en el subsector, devuelve las que hay.
        if data_size(subsector_menor['info']['info'])<6:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_descuentos_tributarios_mayor_menor)
            for i in range(data_size(subsector_menor['info']['info'])):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
            sort(actividades_a_retornar, 'MergeSort', cmp_by_descuentos_tributarios_mayor_menor)
        else:
            actividades_a_retornar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_descuentos_tributarios_menor_mayor)
            i=0
            while i<3:
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i+=1
            i=data_size(subsector_menor['info']['info'])-3
            while i<data_size(subsector_menor['info']['info']):
                dato = lt.getElement(subsector_menor['info']['info']['data'], i+1)
                dato_copia_info = dato['info'].copy()
                for llave in dato['info']:
                    del dato_copia_info[llave] 
                for llave in llaves_a_incluir:
                    dato_copia_info[llave]=dato['info'][llave]
                add_data(actividades_a_retornar, dato_copia_info, dato['id'])
                i+=1
        lista_columnas_a_mostrar = ['Año',
                                    'Código sector económico',
                                    'Nombre sector económico',
                                    'Código subsector económico',
                                    'Nombre subsector económico',
                                    'Total descuentos tributarios del subsector económico',
                                    'Total de ingresos netos del subsector económico',
                                    'Total de costos y gastos del subsector económico',
                                    'Total saldo por pagar del subsector económico',
                                    'Total saldo a favor del subsector económico',
                                    'Actividades a retornar']
        #se crea el datastructure que contiene como datos, en id la columna y en info el valor. 
        #Las columnas están definidas por listas_columnas_a_mostrar
        datos_a_mostrar = new_data_structs('ARRAY_LIST', cmpfunction_=cmp_by_descuentos_tributarios_menor_mayor)
        add_data(datos_a_mostrar, data=anio, id=lista_columnas_a_mostrar[0])
        add_data(datos_a_mostrar, data=codigo_sector, id=lista_columnas_a_mostrar[1])
        add_data(datos_a_mostrar, data=nombre_sector, id=lista_columnas_a_mostrar[2])
        add_data(datos_a_mostrar, data=codigo_subsector, id=lista_columnas_a_mostrar[3])
        add_data(datos_a_mostrar, data=nombre_subsector, id=lista_columnas_a_mostrar[4])
        add_data(datos_a_mostrar, data=total_descuentos_menor_subsector, id=lista_columnas_a_mostrar[5])
        add_data(datos_a_mostrar, data=total_ingresos_netos_menor_subsector, id=lista_columnas_a_mostrar[6])
        add_data(datos_a_mostrar, data=total_costos_gastos_menor_subsector, id=lista_columnas_a_mostrar[7])
        add_data(datos_a_mostrar, data=total_saldo_por_pagar_menor_subsector, id=lista_columnas_a_mostrar[8])
        add_data(datos_a_mostrar, data=total_saldo_a_favor_menor_subsector, id=lista_columnas_a_mostrar[9])
        add_data(datos_a_mostrar, data=actividades_a_retornar, id=lista_columnas_a_mostrar[10])
        
        #Se actualiza el valor del datastructure para el año en cuestión, tal que pueda retornarse al final de forma definitiva.
        data_structure_anio = lt.getElement(data_struct_final['data'], k+1)
        data_structure_anio['info'] = datos_a_mostrar
        k+=1
    return data_struct_final

def req_6(data_structs, anio):
    """
    Función que soluciona el requerimiento 6
    """
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    data_anio1 = data_structs
    data_anio = data_anio1[anio].copy()
    data_anio['data']['cmpfunction']=cmp_impuestos_by_sector
    sort(data_anio, 'MergeSort', data_anio['data']['cmpfunction'])
    dict_sectores = {}
    for element in data_anio["data"]["elements"]:
        if element["info"]["Código sector económico"] not in dict_sectores:
            dict_sectores[element["info"]["Código sector económico"]] = { 
                                                                         "Codigo_sector" : element["info"]["Código sector económico"],
                                                                         "Nombre_sector" : element["info"]["Nombre sector económico"],
                                                                         "Suma_ingresos_netos_sector": 0, 
                                                                         "Suma_costos_y_gastos_sector": 0,
                                                                         "Total_saldo_por_pagar_sector": 0, 
                                                                         "Total_saldo_a_favor_sector": 0,
                                                                         "Subs_menos_codigo": "",
                                                                         "Subs_mas_codigo": "",
                                                                         "Subs_menos": "",
                                                                         "Subs_mas": "",
                                                                         "Subsectores": {},
                                                                         "Datos": []}
        dict_sectores[element["info"]["Código sector económico"]]["Datos"].append(element)
        
        
        if element["info"]["Código subsector económico"] not in dict_sectores[element["info"]["Código sector económico"]]["Subsectores"]:
            dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]] = {
                                                                                                                                  "Nombre_subs": element["info"]["Nombre subsector económico"],
                                                                                                                                  "Codigo_subs": element["info"]["Código subsector económico"],
                                                                                                                                  "Suma_ingresos_netos_subsector": 0, 
                                                                                                                                  "Suma_costos_y_gastos_subsector": 0,
                                                                                                                                  "Total_saldo_por_pagar_subsector": 0, 
                                                                                                                                  "Total_saldo_a_favor_subsector": 0,
                                                                                                                                  "Act_menos": "",
                                                                                                                                  "Act_mas": "",
                                                                                                                                  "Datos_sub": []}
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Suma_ingresos_netos_subsector"] += int(element["info"]["Total ingresos netos"])
        dict_sectores[element["info"]["Código sector económico"]]["Suma_ingresos_netos_sector"]+= int(element["info"]["Total ingresos netos"])
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Suma_costos_y_gastos_subsector"] += int(element["info"]["Total costos y gastos"])
        dict_sectores[element["info"]["Código sector económico"]]["Suma_costos_y_gastos_sector"]+= int(element["info"]["Total costos y gastos"])
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Total_saldo_por_pagar_subsector"] += int(element["info"]["Total saldo a pagar"])
        dict_sectores[element["info"]["Código sector económico"]]["Total_saldo_por_pagar_sector"] += int(element["info"]["Total saldo a pagar"])
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Total_saldo_a_favor_subsector"] += int(element["info"]["Total saldo a favor"])
        dict_sectores[element["info"]["Código sector económico"]]["Total_saldo_a_favor_sector"] += int(element["info"]["Total saldo a favor"])
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Datos_sub"].append(element)      
        

        #1 Hasta este punto se ha creado un dict(dict_sectores) que contiene como llaves a todos los sectores del año ingresado por usuario y los datos pedidos por view como suma ingresos netos sector.
        #2 A su vez, cada sector tiene un dict que contiene como llaves a todos sus subsectores y los datos de las act económicas que se encuentren en ese sector.
        #3 Dentro de la llave de subsectores, se almacenan todos los req que nos piden en el view como suma ingresos netos por subsector ... y se anexan los datos de ese subsector.
        
        

        #sort(dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Datos_sub"], "MergeSort", cmp_by_ingresos_netos)
        
        nuevo_Dt = new_data_structs('ARRAY_LIST', cmp_by_ingresos_netos)
        for data in dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Datos_sub"]:
            add_data(nuevo_Dt, data["info"], data["id"])
        nuevo_Dt_size = data_size(nuevo_Dt)
        sort(nuevo_Dt, "MergeSort", nuevo_Dt["data"]["cmpfunction"])
        dict_sectores[element["info"]["Código sector económico"]]["Subs_menos_codigo"] = lt.getElement(nuevo_Dt["data"], 1)["info"]["Código subsector económico"]
        dict_sectores[element["info"]["Código sector económico"]]["Subs_mas_codigo"] = lt.getElement(nuevo_Dt["data"], nuevo_Dt_size)["info"]["Código subsector económico"]
        dict_sectores[element["info"]["Código sector económico"]]["Subs_menos"] = lt.getElement(nuevo_Dt["data"], 1)["info"]
        dict_sectores[element["info"]["Código sector económico"]]["Subs_mas"] = lt.getElement(nuevo_Dt["data"], nuevo_Dt_size)["info"]
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Act_mas"] = lt.getElement(nuevo_Dt["data"], nuevo_Dt_size)["info"]
        dict_sectores[element["info"]["Código sector económico"]]["Subsectores"][element["info"]["Código subsector económico"]]["Act_menos"] = lt.getElement(nuevo_Dt["data"], 1)["info"]

        #4 Se creo un data structure para poder organizar los subsectores con base en el parametro de ingresos netos. Se define en el dict sectores el subsector mayor y el menor


    lista_datos = []   
    lista_datos2 = []
    lista_datos3 = []
    for sector in dict_sectores:
        data_a_mostrar_tabla1 =    {"Código sector \neconómico": "",
                            "Nombre sector \neconómico": "",
                            "Total ingresos netos \ndel sector económico": "",
                            "Total costos y gastos \ndel sector económico": "",
                            "Total saldo a pagar \ndel sector económico": "",
                            "Total saldo a favor \ndel sector económico": "",
                            "Subsector económico \nque más aportó": "",
                            "Subsector económico \nque menos aportó": ""}  
        for subsector in dict_sectores[sector]["Subsectores"]:
            data_a_mostrar_tabla1['Código sector \neconómico'] = dict_sectores[sector]["Codigo_sector"]
            data_a_mostrar_tabla1['Nombre sector \neconómico'] = dict_sectores[sector]["Nombre_sector"]
            data_a_mostrar_tabla1["Total ingresos netos \ndel sector económico"] = dict_sectores[sector]["Suma_ingresos_netos_sector"]
            data_a_mostrar_tabla1["Total costos y gastos \ndel sector económico"] = dict_sectores[sector]["Suma_costos_y_gastos_sector"]
            data_a_mostrar_tabla1['Total saldo a pagar \ndel sector económico'] = dict_sectores[sector]["Total_saldo_por_pagar_sector"]
            data_a_mostrar_tabla1['Total saldo a favor \ndel sector económico'] = dict_sectores[sector]["Total_saldo_a_favor_sector"]
            data_a_mostrar_tabla1['Subsector económico \nque más aportó'] = dict_sectores[sector]["Subs_mas_codigo"]
            data_a_mostrar_tabla1['Subsector económico \nque menos aportó'] = dict_sectores[sector]["Subs_menos_codigo"]
            
            lista_datos.append(data_a_mostrar_tabla1)     
            #Tabla 1
            
        data_a_mostrar_tabla2 = {"Código subsector económico": "",
                            "Nombre subsector económico": "",
                            "Total ingresos netos del subsector económico": "",
                            "Total costos y gastos del subsector económico": "",
                            "Total saldo a pagar del subsector económico": "",
                            "Total saldo a favor del subsector económico": "",
                            "Actividad económica que más aportó": "",
                            "Actividad económica que menos aportó": ""}  
        
        datos_a_mostrar_actividades_mas = {"Código actividad económica": [],
                                        "Nombre actividad económica": [],
                                        "Total ingresos netos": [],
                                        "Total costos y gastos": [],
                                        "Total saldo a pagar": [], 
                                        "Total saldo a favor": [],}
        datos_a_mostrar_actividades_menos = {"Código actividad económica": [],
                                        "Nombre actividad económica": [],
                                        "Total ingresos netos": [],
                                        "Total costos y gastos": [],
                                        "Total saldo a pagar": [], 
                                        "Total saldo a favor": [],}

        
        for subsector in dict_sectores[sector]["Subsectores"]:
            data_a_mostrar_tabla2['Código subsector económico'] = dict_sectores[sector]["Subs_mas_codigo"]
            data_a_mostrar_tabla2['Nombre subsector económico'] = dict_sectores[sector]["Subs_mas"]["Nombre subsector económico"]
            data_a_mostrar_tabla2['Total ingresos netos del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Suma_ingresos_netos_subsector"]
            data_a_mostrar_tabla2["Total costos y gastos del subsector económico"] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Suma_costos_y_gastos_subsector"]
            data_a_mostrar_tabla2['Total saldo a pagar del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Total_saldo_por_pagar_subsector"]
            data_a_mostrar_tabla2['Total saldo a favor del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Total_saldo_a_favor_subsector"]
            
            datos_a_mostrar_actividades_mas['Código actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Código actividad económica"])
            datos_a_mostrar_actividades_mas['Nombre actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Nombre actividad económica"])
            datos_a_mostrar_actividades_mas['Total ingresos netos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Total ingresos netos"])
            datos_a_mostrar_actividades_mas['Total saldo a pagar'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Total saldo a pagar"])
            datos_a_mostrar_actividades_mas['Total saldo a favor'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Total saldo a favor"])
            datos_a_mostrar_actividades_mas['Total costos y gastos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_mas"]["Total costos y gastos"])
            
            datos_a_mostrar_actividades_menos['Código actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Código actividad económica"])
            datos_a_mostrar_actividades_menos['Nombre actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Nombre actividad económica"])
            datos_a_mostrar_actividades_menos['Total ingresos netos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Total ingresos netos"])
            datos_a_mostrar_actividades_menos['Total saldo a pagar'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Total saldo a pagar"])
            datos_a_mostrar_actividades_menos['Total saldo a favor'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Total saldo a favor"])
            datos_a_mostrar_actividades_menos['Total costos y gastos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_mas_codigo"]]["Act_menos"]["Total costos y gastos"])

            tabla_mas_mas = tabulate((datos_a_mostrar_actividades_mas.items()), headers= "firstrow", tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None])
            tabla_menos_mas = tabulate(datos_a_mostrar_actividades_menos.items(), headers= "firstrow", tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None])
            
            data_a_mostrar_tabla2['Actividad económica que más aportó'] = tabla_mas_mas
            data_a_mostrar_tabla2['Actividad económica que menos aportó'] = tabla_menos_mas
            
            lista_datos2.append(data_a_mostrar_tabla2)            
            
            #Tabla2
            
            
        data_a_mostrar_tabla3 = {"Código subsector económico": "",
                            "Nombre subsector económico": "",
                            "Total ingresos netos del subsector económico": "",
                            "Total costos y gastos del subsector económico": "",
                            "Total saldo a pagar del subsector económico": "",
                            "Total saldo a favor del subsector económico": "",
                            "Actividad económica que más aportó": "",
                            "Actividad económica que menos aportó": ""}
        datos_a_mostrar_actividades_mas = {"Código actividad económica": [],
                                        "Nombre actividad económica": [],
                                        "Total ingresos netos": [],
                                        "Total costos y gastos": [],
                                        "Total saldo a pagar": [], 
                                        "Total saldo a favor": [],}
        datos_a_mostrar_actividades_menos = {"Código actividad económica": [],
                                        "Nombre actividad económica": [],
                                        "Total ingresos netos": [],
                                        "Total costos y gastos": [],
                                        "Total saldo a pagar": [], 
                                        "Total saldo a favor": [],}
        
        for subsector in dict_sectores[sector]["Subsectores"]:
            data_a_mostrar_tabla3['Código subsector económico'] = dict_sectores[sector]["Subs_menos_codigo"]
            data_a_mostrar_tabla3['Nombre subsector económico'] = dict_sectores[sector]["Subs_menos"]["Nombre subsector económico"]
            data_a_mostrar_tabla3['Total ingresos netos del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Suma_ingresos_netos_subsector"]
            data_a_mostrar_tabla3["Total costos y gastos del subsector económico"] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Suma_costos_y_gastos_subsector"]
            data_a_mostrar_tabla3['Total saldo a pagar del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Total_saldo_por_pagar_subsector"]
            data_a_mostrar_tabla3['Total saldo a favor del subsector económico'] = dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Total_saldo_a_favor_subsector"]
            
            datos_a_mostrar_actividades_mas['Código actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Código actividad económica"])
            datos_a_mostrar_actividades_mas['Nombre actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Nombre actividad económica"])
            datos_a_mostrar_actividades_mas['Total ingresos netos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Total ingresos netos"])
            datos_a_mostrar_actividades_mas['Total saldo a pagar'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Total saldo a pagar"])
            datos_a_mostrar_actividades_mas['Total saldo a favor'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Total saldo a favor"])
            datos_a_mostrar_actividades_mas['Total costos y gastos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_mas"]["Total costos y gastos"])
            
            datos_a_mostrar_actividades_menos['Código actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Código actividad económica"])
            datos_a_mostrar_actividades_menos['Nombre actividad económica'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Nombre actividad económica"])
            datos_a_mostrar_actividades_menos['Total ingresos netos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Total ingresos netos"])
            datos_a_mostrar_actividades_menos['Total saldo a pagar'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Total saldo a pagar"])
            datos_a_mostrar_actividades_menos['Total saldo a favor'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Total saldo a favor"])
            datos_a_mostrar_actividades_menos['Total costos y gastos'].append(dict_sectores[sector]["Subsectores"][dict_sectores[sector]["Subs_menos_codigo"]]["Act_menos"]["Total costos y gastos"])

            tabla_mas_menos = tabulate(datos_a_mostrar_actividades_mas.items(), headers= "firstrow", tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None])
            tabla_menos_menos = tabulate(datos_a_mostrar_actividades_menos.items(), headers= "firstrow", tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None])
            
            data_a_mostrar_tabla3['Actividad económica que más aportó'] = tabla_mas_menos
            data_a_mostrar_tabla3['Actividad económica que menos aportó'] = tabla_menos_menos
            
            lista_datos3.append(data_a_mostrar_tabla3)                        
        

    return lista_datos, lista_datos2, lista_datos3



def req_7(datos_anio,n, anio_inicial, anio_final):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    llaves_a_incluir = ['Año',
                        'Código actividad económica',
                        'Nombre actividad económica',
                        'Código sector económico',
                        'Nombre sector económico',
                        'Código subsector económico',
                        'Nombre subsector económico',
                        'Total ingresos netos',
                        'Total costos y gastos',
                        'Total saldo a pagar',
                        'Total saldo a favor']
    #ordena por año los datos y elimina los de los años que no son pedidos
    selector_de_periodo(datos_anio, anio_inicial, anio_final)
    #organiza los datos por sus costos y gastos totales de menor a mayor
    for anio in datos_anio:
        sort(datos_anio[anio], "MergeSort", cmp_by_CyG_totales)
        #crea un nuevo diccionario donde se pondrán los top n datos que se piden
        nuevo_dict = {}
        i=0
        #agrega los top n elementos pedidos
        for elemento in datos_anio[anio]["data"]["elements"]:
            if elemento['info']['Código actividad económica'] not in nuevo_dict:
                nuevo_dict[elemento['info']['Código actividad económica']] = {"Total costos y gastos": 0, "Datos": []}                
                nuevo_dict[elemento['info']['Código actividad económica']]["Total costos y gastos"] += int(elemento['info']["Total costos y gastos"])
                nuevo_dict[elemento['info']['Código actividad económica']]["Datos"].append(elemento)
                i+=1
                if i >= n:
                    break
        datos_anio[anio] = nuevo_dict
    #Crea un nuevo diccionario para filtrar las llaves que se necesitan
    datos_anio2 = {}
    for anio, data in datos_anio.items():
        datos_anio2[anio] = {}
        for codigo,info in data.items():
            for dato in info['Datos']:
                codigo = dato['info']['Código actividad económica']
                diccionario_actividad = {}
                for llave in llaves_a_incluir:
                    diccionario_actividad[llave] = dato['info'][llave]
                datos_anio2[(dato['info']['Año'])][codigo] = diccionario_actividad

        
    return datos_anio2
    
    


def req_8(datos_anio_1, n, anio_inicial, anio_final):
    
    llaves_a_incluir = ['Código actividad económica',
                        'Nombre actividad económica',
                        'Total Impuesto a cargo',
                        'Total ingresos netos',
                        'Total costos y gastos',
                        'Total saldo a pagar',
                        'Total saldo a favor']
    
    #Organiza los datos por año y elimina los que no se piden.
    selector_de_periodo(datos_anio_1, anio_inicial, anio_final)
    
    if len(datos_anio_1)==0:
        return 1
    datos_por_periodo_ingresado = new_data_structs('ARRAY_LIST', cmp_impuestos_by_nombre_subsector)
    subsectores = {}
    
    #une todos los datos del periodo solicitado en una sola estructura de datos
    for anio in datos_anio_1:
        for i in range(data_size(datos_anio_1[anio])):
            dato = lt.getElement(datos_anio_1[anio]['data'], i+1)
            add_data(datos_por_periodo_ingresado, dato['info'], i)
    
    #ordena los datos alfabéticamente por nombre del subsector
    sort(datos_por_periodo_ingresado, 'MergeSort', cmp_impuestos_by_nombre_subsector)
    
    #para cada subsector presente en el periodo se crea un datastructure que contiene todos los datos de ese sector.
    for i in range(data_size(datos_por_periodo_ingresado)):
        dato = lt.getElement(datos_por_periodo_ingresado['data'], i+1)
        if dato['info']['Código subsector económico'] not in subsectores:
            subsectores[dato['info']['Código subsector económico']] = new_data_structs('ARRAY_LIST', cmp_by_total_impuestos_a_cargo)
        add_data(subsectores[dato['info']['Código subsector económico']], dato['info'], i)
        
    #Se crea un nuevo diccionario para cada subsector que contenga la información pedida.
    for subsector in subsectores:
        #Se ordenan los datos de cada subsector por total de impuestos a cargo
        sort(subsectores[subsector], 'MergeSort', cmp_by_total_impuestos_a_cargo)
        nuevo_dict_subsector = {'Código sector económico': '',
                                'Nombre sector económico': '',
                                'Código subsector económico': '',
                                'Nombre subsector económico': '',
                                'Total de impuestos a cargo para el subsector':0,
                                'Total de ingresos netos para el subsector': 0,
                                'Total de costos y gastos para el subsector': 0,
                                'Total saldo por pagar para el subsector':0,
                                'Total saldo a favor para el subsector': 0,
                                'Actividades económicas a mostrar': []}
        #se recorre todo el subsector y se van sumando los parámetros pedidos en el nuevo diccionario.
        for i in range(data_size(subsectores[subsector])):
            dato = lt.getElement(subsectores[subsector]['data'], i+1)
            info = dato['info']
            nuevo_dict_subsector['Total de impuestos a cargo para el subsector']+= int(info['Total Impuesto a cargo'])
            nuevo_dict_subsector['Total de ingresos netos para el subsector']+= int(info['Total ingresos netos']) 
            nuevo_dict_subsector['Total de costos y gastos para el subsector']+= int(info['Total costos y gastos'])
            nuevo_dict_subsector['Total saldo por pagar para el subsector']+= int(info['Total saldo a pagar'])
            nuevo_dict_subsector['Total saldo a favor para el subsector']+= int(info['Total saldo a favor'])
            
        #Como los datos ya están organizados por nombre de subsector y por impuestos a cargo (de mayor a menor), se seleccionan n primeros de cada subsector.
        #Si en el subsector hay <n datos, se toman todos los que existan.
        size = data_size(subsectores[subsector])
        if n>size:
            subsector_actualizado = lt.subList(subsectores[subsector]['data'], 1, size)
        else: 
            subsector_actualizado = lt.subList(subsectores[subsector]['data'], 1, n)
            
        #Como todos los datos del subsector tienen el mismo codigo y nombre de sector y subsector, se toma los del primero para pasarlos como identificador del subsector.
        primer_dato_subsector = lt.getElement(subsector_actualizado, 1)
        nuevo_dict_subsector['Código sector económico'] = primer_dato_subsector['info']['Código sector económico']
        nuevo_dict_subsector['Nombre sector económico'] = primer_dato_subsector['info']['Nombre sector económico']
        nuevo_dict_subsector['Código subsector económico'] = primer_dato_subsector['info']['Código subsector económico']
        nuevo_dict_subsector['Nombre subsector económico'] = primer_dato_subsector['info']['Nombre subsector económico']
        
        #Se seleccionan las columnas pedidas para el top n de las actividades ec. a mostrar.
        if n>size:
            for i in range(size):
                new_data = {}
                dato = lt.getElement(subsector_actualizado, i+1)
                for j in range(len(llaves_a_incluir)):
                    new_data[llaves_a_incluir[j]]=dato['info'][llaves_a_incluir[j]]
                nuevo_dict_subsector['Actividades económicas a mostrar'].append(new_data)    
            subsectores[subsector] = nuevo_dict_subsector
        else:
            for i in range(n):
                new_data = {}
                dato = lt.getElement(subsector_actualizado, i+1)
                for j in range(len(llaves_a_incluir)):
                    new_data[llaves_a_incluir[j]]=dato['info'][llaves_a_incluir[j]]
                nuevo_dict_subsector['Actividades económicas a mostrar'].append(new_data)
            subsectores[subsector] = nuevo_dict_subsector
            #se actualiza el subsector en el diccionarioo de subsectores.
    return subsectores

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if int(data_1["id"]) > int(data_2["id"]):
        return 1
    elif int(data_1["id"]) < int(data_2["id"]):
        return -1
    else:
        return 0

def cmp_impuestos_by_anio_menor_mayor(impuesto1, impuesto2):
    if int(impuesto1['info']['Año'])<int(impuesto2['info']['Año']):
        return True
    else: 
        return False

def cmp_impuestos_by_sector(impuesto1, impuesto2):
    if int(impuesto1['info']['Código sector económico'])<int(impuesto2['info']['Código sector económico']):
        return True
    else: 
        return False

def cmp_impuestos_by_anio_mayor_menor(impuesto1, impuesto2):
    if int(impuesto1['info']['Año'])>int(impuesto2['info']['Año']):
        return True
    else: 
        return False

def cmp_impuestos_by_CAE(impuesto1, impuesto2): 
    """ Devuelve verdadero (True) si el año de impuesto1 es menor 
    que el de impuesto2, en caso de que sean iguales tenga en cuenta 
    el código de la actividad económica, de lo contrario devuelva falso (False). 
    
    Args: 
        impuesto1: información del primer registro de impuestos que incluye el “Año” 
            y el “Código actividad económica” 
        impuesto2: información del segundo registro de 
            impuestos que incluye el “Año” y el “Código actividad económica” """ 
            
    return sort_criteria_1(impuesto1, impuesto2)
   
     
def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2): 
    """ Devuelve verdadero (True) si el año de impuesto1 es menor 
    que el de impuesto2, en caso de que sean iguales tenga en cuenta 
    el código de la actividad económica, de lo contrario devuelva falso (False). 
    
    Args: 
        impuesto1: información del primer registro de impuestos que incluye el “Año” 
            y el “Código actividad económica” 
        impuesto2: información del segundo registro de 
            impuestos que incluye el “Año” y el “Código actividad económica” """ 
            
    if int(impuesto1['info']['Año'])<int(impuesto2['info']['Año']):
        return True
    elif int(impuesto1['info']['Año'])==int(impuesto2['info']['Año']):
        return sort_criteria_1(impuesto1, impuesto2)
    else:
        return False     
    
def compare_by_code(data_1, data_2):
    if data_1['info']['Código actividad económica'] > data_1['info']['Código actividad económica']:
        return 1
    else:
        return -1
    
def cmp_impuestos_by_subsector(impuesto1, impuesto2):
    if int(impuesto1['info']['Código subsector económico'])<int(impuesto2['info']['Código subsector económico']):
        return True
    else: 
        return False

def cmp_impuestos_by_nombre_subsector(impuesto1, impuesto2):
    nombre_1 = impuesto1['info']['Nombre subsector económico']
    nombre_2 = impuesto2['info']['Nombre subsector económico']
    if nombre_1.lower()<=nombre_2.lower():
        return True
    else: 
        return False
    
def cmp_impuestos_by_Total_CGN(impuesto1, impuesto2):
    if int(impuesto1['info']['Costos y gastos nómina'])<int(impuesto2['info']['Costos y gastos nómina']):
        return True
    else: 
        return False

def cmp_datastuctures_by_Total_CGN(datastructure_1, datastructure_2):
    cgn1 = int(datastructure_1['info']['id'])
    cgn2 = int(datastructure_2['info']['id'])
    if cgn1 > cgn2:
        return True
    else:
        return False

def cmp_by_CyG_totales(impuesto1, impuesto2):
    if int(impuesto1['info']['Total costos y gastos'])<int(impuesto2['info']['Total costos y gastos']):
        return True
    else: 
        return False
    

def cmp_by_descuentos_tributarios_menor_mayor(impuesto1, impuesto2):
    if int(impuesto1['info']['Descuentos tributarios'])<int(impuesto2['info']['Descuentos tributarios']):
        return True
    else:
        return False

def cmp_datastuctures_by_total_descuentos_tributarios(datastructure_1, datastructure_2):
    cgn1 = int(datastructure_1['info']['id'])
    cgn2 = int(datastructure_2['info']['id'])
    if cgn1 > cgn2:
        return True
    else:
        return False

def cmp_by_total_impuestos_a_cargo(impuesto1, impuesto2):
    if int(impuesto1['info']['Total Impuesto a cargo'])>int(impuesto2['info']['Total Impuesto a cargo']):
        return True
    else:
        return False
    
def cmp_by_descuentos_tributarios_mayor_menor(impuesto1, impuesto2):
    if int(impuesto1['info']['Descuentos tributarios'])>int(impuesto2['info']['Descuentos tributarios']):
        return True
    else:
        return False

def cmp_by_retenciones(impuesto1, impuesto2):
    if int(impuesto1["info"]["Total retenciones"]) < int(impuesto2["info"]["Total retenciones"]):
        return True
    else:
        return False
def cmp_datastuctures_by_retenciones(datastructure_1, datastructure_2):
    retenciones_1 = int(datastructure_1['info']['id'])
    retenciones_2 = int(datastructure_2['info']['id'])
    if retenciones_1 < retenciones_2:
        return True
    else:
        return False

def cmp_by_ingresos_netos(impuesto1, impuesto2):
    if int(impuesto1["info"]["Total ingresos netos"]) < int(impuesto2["info"]["Total ingresos netos"]):
        return True
    else:
        return False 
# Funciones de ordenamiento



def sort_criteria_1(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Usado para la comparación de códigos de actividad económica que tienen varios valores.

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    codigo_1 = data_1['info']['Código actividad económica'] 
    codigo_2 = data_2['info']['Código actividad económica']
    centinela = True
    digitos = ['0','1','2','3','4','5','6','7','8','9']
    codigo_1_final = ""
    i=0
    while i < len(codigo_1) and centinela:
        if codigo_1[i] in digitos:
            codigo_1_final = codigo_1_final + codigo_1[i]
        else:
            centinela = False
        i+=1
    centinela = True
    codigo_2_final = ""
    i=0
    while i < len(codigo_2) and centinela:
        if codigo_2[i] in digitos:
            codigo_2_final = codigo_2_final + codigo_2[i]
        else:
            centinela = False
        i+=1
    return int(codigo_1_final) <= int(codigo_2_final)


def sort(data_structs, algorithm, cmpfunction):
    """
    Función encargada de ordenar la lista con los datos
    """
    if algorithm == 'Selection':
        se.sort(data_structs["data"], cmpfunction)
    elif algorithm == 'Insertion':
        ins.sort(data_structs["data"], cmpfunction)
    elif algorithm == 'Shell':
        sa.sort(data_structs["data"], cmpfunction)
    elif algorithm == "MergeSort":
        merg.sort(data_structs["data"], cmpfunction)
    elif algorithm == "QuickSort":
        quk.sort(data_structs["data"], cmpfunction)
        


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