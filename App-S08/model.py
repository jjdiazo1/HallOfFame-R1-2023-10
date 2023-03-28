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
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newDataStructs(type):
    """
    Inicializa las estructuras de datos del modelo. Las crea 
    de manera vacía para posteriormente almacenar la información.
    """
    dataStructs = {
        "dian": None,
        "año": None,
    }
    dataStructs["dian"] = lt.newList(datastructure=type, 
                                           cmpfunction=cmp_impuestos_by_anio_CAE)
    dataStructs["año"] = lt.newList("ARRAY_LIST")


    
    return dataStructs

# Funciones para agregar informacion al modelo
def addDianinfo(catalog, info):
    addAño2(catalog, info)
    lt.addLast(catalog["dian"], info)

def addAño2(catalog, info):
    found = False
    for year in lt.iterator(catalog["año"]):
        if lt.firstElement(year)["Año"] == info["Año"]:
            lt.addLast(year, info)
            found = True
    if found == False:
        newY = lt.newList("ARRAY_LIST")
        lt.addLast(newY, info)
        lt.addLast(catalog["año"], newY)

def dianInfo(catalog):
    info = LastandFirst(catalog, "dian")
    return info

def LastandFirst(catalog, llave):
    list = catalog[llave]
    sizeList = lt.size(list)
    listFirst = lt.newList("ARRAY_LIST")
    listLast = lt.newList("ARRAY_LIST")
    for i in range(1,4):
        lt.addLast(listFirst, lt.getElement(list, i))
    for i in range(sizeList-3, sizeList):
        lt.addLast(listLast, lt.getElement(list, i))
    return listFirst, listLast

# Funciones de consulta
def ListtheActivitiesEconomicwithGreatertotalBalancePayableforeveryyear(control):
    """
    Función que soluciona el requerimiento 1:
    Encuentra las actividades económicas con mayor total saldo 
    a pagar para todos los años disponibles (G)
    """
    returnList = lt.newList()
    for linea in lt.iterator(control["año"]):
        mayor = lt.firstElement(linea)
        for linea in lt.iterator(linea):
            if int(linea["Total saldo a pagar"]) > int(mayor["Total saldo a pagar"]):
                mayor = linea
        lt.addLast(returnList, mayor)
    quk.sort(returnList, comparar_anio)
    return returnList

def ListactivitiesEconomicwithGreatertotalBalanceinFavorforallyearsAvailable(control):
    """
    Función que soluciona el requerimiento 2:
    económicas con mayor total saldo 
    a favor para para todos los años disponibles (G)
    """
    returnList = lt.newList()
    for linea in lt.iterator(control["año"]):
        mayor = lt.firstElement(linea)
        for linea in lt.iterator(linea):
            if int(linea["Total saldo a favor"]) > int(mayor["Total saldo a favor"]):
                mayor = linea
        lt.addLast(returnList, mayor)
    quk.sort(returnList, comparar_anio)
    return returnList

#Funciones auxiliares para los requerimientos
def add_por_subsector_o_sector(lineas, subsector):
    listreturn= lt.newList()
    for linea in lt.iterator(lineas):
        esta= False 
        for lineaSubsector in lt.iterator(listreturn):
            if lt.firstElement(lineaSubsector)[subsector]==linea[subsector]:
                lt.addLast(lineaSubsector, linea)
                esta=True
        if not esta:
            nuevaLineaDelSubsector=lt.newList()
            lt.addLast(nuevaLineaDelSubsector, linea)
            lt.addLast(listreturn, nuevaLineaDelSubsector)
    return listreturn

