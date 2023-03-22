"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
import traceback
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import mergesort as merg
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(data_type = "ARRAY_LIST"):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(data_type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Actividad económica con mayor total de saldo a pagar")
    print("3- Actividad económica con mayor total de saldo a favor")
    print("4- Subsector económico con el menor total de retenciones")
    print("5- Subsector económico con los mayores costos y gastos de nómina")
    print("6- Subsector económico con los mayores descuentos tributarios")
    print("7- Actividad económica con el mayor total de ingresos netos de cada sector económico en un año específico")
    print("8- Top de las actividad economicas con el menor total de costos y gastos en un periodo de tiempo")
    print("9- Top de las actividades economicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo")
    print("10- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control, load_table = False):
    """
    Carga los datos
    """
    data = controller.load_data(control, load_table)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)

def def_sort():
    print("\nSeleccione el tipo de sort que desea utilizar: ")
    sort_type = input("\n")
    valid = True
    s_dato = ""
    try:
        if int(sort_type) == 1:
            s_dato = "Insertion"
        elif int(sort_type) == 2:
            s_dato = "Merge"
        elif int(sort_type) == 3:
            s_dato = "Quick"
        elif int(sort_type) == 4:
            s_dato = "Selection"
        elif int(sort_type) == 5:
            s_dato = "Shell"  
        else:
            print("Opción errónea, vuelva a elegir.\n")
            valid = False
    except ValueError:
        valid = False
        print("Ingrese una opción válida.\n")
        traceback.print_exc()
    return s_dato, valid

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    req_1, time = controller.req_1(control)

    headers = ["Año", "Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico", "Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    table = []

    for element in req_1["elements"]:
        row = []
        for key in element:
            if key in headers:  
                row.append(element[key]) 
        table.append(row)

    print("\n---------------------------------Requerimiento 1---------------------------------")
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("El tiempo de ejecucion es: ", round(time,2))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    req_2, time = controller.req_2(control)

    headers = ["Año", "Código actividad económica","Nombre actividad económica",
               "Código sector económico","Nombre sector económico","Código subsector económico",
               "Nombre subsector económico", "Total ingresos netos","Total costos y gastos",
               "Total saldo a pagar","Total saldo a favor"]
    table = []

    for element in req_2["elements"]:
        row = []
        for key in element:
            if key in headers:  
                row.append(element[key]) 
        table.append(row)

    print("\n---------------------------------Requerimiento 2---------------------------------")
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("El tiempo de ejecucion es: ", round(time,2))

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    tableanios, req_3, time = controller.req_3(control)

    table = []
    table_grande = []
    headers = ['Año','Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de retenciones del subsector economico', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']

    for element in req_3["elements"]:
        table = [element["Año"],element["Código sector económico"],element["Nombre sector económico"],element["Código subsector económico"],
                  element["Nombre subsector económico"],element["Total de retenciones del subsector economico"],element["Total ingresos netos del subsector economico"],
                  element["Total costos y gastos del subsector"],element["Total saldo a pagar del subsector"], element["Total saldo a favor del subsector"]]
        table_grande.append(table)
    


    print("\n---------------------------------Requerimiento 3---------------------------------")
    print("Economic subsectors with the lowest total withholdings (Total retenciones) for each year")
    print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    headers_tabulate = ["Código actividad económica","Nombre actividad económica","Total retenciones", 
                   "Total ingresos netos","Total saldo a pagar","Total saldo a favor"]


    tableanios_tabulate1 = []
    tableanios_tabulate2 = []
    tableanios_tabulate3 = []
    tableanios_tabulate4 = []
    tableanios_tabulate5 = []
    tableanios_tabulate6 = []
    tableanios_tabulate7 = []
    tableanios_tabulate8 = []
    tableanios_tabulate9 = []
    tableanios_tabulate10 = []

    for listas in tableanios:

        if listas[0] == "2012":
            cod1 = listas[1]
        
        if listas[0] == "2013":
            cod2 = listas[1]
        
        if listas[0] == "2014":
            cod3 = listas[1]
   
        if listas[0] == "2015":
            cod4 = listas[1]

        if listas[0] == "2016":
            cod5 = listas[1]

        if listas[0] == "2017":
            cod6 = listas[1]

        if listas[0] == "2018":
            cod7 = listas[1]
  
        if listas[0] == "2019":
            cod8 = listas[1]
            
        if listas[0] == "2020":
            cod9 = listas[1]
   
        if listas[0] == "2021":
            cod10 = listas[1]
         
    for listas in tableanios:

        if listas[0] == "2012":
            tableanios_tabulate1.append(listas[2:])
       
        if listas[0] == "2013":
            tableanios_tabulate2.append(listas[2:])
       
        if listas[0] == "2014":
            tableanios_tabulate3.append(listas[2:])
        
        if listas[0] == "2015":
            tableanios_tabulate4.append(listas[2:])
    
        if listas[0] == "2016":
           
            tableanios_tabulate5.append(listas[2:])

        if listas[0] == "2017":
            
            tableanios_tabulate6.append(listas[2:])
        
        if listas[0] == "2018":
          
            tableanios_tabulate7.append(listas[2:])
        
        if listas[0] == "2019":
            
            tableanios_tabulate8.append(listas[2:])
       
        if listas[0] == "2020":
          
            tableanios_tabulate9.append(listas[2:])
        
        if listas[0] == "2021":
            
            tableanios_tabulate10.append(listas[2:])


    print("La(s)",len(tableanios_tabulate1),"actividades economicas que más y menos aportaron en 2012 en el subsector " + cod1 + " son: ")    
    print(tabulate(tableanios_tabulate1,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate2),"actividades economicas que más y menos aportaron en 2013 en el subsector " + cod2 + " son: ")    
    print(tabulate(tableanios_tabulate2,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate3),"actividades economicas que más y menos aportaron en 2014 en el subsector " + cod3 + " son: ")
    print(tabulate(tableanios_tabulate3,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate4),"actividades economicas que más y menos aportaron en 2015 en el subsector " + cod4 + " son: ")
    print(tabulate(tableanios_tabulate4,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate5),"actividades economicas que más y menos aportaron en 2016 en el subsector " + cod5 + " son: ")     
    print(tabulate(tableanios_tabulate5,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate6),"actividades economicas que más y menos aportaron en 2017 en el subsector " + cod6 + " son: ")   
    print(tabulate(tableanios_tabulate6,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate7),"actividades economicas que más y menos aportaron en 2018 en el subsector " + cod7 + " son: ")  
    print(tabulate(tableanios_tabulate7,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate8),"actividades economicas que más y menos aportaron en 2019 en el subsector " + cod8 + " son: ")
    print(tabulate(tableanios_tabulate8,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate9),"actividades economicas que más y menos aportaron en 2020 en el subsector " + cod9 + " son: ")  
    print(tabulate(tableanios_tabulate9,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate10),"actividades economicas que más y menos aportaron en 2021 en el subsector " + cod10 + " son: ") 
    print(tabulate(tableanios_tabulate10,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4

    req_4,tableanios,time = controller.req_4(control)

    headers = ['Año','Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de costos y gastos nomina del subsector economico', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    
    table = []

    for element in req_4["elements"]:
        row = []
        for key in element:
            if key in headers:  
                row.append(element[key]) 
        table.append(row)

    print("\n---------------------------------Requerimiento 4---------------------------------")
    print("Subsectores economicos con los mayores costos y gastos nomina para cada año")
    print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    headers_tabulate = ["Código actividad económica","Nombre actividad económica","Total costos y gastos nómina", 
                   "Total ingresos netos","Total saldo a pagar","Total saldo a favor"]
    
    tableanios_tabulate1 = []
    tableanios_tabulate2 = []
    tableanios_tabulate3 = []
    tableanios_tabulate4 = []
    tableanios_tabulate5 = []
    tableanios_tabulate6 = []
    tableanios_tabulate7 = []
    tableanios_tabulate8 = []
    tableanios_tabulate9 = []
    tableanios_tabulate10 = []

    for listas in tableanios:

        if listas[0] == "2012":
            cod1 = listas[1]
        
        if listas[0] == "2013":
            cod2 = listas[1]
        
        if listas[0] == "2014":
            cod3 = listas[1]
   
        if listas[0] == "2015":
            cod4 = listas[1]

        if listas[0] == "2016":
            cod5 = listas[1]

        if listas[0] == "2017":
            cod6 = listas[1]

        if listas[0] == "2018":
            cod7 = listas[1]
  
        if listas[0] == "2019":
            cod8 = listas[1]
            
        if listas[0] == "2020":
            cod9 = listas[1]
   
        if listas[0] == "2021":
            cod10 = listas[1]
         
    for listas in tableanios:

        if listas[0] == "2012":
            tableanios_tabulate1.append(listas[2:])
       
        if listas[0] == "2013":
            tableanios_tabulate2.append(listas[2:])
       
        if listas[0] == "2014":
            tableanios_tabulate3.append(listas[2:])
        
        if listas[0] == "2015":
            tableanios_tabulate4.append(listas[2:])
    
        if listas[0] == "2016":
           
            tableanios_tabulate5.append(listas[2:])

        if listas[0] == "2017":
            
            tableanios_tabulate6.append(listas[2:])
        
        if listas[0] == "2018":
          
            tableanios_tabulate7.append(listas[2:])
        
        if listas[0] == "2019":
            
            tableanios_tabulate8.append(listas[2:])
       
        if listas[0] == "2020":
          
            tableanios_tabulate9.append(listas[2:])
        
        if listas[0] == "2021":
            
            tableanios_tabulate10.append(listas[2:])


    print("La(s)",len(tableanios_tabulate1),"actividades economicas que más y menos aportaron en 2012 en el subsector " + cod1 + " son: ")    
    print(tabulate(tableanios_tabulate1,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate2),"actividades economicas que más y menos aportaron en 2013 en el subsector " + cod2 + " son: ")    
    print(tabulate(tableanios_tabulate2,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate3),"actividades economicas que más y menos aportaron en 2014 en el subsector " + cod3 + " son: ")
    print(tabulate(tableanios_tabulate3,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate4),"actividades economicas que más y menos aportaron en 2015 en el subsector " + cod4 + " son: ")
    print(tabulate(tableanios_tabulate4,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate5),"actividades economicas que más y menos aportaron en 2016 en el subsector " + cod5 + " son: ")     
    print(tabulate(tableanios_tabulate5,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate6),"actividades economicas que más y menos aportaron en 2017 en el subsector " + cod6 + " son: ")   
    print(tabulate(tableanios_tabulate6,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate7),"actividades economicas que más y menos aportaron en 2018 en el subsector " + cod7 + " son: ")  
    print(tabulate(tableanios_tabulate7,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate8),"actividades economicas que más y menos aportaron en 2019 en el subsector " + cod8 + " son: ")
    print(tabulate(tableanios_tabulate8,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate9),"actividades economicas que más y menos aportaron en 2020 en el subsector " + cod9 + " son: ")  
    print(tabulate(tableanios_tabulate9,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate10),"actividades economicas que más y menos aportaron en 2021 en el subsector " + cod10 + " son: ") 
    print(tabulate(tableanios_tabulate10,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    req_5,tableanios,time = controller.req_5(control)

    headers = ['Año','Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de descuentos tributarios del subsector economico', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    
    table = []
    table_grande = []

    for element in req_5["elements"]:
        table = [element["Año"],element["Código sector económico"],element["Nombre sector económico"],element["Código subsector económico"],
                  element["Nombre subsector económico"],element["Total de descuentos tributarios del subsector economico"],element["Total ingresos netos del subsector economico"],
                  element["Total costos y gastos del subsector"],element["Total saldo a pagar del subsector"], element["Total saldo a favor del subsector"]]
        table_grande.append(table)


    print("\n---------------------------------Requerimiento 5---------------------------------")
    print("Subsectores economicos con los mayores descuentos tributarios0 para cada año")
    print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    headers_tabulate = ["Código actividad económica","Nombre actividad económica","Total de descuentos tributarios del subsector economico", 
                   "Total ingresos netos","Total saldo a pagar","Total saldo a favor"]
    
    tableanios_tabulate1 = []
    tableanios_tabulate2 = []
    tableanios_tabulate3 = []
    tableanios_tabulate4 = []
    tableanios_tabulate5 = []
    tableanios_tabulate6 = []
    tableanios_tabulate7 = []
    tableanios_tabulate8 = []
    tableanios_tabulate9 = []
    tableanios_tabulate10 = []

    for listas in tableanios:

        if listas[0] == "2012":
            cod1 = listas[1]
        
        if listas[0] == "2013":
            cod2 = listas[1]
        
        if listas[0] == "2014":
            cod3 = listas[1]
   
        if listas[0] == "2015":
            cod4 = listas[1]

        if listas[0] == "2016":
            cod5 = listas[1]

        if listas[0] == "2017":
            cod6 = listas[1]

        if listas[0] == "2018":
            cod7 = listas[1]
  
        if listas[0] == "2019":
            cod8 = listas[1]
            
        if listas[0] == "2020":
            cod9 = listas[1]
   
        if listas[0] == "2021":
            cod10 = listas[1]
         
    for listas in tableanios:

        if listas[0] == "2012":
            tableanios_tabulate1.append(listas[2:])
       
        if listas[0] == "2013":
            tableanios_tabulate2.append(listas[2:])
       
        if listas[0] == "2014":
            tableanios_tabulate3.append(listas[2:])
        
        if listas[0] == "2015":
            tableanios_tabulate4.append(listas[2:])
    
        if listas[0] == "2016":
           
            tableanios_tabulate5.append(listas[2:])

        if listas[0] == "2017":
            
            tableanios_tabulate6.append(listas[2:])
        
        if listas[0] == "2018":
          
            tableanios_tabulate7.append(listas[2:])
        
        if listas[0] == "2019":
            
            tableanios_tabulate8.append(listas[2:])
       
        if listas[0] == "2020":
          
            tableanios_tabulate9.append(listas[2:])
        
        if listas[0] == "2021":
            
            tableanios_tabulate10.append(listas[2:])


    print("La(s)",len(tableanios_tabulate1),"actividades economicas que más y menos aportaron en 2012 en el subsector " + cod1 + " son: ")    
    print(tabulate(tableanios_tabulate1,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate2),"actividades economicas que más y menos aportaron en 2013 en el subsector " + cod2 + " son: ")    
    print(tabulate(tableanios_tabulate2,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate3),"actividades economicas que más y menos aportaron en 2014 en el subsector " + cod3 + " son: ")
    print(tabulate(tableanios_tabulate3,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate4),"actividades economicas que más y menos aportaron en 2015 en el subsector " + cod4 + " son: ")
    print(tabulate(tableanios_tabulate4,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate5),"actividades economicas que más y menos aportaron en 2016 en el subsector " + cod5 + " son: ")     
    print(tabulate(tableanios_tabulate5,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate6),"actividades economicas que más y menos aportaron en 2017 en el subsector " + cod6 + " son: ")   
    print(tabulate(tableanios_tabulate6,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate7),"actividades economicas que más y menos aportaron en 2018 en el subsector " + cod7 + " son: ")  
    print(tabulate(tableanios_tabulate7,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate8),"actividades economicas que más y menos aportaron en 2019 en el subsector " + cod8 + " son: ")
    print(tabulate(tableanios_tabulate8,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate9),"actividades economicas que más y menos aportaron en 2020 en el subsector " + cod9 + " son: ")  
    print(tabulate(tableanios_tabulate9,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("La(s)",len(tableanios_tabulate10),"actividades economicas que más y menos aportaron en 2021 en el subsector " + cod10 + " son: ") 
    print(tabulate(tableanios_tabulate10,headers_tabulate,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))



def print_req_6(control, year):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6

    sector, max_subsector, min_subsector, max_actividad, min_actividad, time = controller.req_6(control, year)

    max_max_actividad, max_min_actividad = max_actividad
    min_max_actividad, min_min_actividad = min_actividad
    headers_sect = ["Código sector económico", 
                    "Nombre sector económico",
                    "Total ingresos netos del sector económico",
                    "Total costos y gastos del sector económico",
                    "Total saldo por pagar del sector económico",
                    "Total saldo a favor del sector económico",
                    "Subsector económico que más aportó",
                    "Subsector económico que menos aportó"]
    headers_subsect = ["Código subsector económico",
                       "Nombre subsector económico",
                       "Total ingresos netos para el subsector",
                       "Total costos y gastos para el subsector",
                       "Total saldo por pagar para el subsector",
                       "Total saldo a favor para el subsecto",
                       "Actividad económica que más aportó",
                       "Actividad económica que menos aportó"]
    headers_actividad = ["Código actividad económica",
                       "Nombre actividad económica",
                       "Total ingresos netos",
                       "Total costos y gastos",
                       "Total saldo por pagar",
                       "Total saldo a favor"]
    
    tabla_sector = []
    tabla_max_sub = []
    tabla_min_sub = []
    tabla_max_act = []
    tabla_min_act = []
    for i in range(sector["size"]):
        if i == 1:
            tabla_sector.append(sector["elements"][i]["elements"][0]["Nombre sector económico"])
        else:
            tabla_sector.append(str(sector["elements"][i]))
    tabla_sector.append(max_subsector["elements"][0])
    tabla_sector.append(min_subsector["elements"][0])
    ttabla_sector = []   
    ttabla_sector.append(tabla_sector)
    
    for i in range(max_subsector["size"]):
        if i == 1:
            tabla_max_sub.append(max_subsector["elements"][i]["elements"][0]["Nombre subsector económico"])
        else:
            tabla_max_sub.append(str(max_subsector["elements"][i]))
    tabla_max_sub.append(max_max_actividad["Código actividad económica"])
    tabla_max_sub.append(max_min_actividad["Código actividad económica"]) 
    ttabla_max_sub = []
    ttabla_max_sub.append(tabla_max_sub)
    
    for i in range(min_subsector["size"]):
        if i == 1:
            tabla_min_sub.append(min_subsector["elements"][i]["elements"][0]["Nombre subsector económico"])
        else:
           tabla_min_sub.append(str(min_subsector["elements"][i]))
    tabla_min_sub.append(min_max_actividad["Código actividad económica"])
    tabla_min_sub.append(min_min_actividad["Código actividad económica"]) 
    ttabla_min_sub = []
    ttabla_min_sub.append(tabla_min_sub)  
    
    for minmaxactividad in max_actividad:
        row = []
        for key in minmaxactividad:
            if key in headers_actividad:
                row.append(minmaxactividad[key])
        tabla_max_act.append(row)
            
    for minmaxactividad in max_actividad:
        row = []
        for key in minmaxactividad:
            if key in headers_actividad:
                row.append(minmaxactividad[key])
        tabla_min_act.append(row)
    
    print("\n---------------------------------Requerimiento 6---------------------------------")
    print("\n=======================Sector economico que mas contribuyo=======================\n")
    print(tabulate(ttabla_sector,headers_sect,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("\n=====================Subsector economico que mas contribuyo======================\n")
    print(tabulate(ttabla_max_sub,headers_subsect,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("\n////////////Actividad economico que mas y menos contribuyo al subsector////////////\n")
    print(tabulate(tabla_max_act,headers_actividad,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("\n====================Subsector economico que menos contribuyo=====================\n")
    print(tabulate(ttabla_min_sub,headers_subsect,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
    print("\n////////////Actividad economico que mas y menos contribuyo al subsector////////////\n")
    print(tabulate(tabla_min_act,headers_actividad,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7

    n = int(input("\nSeleccione el número de actividades económicas a identificar: "))
    anio_inicial = str(input("\nIndique el año inicial de consulta: "))
    anio_final = str(input("\nIndique el año final de consulta: "))

    req_7, time = controller.req_7(control,n,anio_inicial,anio_final)

    headers = ["Año", "Código actividad económica","Nombre actividad económica",
               "Código sector económico","Nombre sector económico","Código subsector económico",
               "Nombre subsector económico", "Total ingresos netos","Total costos y gastos",
               "Total saldo a pagar","Total saldo a favor"]
    
    table = []

    for element in req_7["elements"]:
        row = []
        for key in element:
            if key in headers:  
                row.append(element[key]) 
        table.append(row)


    headers2 = ["Año", "Código actividad económica","Nombre actividad económica",
               "Código sector económico","Nombre sector económico","Código subsector económico",
               "Nombre subsector económico", "Total ingresos netos consolidados para el periodo",
               "Total costos y gastos consolidados para el periodo",
               "Total saldo a pagar consolidado para el periodo","Total saldo a favor consolidados para el periodo"]

    print("\n---------------------------------Requerimiento 7---------------------------------")
    print("Encontrar las top ", n," actividades economicas con el menor total de costos y gastos entre" + " " + anio_inicial + " y " + anio_final)
    print(tabulate(table,headers2,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8

    
    n = int(input("\nSeleccione el número de actividades económicas a identificar: "))
    anio_inicial = str(input("\nIndique el año inicial de consulta: "))
    anio_final = str(input("\nIndique el año final de consulta: "))
    print("\n")

    lista, time= controller.req_8(control,n,anio_inicial,anio_final)


    table_grande = []

    headers = ['Código sector económico','Nombre sector económico', 'Código subsector económico', 
               'Nombre subsector económico','Total de impuestos a cargo para el subsector', 
               'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector', 
               'Total saldo a pagar del subsector','Total saldo a favor del subsector']
    

    for element in lista["elements"]:
        table = [element['Código sector económico'],element['Nombre sector económico'], element['Código subsector económico'], 
               element['Nombre subsector económico'],element['Total de impuestos a cargo para el subsector'], 
               element['Total ingresos netos del subsector economico'], element['Total costos y gastos del subsector'], 
               element['Total saldo a pagar del subsector'],element['Total saldo a favor del subsector']]
    
        table_grande.append(table)


    print("\n---------------------------------Requerimiento 8---------------------------------")
    print("Encontrar las top ", n," actividades economicas de cada subsector con el mayor total de impuestos a cargo entre" + " " + anio_inicial + " y " + anio_final)
    print(tabulate(table_grande,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")

    print("El tiempo de ejecucion es: ", round(time,2))




# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    all_data = None
    
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                
                
                print("\n---------------------------------------------------------")
                print("Cargando información de los archivos ....\n")
                all_data, size, table, headers= load_data(control, True)
                   
                print("Se cargaron", size, "datos")
                print("Se cargaron", len(headers), "filas")
                print("---------------------------------------------------------\n")
                    
                print("Los primeros y ultimos 3 datos cargados son:")
                print("Los datos estan ordenados con respecto al año")
                print(tabulate(table,headers,tablefmt="grid",maxcolwidths=14, maxheadercolwidths=10,numalign="right"), "\n")
            
                   
                
            elif int(inputs) == 2:
                print_req_1(all_data)
            
            elif int(inputs) == 3:
                print_req_2(all_data)

            elif int(inputs) == 4:
                print_req_3(all_data)

            elif int(inputs) == 5:
                print_req_4(all_data)

            elif int(inputs) == 6:
                print_req_5(all_data)

            elif int(inputs) == 7:
                year = int(input("Ingrese el año que desea consultar: "))
                print_req_6(all_data, year)

            elif int(inputs) == 8:
                print_req_7(all_data)
            
            elif int(inputs) == 9:
                print_req_8(all_data)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
