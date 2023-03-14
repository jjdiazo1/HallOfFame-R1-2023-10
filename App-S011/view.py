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


def new_controller(data_type):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(data_type)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Total saldo a pagar")
    print("3- Total saldo a favor")
    print("4- Total retenciones")
    print("5- Gastos y gastos nómina")
    print("6- Descuentos tributarios")
    print("7- Total ingresos netos")
    print("8- Total costos y gastos")
    print("9- Total impuesto a cargo")
    print("10- Obtener dato dado un ID")
    print("0- Salir")

def print_data_structure():
    print('1. ARRAY_LIST')
    print('2. SINGLE_LINKED')
    
def print_sorting_algorithms():
    print('1. Selection sorting algorithm')
    print('2. Insert sorting algorithm')
    print('3. Shell sorting algorithm')
    print('4. Merge sorting algorithm')
    print('5. Quick sorting algorithm')
    
def choose_sorting_algorithm(opt):
    if opt == 1:
        sorting_algorithm = 'Selection'
    if opt == 2:
        sorting_algorithm = 'Insertion'
    if opt == 3:
        sorting_algorithm = 'Shell'
    if opt == 4:
        sorting_algorithm = 'MergeSort'
    if opt == 5:
        sorting_algorithm = 'QuickSort'
        
    return sorting_algorithm


def choose_data_structure(input):
    data_structure = ''
    if input == 1:
        data_structure = 'ARRAY_LIST'
    if input == 2:
        data_structure = 'SINGLE_LINKED'
    return data_structure

def load_data(control, filename):
    """
    Carga los datos
    """
    size = controller.load_data(control, filename)
    return size


def datos_tabla(data_struct, size):
    llaves_a_incluir = ["Año", "Código actividad económica", "Nombre actividad económica", 
                    "Código sector económico", "Nombre sector económico", "Código subsector económico", 
                    "Nombre subsector económico","Total ingresos netos", "Total costos y gastos", 
                    "Total saldo a pagar", "Total saldo a favor"]
    list_values_info = controller.datos_filtrados(data_struct, size, llaves_a_incluir)
    return list_values_info
def print_opciones_archivo():
    print('1. 0.5% ')
    print('2. 5% ')
    print('3. 10% ')
    print('4. 20% ')
    print('5. 30% ')
    print('6. 50% ')
    print('7. 80% ')
    print('8. 100% ') 

    
def seleccionar_archivo(opt):
    filename = "Salida_agregados_renta_juridicos_AG"
    filename_modificado = ''
    porcentaje_seleccionado = ''
    if opt == 1:
        filename_modificado = filename + "-small.csv"
        porcentaje_seleccionado = '0.5%'
    if opt == 2:
        filename_modificado = filename + "-5pct.csv"
        porcentaje_seleccionado = '5%'
    elif opt == 3:
        filename_modificado = filename + "-10pct.csv"
        porcentaje_seleccionado = '10%'
    elif opt == 4:
        filename_modificado = filename + "-20pct.csv"
        porcentaje_seleccionado = '20%'
    elif opt == 5:
        filename_modificado = filename + "-30pct.csv"
        porcentaje_seleccionado = '30%'
    elif opt == 6:
        filename_modificado = filename + "-50pct.csv"
        porcentaje_seleccionado = '50%'
    elif opt == 7:
        filename_modificado = filename + "-80pct.csv"
        porcentaje_seleccionado = '80%'
    elif opt == 8:
        filename_modificado = filename + "-large.csv"
        porcentaje_seleccionado = '100%'

    return filename_modificado, porcentaje_seleccionado

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)

