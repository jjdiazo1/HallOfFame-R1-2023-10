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
import traceback
from tabulate import tabulate
import pandas as pd

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_controller(list_type):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(list_type)
    return control


def print_menu():
    print("Bienvenidx")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 5")
    print("5- Ejecutar Requerimiento 6")
    print("6- Ejecutar Requerimiento 7")
    print("7- Ejecutar Requerimiento 8")
    print("8- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control, pct):
    """
    Carga los datos
    """
    data = controller.load_data(control,pct)
    
    return data



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    a = controller.organizar_actividades_por_saldo_a_pagar(control)
    x = pd.DataFrame(a)
    print("================== Req No. 1 Answer ==================")
    print(tabulate(x, headers = 'keys', tablefmt = 'grid',maxheadercolwidths=12,maxcolwidths=12))
    
   

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    a,b= controller.req_3(control)
    x = pd.DataFrame(a)
    print("================== Req No. 3 Answer ==================")
    print("Economic sub-sectors with the lowest total withholdings (Total retenciones) for each year")
    print(tabulate(x, headers = 'keys', tablefmt = 'grid',maxheadercolwidths=12,maxcolwidths=12))
    for i in b:
        x = i["elements"]
        print(pd.DataFrame(x))
   

    
def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    a, b = controller.req_5(control)
    x = pd.DataFrame(a)
    print("================== Req No. 5 Answer ==================")
    print("Economic sub-sectors with the lowest total withholdings (Descuentos tributarios) for each year")
    print(tabulate(x, headers = 'keys', tablefmt = 'grid',maxheadercolwidths=12,maxcolwidths=12))
    
    for i in b:
        x = i["elements"]
        print(pd.DataFrame(x))



def print_req_6(control, año):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    a, b, c = controller.req_6(control, año)
    
    
    x = pd.DataFrame(a)
    y = pd.DataFrame(b)
    z = pd.DataFrame(c)
    y = y.drop("Actividad económica que más aportó",axis=1)
    y = y.drop("Actividad económica que menos aportó",axis=1)
    z = z.drop("Actividad económica que más aportó",axis=1)
    z = z.drop("Actividad económica que menos aportó",axis=1)
    print("================== Req No. 6 Answer ==================")
    print(tabulate(x,headers="keys",tablefmt="grid" ,maxcolwidths=15,maxheadercolwidths=15))
    print(tabulate(y,headers="keys",tablefmt="grid" ,maxcolwidths=15,maxheadercolwidths=15))
    print(tabulate(z,headers="keys",tablefmt="grid" ,maxcolwidths=15,maxheadercolwidths=15))  
        

def print_req_7(control,año_i,año_f, cantidad):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    x = pd.DataFrame(controller.req_7(control,año_i,año_f, cantidad))
    print("================== Req No. 7 Answer ==================")
    print(tabulate(x,headers="keys",tablefmt="grid",maxcolwidths=12,maxheadercolwidths=12))

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))

def printLastAndFirst(sorted_list, sample=3):
    print("------------------------------------------\nLoaded streaming service info:\nTotal loaded titles: 49\nTotal loaded features: 50")
    print("------------------------------------------\nThe first 3 and last titles in content range are...\nContent sorted by title:")
    size = lt.size(sorted_list)
    i = 1
    a = []
    b = None
    c = None
    while i <= sample:
        b = lt.getElement(sorted_list,i)
        a.append(b)
        i+=1
    x = size - sample+1
    while x <= size:
        c = lt.getElement(sorted_list,x)
        a.append(c)
        x += 1
    return a
        

# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar:\n')
        try:
            if int(inputs) == 1:
                print("Seleccione el tipo de lista a utilizar:\n1.Single Linked\n2.Array List")
                list_type = int(input())
                print("Seleccione el tamaño de la muestra de datos:\n",
                      "1.1%\n",
                      "2.5%\n",
                      "3.10%\n",
                      "4.20%\n",
                      "5.30%\n",
                      "6.50%\n",
                      "7.80%\n",
                      "8.100%\n")
                pct = int(input())
                print("Cargando los datos...")
                print("\nSeleccione el tipo de ordenamiento que quiere utilizar:\n",
                      "1.Selection Sort\n",
                      "2.Insertion Sort\n",
                      "3.Shell Short\n",
                      "4.Quick sort\n",
                      "5.Merge sort\n")
                print("Ordenando los datos...")
                type_sort = int(input())
                control = new_controller(list_type)
                data = load_data(control, pct)
                delta_t, sorted_list = controller.sort(data,type_sort)
                print("El tiempo que tomó fue {0} ms".format(delta_t))
                print("La cantidad de la muestra es de {0} lineas".format(lt.size(sorted_list))) 
                a = printLastAndFirst(sorted_list)
                dtfr = pd.DataFrame(a)
                print(dtfr)
                
                
            elif int(inputs) == 2:
                print_req_1(sorted_list)

            elif int(inputs) == 3:
                print_req_3(sorted_list)

            elif int(inputs) == 4:
                print_req_5(sorted_list)

            elif int(inputs) == 5:
                año = input("Ingrese el año que desea consultar")
                print_req_6(control, año)

            elif int(inputs) == 6:
                cantidad = int(input("Ingresa el numero de actividades económicas a identificar: "))
                año_i = int(input("Ingresa el año inicial: "))
                año_f = int(input("Ingresa el año final: "))
                print_req_7(sorted_list,año_i,año_f, cantidad)

            elif int(inputs) == 7:
                print("Ingrese el año a consultar\n")
                año = input()
                print_req_6(control, año)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)
                
            elif int(inputs) == 8:
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
