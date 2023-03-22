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
from tabulate import tabulate

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(data_type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None
    }

    data_structs["data"] = lt.newList(datastructure=data_type)
    return data_structs

def sublistas(lst,pos,num):
    return lt.subList(lst,pos,num)

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], 
    data["Código actividad económica"], 
    data["Nombre actividad económica"], 
    data["Código sector económico"], 
    data["Nombre sector económico"], 
    data["Código subsector económico"], 
    data["Nombre subsector económico"], 
    data["Total ingresos netos"], 
    data["Total costos y gastos"], 
    data["Total saldo a pagar"], 
    data["Total saldo a favor"],
    data["Total retenciones"],
    data["Costos y gastos nómina"],
    data["Total Impuesto a cargo"],
    data["Descuentos tributarios"])

    lt.addLast(data_structs["data"], d)

    return data_structs


# Funciones para creacion de datos

def new_data(Año, Cod_act_eco, Nom_act_econ, Cod_sec_eco, Nom_sec_eco, Cod_sub_eco, Nom_sub_eco, Tta_ing_net, Tta_cost_gas, Tta_sld_pag, Tta_sld_fav, Tta_ret, Cos_nom, Tta_impuesto_cargo, Des_Tri):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {"Año":Año, 
    "Código actividad económica":Cod_act_eco,
    "Nombre actividad económica":Nom_act_econ,
    "Código sector económico":Cod_sec_eco, 
    "Nombre sector económico":Nom_sec_eco, 
    "Código subsector económico":Cod_sub_eco,
    "Nombre subsector económico":Nom_sub_eco, 
    "Total ingresos netos":Tta_ing_net, 
    "Total costos y gastos":Tta_cost_gas,  
    "Total saldo a pagar":Tta_sld_pag, 
    "Total saldo a favor":Tta_sld_fav,
    "Total retenciones": Tta_ret,
     "Costos y gastos nómina": Cos_nom,
     "Total Impuesto a cargo": Tta_impuesto_cargo,
     "Descuentos tributarios": Des_Tri}

    return data

# Funciones de consulta

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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 
    
    size = lt.size(data_structs["data"])
   
    lista = lt.newList(datastructure="ARRAY_LIST",cmpfunction = compare2)
    
    for i in range(1,size + 1):
        x = lt.getElement(data_structs["data"],i)
        
        estar = lt.isPresent(lista, x["Año"])
        
        if estar == 0:
            lt.addLast(lista, x)

        if estar >0:
            if int(x["Total saldo a pagar"]) > int(lt.getElement(lista,estar)["Total saldo a pagar"]):
                lt.changeInfo(lista,estar,x)
                
    
    

    return lista


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    size = lt.size(data_structs["data"])
   
    lista = lt.newList(datastructure="ARRAY_LIST",cmpfunction = compare2)
    
    for i in range(1,size + 1):
        x = lt.getElement(data_structs["data"],i)
        
        estar = lt.isPresent(lista, x["Año"])
        
        if estar == 0:
            lt.addLast(lista, x)

        if estar >0:
            if int(x["Total saldo a favor"]) > int(lt.getElement(lista,estar)["Total saldo a favor"]):
                lt.changeInfo(lista,estar,x)
                
    
    return lista