def print_opt_1():
    #se deja por defecto que los datos se carguen en ARRAY_LIST
    """ print_data_structure()
    data_type = int(input("Ingrese el tipo de representación de la lista que desea: "))
    data_structure = choose_data_structure(data_type) """
    print('\n')
    print_opciones_archivo()
    data_structure = 'ARRAY_LIST'
    opt = int(input('Seleccione el porcentaje del archivo que desea cargar: '))
    control = new_controller(data_structure)
    filename, porcentaje = seleccionar_archivo(opt)
    print(f"Cargando el {porcentaje} de la información")
    size = load_data(control, filename)
    columnas_a_mostrar = ["Año", 
                        "Código actividad \neconómica", 
                        "Nombre actividad \neconómica", 
                        "Código sector \neconómico",
                        "Nombre sector \neconómico",
                        "Código subsector \neconómico", 
                        "Nombre subsector \neconómico",
                        "Total ingresos netos", 
                        "Total costos y gastos", 
                        "Total saldo a pagar", 
                        "Total saldo a favor"]
    list_values_info = datos_tabla(control['model'], size)
    print("Total de filas cargadas:" + str(size))
    print(tabulate(list_values_info, headers=columnas_a_mostrar, tablefmt='grid', maxcolwidths=[None, None,20,None,20,None,20, None, None, None]))
    return control, data_structure
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    data_structure, size = controller.req_1(control)
    columnas = ['Año',
                'Código actividad \neconómica', 
                'Nombre actividad económica', 
                'Código sector \neconómico',
                'Nombre sector económico',
                'Código subsector \neconómico',
                'Nombre subsector económico',
                'Total ingresos netos',
                'Total costos y gastos',
                'Total saldo a pagar',
                'Total saldo a favor'] 
        
    lista_datos = []
    for i in range(size):
        dato = lt.getElement(data_structure['data'], i+1)
        info = list(dato['info'].values())
        lista_datos.append(info)

    
    print(tabulate(lista_datos, headers=columnas, tablefmt='grid', maxcolwidths=[None, None, 30, None, 30, None, 30, None, None, None, None]))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    data_structure, size = controller.req_2(control)
    columnas = ['Año',
                'Código actividad \neconómica', 
                'Nombre actividad económica', 
                'Código sector \neconómico',
                'Nombre sector económico',
                'Código subsector \neconómico',
                'Nombre subsector económico',
                'Total ingresos netos',
                'Total costos y gastos',
                'Total saldo a pagar',
                'Total saldo a favor'] 
        
    lista_datos = []
    for i in range(size):
        dato = lt.getElement(data_structure['data'], i+1)
        info = list(dato['info'].values())
        lista_datos.append(info)

    
    print(tabulate(lista_datos, headers=columnas, tablefmt='grid', maxcolwidths=[None, None, 30, None, 30, None, 30, None, None, None, None]))




