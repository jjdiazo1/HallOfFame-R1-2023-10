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
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate 
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def newController(type):
    """
        Se crea una instancia del controlador
    """
    control = controller.loadCatalog(type)
    return control

def dianInfo(catalog):
    return controller.dianInfo(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("0- Salir")

def loadData(control, size, ordenamiento):
    """
    Carga los datos
    """
    controller.loadData(control, size, ordenamiento)

"""
def printData(control, id):
    
        Función que imprime un dato dado su ID
    
    data = controller.getData(control, id)
    print("El dato con el ID",id, "es:", data)
"""

def printReq1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    info, time = controller.req1(control)
    headers = ['Año', "Código actividad económica", "Código sector económico",
                "Nombre sector económico", "Código subsector económico",  
                "Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    Createtabulate(info, headers, "grid")
    print("El programa demora " + str(time) + " caragando el requerimiento 1")

def printReq2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    info, time = controller.req2(control)
    headers = ['Año', "Código actividad económica", "Código sector económico",
                "Nombre sector económico", "Código subsector económico",  
                "Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    Createtabulate(info, headers, "grid")
    print("El programa demora " + str(time) + "caragando el requerimiento 2")

def printReq3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    info, delta = controller.req3(control)
    headers = ['Año', "Código sector económico","Nombre sector económico", "Código subsector económico", 
               "Nombre subsector económico", "Total costos y gastos nómina del subsector",
               "Total ingresos netos del subsector", "Total costos y gastos del subsector",
                 "Total saldo por pagar del subsector","Total saldo a favor del subsector"]
    headers2 = ["Código actividad económica", "Nombre actividad económica", "Total retenciones", "Total ingresos netos", "Total costos y gastos", 
                "Total saldo a pagar","Total saldo a favor"]
    Createtabulate(info[0], headers, "grid")
    for a in lt.iterator(info[1]):
        Createtabulate(a, headers2, "grid")
    print("El programa demora " + str(delta) + "caragando el requerimiento 3")

def printReq4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    info, delta = controller.req4(control)
    headers = ['Año', "Código sector económico","Nombre sector económico", "Código subsector económico", 
               "Nombre subsector económico", "Total costos y gastos nómina del subsector",
               "Total ingresos netos del subsector", "Total costos y gastos del subsector",
                 "Total saldo por pagar del subsector","Total saldo a favor del subsector"]
    headers2 = ["Código actividad económica", "Nombre actividad económica", "Costos y gastos nómina", "Total ingresos netos", "Total costos y gastos", 
                "Total saldo a pagar","Total saldo a favor"]
    Createtabulate(info[0], headers, "grid")
    for a in lt.iterator(info[1]):
        Createtabulate(a, headers2, "grid")

    print("El programa demora " + str(delta) + "caragando el requerimiento 4")

def printReq5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """

    info, delta = controller.req5(control)
    headers = ['Año', "Código sector económico","Nombre sector económico", "Código subsector económico", 
               "Nombre subsector económico", "Total de descuentos tributarios del subsector económico",
               "Total ingresos netos del subsector", "Total costos y gastos del subsector",
                 "Total saldo por pagar del subsector","Total saldo a favor del subsector"]
    headers2 = ["Código actividad económica", "Nombre actividad económica", "Descuentos tributarios", 
                "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]
    Createtabulate(info[0], headers, "grid")
    for a in lt.iterator(info[1]):
        Createtabulate(a, headers2, "grid")

    print("El programa demora " + str(delta) + "caragando el requerimiento 5")

def printReq6(control, año):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    info, delta = controller.req6(control, año)
    headers = ['Año', "Código sector económico","Nombre sector económico", 'Total ingresos netos del sector económico', "Código subsector económico", 
               "Nombre subsector económico", "Total de descuentos tributarios del sector económico",
               "Total ingresos netos del sector", "Total costos y gastos del sector",
                 "Total saldo por pagar del sector","Total saldo a favor del sector"]
    headers2 = ["Código actividad económica", "Nombre actividad económica","Total ingresos netos del sector económico","Total costos y gastos del sector económico",
                 "Total saldo por pagar del sector económico","Total saldo a favor del sector económico", 
                "Actividad económica que más aportó económico", "Actividad económica que menos aportó económico"]
    Createtabulate(info[0], headers, "grid")
    for a in lt.iterator(info[1]):
        Createtabulate(a, headers2, "grid")
    print("El programa demora " + str(delta) + "caragando el requerimiento 6")
    

def printReq7(control, top, anioinicial, aniofinal):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    
    info, delta = controller.req7(control, top, anioinicial, aniofinal)
    headers = ['Año', "Código actividad económica", "Nombre actividad económica", "Código sector económico","Nombre sector económico", 
               "Código subsector económico", "Nombre subsector económico", "Total ingresos netos","Total costos y gastos",
                 "Total saldo a pagar","Total saldo a favor"]
    Createtabulate(info, headers, "grid")
    print("El programa demora " + str(delta) + "caragando el requerimiento 6")

def printReq8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    pass

                   
    

# Se crea el controlador asociado a la vista
control = None

def Createtabulate(lista, headers, formato):
    table = []
    for elemento in lt.iterator(lista):
        fila = []
        for header in headers:
            fila.append(elemento[header])
        table.append(fila)
    print(tabulate(table, headers, tablefmt=formato, maxcolwidths=12, maxheadercolwidths=12))

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        try: 
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                estructura = "ARRAY_LIST"
                control = newController(estructura)

                print("1. 5%")
                print ("2. 10%")
                print("3. 20%")
                print ("4. 30%")
                print("5. 40%")
                print("6. 50%")
                print("7. 80%")
                print("8. large")
                print("9. small")
                
                tamanio_usu= int(input("\nIngrese el tamaño del archivo que quiere cargar\n"))
                if tamanio_usu == 1:
                    tamanio = "5pct"
                elif tamanio_usu == 2:
                    tamanio="10pct"
                elif tamanio_usu == 3:
                    tamanio="20pct"
                elif tamanio_usu == 4:
                    tamanio="30pct"
                elif tamanio_usu== 5:
                    tamanio="40pct"
                elif tamanio_usu== 6:
                    tamanio="50pct"
                elif tamanio_usu ==  7:
                    tamanio = "80pct"
                elif tamanio_usu == 8:
                    tamanio = "large"
                elif tamanio_usu == 9:
                    tamanio= "small"
                ordenamiento= "sa"
                timei = controller.getTime()
                loadData(control, tamanio , ordenamiento)
                timef = controller.getTime()
                delta = controller.deltaTime(timei, timef)
                print("El total de resgitros cargados es: " + str(lt.size(control["dian"])))
                print("Los primeros y últimos 3 elementos cargados son:")
                listaD = dianInfo(control)
                headers = ['Año', "Código actividad económica", 'Nombre actividad económica', "Código sector económico",
                            "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", 
                            "Total ingresos netos","Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
                Createtabulate(listaD[0], headers,"grid")
                Createtabulate(listaD[1], headers, "grid")
                print("El programa demora " + str(delta) + " caragando los datos")

            elif int(inputs) == 2:
                printReq1(control)

            elif int(inputs) == 3:
                printReq2(control)

            elif int(inputs) == 4:
                printReq3(control)

            elif int(inputs) == 5:
                printReq4(control)

            elif int(inputs) == 6:
                printReq5(control)

            elif int(inputs) == 7:
                año = int(input("Ingrese el año a buscar: "))
                printReq6(control, año)

            elif int(inputs) == 8:
                anio_inicial = int(input("Ingrese el año inicial: "))
                anio_final = int(input("Ingrese el año final: "))
                top = int(input("Ingrese el top: "))
                printReq7(control, top, anio_inicial, anio_final)

            elif int(inputs) == 9:
                printReq8(control)

            elif int(inputs) == 0:
                print("\nGracias por utilizar el programa")
                break

            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            # print("Ingrese una opción válida.\n")
            print(exp)
            traceback.print_exc()
    sys.exit(0)