def subsectores_sumas(data_structs):
     """
     Esta funcion se encarga de sumar los elementos de los subsectores por medio de un diccionario
     """

     dic = {}
     for elemento in lt.iterator(data_structs["data"]):
        anio = elemento["Año"]
        total_retenciones = int(elemento["Total retenciones"])
        total_ingresos = int(elemento["Total ingresos netos"])
        total_costos_gastos = int(elemento["Total costos y gastos"])
        total_saldo_pagar = int(elemento["Total saldo a pagar"])
        total_saldo_favor = int(elemento["Total saldo a favor"])
        total_nomina = int(elemento["Costos y gastos nómina"])
        total_impuesto = int(elemento["Total Impuesto a cargo"])
        descuento = int(elemento["Descuentos tributarios"])
        

        if anio not in dic.keys():
            dic[anio] = {}

            if elemento["Código subsector económico"] not in dic[anio]:
                dic[anio][elemento["Código subsector económico"]] = {'Año': anio, 'Código sector económico': elemento["Código sector económico"], 'Nombre sector económico': elemento["Nombre sector económico"], 
                         'Código subsector económico': elemento["Código subsector económico"], 'Nombre subsector económico': elemento["Nombre subsector económico"],
                         'Total de costos y gastos nomina del subsector economico': total_nomina , 'Total ingresos netos del subsector economico': total_ingresos, 
                         'Total costos y gastos del subsector': total_costos_gastos, 'Total saldo a pagar del subsector': total_saldo_pagar, 
                         'Total saldo a favor del subsector': total_saldo_favor, 'Total de retenciones del subsector economico': total_retenciones,'Total de impuestos a cargo para el subsector': total_impuesto,
                         "Total de descuentos tributarios del subsector economico": descuento}
                
            else:
                dic[anio][elemento["Código subsector económico"]]["Total de costos y gastos nomina del subsector economico"]+=total_nomina
                dic[anio][elemento["Código subsector económico"]]["Total ingresos netos del subsector economico"]+=total_ingresos
                dic[anio][elemento["Código subsector económico"]]["Total costos y gastos del subsector"]+=total_costos_gastos
                dic[anio][elemento["Código subsector económico"]]["Total saldo a pagar del subsector"]+=total_saldo_pagar
                dic[anio][elemento["Código subsector económico"]]["Total saldo a favor del subsector"]+=total_saldo_favor
                dic[anio][elemento["Código subsector económico"]]["Total de retenciones del subsector economico"]+=total_retenciones
                dic[anio][elemento["Código subsector económico"]]["Total de impuestos a cargo para el subsector"]+=total_impuesto
                dic[anio][elemento["Código subsector económico"]]["Total de descuentos tributarios del subsector economico"]+=descuento
                
        else:
            if elemento["Código subsector económico"] not in dic[anio]:
                dic[anio][elemento["Código subsector económico"]] = {'Año': anio, 'Código sector económico': elemento["Código sector económico"], 'Nombre sector económico': elemento["Nombre sector económico"], 
                         'Código subsector económico': elemento["Código subsector económico"], 'Nombre subsector económico': elemento["Nombre subsector económico"],
                         'Total de costos y gastos nomina del subsector economico': total_nomina , 'Total ingresos netos del subsector economico': total_ingresos, 
                         'Total costos y gastos del subsector': total_costos_gastos, 'Total saldo a pagar del subsector': total_saldo_pagar, 
                         'Total saldo a favor del subsector': total_saldo_favor, 'Total de retenciones del subsector economico': total_retenciones,'Total de impuestos a cargo para el subsector': total_impuesto,
                         "Total de descuentos tributarios del subsector economico": descuento}
                
            else:
                dic[anio][elemento["Código subsector económico"]]["Total de costos y gastos nomina del subsector economico"]+=total_nomina
                dic[anio][elemento["Código subsector económico"]]["Total ingresos netos del subsector economico"]+=total_ingresos
                dic[anio][elemento["Código subsector económico"]]["Total costos y gastos del subsector"]+=total_costos_gastos
                dic[anio][elemento["Código subsector económico"]]["Total saldo a pagar del subsector"]+=total_saldo_pagar
                dic[anio][elemento["Código subsector económico"]]["Total saldo a favor del subsector"]+=total_saldo_favor
                dic[anio][elemento["Código subsector económico"]]["Total de retenciones del subsector economico"]+=total_retenciones
                dic[anio][elemento["Código subsector económico"]]["Total de impuestos a cargo para el subsector"]+=total_impuesto
                dic[anio][elemento["Código subsector económico"]]["Total de descuentos tributarios del subsector economico"]+=descuento

     return dic



def organizar_retenciones(data_structs):
     """
     Esta funcion se encarga de organziar las retenciones por la funcion de comparacion indicada
     """
     
     dic = subsectores_sumas(data_structs)

     lista_sub_ordenada = lt.newList(datastructure="ARRAY_LIST")
     
     for anio in dic:
        for cod in dic[anio]:
            lt.addLast(lista_sub_ordenada,dic[anio][cod])

     merg.sort(lista_sub_ordenada,cmp_impuestos_by_retenciones_sub)

     return lista_sub_ordenada