def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    data= controller.req_3(control)
    llaves_a_incluir_1 = ['Año',
                          'Código sector \neconómico',
                          'Nombre sector \neconómico',
                          'Código subsector \neconómico',
                          'Nombre subsector \neconómico',
                          'Total de retenciones \ndel subsector económico', 
                          'Total ingresos netos \ndel subsector económico',
                          'Total costos y gastos \ndel subsector económico',
                          'Total saldo a pagar \ndel subsector económico',
                          'Total saldo a favor \ndel subsector económico']
    
    llaves_a_incluir_2 = ['Código actividad \neconómica', 
                          'Nombre actividad \neconómica', 
                          'Total retenciones',
                          'Total ingresos \nnetos',
                          'Total costos \ny gastos',
                          'Total saldo a \npagar',
                          'Total saldo a \nfavor']
    informacion_1 = []
    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        año = dato['id']
        datastructure_año = dato['info']
        tamaño_datastructure_año = datastructure_año['data']['size']
        dato_info_lista = []
        for j in range(tamaño_datastructure_año-1):
            dato_1 =lt.getElement(datastructure_año['data'], j+1)
            dato_info_lista.append(dato_1['info'])
        informacion_1.append(dato_info_lista)
    print(tabulate(informacion_1, headers=llaves_a_incluir_1, tablefmt='grid', maxcolwidths=[None,None,20,None,20,None,None, None, None, None]))
    print('\n\n')

    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        dato_1 =lt.getElement(dato['info']['data'], 4)
        subsector = dato_1['info']
        año = dato['id']
        datastructure_año = dato['info']

        actividades = lt.getElement(datastructure_año['data'], tamaño_datastructure_año)
        datastructure_actividades = actividades['info']
        tamaño_datastructure_actividades = datastructure_actividades['data']['size']
        informacion_2 = []
        if tamaño_datastructure_actividades<6:
            print(f'Solo se encontraron {tamaño_datastructure_actividades} actividades económicas en {año} y en el subsector {subsector}')    
        else:
            print(f'Tres actividades que menos y más aportaron al total de retenciones en {año} y en el subsector {subsector}')
        for k in range(datastructure_actividades['data']['size']):
            dato_info_lista = []
            dato = lt.getElement(datastructure_actividades['data'], k+1)
            info_dato = dato['info']
            for llave in info_dato:
                dato_info_lista.append(info_dato[llave])
            informacion_2.append(dato_info_lista)
        print(tabulate(informacion_2, headers=llaves_a_incluir_2, tablefmt='grid',maxcolwidths=[None,20,None,None,None,None,None]))
        print('\n')


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    data= controller.req_4(control)
    llaves_a_incluir_1 = ['Año',
                          'Código sector \neconómico',
                          'Nombre sector \neconómico',
                          'Código subsector \neconómico',
                          'Nombre subsector \neconómico',
                          'Total de costos y gastos de \nnómina del subsector económico', 
                          'Total ingresos netos \ndel subsector económico',
                          'Total costos y gastos \ndel subsector económico',
                          'Total saldo a pagar \ndel subsector económico',
                          'Total saldo a favor \ndel subsector económico']
    
    llaves_a_incluir_2 = ['Código actividad \neconómica', 
                          'Nombre actividad \neconómica', 
                          'Total costos y \ngastos de nómina',
                          'Total ingresos \nnetos',
                          'Total costos \ny gastos',
                          'Total saldo a \npagar',
                          'Total saldo a \nfavor']
    informacion_1 = []
    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        año = dato['id']
        datastructure_año = dato['info']
        tamaño_datastructure_año = datastructure_año['data']['size']
        dato_info_lista = []
        for j in range(tamaño_datastructure_año-1):
            dato_1 =lt.getElement(datastructure_año['data'], j+1)
            dato_info_lista.append(dato_1['info'])
        informacion_1.append(dato_info_lista)
    print(tabulate(informacion_1, headers=llaves_a_incluir_1, tablefmt='grid', maxcolwidths=[None,None,20,None,20,None,None, None, None, None]))
    print('\n\n')

    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        dato_1 =lt.getElement(dato['info']['data'], 4)
        subsector = dato_1['info']
        año = dato['id']
        datastructure_año = dato['info']

        actividades = lt.getElement(datastructure_año['data'], tamaño_datastructure_año)
        datastructure_actividades = actividades['info']
        tamaño_datastructure_actividades = datastructure_actividades['data']['size']
        informacion_2 = []
        if tamaño_datastructure_actividades<6:
            print(f'Solo se encontraron {tamaño_datastructure_actividades} actividades económicas en {año} y en el subsector {subsector}')    
        else:
            print(f'Tres actividades que menos y más aportaron al total de costos y gastos de nómina en {año} y en el subsector {subsector}')
        for k in range(datastructure_actividades['data']['size']):
            dato_info_lista = []
            dato = lt.getElement(datastructure_actividades['data'], k+1)
            info_dato = dato['info']
            for llave in info_dato:
                dato_info_lista.append(info_dato[llave])
            informacion_2.append(dato_info_lista)
        print(tabulate(informacion_2, headers=llaves_a_incluir_2, tablefmt='grid',maxcolwidths=[None,20,None,None,None,None,None]))
        print('\n')

    

                          

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    data= controller.req_5(control)
    llaves_a_incluir_1 = ['Año',
                          'Código sector \neconómico',
                          'Nombre sector \neconómico',
                          'Código subsector \neconómico',
                          'Nombre subsector \neconómico',
                          'Total de descuentos tributarios \ndel subsector económico', 
                          'Total ingresos netos \ndel subsector económico',
                          'Total costos y gastos \ndel subsector económico',
                          'Total saldo a pagar \ndel subsector económico',
                          'Total saldo a favor \ndel subsector económico']
    
    llaves_a_incluir_2 = ['Código actividad \neconómica', 
                          'Nombre actividad \neconómica', 
                          'Total descuentos \ntributarios',
                          'Total ingresos \nnetos',
                          'Total costos \ny gastos',
                          'Total saldo a \npagar',
                          'Total saldo a \nfavor']
    informacion_1 = []
    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        año = dato['id']
        datastructure_año = dato['info']
        tamaño_datastructure_año = datastructure_año['data']['size']
        dato_info_lista = []
        for j in range(tamaño_datastructure_año-1):
            dato_1 =lt.getElement(datastructure_año['data'], j+1)
            dato_info_lista.append(dato_1['info'])
        informacion_1.append(dato_info_lista)
    print(tabulate(informacion_1, headers=llaves_a_incluir_1, tablefmt='grid', maxcolwidths=[None,None,20,None,20,None,None, None, None, None]))
    print('\n\n')

    for i in range(data['data']['size']):
        dato = lt.getElement(data['data'], i+1)
        dato_1 =lt.getElement(dato['info']['data'], 4)
        subsector = dato_1['info']
        año = dato['id']
        datastructure_año = dato['info']

        actividades = lt.getElement(datastructure_año['data'], tamaño_datastructure_año)
        datastructure_actividades = actividades['info']
        tamaño_datastructure_actividades = datastructure_actividades['data']['size']
        informacion_2 = []
        if tamaño_datastructure_actividades<6:
            print(f'Solo se encontraron {tamaño_datastructure_actividades} actividades económicas en {año} y en el subsector {subsector}')    
        else:
            print(f'Tres actividades que menos y más aportaron al total de descuentos tributarios en {año} y en el subsector {subsector}')
        for k in range(datastructure_actividades['data']['size']):
            dato_info_lista = []
            dato = lt.getElement(datastructure_actividades['data'], k+1)
            info_dato = dato['info']
            for llave in info_dato:
                dato_info_lista.append(info_dato[llave])
            informacion_2.append(dato_info_lista)
        print(tabulate(informacion_2, headers=llaves_a_incluir_2, tablefmt='grid',maxcolwidths=[None,20,None,None,None,None,None]))
        print('\n')


