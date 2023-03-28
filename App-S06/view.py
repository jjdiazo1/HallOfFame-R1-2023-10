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

#Hola como amanecemos 

import config as cf
import pandas as pd
from tabulate import tabulate
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

#from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""



def new_controller(estructura):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(estructura)
    return control


def print_menu():
    """
    Muestra el menu al usuario, dandole opciones del 0 al 11
    """
    print("Bienvenido")
    print("1- Carga de datos del Reto")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("11- Carga de Datos Personalizada")
    print("0- Salir")


def load_data(control,filename):
    """
    Carga los datos
    """
    data = controller.load_data(control, filename)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)

def Print_Req_1y2(lista_req , num_criterio):
    
    """
    Tabula las listas previamente hechas de los requimientos 1 y 2 con sus respectivas columnas y luego las muestra al usuario junto
    con el tiempo que la maquina tarda en procesar el requerimiento elejido
    """
    
    lista = ["Año","Código actividad económica","Nombre actividad económica",
                "Código sector económico","Nombre sector económico","Código subsector económico", "Nombre subsector económico",
                "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]
    
    dataframe = CrearDataframe(lista_req[0],lista,"Año")
    
    print("-------------------------------")
    print(f"REQUERIMIENTO {num_criterio}")
    print("-------------------------------")
    
    print(tabulate(dataframe[0], headers="keys", tablefmt="grid", maxcolwidths = 12, maxheadercolwidths = 12))
    print(f"El tiempo que tomó fue de {lista_req[1]} milisegundos")
    

def print_req_3_4y5(lista_req , criterio , indice, num_req):
    
    """
    Tabula las listas previamente hechas de los requimientos 3, 4 y 5 con sus respectivas columnas y luego las muestra al usuario junto
    con el tiempo que la maquina tarda en procesar el requerimiento elejido.
    """
    
    lista = ["Año","Código sector económico","Nombre sector económico","Código subsector económico", "Nombre subsector económico",criterio,
                "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]
    
    dataframe = CrearDataframe(lista_req[0][0] , lista ,"Año")
    frame = dataframe[0]
    frame.rename(columns ={"Año":"Año","Código sector económico":"Código sector económico", "Nombre sector económico":"Nombre sector económico", 
                               "Código subsector económico":"Código subsector económico",criterio:f"{criterio} del subsector económico",
                               "Total ingresos netos": "Total ingresos netos del subsector económico","Total costos y gastos":"Total costos y gastos del subsector económico",
                               "Total saldo a pagar":"Total saldo a pagar del subsector económico","Total saldo a favor":"Total saldo a favor del subsector económico"}, inplace = True)
    
    lista_sub = ["Código actividad económica","Nombre actividad económica", criterio ,  "Total ingresos netos", "Total costos y gastos",
                 "Total saldo a pagar", "Total saldo a favor"]
    print("-------------------------------")
    print(f"REQUERIMIENTO {num_req}")
    print("-------------------------------")
    
    print(tabulate(frame, headers="keys", tablefmt="grid", maxcolwidths = 12, maxheadercolwidths = 12))
    print("\n\n")
    
    sublistas = lista_req[0][1]
    
    for datos in lt.iterator(sublistas):
    
        anio = lt.firstElement(datos)["Año"]
        datos_imprimir = DataFrame(datos)  
        dataframe_sublistas = CrearDataframe(datos_imprimir, lista_sub,indice)
        if (dataframe_sublistas[0].shape[0]) >= 6:
            print("--------------------")
            print(f"Las primeras 3 y ultimas 3 actividades que menos contribuyeron en el año {anio} fueron:")
            print("--------------------")
            
        else:
            print("--------------------")
            print(f"Solo hay {dataframe_sublistas[0].shape[0]} actividades en el año {anio} del subsector económico " + str(lt.firstElement(datos)["Código subsector económico"]))
            print("--------------------")
            
        print(tabulate(dataframe_sublistas[0], headers=lista_sub, tablefmt="grid", maxcolwidths = 12, maxheadercolwidths = 12))
        print("\n\n")
        
    print(f"Tardo en procesarse {lista_req[1]} milisegundos")
    print("\n\n")
    
    pass
    

def print_req_6(control,anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    
    lista = ["Código sector económico","Nombre sector económico", "Total ingresos netos", "Total costos y gastos", 
             "Total saldo a pagar","Total saldo a favor","Subsector económico que más aportó", "Subsector económico que menos aportó"]
    
    lista_req6 = controller.req_6(control, anio)
    dataframe = CrearDataframe(lista_req6[0][0], lista, "Código sector económico")
    frame = dataframe[0]
    
    frame.rename(columns ={"Código sector económico": "Código sector económico", "Nombre sector económico":"Nombre sector económico",
                           "Total ingresos netos": "Total ingresos netos del sector económico", "Total costos y gastos": "Total costos y gastos del sector económico",
                           "Total saldo a pagar":"Total saldo a pagar del sector económico", "Total saldo a favor":"Total saldo a favor del sector económico",
                           "Subsector económico que más aportó":"Subsector económico que más aportó", "Subsector económico que menos aportó": "Subsector económico que menos aportó" }, inplace = True)
    
    print("-------------------------------")
    print("REQUERIMIENTO 6")
    print("-------------------------------")
    
    print(tabulate(frame, headers="keys", tablefmt="grid", maxcolwidths = 12, maxheadercolwidths = 12))
    print("\n\n")
    
    segunda_lista = ["Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", 
             "Total saldo a pagar","Total saldo a favor", "Actividad económica que más aportó", "Actividad económica que menos aportó"]
    
    process = PrintTabladentroTabla(lista_req6[0][3])
    
    subsidiario = lt.newList("ARRAY_LIST")
    subsidiario2 = lt.newList("ARRAY_LIST")
    
    for data in lista_req6[0][1]["elements"]:
        lt.addLast(subsidiario,(data))
    
    for elemen in lista_req6[0][2]["elements"]:
        lt.addLast(subsidiario2,(elemen))
        
    print("--------------------------------------------")
    print("SUBSECTORES ECONOMICOS QUE CONTRIBUYERON MÁS")
    print("--------------------------------------------")
    
    segundo_frame = pd.DataFrame(subsidiario["elements"]) 
    segundo_frame = segundo_frame[segunda_lista]
    segundo_frame = wrapping_time(segundo_frame)
    segundo_frame = rename(segundo_frame)
    segundo_frame = segundo_frame.set_index("Código\nsubsector\neconómico")

    print(tabulate(segundo_frame, headers="keys", tablefmt="grid"))
    print("\n\n")
    
    print("--------------------------------------------")
    print("SUBSECTORES ECONOMICOS QUE CONTRIBUYERON MENOS")
    print("--------------------------------------------")
    
    segundo_frame = pd.DataFrame(subsidiario2["elements"]) 
    segundo_frame = segundo_frame[segunda_lista]
    segundo_frame = wrapping_time(segundo_frame)
    segundo_frame = rename(segundo_frame)
    segundo_frame = segundo_frame.set_index("Código\nsubsector\neconómico")

    print(tabulate(segundo_frame, headers="keys", tablefmt="grid"))
    print("\n\n")
    
    print(f"El tiempo que tomó fueron {lista_req6[1]} milisegundos")
    
    
    pass

def PrintTabladentroTabla(lista):
    
    columnas = ["Código actividad económica", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", 
             "Total saldo a pagar","Total saldo a favor"]
    
    for datos in lt.iterator(lista):
   
        lista_general = lt.newList("ARRAY_LIST")
        lista_general_menor = lt.newList("ARRAY_LIST")
        
        if datos.get("Actividad económica que más aportó",-10) == -10:
            datos["Actividad económica que más aportó"] = {"Código actividad económica":0,  "Nombre subsector económico":0, "Total ingresos netos":0,
                                                             "Total costos y gastos":0, "Total saldo a pagar":0, "Total saldo a favor":0}
            
        if datos.get("Actividad económica que menos aportó",-10) == -10:
            datos["Actividad económica que menos aportó"] = {"Código actividad económica":0,  "Nombre subsector económico":0, "Total ingresos netos":0,
                                                             "Total costos y gastos":0, "Total saldo a pagar":0, "Total saldo a favor":0}
            
        temp1 = datos["Actividad económica que más aportó"]
        temp2 = datos["Actividad económica que menos aportó"]
        
        for elemen in temp1:
            dic = {}
            dic["llave"] = str(elemen)
            dic["valor"] = temp1[elemen]
            if str(elemen) in columnas:
                lt.addLast(lista_general,dic)
        
        for data in temp2:
            
            dic_menor = {}
            dic_menor["llave"] = str(data)
            dic_menor["valor"] = temp2[data]
            if str(data) in columnas:
                lt.addLast(lista_general_menor,dic_menor)
        
        datos["Actividad económica que más aportó"] = tabulate(pd.DataFrame(lista_general["elements"]).set_index("llave"),tablefmt= "grid" , maxcolwidths = 20, maxheadercolwidths = 20 )
        datos["Actividad económica que menos aportó"] = tabulate(pd.DataFrame(lista_general_menor["elements"]).set_index("llave"),tablefmt= "grid" , maxcolwidths = 20, maxheadercolwidths = 20 )
        
    pass
    
    

def wrapping_time(dataframe:pd.DataFrame):
    
    """
    Reduce el tamaño de las columnas, haciendo que solo quepan 16 caracteres horizontalmente.
    """
    
    dataframe["Nombre subsector económico"] = dataframe["Nombre subsector económico"].str.wrap(16)
    
    return dataframe

def rename(dataframe:pd.DataFrame):
     diccionario = {"Código subsector económico": "Código\nsubsector\neconómico",
                    "Nombre subsector económico": "Nombre\nsubsector\neconómico",
                    "Total ingresos netos" : "Total\ningresos\nnetos",
                     "Total costos y gastos" : "Total\ncostos y\ngastos",
                    "Total saldo a pagar": "Total\nsaldo a\npagar",
                    "Total saldo a favor" : "Total\nsaldo a\nfavor",
                    "Actividad económico que más aporto" :"Actividad económica que más aporto",
                    "Actividad económico que menos aporto" : "Actividad económica que menos aporto"}
     
     dataframe = dataframe.rename(columns = diccionario)
     
     return dataframe
 
def print_req_7(control,top,inicio,final):
    """
        Tabula la lista previamente hecha del requerimiento 7 con sus respectivas columnas y luego las muestra al usuario junto
    con el tiempo que la maquina tarda en procesar el requerimiento.
    """
    lista = ["Año","Código actividad económica","Nombre actividad económica",
                "Código sector económico","Nombre sector económico","Código subsector económico", "Nombre subsector económico",
                "Total ingresos netos","Total costos y gastos",  "Total saldo a pagar","Total saldo a favor"]
    
    lista_req7 = controller.req_7(control,top,inicio,final)
    dataframe = CrearDataframe(lista_req7[0] , lista ,"Año")
    frame = dataframe[0]
    frame.rename(columns ={"Año":"Año","Código actividad económica":"Código actividad económica", "Nombre actividad económica":"Nombre actividad económica", 
                               "Código sector económico":"Código sector económico",
                               "Nombre sector económico": "Nombre sector económico","Código subsector económico":"Código subsector económico",
                               "Nombre subsector económico": "Nombre subsector económico",
                               "Total ingresos netos":"Total ingresos netos consolidados para el periodo",
                               "Total costos y gastos":"Total costos y gastos consolidados para el periodo",
                               "Total saldo a pagar":"Total saldo a pagar consolidados para el periodo",
                               "Total saldo a favor":"Total saldo a favor consolidados para el periodo"}, inplace = True)
    
    print("-------------------------------")
    print("REQUERIMIENTO 7")
    print("-------------------------------")
    
    print(tabulate(frame, headers="keys", tablefmt="grid", maxcolwidths = 12, maxheadercolwidths = 12))
    print(f"El tiempo que tomó fue de {lista_req7[1]} milisegundos")
    
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))
    

def CrearDataframe(new_data , lista , indice):
    """
    Crea un dataframe de pandas con las columnas deseadas y nos da la cantidad de columnas en el dataframe. 
    """
    
        
    frame = pd.DataFrame(new_data["elements"])      
    cantidad_columnas = len(frame.columns)         
    dataframe = frame[lista].set_index(indice)
        
    return dataframe,cantidad_columnas
  
 
def printDataframe(dataframe,columnas, tamanio):
    
    """
    Convierte el dataframe de pandas a tabulate, y hace print del mensaje antes de la tabla con la cantidad de titulos cargados,
    y columnas cargadas. Luego imprime la tabla ya tabulada.
    """
    
    
    print("-------------------------------------")
    print("Información sobre los datos cargados: \n")
    print(f"Total de titulos cargados: {tamanio}")
    print(f"Cantidad de características cargadas: {columnas}")
    print("-------------------------------------\n")
    print("Los 3 primeros y 3 últimos titulos en el rango de contenido son: ...")
    print("Contenido organizado por titulo:")
    print(tabulate(dataframe, headers="keys", tablefmt="grid", maxcolwidths = 15, maxheadercolwidths = 15))
     
    pass


def DataFrame(data,sample = 3):
    
    """ 
    Crea un array list donde están los primers 3 y últimos 3 elementos de todos los datos.
    """
    
    size = lt.size(data)
    new_data = lt.newList(datastructure="ARRAY_LIST")
     
    if size > sample*2:
        #primeros ordenados
        i = 1
        while i <= sample:
            elemento = lt.getElement(data,i)
            lt.addLast(new_data, elemento)
            i += 1
        
        #ultimos ordenados 
        i = size - sample + 1 
        while i <= size:
            elemento = lt.getElement(data, i)
            lt.addLast(new_data,elemento)
            i += 1
    else:
        new_data = data
    
    return new_data

def imprimir_carga_de_datos(data):
    
    """ 
    Imprime la carga de los datos, con las columnas organizadas.
    
    """
    
    new_data = DataFrame(data)
    lista = ["Año","Código actividad económica","Nombre actividad económica",
                "Código sector económico","Nombre sector económico","Código subsector económico", "Nombre subsector económico",
                "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]
     
    tupla_dataframe = CrearDataframe(new_data,lista,"Año")
    cantidad_columnas = tupla_dataframe[1]
    dataframe = tupla_dataframe[0]
    tamanio = controller.tamanio_lista(control)
    
    printDataframe(dataframe, cantidad_columnas, tamanio)
    
    pass

#Muestra las opciones de los archivos que se pueden cargar
def printTamanio():
    
    """
    Muestra un menu de los tamaños disponibles del archivo, con opciones del 1 al 8.
    """
    
    print("Qué tamaño del archivo desea cargar: ")
    print("1. 1%")
    print("2. 5%")
    print("3. 10%")
    print("4. 20%")
    print("5. 30%")
    print("6. 50%")
    print("7. 80%")
    print("8. 100%")
    
    pass

#dependiendo de lo que escoje el usuario devuelve el sufijo del archivo que se desea cargar
def obtener_porcentaje(opcion):
    
    """ 
    Declara segun la respuesta del usuario, el nombre del archivo que se va a utilizar segun su tamaño.
    """
    
    opcion = int(opcion)
    porcentaje = "No entro"
    
    if opcion == 1:
        porcentaje = "small"
    elif opcion == 2:
        porcentaje = "5pct"
    elif opcion == 3:
        porcentaje = "10pct"
    elif opcion == 4:
        porcentaje = "20pct"
    elif opcion == 5:
        porcentaje = "30pct"
    elif opcion == 6:
        porcentaje = "50pct"
    elif opcion == 7:
        porcentaje = "80pct"
    elif opcion == 8:
        porcentaje = "large"
    
    return porcentaje
    
#Muestra al usuario las opciones de sort
def printSort():
    
    """
    Muestra al usuario un menu de las opciones de sorteo disponibles, las opciones van desde el 1 hasta el 5.
    """
    
    print("Que tipo de sort desea utilizar: ")
    print("1. Selection Sort")
    print("2. Insert Sort")
    print("3. Shell Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    
pass

#Obtiene la variable en string del sort que se quiere, para utilizarlo en el modelo como criterio de ordenamiento.
def obtenerSort(opcion):
    
    """ 
    Declara segun la respuesta del usuario, el tipo de sorteo que se va a utilizar.
    """
    
    opcion = int(opcion)
    porcentaje = "No entro"
    
    if opcion == 1:
        porcentaje = "selection"
    elif opcion == 2:
        porcentaje = "insert"
    elif opcion == 3:
        porcentaje = "shell"
    elif opcion == 4:
        porcentaje = "merge"
    elif opcion == 5:
        porcentaje = "quick"
        
    return porcentaje
#Muestra la estructura que se puede escoger 
def printEstructura():
    
    """
    Muestra al usuario un menu de las opciones tipo de lista, las opciones son 1 o 2.
    """
    
    print("Que tipo de lista desea utilizar: ")
    print("1. Array list")
    print("2. Single Linked List")
    pass

#Obtiene la variable string de la estructura que se desea trabajar.
def obtenerEstructura(opcion):
    
    """ 
    Declara segun la respuesta del usuario, el tipo de lista que se va a utilizar.
    """
    opcion = int(opcion)
    
    if opcion == 1:
        porcentaje = "ARRAY_LIST"
    elif opcion == 2:
        porcentaje = "SINGLE_LINKED"
        
    return  porcentaje 


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
            #Carga los datos en una estructura de Array List ordenado por un shell sort. 
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                printTamanio()
                
                opcion_porcentaje = input()
                control = new_controller("ARRAY_LIST")
                data = load_data(control, obtener_porcentaje(opcion_porcentaje))
                
                tupla_sort = controller.sort(control, "merge")  
                
                imprimir_carga_de_datos(tupla_sort[1])
                print(f"El tiempo que tomo fue: {tupla_sort[0]} milisegundos")
            
            elif int(inputs) == 2:
                Print_Req_1y2(controller.req_1(control),1)

            elif int(inputs) == 3:
                Print_Req_1y2(controller.req_2(control),2)

            elif int(inputs) == 4:
                print_req_3_4y5(controller.req_3(control),"Total retenciones","Código actividad económica", 3)  
                
            elif int(inputs) == 5:
                print_req_3_4y5(controller.req_4(control),"Costos y gastos nómina","Código actividad económica", 4)

            elif int(inputs) == 6:
                print_req_3_4y5(controller.req_5(control),"Descuentos tributarios","Código actividad económica", 5)
                
            elif int(inputs) == 7:
                print("¿Qué año desea consultar?")
                anio = input()
                print_req_6(control,anio)

            elif int(inputs) == 8:
                print("Inserte el N para encontrar el top (N): ")
                top = input()
                print("Año inicial: ")
                inicio = input()
                print("Año final ")
                final = input()
                print_req_7(control,top,inicio,final)
                
                    
            elif int(inputs) == 9:
                
                print("Inserte el N para encontrar el top (N): ")
                top = input()
                print("Año inicial: ")
                inicio = input()
                print("Año final ")
                final = input()
                a = controller.req_8(control,top,inicio,final)
                
            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            elif int(inputs) == 11:
                printTamanio()
                opcion_porcentaje = input()
                printEstructura()
                opcion_estructura = input()
                printSort()
                opcion_sort = input()
                
                filename = obtener_porcentaje(opcion_porcentaje)
                tipoEstructura = obtenerEstructura(opcion_estructura)
                tipoSort = obtenerSort(opcion_sort)
                
                control = new_controller(tipoEstructura)

                data = load_data(control, filename)
                
                tupla_sort = controller.sort(control, tipoSort)
                estructura_ordenada = tupla_sort[1]
                tiempo = tupla_sort[0]
                
                DataFrame(estructura_ordenada)
                print(f"El tiempo que tomo fue: {tiempo} milisegundos")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
    sys.exit(0)