def organizar_nomina(data_structs):
     
     dic = subsectores_sumas(data_structs)

     lista_sub_ordenada = lt.newList(datastructure="ARRAY_LIST")
     
     for anio in dic:
        for cod in dic[anio]:
            lt.addLast(lista_sub_ordenada,dic[anio][cod])

     merg.sort(lista_sub_ordenada,cmp_impuestos_by_nomina_sub)

     return lista_sub_ordenada

def organizar_impuesto_cargo(data_structs,anio_inicial,anio_final):
     
     dic = subsectores_sumas(data_structs)

     lista_sub_impuestos = lt.newList(datastructure="ARRAY_LIST")
     anio1 = int(anio_inicial)
     anio2 = int(anio_final)
     for anio in dic:
        if int(anio) in range(anio1,anio2+1):
            for cod in dic[anio]:
                lt.addLast(lista_sub_impuestos,dic[anio][cod])

     return lista_sub_impuestos

def organizar_descuento(data_structs):

    dic = subsectores_sumas(data_structs)

    lista_sub_ordenada = lt.newList(datastructure="ARRAY_LIST")
     
    for anio in dic:
        for cod in dic[anio]:
            lt.addLast(lista_sub_ordenada,dic[anio][cod])

    merg.sort(lista_sub_ordenada,cmp_impuestos_by_descuento_sub)

    return lista_sub_ordenada



def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    lista_sub = organizar_retenciones(data_structs)
    lista_min = lt.newList(datastructure="ARRAY_LIST",cmpfunction=compare2)
    
    for elemento in lt.iterator(lista_sub):
        estar = lt.isPresent(lista_min, elemento["Año"])
        
        if estar == 0:
            lt.addLast(lista_min, elemento)

    tabla_grande = []
    table = []

    for subsector in lt.iterator(lista_min):
        cod = subsector["Código subsector económico"]
        anio = subsector["Año"]
        
        lista = lt.newList(datastructure="ARRAY_LIST")
        for elemento in lt.iterator(data_structs["data"]):
            if elemento["Año"] == anio and elemento["Código subsector económico"] == cod:
                lt.addLast(lista,elemento)
        
        if lt.size(lista) > 1:    
            merg.sort(lista,cmp_impuestos_by_retencion_act)

        if lt.size(lista) <= 6:
             for elemento in lista["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total retenciones"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)

        else:
    
            peores = lt.subList(lista,1,3)
            mejores = lt.subList(lista,lt.size(lista)-3,3)
    
            for elemento in peores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total retenciones"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
            for elemento in mejores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total retenciones"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
        
    return lista_min, tabla_grande


def req_4(data_structs):
    """"
    Funcion que soluciona el requerimiento 4
    """

    lista_sub = organizar_nomina(data_structs)
    lista_max = lt.newList(datastructure="ARRAY_LIST",cmpfunction=compare2)
    
    for elemento in lt.iterator(lista_sub):
        estar = lt.isPresent(lista_max, elemento["Año"])
        
        if estar == 0:
            lt.addLast(lista_max, elemento)

        if estar >0:
            if int(elemento["Total de costos y gastos nomina del subsector economico"]) > int(lt.getElement(lista_sub,estar)["Total de costos y gastos nomina del subsector economico"]):
                lt.changeInfo(lista_max,estar,elemento)

    tabla_grande = []
    table = []

    for subsector in lt.iterator(lista_max):
        cod = subsector["Código subsector económico"]
        anio = subsector["Año"]
        
        lista = lt.newList(datastructure="ARRAY_LIST")
        for elemento in lt.iterator(data_structs["data"]):
            if elemento["Año"] == anio and elemento["Código subsector económico"] == cod:
                lt.addLast(lista,elemento)
        
        if lt.size(lista) > 1:    
            merg.sort(lista,cmp_impuestos_by_nomina_act)

        if lt.size(lista) <= 6:
             for elemento in lista["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Costos y gastos nómina"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)

        else:
    
            peores = lt.subList(lista,1,3)
            mejores = lt.subList(lista,lt.size(lista)-3,3)
    
            for elemento in peores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Costos y gastos nómina"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
            for elemento in mejores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Costos y gastos nómina"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
        
    
    return lista_max, tabla_grande