def print_req_6(control, anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    data = (controller.req_6(control, anio))
    
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    
    lista_headers = list(data1[0].keys())
    lista_datos = []
    for i in range(len(data1)):
        lista_datos.append(list(data1[i].values()))
    print(tabulate(lista_datos, headers=lista_headers, tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None]))
    
    print("\n\n\n")
    print("===== Subsector económico que más contribuyó: =====")
    lista_headers2 = list(data2[0].keys())
    lista_datos2 = []
    for j in range(len(data2)):
        lista_datos2.append(list(data2[j].values()))
    print(tabulate(lista_datos2, headers=lista_headers2, tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None]))

    print("\n\n\n")
    print("===== Subsector económico que menos contribuyó: =====")
    lista_headers3 = list(data3[0].keys())
    lista_datos3 = []
    for k in range(len(data3)):
        lista_datos3.append(list(data3[k].values()))
    print(tabulate(lista_datos3, headers=lista_headers3, tablefmt='grid', maxcolwidths=[None,20,None,None,None,None,None]))
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    n = int(input('Introduzca el número de actividades a identificar: '))
    anio_inicial = int(input('Introduzca el año inicial: '))
    anio_final = int(input('Introduzca el año final: '))
    if anio_inicial>anio_final:
        print('Ingrese un periodo válido')
        return
    infoMostrar = controller.req_7(control, n, anio_inicial, anio_final)

    columnas = ['Año',
                'Código actividad \neconómica', 
                'Nombre actividad económica', 
                'Código sector \neconómico',
                'Nombre sector económico',
                'Código subsector \neconómico',
                'Nombre subsector económico',
                'Total ingresos netos consolidados para el periodo',
                'Total costos y gastos consolidados para el periodo',
                'Total saldo a pagar consolidados para el periodo',
                'Total saldo a favor consolidados para el periodo'] 
    
    lista_datos = []
    for anio,datos in infoMostrar.items():
        for dato in datos:
            lista_datos_anio = list(infoMostrar[anio][dato].values())
            lista_datos.append(lista_datos_anio)
    
    print(tabulate(lista_datos, headers=columnas, tablefmt='grid', maxcolwidths=[None, None, 30, None, 30, None, 30, None, None, None, None]))

