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
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(list_type):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(list_type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
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
    
def print_menu_load_data():
    print("="*60)
    print("1- small")
    print("2- 5pct")
    print("3- 10pct")
    print("4- 20pct")
    print("5- 30pct")
    print("6- 50pct")
    print("7- 80pct")
    print("8- large")
    print("0- cancelar")

def print_list_type():
    print("="*60)
    print("1. ARRAY_LIST")
    print("2. SINGLE_LINKED")
    print("0. cancelar")
    
def print_sorting_type():
    print("="*60)
    print("1. Selection") 
    print("2. Insertion")   
    print("3. Shell")
    print("4. Merge")
    print("5. Quick")
    print("0. Cancelar")
    
    

def load_data(control, size,sort_type):
    """
    Carga los datos
    """
    data = controller.load_data(control, "DIAN/Salida_agregados_renta_juridicos_AG-" + size + ".csv",sort_type)
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
    result, delta_t = controller.req_1(control)
    print(tabulate(result,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))   
    print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    result,delta_t = controller.req_2(control)
    print(tabulate(result,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))  
    print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    result,delta_t = controller.req_3(control)
    ans, tabla_anios = result
    print(tabulate(ans,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12)) 
    iteraciones = 0 
    for x in tabla_anios:
        print(str(2012+iteraciones))
        print(tabulate(x,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))
        iteraciones +=1
    print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")
         
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    result,delta_t = controller.req_4(control)
    tabla, tabla_anios = result
    print(tabulate(tabla,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12)) 
    anio = 2012
    for x in tabla_anios:
        print(str("There are only "+ str(len(x)-1)+" activities in "+ str(anio) + ""))
        print(tabulate(x,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))
        anio +=1
    print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    result,tabla_anios, delta_tiempo = controller.req_5(control)
    resultado = []
    for i in result:
        j = i["elements"][:5] + [i["elements"][7]] + i["elements"][5:7] + i["elements"][8:]
        resultado.append(j)
    print(tabulate(resultado,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12)) 
    iteraciones = 0
    for x in tabla_anios:
        print(str(2012+iteraciones))
        print(tabulate(x,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))
        iteraciones +=1
    print("El tiempo de ejecución fue de "+str(delta_tiempo)+"ms.")


def print_req_6(control,anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control,anio))


def print_req_7(control,topN,anio_inicial,anio_final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    result,delta_t = controller.req_7(control,topN,anio_inicial,anio_final)
    print(tabulate(result,tablefmt = "fancy_grid",headers = "firstrow",stralign="center",
                   maxcolwidths=12,maxheadercolwidths=12))
    print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")
    
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))


# Se crea el controlador asociado a la vista
control = None

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                working2 = True
                working3 = True
                while working2: 
                    print_list_type()
                    tipo_lista = input("Seleccione el tipo de lista de desea crear\n")
                    if int(tipo_lista) == 0:
                        working = False                                             
                    print_menu_load_data()
                    while working3:
                            inputs_size = input('Seleccione una opción para continuar\n')
                            if int(inputs_size) == 1:
                                size = "small"
                                working3 = False
                            elif int(inputs_size) == 2:
                                size = "5pct"
                                working3 = False
                            elif int(inputs_size) == 3:
                                size = "10pct"
                                working3 = False
                            elif int(inputs_size) == 4:
                                size = "20pct"
                                working3 = False
                            elif int(inputs_size) == 5:
                                size = "30pct"
                                working3 = False
                            elif int(inputs_size) == 6:
                                size = "50pct"
                                working3 = False
                            elif int(inputs_size) == 7:
                                size = "80pct"
                                working3 = False    
                            elif int(inputs_size) == 8:
                                size = "large"
                                working3 = False    
                            elif int(inputs_size) == 0:
                                working = False
                                working2 = False
                                working3 = False                
                            else:
                                print("Opción errónea, vuelva a elegir.\n") 
                                
                    if int(tipo_lista) != 0 and working2 == False:
                        working = False
                        
                    else:
                        go_on = True
                        print_sorting_type()
                        while go_on:
                            algoritm = int(input("Seleccione el tipo de algoritmo de ordenamiento que desea usar.\n"))
                            if algoritm == 1:
                                sort_type = "SELECTION_SORT"
                                go_on = False
                            elif algoritm == 2:
                                sort_type = "INSERTION_SORT"
                                go_on = False
                            elif algoritm == 3:
                                sort_type = "SHELL_SORT"
                                go_on = False
                            elif algoritm == 4:
                                sort_type = "MERGE_SORT"
                                go_on = False
                            elif algoritm == 5:
                                sort_type = "QUICK_SORT"
                                go_on = False
                            elif algoritm == 0:
                                working = False
                            else:
                                print("Opción errónea, vuelva a elegir.\n") 
                                
                    if int(tipo_lista) == 1:
                        control = new_controller("ARRAY_LIST")
                        data,fal3,delta_t = load_data(control,size,sort_type)
                        print("Cargando información de los archivos ....\n")
                        print("El número total de registros cargados es:", data,"\n")
                        lista = fal3["elements"]
                        param = {"Año":[],"Código actividad económica":[],"Nombre actividad económica":[],
                                 "Código sector económico":[],"Nombre sector económico":[],"Código subsector económico":[],
                                 "Nombre subsector económico":[],"Total ingresos netos":[],"Total costos y gastos":[],
                                 "Total saldo a pagar":[],"Total saldo a favor":[]}
                        for element in lista:
                            for key in param.keys():
                                param[key].append(element[key])
                                                
                        print(tabulate(param,tablefmt = "fancy_grid",headers = list(param),stralign="center",
                                       maxcolwidths=12,maxheadercolwidths=12))               
                        print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")
                        working2 = False
                    
                    elif int(tipo_lista) == 2:
                        control = new_controller("SINGLE_LINKED")
                        data,fal3,delta_t  = load_data(control,size,sort_type)
                        print("Cargando información de los archivos ....\n")
                        print("El número total de registros cargados es:", data,"\n")
                        lista = fal3["elements"]
                        param = {"Año":[],"Código actividad económica":[],"Nombre actividad económica":[],
                                 "Código sector económico":[],"Nombre sector económico":[],"Código subsector económico":[],
                                 "Nombre subsector económico":[],"Total ingresos netos":[],"Total costos y gastos":[],
                                 "Total saldo a pagar":[],"Total saldo a favor":[]}
                        for element in lista:
                            for key in param.keys():
                                param[key].append(element[key])                       
                        print(tabulate(param,tablefmt = "fancy_grid",headers = list(param),stralign="center",
                                       maxcolwidths=12,maxheadercolwidths=12))  
                        print("El tiempo de ejecución fue de "+str(delta_t)+"ms.")
                        working2 = False
                    

                #ciclo del menu

                          
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                topN = int(input("Seleccione un N para un top N.\n"))
                anio_inicial = str(input("Año de inicio para la toma de datos.\n"))
                anio_final = str(input("Año de corte para la toma de datos.\n"))
                print_req_7(control,topN,anio_inicial,anio_final)
                
            elif int(inputs) == 9:
                print_req_8(control)

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