def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    lista_sub = organizar_descuento(data_structs)
    lista_max = lt.newList(datastructure="ARRAY_LIST",cmpfunction=compare2)
    
    for elemento in lt.iterator(lista_sub):
        estar = lt.isPresent(lista_max, elemento["Año"])
        
        if estar == 0:
            lt.addLast(lista_max, elemento)

        if estar >0:
            if int(elemento["Total de impuestos a cargo para el subsector"]) > int(lt.getElement(lista_sub,estar)["Total de impuestos a cargo para el subsector"]):
                lt.changeInfo(lista_max,estar,elemento)

    tabla_grande = []
    table = []

    for subsector in lt.iterator(lista_max):
        cod = subsector["Código subsector económico"]
        anio = subsector["Año"]
        
        lista = lt.newList(datastructure="ARRAY_LIST")
        for elemento in lt.iterator(data_structs["data"]):
            if elemento["Año"] == anio and elemento["Código subsector económico"] == cod:
                lt.addLast(lista,elemento)
        
        if lt.size(lista) > 1:    
            merg.sort(lista,cmp_by_descuento_act)

        if lt.size(lista) <= 6:
             for elemento in lista["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Descuentos tributarios"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)

        else:
    
            peores = lt.subList(lista,1,3)
            mejores = lt.subList(lista,lt.size(lista)-3,3)
    
            for elemento in peores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Descuentos tributarios"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
            for elemento in mejores["elements"]:
                table = [elemento["Año"],elemento["Código subsector económico"],elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Descuentos tributarios"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)
        
    
    return lista_max, tabla_grande


def req_6(data_structs, year = 2019):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6

    anio = lt.newList("ARRAY_LIST")
    
    for act_eco in lt.iterator(data_structs["data"]):
        if int(act_eco["Año"]) == year:
            lt.addLast(anio, act_eco)
            
    sectores = lt.newList("ARRAY_LIST")
    cod_sectores = lt.newList("ARRAY_LIST")
        
    for actividad in lt.iterator(anio):
        if actividad["Código sector económico"] not in lt.iterator(cod_sectores):
            lt.addLast(cod_sectores, actividad["Código sector económico"])
            sector = lt.newList("ARRAY_LIST")
            lt.addLast(sector, actividad["Código sector económico"])
            actividades = lt.newList("ARRAY_LIST")
            lt.addLast(actividades, actividad)
            lt.addLast(sector, actividades)
            lt.addLast(sectores, sector)
        else:
            for sec in lt.iterator(sectores):
                if int(lt.firstElement(sec)) == int(actividad["Código sector económico"]):
                    lt.addLast(lt.getElement(sec, 2), actividad)
                    
    for sect in lt.iterator(sectores):
        sum_in = 0
        sum_cg = 0
        sum_sp = 0
        sum_sf = 0
        for act in lt.iterator(lt.getElement(sect, 2)):
            sum_in = sum_in + int(act["Total ingresos netos"])
            sum_cg = sum_cg + int(act["Total costos y gastos"])
            sum_sp = sum_sp + int(act["Total saldo a pagar"])
            sum_sf = sum_sf + int(act["Total saldo a favor"])
        lt.addLast(sect, sum_in)
        lt.addLast(sect, sum_cg)
        lt.addLast(sect, sum_sp)
        lt.addLast(sect, sum_sf)
        
    sector_max = lt.firstElement(sectores)
    
    for s in lt.iterator(sectores):
        if int(lt.getElement(s, 3)) > int(lt.getElement(sector_max, 3)):
            sector_max = s
            
    sub_sectores = lt.newList("ARRAY_LIST")
    cod_subsectores = lt.newList("ARRAY_LIST")
        
    for actividad in lt.iterator(lt.getElement(sector_max, 2)):
        if not actividad["Código subsector económico"] in lt.iterator(cod_subsectores):
            lt.addLast(cod_subsectores, actividad["Código subsector económico"])
            subsector = lt.newList("ARRAY_LIST")
            lt.addLast(subsector, actividad["Código subsector económico"])
            actividades = lt.newList("ARRAY_LIST")
            lt.addLast(actividades, actividad)
            lt.addLast(subsector, actividades)
            lt.addLast(sub_sectores, subsector)
        else:
            for sec in lt.iterator(sub_sectores):
                if int(lt.firstElement(sec)) == int(actividad["Código subsector económico"]):
                    lt.addLast(lt.getElement(sec, 2), actividad)
                    
    for subsect in lt.iterator(sub_sectores):
        sum_in = 0
        sum_cg = 0
        sum_sp = 0
        sum_sf = 0
        for act in lt.iterator(lt.getElement(subsect, 2)):
            sum_in = sum_in + int(act["Total ingresos netos"])
            sum_cg = sum_cg + int(act["Total costos y gastos"])
            sum_sp = sum_sp + int(act["Total saldo a pagar"])
            sum_sf = sum_sf + int(act["Total saldo a favor"])
        lt.addLast(subsect, sum_in)
        lt.addLast(subsect, sum_cg)
        lt.addLast(subsect, sum_sp)
        lt.addLast(subsect, sum_sf)
     
    merg.sort(sub_sectores, cmp_t_ing)

    sub_max = lt.firstElement(sub_sectores)
    sub_min = lt.lastElement(sub_sectores)

    merg.sort(lt.getElement(sub_max, 2), compere_actividad)
    merg.sort(lt.getElement(sub_min, 2), compere_actividad)
    
    max_act = (lt.firstElement(lt.getElement(sub_max, 2)), lt.lastElement(lt.getElement(sub_max, 2)))
    min_act = (lt.firstElement(lt.getElement(sub_min, 2)), lt.lastElement(lt.getElement(sub_min, 2)))

    return sector_max, sub_max, sub_min, max_act, min_act


def req_7(data_structs,n,anio_inicial,anio_final):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7

    anio1 = int(anio_inicial)
    anio2 = int(anio_final)

    lista = lt.newList(datastructure="ARRAY_LIST")

    
    for elemento in lt.iterator(data_structs["data"]):
        if int(elemento["Año"]) in range(anio1,anio2+1):
            lt.addLast(lista,elemento)
    
    merg.sort(lista,cmp_impuestos_by_costos_gastos_act)

    sublista = lt.subList(lista,1,n)
    merg.sort(sublista,cmp_impuestos_by_costos_gastos_act_anio)

    return sublista



def req_8(data_structs,n,anio_inicial,anio_final):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    
    lista_cod_disjuntos = organizar_impuesto_cargo(data_structs,anio_inicial,anio_final)
    lista_cod_unidos = lt.newList(datastructure="ARRAY_LIST")
    merg.sort(lista_cod_disjuntos,cmp_by_cod)

    num = int(n)

    anio1 = int(anio_inicial)
    anio2 = int(anio_final)

    for elemento in lt.iterator(lista_cod_disjuntos):
    
        if lt.size(lista_cod_unidos) <1:
            lt.addLast(lista_cod_unidos,elemento)

        else:
            i = lt.size(lista_cod_unidos)
            if elemento["Código sector económico"] == lt.getElement(lista_cod_unidos,i)["Código sector económico"]:
                costos_gastos = elemento["Total costos y gastos del subsector"] + int(lt.getElement(lista_cod_unidos,i)["Total costos y gastos del subsector"])
                ingresos = elemento["Total ingresos netos del subsector economico"] + int(lt.getElement(lista_cod_unidos,i)["Total ingresos netos del subsector economico"])
                saldo_pagar = elemento["Total saldo a pagar del subsector"] + int(lt.getElement(lista_cod_unidos,i)["Total saldo a pagar del subsector"])
                saldo_favor = elemento["Total saldo a favor del subsector"] + int(lt.getElement(lista_cod_unidos,i)["Total saldo a favor del subsector"])
                impuestos = elemento["Total de impuestos a cargo para el subsector"] + int(lt.getElement(lista_cod_unidos,i)["Total de impuestos a cargo para el subsector"])
                dic = {'Código sector económico': elemento["Código sector económico"], 'Nombre sector económico': elemento["Nombre sector económico"], 
                         'Código subsector económico': elemento["Código subsector económico"], 'Nombre subsector económico': elemento["Nombre subsector económico"],
                         'Total ingresos netos del subsector economico': ingresos, 
                         'Total costos y gastos del subsector': costos_gastos, 'Total saldo a pagar del subsector': saldo_pagar, 
                         'Total saldo a favor del subsector': saldo_favor, 'Total de impuestos a cargo para el subsector': impuestos}
                lt.changeInfo(lista_cod_unidos,i,dic)
            else:
                lt.addLast(lista_cod_unidos,elemento)

    merg.sort(lista_cod_unidos,cmp_by_letra)

    headers = ["Código actividad económica","Nombre actividad económica","Total Impuesto a cargo", 
                   "Total ingresos netos","Total saldo a pagar","Total saldo a favor"]

    for subsector in lt.iterator(lista_cod_unidos):
        cod = subsector["Código subsector económico"]
        tabla_grande = []
        table = []
        lista = lt.newList(datastructure="ARRAY_LIST")
        for elemento in lt.iterator(data_structs["data"]):
            if elemento["Código subsector económico"] == cod and int(elemento["Año"]) in range(anio1,anio2+1):
                lt.addLast(lista,elemento)
        
        if lt.size(lista) > 1:    
            merg.sort(lista,cmp_total_impuestos_act)

        if lt.size(lista) <= num:
            for elemento in lista["elements"]:
                table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)

            
        elif lt.size(lista)> num:
    
            top = lt.subList(lista,1,num)
            
            for elemento in top["elements"]:
                table = [elemento["Código actividad económica"], elemento["Nombre actividad económica"],
                        elemento["Total Impuesto a cargo"],elemento["Total ingresos netos"],
                        elemento["Total saldo a pagar"],elemento["Total saldo a favor"]]
                tabla_grande.append(table)

        print("La(s)",len(tabla_grande),"actividades economicas que más y menos aportaron en el subsector " + cod + " son: ")

        print(tabulate(tabla_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    return lista_cod_unidos


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar las actividades económicas por el año y por el código de actividad económica.
    """
    if data_1["Año"] < data_2["Año"]:
        return True
    elif data_1["Año"] > data_2["Año"]:
        return False
    
    else:
        if data_1["Código actividad económica"] < data_2["Código actividad económica"]:
            return True
           
        
def compare2(data_1, data_2):
    """
    Función encargada de comparar el año de dos datos.
    """
    if data_1 < data_2["Año"]:
        return -1
    elif data_1 > data_2["Año"]:
        return 1
    
    else:
        return 0
    
    
def compare_subsector(data_1, data_2):
    """
    Función encargada de comparar el año.
    """
    if int(data_1) < int(lt.getElement(data_2,2)["Año"]):
        return -1
    elif int(data_1) > int(lt.getElement(data_2,2)["Año"]):
        return 1
    
    else:
        return 0
    
def compare_subsector2(data_1, data_2):
    """
    Función encargada de comparar dos subsectores por año.
    """
    if data_1["Año"] < data_2:
        return -1
    elif data_1["Año"] > data_2:
        return 1
    
    else:
        return 0
    
def compere_actividad(data1, data2):
    """
    Esta función se encarga de organizar las actividades de mayor a menor dependiendo de su total de ingresos netos.
    """
    
    if int(data1["Total ingresos netos"]) > int(data2["Total ingresos netos"]):
        return True
    else:
        return False

def cmp_impuestos_by_nomina_sub(sub1, sub2):
    """
    Esta función se encarga de organizar los subsectores de menor a mayor dependiendo del año y del total de costos y gastos nómina del subsector.
    """
        
    if sub1["Año"] == sub2["Año"]:
        if sub1["Total de costos y gastos nomina del subsector economico"] < sub2["Total de costos y gastos nomina del subsector economico"]:
            return True
        else:
            return False
    elif sub1["Año"] < sub2["Año"]:
        return True
    else:
        return False
    
def cmp_t_ing(data1, data2):
    if int(lt.getElement(data1, 3)) > int(lt.getElement(data2, 3)):
        return True
    else:
        False  
      
def cmp_impuestos_by_descuento_sub(sub1, sub2):
    """
    Esta función se encarga de organizar los subsectores de menor a mayor dependiendo del año y del total de descuentos tributarios del subsector.
    """
        
    if sub1["Año"] == sub2["Año"]:
        if sub1["Total de descuentos tributarios del subsector economico"] < sub2["Total de descuentos tributarios del subsector economico"]:
            return True
        else:
            return False
    elif sub1["Año"] < sub2["Año"]:
        return True
    else:
        return False
    
def cmp_impuestos_by_retenciones_sub(sub1, sub2):
    """
    Esta funcion se encarga de organizar los subsectores de menor a mayor por total de retenciones del subsector y por su año.
    """
        
    if sub1["Año"] == sub2["Año"]:
        if sub1["Total de retenciones del subsector economico"] < sub2["Total de retenciones del subsector economico"]:
            return True
        else:
            return False
    elif sub1["Año"] < sub2["Año"]:
        return True
    else:
        return False
    
def cmp_impuestos_by_nomina_act(act1, act2):
    """
    Esta funcion se encarga de organizar las actividades economicas de menor a mayor por total de costos y gastos nomina.
    """
    if int(act1["Costos y gastos nómina"]) < int(act2["Costos y gastos nómina"]):
        return True
    else:
        return False
    
def cmp_by_descuento_act(act1, act2):
    """
    Esta funcion se encarga de organizar las actividades de menor a mayor por el total de descuentos tributarios.
    """
    if int(act1["Descuentos tributarios"]) < int(act2["Descuentos tributarios"]):
        return True
    else:
        return False
    
def cmp_total_impuestos_act(act1, act2):
    """
    Esta funcion se enargar de organizar las actividades de mayor a menor por total de impuestos a cargo.
    """
    if int(act1["Total Impuesto a cargo"]) > int(act2["Total Impuesto a cargo"]):
        return True
    else:
        return False
    
def cmp_impuestos_by_retencion_act(act1, act2):
    """
    Esta funcion se enargar de organizar las actividades de menor a mayor por total de retenciones.
    """
    if int(act1["Total retenciones"]) < int(act2["Total retenciones"]):
        return True
    else:
        return False
    
def cmp_impuestos_by_costos_gastos_act(act1, act2):
    """
    Esta funcion se encarga de organizar las actividades de menor a mayor por total de costos y gastos.
    """
   
    if int(act1["Total costos y gastos"]) < int(act2["Total costos y gastos"]):
        return True
    else:
        return False
    
def cmp_impuestos_by_costos_gastos_act_anio(act1, act2):
    """
    Esta funcion se enargar de organizar las actividades de menor a mayor por total de costos y gastos y año.
    """
    if int(act1["Año"]) == int(act2["Año"]):
        if int(act1["Total costos y gastos"]) < int(act2["Total costos y gastos"]):
            return True
        else:
            return False
    elif int(act1["Año"]) > int(act2["Año"]):
        return True
    else:
        return False
    
def cmp_impuestos_cargo_act(act1, act2):
    """
    Esta funcion se enargar de organizar las actividades de mayor a menor por el total de impuestos a cargo.
    """
    if int(act1["Total Impuesto a cargo"]) > int(act2["Total Impuesto a cargo"]):
        return True
    else:
        return False
    
def cmp_by_cod(d1,d2):
    """
    Esta funcion se enargar de organizar las actividades de menor a mayor por su código de sector económico.
    """
    if int(d1["Código sector económico"]) < int(d2["Código sector económico"]):
        return True
    else:
        return False

def cmp_by_letra(d1,d2):
    """
    Esta funcion se enargar de organizar los subsectores económicos por orden alfabético y total de impuestos a cargo.
    """

    if d1["Nombre subsector económico"][0].lower() == d2["Nombre subsector económico"][0].lower():
        if int(d1["Total de impuestos a cargo para el subsector"]) < int(d2["Total de impuestos a cargo para el subsector"]):
            return True
        else:
            return False
        
    elif d1["Nombre subsector económico"][0].lower() < d2["Nombre subsector económico"][0].lower():
        return True
    else:
        return False
    

# Funciones de ordenamiento

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos a partir del año y del código económico.
    """
    merg.sort(data_structs["data"], compare)
    
     
   