def print_opt_9(data_structure):
    print_opciones_archivo()
    opt_archive = int(input('Seleccione el porcentaje del archivo que desea cargar: '))
    control = new_controller(data_structure)
    filename = seleccionar_archivo(opt_archive)
    if opt_archive==1:
        new_data_struct, size = load_data(control, filename)
        new_data_struct = {'data': lt.subList(new_data_struct['data'], 1, (size//2))}
    else:
        new_data_struct, size = load_data(control, filename)
    print_sorting_algorithms()
    opt_sort = int(input("Seleccione el algoritmo de ordenamiento que desea usar: "))
    sorting_algorithm = choose_sorting_algorithm(opt_sort)
    print(f"Cargando información de los archivos en tipo de lista: {data_structure} ....\n")
    print(f"Ordenando la información con: {sorting_algorithm} sorting algorithm ....\n")
    sorting_time = controller.sort_1(new_data_struct, sorting_algorithm)
    print("Size:" + str(size))
    print(f"Sorting time: {sorting_time} \n")

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    llaves_a_incluir_1 = ['Código sector \neconómico',
                        'Nombre sector \neconómico',
                        'Código subsector \neconómico',
                        'Nombre subsector \neconómico',
                        'Total de impuestos a \ncargo para el subsector',
                        'Total de ingresos netos \npara el subsector',
                        'Total de costos y gastos \npara el subsector',
                        'Total saldo por pagar \npara el subsector',
                        'Total saldo a favor \npara el subsector']
    
    llaves_a_incluir_2 = ['Código actividad \neconómica',
                        'Nombre actividad económica',
                        'Total Impuesto \na cargo',
                        'Total ingresos \nnetos',
                        'Total costos \ny gastos',
                        'Total saldo \na pagar',
                        'Total saldo \na favor']
    n = int(input('Introduzca el número de actividades a identificar: '))
    anio_inicial = int(input('Introduzca el año inicial: '))
    anio_final = int(input('Introduzca el año final: '))
    if anio_inicial>anio_final:
        print('Ingrese un periodo válido')
        return
    data = controller.req_8(control, n, anio_inicial, anio_final)
    if data==1:
        print('No se encontraron registros para el periodo indicado, por favor ingrese uno válido')
        return
    list_values_info_1= []
    for subsector in data:
        datos_a_presentar = list(data[subsector].values())
        datos_a_presentar_1 = datos_a_presentar[0:9]
        list_values_info_1.append(datos_a_presentar_1)
    
    print(f'Los parámetros ingresados son: Top {n} de actividades económicas por cada subsector entre {anio_inicial} y {anio_final}')
    print(tabulate(list_values_info_1, headers=llaves_a_incluir_1, tablefmt='grid', maxcolwidths=[None,30,None,30,None,None, None, None, None]))
    print('\n\n')

    for subsector in data:
        datos_a_presentar = list(data[subsector].values())
        datos_a_presentar_2 = []
        for dato in datos_a_presentar[9]:
            datos_a_presentar_2.append(list(dato.values()))
        if len(datos_a_presentar_2)<n:
            print(f'---------- Hay solo {len(datos_a_presentar_2)} actividades económicas en subsector {subsector} -------------')
            print(tabulate(datos_a_presentar_2, headers=llaves_a_incluir_2, tablefmt='grid', maxcolwidths=[None,30,None,None, None, None, None]))
            print('\n\n')
        else:
            print(f'------------- Top {n} actividades económicas en subsector {subsector} -------------')
            print(tabulate(datos_a_presentar_2, headers=llaves_a_incluir_2, tablefmt='grid', maxcolwidths=[None,30,None,None, None, None, None]))
            print('\n\n')
    
    
        


# Se crea el controlador asociado a la vista
#control = new_controller(data_type)

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
                control, data_type = print_opt_1()
            elif int(inputs) == 2:
                print_req_1(control['req1'])

            elif int(inputs) == 3:
                print_req_2(control['req2'])

            elif int(inputs) == 4:
                print_req_3(control['req3'])

            elif int(inputs) == 5:
                print_req_4(control['req4'])

            elif int(inputs) == 6:
                print_req_5(control['req5'])

            elif int(inputs) == 7:
                anio = input("Ingrese el año del que desea saber el sector que más contribuyó al total de ingresos netos: ")
                print_req_6(control['req6'], anio)

            elif int(inputs) == 8:
                print_req_7(control['req7'])

            elif int(inputs) == 9:
                print_req_8(control['req8'])
            
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
 