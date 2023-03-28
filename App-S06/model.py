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

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

""" 
FUNCION RELACIONADAS A CARGA DE DATOS
"""

def new_data_structs(estructura):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }
    
    data_structs["data"] = lt.newList(datastructure= f"{estructura}",
                                     cmpfunction=compare)

    return data_structs

    
""" 
FUNCIONES AGREGAR DATOS A LA ESTRUCTURA DE DATOS
"""

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["data"], data)
    
    return data_structs

def new_data(info):
    """
    Crea una nueva estructura para modelar los datos
    """
    
    data = {"Info":None}
    data["Info"] = info
 
    return data


""" 
FUNCIONES DE OBTENER DATOS
"""

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None

""" 
FUNCIONES SIZE
"""

def data_size(data_structs):
    """ 
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


"""
FUNCIONES DE SORT
"""

def SortLista(data_structs,cmpfunction):
    return merg.sort(data_structs,cmpfunction)

""" 
FUNCIONES CMP DE COMPARACIÓN
"""

def cmpCodigoActividadEconomica(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    
    if float(limpiar_datos(data_1["Código actividad económica"])) < float(limpiar_datos(data_2["Código actividad económica"])):
        return True
    else:
        return False

def cmpSubsectorEconomico(data_1, data_2):
    
    if float(limpiar_datos(data_1["Código subsector económico"])) >= float(limpiar_datos(data_2["Código subsector económico"])):
        return True
    
    else:
        return False
    
def cmpSectorEconomico(data_1, data_2):
    if float(limpiar_datos(data_1["Código sector económico"])) <= float(limpiar_datos(data_2["Código sector económico"])):
        return True
    
    else:
        return False
    
def cmpTotalRetenciones(data_1, data_2):
    
    if float(limpiar_datos(data_1["Total retenciones"])) <= float(limpiar_datos(data_2["Total retenciones"])):
        return True
    
    elif float(limpiar_datos(data_1["Total retenciones"])) == float(limpiar_datos(data_2["Total retenciones"])):
        if float(limpiar_datos(data_1["Código actividad económica"])) < float(limpiar_datos(data_2["Código actividad económica"])):
            return True
    else:
        return False
    
def cmpCostosyGastosNomina(data_1, data_2):
    
    if float(limpiar_datos(data_1["Costos y gastos nómina"])) < float(limpiar_datos(data_2["Costos y gastos nómina"])):
        return True
    
    elif float(limpiar_datos(data_1["Costos y gastos nómina"])) == float(limpiar_datos(data_2["Costos y gastos nómina"])):
        if float(limpiar_datos(data_1["Código actividad económica"])) < float(limpiar_datos(data_2["Código actividad económica"])):
            return True
    
    else:
        return False
    
def cmpDescuentosTributarios(data_1, data_2):
    
    if float(limpiar_datos(data_1["Descuentos tributarios"])) < float(limpiar_datos(data_2["Descuentos tributarios"])):
        return True
    
    elif float(limpiar_datos(data_1["Descuentos tributarios"])) == float(limpiar_datos(data_2["Descuentos tributarios"])):
        if float(limpiar_datos(data_1["Código actividad económica"])) < float(limpiar_datos(data_2["Código actividad económica"])):
            return True
        
    else:
        return False

def cmpIngresosNetos(data_1, data_2):
    
    if float(limpiar_datos(data_1["Total ingresos netos"])) <= float(limpiar_datos(data_2["Total ingresos netos"])):
        return True
    
    else:
        return False
    
def cmpTotalCostosGastos(data_1, data_2):
    
    if float(limpiar_datos(data_1["Total costos y gastos"])) <= float(limpiar_datos(data_2["Total costos y gastos"])):
        return True
    
    else:
        return False

def cmpAnio(data_1, data_2):
    
    if float(limpiar_datos(data_1["Año"])) > float(limpiar_datos(data_2["Año"])):
        return True
    
    elif float(limpiar_datos(data_1["Año"])) == float(limpiar_datos(data_2["Año"])):
        
        if float(limpiar_datos(data_1["Total costos y gastos"])) <= float(limpiar_datos(data_2["Total costos y gastos"])):
            return True
         
    else:
        return False
    
""" 
FUNCIONES DE SUBLISTAS
"""

def Sublista(data_structs,pos,numelem):
    return lt.subList(data_structs,pos,numelem)

def ListasPorAnio(data_structs):
    
    Lista_separadas_anio = lt.newList("ARRAY_LIST")
    num_elementos = hasta = 0
    pos = 1
    anio_actual = lt.firstElement(data_structs)["Año"]
    
    for data in lt.iterator(data_structs):
        
        if (data["Año"] == anio_actual):
            num_elementos += 1
            hasta += 1
        
        else:
            sublista = Sublista(data_structs, pos, num_elementos)
            lt.addLast(Lista_separadas_anio,sublista)
            pos = hasta + 1
            hasta += 1
            num_elementos = 1
            anio_actual = data["Año"]
    
    lt.addLast(Lista_separadas_anio, Sublista(data_structs,pos,num_elementos))   
      
    return Lista_separadas_anio

def SubListasPorCriterio(data_structs,criterio):
    
    Lista_separadas_criterio = lt.newList("ARRAY_LIST")
    num_elementos = hasta = 0
    pos = 1
    criterio_actual = lt.firstElement(data_structs)[criterio]
    
    for data in lt.iterator(data_structs):
        
        if (data[criterio] == criterio_actual):
            num_elementos += 1
            hasta += 1
        
        else:
            sublista = Sublista(data_structs, pos, num_elementos)
            lt.addLast(Lista_separadas_criterio,sublista)
            pos = hasta + 1
            hasta += 1
            num_elementos = 1
            criterio_actual = data[criterio]
    
    lt.addLast(Lista_separadas_criterio, Sublista(data_structs,pos,num_elementos))   
      
    return Lista_separadas_criterio

""" 
FUNCION PARA OBTENER LISTA DE AÑO ESPECIFICO
"""

def ObtenerListaConAnio(lista, anio):
    if anio == "2012":
        return lt.getElement(lista , 1)
    if anio == "2013":
        return lt.getElement(lista , 2)
    if anio == "2014":
        return lt.getElement(lista , 3)
    if anio == "2015":
        return lt.getElement(lista , 4)
    if anio == "2016":
        return lt.getElement(lista , 5)
    if anio == "2017":
        return lt.getElement(lista , 6)
    if anio == "2018":
        return lt.getElement(lista , 7)
    if anio == "2019":
        return lt.getElement(lista , 8)
    if anio == "2020":
        return lt.getElement(lista , 9)
    if anio == "2021":
        return lt.getElement(lista , 10)


""" 
FUNCIONES QUE ENCUENTREN MAYOR O MENOR DATO
"""

def MayoresPorAnioConCriterio(lista , criterio):
    
    mayores_por_anio = lt.newList("ARRAY_LIST")
    
    for year in range(2012,2022):
        
        mayor = MayorElementoPorCriterio( ObtenerListaConAnio(lista,str(year)) , criterio)
        lt.addLast(mayores_por_anio , mayor)
   
    return mayores_por_anio

def MayorElementoPorCriterio(lista,criterio):
    
    
    mayor = 0
    dato_retornar = None
    
    for data in lt.iterator(lista):
        
        if float(limpiar_datos(data[criterio])) >= mayor:
            dato_retornar = data
            mayor = float(limpiar_datos(data[criterio]))
    
    return dato_retornar
    
def MenorElementoPorCriterio(lista,criterio):
    
    menor = float(lt.firstElement(lista)[criterio]) + 1
    dato_retornar = None
    
    for data in lt.iterator(lista):
        
        if float(limpiar_datos(data[criterio])) < menor:
            dato_retornar = data
            menor = float(limpiar_datos(data[criterio]))
    
    return dato_retornar

""" 
FUNCIONES PARA EL REQUERIMIENTO 1
"""

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    return MayoresPorAnioConCriterio(ListasPorAnio(data_structs["data"]), "Total saldo a pagar")
    

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    return MayoresPorAnioConCriterio(ListasPorAnio(data_structs["data"]), "Total saldo a favor")
    
    
""" 
FUNCION SUMA COLUMNAS POR CRITERIO
"""
def SumaColumnasPorCriterio(lista,separador,criterio,criterio2,criterio3,criterio4,criterio5):
    
    lista_retornar = lt.newList("ARRAY_LIST")
    num_elementos = pos = i = 1
    suma = suma2 = suma3 = suma4 = suma5 = 0
    separadaor_actual = lt.firstElement(lista)[separador]

    for data in lt.iterator(lista):

        if (data[separador] == separadaor_actual):
            num_elementos +=1
           
            suma += float(limpiar_datos(data[criterio]))
            suma2 += float(limpiar_datos(data[criterio2]))
            suma3 += float(limpiar_datos(data[criterio3]))
            suma4 += float(limpiar_datos(data[criterio4]))
            suma5 += float(limpiar_datos(data[criterio5]))
    
        if (i) == lt.size(lista):
            reemplazo = lt.getElement(lista,pos).copy()
            
            reemplazo[criterio] = suma
            reemplazo[criterio2] = suma2
            reemplazo[criterio3] = suma3
            reemplazo[criterio4] = suma4
            reemplazo[criterio5] = suma5
            lt.addLast(lista_retornar,reemplazo)
            
          
        elif (lt.getElement(lista,i+1)[separador] != separadaor_actual):
            
            reemplazo = lt.getElement(lista,pos).copy()
            reemplazo[criterio] = suma
            reemplazo[criterio2] = suma2
            reemplazo[criterio3] = suma3
            reemplazo[criterio4] = suma4
            reemplazo[criterio5] = suma5
            
            lt.addLast(lista_retornar,reemplazo)
            pos = num_elementos 
            suma = suma2 = suma3 = suma4 = suma5 = 0
            separadaor_actual = lt.getElement(lista,i+1)[separador]
           
        i +=1
        
    return lista_retornar

""" 
FUNCIONES PARA EL REQUERIMIENTO 3,4 y 5
"""
    
def req_3(data_structs):
    
    menor_criterio = lt.newList("ARRAY_LIST")
    sectores_por_anio = lt.newList("ARRAY_LIST")
    listas_de_listas = ListasPorAnio(data_structs["data"])

    
    for i in range(2012,2022):
        
        temp1 = lt.newList("ARRAY_LIST")
        
        data_organizada_subsector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)),cmpSubsectorEconomico)
        Columnas_sumadas = SumaColumnasPorCriterio(data_organizada_subsector, "Código subsector económico", 
                                                   "Total retenciones", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        menor_del_anio = MenorElementoPorCriterio(Columnas_sumadas,"Total retenciones")
        lt.addLast(menor_criterio,menor_del_anio)
        
        data_organizada_sector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)), cmpCodigoActividadEconomica)
        Sumatoria_sector = SumaColumnasPorCriterio(data_organizada_sector,"Código actividad económica", "Total retenciones", 
                                                   "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        
        sumatoria_organizada = SortLista(Sumatoria_sector, cmpTotalRetenciones)
        
        for data in lt.iterator(sumatoria_organizada):
            if data["Código subsector económico"] == menor_del_anio["Código subsector económico"]:
                lt.addLast(temp1,data)
        lt.addLast(sectores_por_anio,temp1)    
                    
    return menor_criterio , sectores_por_anio


def req_4(data_structs):
    mayor_criterio = lt.newList("ARRAY_LIST")
    sectores_por_anio = lt.newList("ARRAY_LIST")
    listas_de_listas = ListasPorAnio(data_structs["data"])

    
    for i in range(2012,2022):
        
        temp1 = lt.newList("ARRAY_LIST")
        
        data_organizada_subsector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)),cmpSubsectorEconomico)
        Columnas_sumadas = SumaColumnasPorCriterio(data_organizada_subsector, "Código subsector económico", 
                                                   "Costos y gastos nómina", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        mayor_del_anio = MayorElementoPorCriterio(Columnas_sumadas,"Costos y gastos nómina")
        lt.addLast(mayor_criterio,mayor_del_anio)
        
        data_organizada_sector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)), cmpCodigoActividadEconomica)
        Sumatoria_sector = SumaColumnasPorCriterio(data_organizada_sector,"Código actividad económica", "Costos y gastos nómina", 
                                                   "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        
        sumatoria_organizada = SortLista(Sumatoria_sector, cmpCostosyGastosNomina)
        
        for data in lt.iterator(sumatoria_organizada):
            if data["Código subsector económico"] == mayor_del_anio["Código subsector económico"]:
                lt.addLast(temp1,data)
        lt.addLast(sectores_por_anio,temp1)    
                    
    return mayor_criterio , sectores_por_anio

def req_5(data_structs):
    
    mayor_criterio = lt.newList("ARRAY_LIST")
    sectores_por_anio = lt.newList("ARRAY_LIST")
    listas_de_listas = ListasPorAnio(data_structs["data"])

    
    for i in range(2012,2022):
        
        temp1 = lt.newList("ARRAY_LIST")
        
        data_organizada_subsector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)),cmpSubsectorEconomico)
        Columnas_sumadas = SumaColumnasPorCriterio(data_organizada_subsector, "Código subsector económico", 
                                                   "Descuentos tributarios", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        
        mayor_del_anio = MayorElementoPorCriterio(Columnas_sumadas,"Descuentos tributarios")
        lt.addLast(mayor_criterio,mayor_del_anio)
        
        data_organizada_sector = SortLista(ObtenerListaConAnio(listas_de_listas,str(i)), cmpCodigoActividadEconomica)
        Sumatoria_sector = SumaColumnasPorCriterio(data_organizada_sector,"Código actividad económica", "Descuentos tributarios", 
                                                   "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor")
        
        sumatoria_organizada = SortLista(Sumatoria_sector, cmpDescuentosTributarios)
       
        for data in lt.iterator(sumatoria_organizada):
            
            if data["Código subsector económico"] == mayor_del_anio["Código subsector económico"]:
                lt.addLast(temp1,data)
        lt.addLast(sectores_por_anio,temp1)    
                    
    return mayor_criterio , sectores_por_anio

    
""" 
FUNCIONEES PARA REQUERIMIENTO 6
"""

def req_6(data_structs,anio):
    
    lista_a_procesar = lt.newList("ARRAY_LIST")
    
    retornar_mayor_actividad = lt.newList("ARRAY_LIST")
    retornar_menor_actividad = lt.newList("ARRAY_LIST")
    
    lista_de_listas = ListasPorAnio(data_structs["data"])
    lista_trabajar = ObtenerListaConAnio(lista_de_listas,anio)
    
    sectores_ordenados = SortLista(lista_trabajar,cmpSectorEconomico)
    sumatoria_sector = SumaColumnasPorCriterio(sectores_ordenados,"Código sector económico", 
                                               "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar",
                                               "Total saldo a favor", "Costos ganancias ocasionales")
    
    lista_sublistas_sectoreco = SubListasPorCriterio(lista_trabajar, "Código sector económico")
    i = 1 
    
    for element in lt.iterator(sumatoria_sector):
        
        lista_recorrer = SortLista(lt.getElement(lista_sublistas_sectoreco,i),cmpSubsectorEconomico)
        lista_limpia = SumaColumnasPorCriterio(lista_recorrer,"Código subsector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar",
                                        "Total saldo a favor", "Costos ganancias ocasionales")
        
        lista_sublistas_actividadeco = SubListasPorCriterio(lista_recorrer, "Código subsector económico")
        
        element["Subsector económico que más aportó"] = MayorElementoPorCriterio(lista_limpia,"Total ingresos netos")["Código subsector económico"]
        element["Subsector económico que menos aportó"] = MenorElementoPorCriterio(lista_limpia,"Total ingresos netos")["Código subsector económico"]
        
        for data in lt.iterator(lista_sublistas_actividadeco):
            
            mayor_maxsub = mayor_menorsub = -1
            menor_maxsub = menor_menorsub = float(limpiar_datos(lt.firstElement(data)["Total ingresos netos"])) + 1
            
            if (float(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]) >= mayor_maxsub) and (int(MayorElementoPorCriterio(data,"Total ingresos netos")["Código subsector económico"]) == int(element["Subsector económico que más aportó"])):
                mayor_maxsub = float(limpiar_datos(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]))
                mayor_dato_mayorsub = MayorElementoPorCriterio(data,"Total ingresos netos")
                
            if float(MenorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]) <= menor_maxsub and (int(MayorElementoPorCriterio(data,"Total ingresos netos")["Código subsector económico"]) == int(element["Subsector económico que más aportó"]) ):
                menor_maxsub = float(limpiar_datos(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]))
                menor_dato_mayorsub = MenorElementoPorCriterio(data,"Total ingresos netos")
                
            if (float(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]) >= mayor_menorsub) and (int(MayorElementoPorCriterio(data,"Total ingresos netos")["Código subsector económico"]) == int(element["Subsector económico que menos aportó"])):
                mayor_menorsub = float(limpiar_datos(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]))
                mayor_dato_menorsub = MayorElementoPorCriterio(data,"Total ingresos netos")
                
            if float(MenorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]) <= menor_menorsub and (int(MayorElementoPorCriterio(data,"Total ingresos netos")["Código subsector económico"]) == int(element["Subsector económico que menos aportó"]) ):
                menor_menorsub = float(limpiar_datos(MayorElementoPorCriterio(data,"Total ingresos netos")["Total ingresos netos"]))
                menor_dato_menorsub = MenorElementoPorCriterio(data,"Total ingresos netos")
                
        for data in lt.iterator(lista_limpia):
            
            if data["Código subsector económico"] == element["Subsector económico que más aportó"]:
                data["Actividad económica que más aportó"] = mayor_dato_mayorsub
                data["Actividad económica que menos aportó"] = menor_dato_mayorsub
                lt.addLast(retornar_mayor_actividad,data)
                
            if data["Código subsector económico"] == element["Subsector económico que menos aportó"]:
                data["Actividad económica que más aportó"] = mayor_dato_menorsub
                data["Actividad económica que menos aportó"] = menor_dato_menorsub
                lt.addLast(retornar_menor_actividad,data)
            
            lt.addLast(lista_a_procesar,data)
        
        i += 1
        
    return sumatoria_sector, retornar_mayor_actividad, retornar_menor_actividad, lista_a_procesar
    

def req_7(data_structs,top,inicio,final):
    """
    Función que soluciona el requerimiento 7
    """
    top = int(top)
    
    lista_de_listas = ListasPorAnio(data_structs["data"])
    lista_retornar = lt.newList("ARRAY_LIST")
    
    for i in range(int(inicio), int(final)+1):
    
        lista_inicio = SumaColumnasPorCriterio(ObtenerListaConAnio(lista_de_listas, str(i)),"Código actividad económica","Total ingresos netos", 
                                                "Total costos y gastos", "Total saldo a pagar","Total saldo a favor", "Costos ganancias ocasionales")

        for data in lt.iterator(lista_inicio):
            lt.addLast(lista_retornar , data)
            
    agrupados = Sublista(SortLista(lista_retornar,cmpTotalCostosGastos) , 1 ,top)
    retorno = SortLista( agrupados, cmpAnio )
    
    return retorno


def req_8(data_structs,top,inicio,final):
    """
    Función que soluciona el requerimiento 8
    """
    
    top = int(top)
    
    lista_de_listas = ListasPorAnio(data_structs["data"])
    lista_retornar = lt.newList("ARRAY_LIST")
    
    for i in range(int(inicio), int(final)+1):
        lista_inicio = SumaColumnasPorCriterio(ObtenerListaConAnio(lista_de_listas, str(i)),"Código sector económico","Total ingresos netos", 
                                                "Total costos y gastos", "Total saldo a pagar","Total saldo a favor", "Costos ganancias ocasionales")
    
        for data in lt.iterator(lista_inicio):
            lt.addLast(lista_retornar, data)
        
    agrupados = Sublista(SortLista(lista_retornar,cmpSectorEconomico))
    
    
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

#Limpia un dato que se supone que es un número float.
def limpiar_datos(data_1):
    
    lista_dato = list(str(data_1))
    nueva_lista = lt.newList("ARRAY_LIST") 
    
    i = 0
    while i < len(lista_dato):

        if (lista_dato[i].isnumeric()) or (lista_dato[i] == ".") or (lista_dato[i] == ","):
            if lista_dato[i] == ",":
                lista_dato[i] = ""

            lt.addLast(nueva_lista, lista_dato[i])
            
        if (lista_dato[i] == "y") or (lista_dato[i] == "o"):
            i += len(lista_dato) + 1
        i += 1

    mensaje = None
    
    if lt.size(nueva_lista) != 0:
        mensaje = ""
        for numeros in nueva_lista["elements"]:
            mensaje += numeros

        mensaje = float(mensaje)
    
    return mensaje


#Funcion criterio de comparacion (Año) y (codigo de actividad económica)
def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento
    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_
    Returns:
        _type_: _description_
    """
    
    comparacion = False
    if data_1["Año"] < data_2["Año"]:
        comparacion = True
        
    elif data_1["Año"] == data_2["Año"]:
        
        dato1 = str(limpiar_datos(data_1["Código actividad económica"]))
        dato2 = str(limpiar_datos(data_2["Código actividad económica"]))
        
        if float(dato1) < float(dato2):
            comparacion = True 

    return comparacion

#Funcion que ordena los datos con diferentes métodos dependiendo de lo que se seleccione.
def sort(data_structs,tipoSort):
    """
    Función encargada de ordenar la lista con los datos
    """
    if tipoSort == "selection":
        lista_ordenada = se.sort(data_structs["data"], sort_criteria)
        
    elif tipoSort == "insert":
        lista_ordenada = ins.sort(data_structs["data"],sort_criteria)

    elif tipoSort == "shell":
        lista_ordenada = sa.sort(data_structs["data"], sort_criteria)
    
    elif tipoSort == "merge":
        lista_ordenada = merg.sort(data_structs["data"],sort_criteria)

    elif tipoSort == "quick":
        lista_ordenada = quk.sort(data_structs["data"], sort_criteria)
    
        
    return lista_ordenada




