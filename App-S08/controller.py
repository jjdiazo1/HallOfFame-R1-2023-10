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
import os
from DISClib.ADT import list as lt
import re


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Funciones para la carga de datos
def loadCatalog(type):
    catalog = model.newDataStructs(type)
    return catalog

def loadData(catalog, size, ordenamiento):
    loadDian(catalog, size, ordenamiento)

def loadDian(catalog, size, ordenamiento):
    tracksfile = cf.data_dir + "Salida_agregados_renta_juridicos_AG-" + size + ".csv"
    input_file = csv.DictReader(open(tracksfile, encoding='utf-8'))
    for info in input_file:    
        model.addDianinfo(catalog, info)
    model.sort(catalog, ordenamiento)
        

# Funciones de ordenamiento
def sort(control):
    """
    Ordena los datos del modelo
    """
    start_time = getTime()
    model.sort(control["model"])
    end_time = getTime()
    delta_time = deltaTime(start_time, end_time)
    return delta_time

# Funciones de consulta sobre el catálogo
def getData(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.getData(control["model"], id)
    return data

def dianInfo(catalog):
    return model.dianInfo(catalog)

def req1(control):
    timei = getTime()
    info = model.ListtheActivitiesEconomicwithGreatertotalBalancePayableforeveryyear(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta

def req2(control):
    timei = getTime()
    info = model.ListactivitiesEconomicwithGreatertotalBalanceinFavorforallyearsAvailable(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


def req3(control):
    timei = getTime()
    info = model.FindtheSubsectorEconomicwithTheLowesttotalofWithholdingsforallYearsavailable(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


def req4(control):
    timei = getTime()
    info = model.FindtheSubsectoreconomicwithTheHighestcostsandPayrollExpensesforallYearsAvailable(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


def req5(control):
    timei = getTime()
    info = model.FindtheSubsectorEconomicwiththeElderlyTaxDiscountsforEveryoneyearsAvailable(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


def req6(control, año):
    timei = getTime()
    info = model.EconomicActivityWithTheHighestTotalofNetIncomeforEachEconomicSectorInSpecificYear(control, año)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


def req7(control, top, anioinicial, aniofinal):
    timei = getTime()
    info = model.ListtheTOPofTheeconomicActivitieswiththeLowertotalcostsandexpenses(control, top, anioinicial, aniofinal)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta

def req8(control):
    timei = getTime()
    info = model.req8(control)
    timef = getTime()
    delta = deltaTime(timei, timef)
    return info, delta


# Funciones para medir tiempos de ejecucion
def getTime():
    
    "devuelve el instante tiempo de procesamiento en milisegundos"
    
    return float(time.perf_counter()*1000)


def deltaTime(start, end):

    "devuelve la diferencia entre tiempos de procesamiento muestreados"
    elapsed = float(end - start)
    return elapsed