def suma_totales_subsector(subsector):
    """Suma los totales del subsector o sector, dependiendo del parametro de entrada
    """
    totalSubsector= {"Aporte":lt.newList("ARRAY_LIST")}
    for c in ["Año", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Código actividad económica", "Nombre actividad económica"]:
        totalSubsector[c]=lt.firstElement(subsector)[c]
    sumas=["Total retenciones", "Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor", "Costos y gastos nómina", "Descuentos tributarios"]
    totalsumas=["Total retenciones del subsector", "Total ingresos netos del subsector", "Total costos y gastos del subsector",
                 "Total saldo por pagar del subsector", "Total saldo a favor del subsector", "Total costos y gastos nómina del subsector", "Total de descuentos tributarios del subsector económico"]
    for c in totalsumas:
        totalSubsector[c]=0
    for linea in lt.iterator(subsector):
        for n in range(0,len(totalsumas)):
            totalSubsector[totalsumas[n]]+= int(linea[sumas[n]])
        lt.addLast(totalSubsector["Aporte"], linea)
    totalSubsector['Aporte']['Año'] = lt.firstElement(subsector)['Año']
    return totalSubsector

def suma_totales_cada_subsector(subsector, sub):
    """Suma los totales del subsector o sector, dependiendo del parametro de entrada
    """
    totalSubsector= {"Aporte":lt.newList("ARRAY_LIST")}
    for c in ["Año", "Código subsector económico","Nombre subsector económico", "Código subsector económico", "Nombre subsector económico", "Código actividad económica","Nombre actividad económica"]:
        totalSubsector[c]=lt.firstElement(sub)[c]
    sumas=["Total ingresos netos del subsector económico","Total costos y gastos del subsector económico", "Total saldo a pagar del subsector económico", "Total saldo a favor del subsector económico"]
    totalsumas=["Total ingresos netos del sector económico", "Total costos y gastos del sector económico",
                 "Total saldo por pagar del sector económico", "Total saldo a favor del sector económico"]
    for c in totalsumas:
        totalSubsector[c]=0
    for linea in lt.iterator(subsector):
        for n in range(0,len(totalsumas)):
            totalSubsector[totalsumas[n]]+= int(linea[sumas[n]])
        lt.addLast(totalSubsector["Aporte"], linea)
    totalSubsector['Aporte']['Año'] = lt.firstElement(subsector)['Año']
    return totalSubsector

def FindtheSubsectorEconomicwithTheLowesttotalofWithholdingsforallYearsavailable(control):
    """
    Función que solucion el requerimiento 3:
    Encontrar el subsector económico con el menor total de 
    retenciones para todos los años disponibles (I)
    """
    returnList = lt.newList()
    actividades = lt.newList()
    for linea in lt.iterator(control["año"]):
        lineasporSubsector = add_por_subsector_o_sector(linea, "Código subsector económico")
        menor = None
        for SubsectorE in lt.iterator(lineasporSubsector):
            totalSubesectorE = suma_totales_subsector(SubsectorE)
            if menor is None:
                menor = totalSubesectorE
            else:
                if int(totalSubesectorE["Total retenciones del subsector"]) < int(menor["Total retenciones del subsector"]):
                    menor = totalSubesectorE
        quk.sort(menor["Aporte"], cmpRetencion)
        lt.addLast(returnList, menor)
        lt.addLast(actividades, menor["Aporte"])
    quk.sort(returnList, comparar_anio)
    quk.sort(actividades, comparar_anio)    
    return returnList, actividades


def FindtheSubsectoreconomicwithTheHighestcostsandPayrollExpensesforallYearsAvailable(control):
    """
    Función que soluciona el requerimiento 4:
    Encontrar el subsector económico con los mayores costos y 
    gastos de nómina para todos los años disponibles (I)

    """
    returnList = lt.newList()
    actividades = lt.newList()
    for linea in lt.iterator(control["año"]):
        lineasporSubsector = add_por_subsector_o_sector(linea, "Código subsector económico")
        mayor = None
        for SubsectorE in lt.iterator(lineasporSubsector):
            totalSubesectorE = suma_totales_subsector(SubsectorE)
            if mayor is None:
                mayor = totalSubesectorE
            else:
                if int(totalSubesectorE["Total costos y gastos nómina del subsector"]) > int(mayor["Total costos y gastos nómina del subsector"]):
                    mayor = totalSubesectorE
        quk.sort(mayor["Aporte"], cmpPay)
        lt.addLast(returnList, mayor)
        lt.addLast(actividades, mayor["Aporte"])
    quk.sort(returnList, comparar_anio)
    #quk.sort(actividades, comparar_anio)    
    return returnList, actividades

def FindtheSubsectorEconomicwiththeElderlyTaxDiscountsforEveryoneyearsAvailable(control):
    """
    Función que soluciona el requerimiento 5:
    Encontrar el subsector económico con los mayores
    descuentostributarios para todos los años disponibles (I)

    """
    returnList = lt.newList()
    actividades = lt.newList()
    for linea in lt.iterator(control["año"]):
        lineasporSubsector = add_por_subsector_o_sector(linea, "Código subsector económico")
        mayor = None
        for SubsectorE in lt.iterator(lineasporSubsector):
            totalSubesectorE = suma_totales_subsector(SubsectorE)
            if mayor is None:
                mayor = totalSubesectorE
            else:
                if int(totalSubesectorE["Total de descuentos tributarios del subsector económico"]) > int(mayor["Total de descuentos tributarios del subsector económico"]):
                    mayor = totalSubesectorE
        quk.sort(mayor["Aporte"], cmpTax)
        lt.addLast(returnList, mayor)
        lt.addLast(actividades, mayor["Aporte"])
    quk.sort(returnList, comparar_anio)
    #quk.sort(actividades, comparar_anio)    
    return returnList, actividades

def EconomicActivityWithTheHighestTotalofNetIncomeforEachEconomicSectorInSpecificYear(control, year):
    """
    Función que soluciona el requerimiento 6:
     Encontrar la actividad económica con el mayor total de 
     ingresos netos para cada sector económico en un año específico
    """
    returnList = lt.newList("ARRAY_LIST")
    SubsectorContribution = lt.newList("ARRAY_LIST")
    for anio in lt.iterator(control["año"]):
        if int(lt.firstElement(anio)["Año"]) == year:
            lineasporSector = add_por_subsector_o_sector(anio, "Código sector económico")
            for sectorE in lt.iterator(lineasporSector):
                subsectorE = lt.newList("ARRAY_LIST")
                lineasporSubsector = add_por_subsector_o_sector(sectorE, "Código subsector económico")
                for subsectorsE in lt.iterator(lineasporSubsector):
                    totalSubsectorE = suma_totales_subsector(subsectorsE)
                    lt.addLast(subsectorE, totalSubsectorE)
                totalSectorE = suma_totales_cada_subsector(totalSubsectorE, sectorE)
                lt.addLast(returnList, totalSectorE)
                lt.addLast(SubsectorContribution, lt.firstElement(totalSectorE["Aporte"]))
    return returnList, SubsectorContribution

def ListtheTOPofTheeconomicActivitieswiththeLowertotalcostsandexpenses(control, topN, anio_inicial, anio_final):
    """
    Función que soluciona el requerimiento 7
    """

    listreturn= lt.newList()
    for anio in lt.iterator(control["año"]):
        if int(lt.firstElement(anio)["Año"]) in range(anio_inicial, anio_final+1):
            quk.sort(anio, cmpCyG)
            if topN> lt.size(anio):
                topN=lt.size(anio)
            for i in range(1, topN+1):
                linea=lt.getElement(anio, i)
                lt.addLast(listreturn, linea)


    return listreturn

def req8(dataStructs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass



# Funciones utilizadas para comparar elementos dentro de una lista
def cmp_saldo(saldo1, saldo2):
    return int(saldo1["Total saldo a pagar"]) > int(saldo2["Total saldo a pagar"])

def cmp_saldo_favor(saldo1, saldo2):
    return int(saldo1["Total saldo a favor"]) > int(saldo2["Total saldo a favor"])


def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2):
    if int(impuesto1["Año"])==int(impuesto2["Año"]):
        return comparar_actividad_eco(impuesto1, impuesto2)
        
    else:
        return comparar_anio(impuesto1, impuesto2)
        
def comparar_anio(impuesto1, impuesto2):
    if (impuesto1["Año"].isnumeric() and impuesto2["Año"].isnumeric()):
        return int(impuesto2["Año"])>int(impuesto1["Año"]) 

def comparar_actividad_eco(impuesto1, impuesto2):
    x = impuesto1["Código actividad económica"].isnumeric()
    y = impuesto2["Código actividad económica"].isnumeric()
    if (x and y):
        return int(impuesto2["Código actividad económica"])>int(impuesto1["Código actividad económica"])

def cmpPay(pay1, pay2):
    return int(pay1["Costos y gastos nómina"]) > int(pay2["Costos y gastos nómina"])

def cmpCyG(impuesto1, impuesto2):
    return int(impuesto1["Total costos y gastos"]) > int(impuesto2["Total costos y gastos"])

def cmpRetencion(retencion1, retencion2):
    return int(retencion1["Total retenciones"]) > int(retencion2["Total retenciones"])

def cmpTax(tax1, tax2):
    return int(tax1["Descuentos tributarios"]) > int(tax2["Descuentos tributarios"])

def compare(data1, data2):
    """
    Función encargada de comparar dos datos
    """
    if data1["id"] > data2["id"]:
        return 1
    elif data1["id"] < data2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento
def sort(data_structs, ordenamiento):
    """
    Función encargada de ordenar la lista con los datos
    """

    #TODO: Crear función de ordenamiento
    if ordenamiento == "sa":
        sa.sort(data_structs["dian"], cmp_impuestos_by_anio_CAE)
    elif ordenamiento == "ins":
        ins.sort(data_structs["dian"], cmp_impuestos_by_anio_CAE)
    elif ordenamiento == "se":
        se.sort(data_structs["dian"], cmp_impuestos_by_anio_CAE)

    elif ordenamiento=="merg":
        merg.sort(data_structs["dian"], cmp_impuestos_by_anio_CAE)

    elif ordenamiento=="quk":
        quk.sort(data_structs["dian"], cmp_impuestos_by_anio_CAE)





