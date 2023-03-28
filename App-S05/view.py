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
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    n = chooseListType()
    a = chooseFileSize()
    al = chooseSortingType()
    control = controller.new_controller(n, a, al)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Mostrar la actividad económica con mayor saldo total a pagar de todos los años")
    print("3- Mostrar la actividad económica con mayor saldo total a favor de todos los años ")
    print("4- Encontrar el subsector económico con el menor total de retenciones para todos los años")
    print("5- Encontrar el subsector económico con los mayores costos y gasto de nómina para todos los años")
    print("6- Encontrar el subsector económico con los mayores descuentos tributarios de todos los años")
    print("7- Encontrar la actividad económica con mayores ingresos netos para cada sector económico en un año")
    print("8- Listar el top de las actividades económicas con el menor total de costos y gastos para un periodo")
    print("9- Listar el top de las actividades económicas de cada subsector con los mayores totales de impuestos en un periodo")
    print("10- Obtener dato dado un ID")
    print('11- Prueba Sort')
    print("0- Salir")


def load_data(control, filename):
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



def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1 bello
    print(controller.req_1(control))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req_2(control))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6    
    print(controller.req_6(control))


def print_req_7(control,Ain, Afn, TOP):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control,Ain, Afn, TOP))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola1
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))
      

def chooseListType():
    
    print('1: Array List')
    print('2: Linked List')
    
    working = True
    while working:
        inputs = input('Seleccione el tipo de lista que desea implementar: ')

        if int(inputs) == 1:   
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        else: 
            print('Presione un numero valido') 
            
def chooseFileSize():
    print('1: Datos al 5%')
    print('2: Datos al 10%')
    print('3: Datos al 20%')
    print('4: Datos al 30%')
    print('5: Datos al 50%')
    print('6: Datos al 80%')
    print('7: Datos al 100%')
    print('8: Datos small')
    
    working = True 
    while working:
        inputs = input('Seleccione el porcentaje de datos que quiere utilizar: ')
        if int(inputs) == 1:   
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        elif int(inputs) == 3:
            return int(inputs)
        elif int(inputs) == 4:
            return int(inputs)
        elif int(inputs) == 5:
            return int(inputs)
        elif int(inputs) == 6:
            return int(inputs)
        elif int(inputs) == 7:
            return int(inputs)
        elif int(inputs) == 8:
            return int(inputs)        
        else: 
            print('Presione un numero valido') 
            
def imput_anno_seguridad(lista):
    Ain = str(input("Ingrese el Ano inicial: "))
    Afn = str(input("Ingrese el Ano Final: "))
    TOP = str(input("Ingrese el TOP que desea ver: "))
    print("\n")
    Aun = controller.seguridad(lista)
    e = "Error"
    working = True
    while working:
        if lt.isPresent(Aun,Ain) == 0:   
            print("El anno inicial seleccionado no se encunetra disponible, Rectifique. \n")
            return e
        elif lt.isPresent(Aun,Afn) == 0:
            print("El anno Final seleccionado no se encunetra disponible, Rectifique. \n")
            return e
        elif int(Afn) < int(Ain):
            print("El anno inicial no puede ser mayor que el anno final, Rectifique. \n")      
            return e 
        else: 
            return Ain,Afn,TOP

            
def chooseSortingType():
    print('1: Selection sort')
    print('2: Insertion sort')
    print('3: Shell sort')
    print('4: Merge sort')
    print('5: Quick sort')
    
    working = True
    while working:
        inputs = input('Seleccione el tipo de ordenamiento que desea utilizar: ')

        if int(inputs) == 1:   
            return 'selectionsort'
        elif int(inputs) == 2:
            return 'insertionsort'
        elif int(inputs) == 3:
            return 'shellsort'
        elif int(inputs) == 4:
            return 'mergesort'
        elif int(inputs) == 5:
            return 'quicksort'        
        else: 
            print('Presione una opcion valida')
         
def tabulateLindo(list, headers):
    matriz = []
    for registro in lt.iterator(list):
        fila = []
        for header in headers:
            fila.append(registro[header])
        matriz.append(fila)
    print(tabulate(matriz, headers, tablefmt="grid",maxcolwidths=14, maxheadercolwidths=14))
def chooseYear():
    print('1: 2012')
    print('2: 2013')
    print('3: 2014')
    print('4: 2015')
    print('5: 2016')
    print('6: 2017')
    print('7: 2018')
    print('8: 2019')
    print('9: 2020')
    print('10: 2021')
    
    working = True
    while working:
        inputs = input('Seleccione el año que desea conocer la actividad con mayor cantidad de ingresos netos: ')

        if int(inputs) == 1:
            return int(inputs)
        elif int(inputs) == 2:
            return int(inputs)
        elif int(inputs) == 3:
            return int(inputs)
        elif int(inputs) == 4:
            return int(inputs) 
        elif int(inputs) == 5:
            return int(inputs)
        elif int(inputs) == 6:
            return int(inputs)
        elif int(inputs) == 7:
            return int(inputs)
        elif int(inputs) == 8:
            return int(inputs)
        elif int(inputs) == 9:
            return int(inputs)
        elif int(inputs) == 10:
            return int(inputs)
    

# Se crea el controlador asociado a la vista
control, filename, sortingtype = new_controller()

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
                print("Cargando información de los archivos ....\n")
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                data = load_data(control, filename)
            
                print(f'El tamaño de muestras cargadas es: {lt.size(data["data"])}.')
                tabulateLindo(controller.recortarLista(data['data']), headers)
            elif int(inputs) == 2:
                delta_t, datos_ordenados = controller.req_1(control)
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                tabulateLindo(controller.listaPorCadaAnio(datos_ordenados), headers)
                delta_time = f'{delta_t:.3f}'
                print(f'Hubo un tiempo de {delta_time} ms.')

            elif int(inputs) == 3:
                delta_t, datos_ordenados = controller.req_2(control)
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                tabulateLindo(controller.listaPorCadaAnio(datos_ordenados), headers)
                delta_time = f'{delta_t:.3f}'
                print(f'Hubo un tiempo de {delta_time} ms.')

            elif int(inputs) == 4:
                delta_t, datos_ordenados, datos_ordenados_pt2 = controller.req_3(control)
            
                headers = ['Año', 'Codigo sector economico', 'Nombre del sector economico', 'Codigo subsector economico', 'Nombre del subsector económico', 
                           'Total retenciones subsector economico', 'Total ingresos netos del subsector economico', 'Total costos y gastos del subsector economico', 
                           'Total saldo por pagor del subsector economico', 'Total saldo a favor del subsector economico', ]
                print(tabulateLindo(datos_ordenados, headers))
                
                for i in datos_ordenados_pt2['elements']:
                    headers_2 = ['Código actividad económica', 'Nombre actividad económica', 'Total retenciones', 
                                'Total ingresos netos','Total costos y gastos','Total saldo a pagar', 'Total saldo a favor']
                    print("Hay "+str(lt.size(i))+" actividades en el Año " +str(i['elements'][0]['Año']) +" y en Subsector ecomico "+str(i['elements'][0]['Código subsector económico'])) 
                    if len(i['elements']) < 6:
                        tabulateLindo(i, headers_2)
                    else: 
                        tabulateLindo(controller.recortarLista(i), headers_2)             
                
                delta_time = f'{delta_t:.3f}'
                print(f'Hubo un tiempo de {delta_time} ms.')

            elif int(inputs) == 5:
                #print_req_4(control)
                r4_1,r4_2,deltat = controller.req_4(control)
                headers1 = ['Año', 'Código sec', 'nom sec', 'Cod sub sec', 'Nombre subsector económico', 
                           'tot cyg n', 'tot ing net', 'Total cyg', 'Total spp', 'Total s a fr', ]
                #impresion Actitivades econ 
                tabulateLindo(r4_1, headers1)
                
                for i in r4_2['elements']:
                    headers2 = ['Código actividad económica', 'Nombre actividad económica', 'Costos y gastos nómina', 'Total ingresos netos','Total saldo a pagar', 
                        'Total saldo a favor']    
                    print("Hay "+str(lt.size(i))+" actividades en el Año " +str(i['elements'][0]['Año']) +" y en Subsector ecomico "+str(i['elements'][0]['Código subsector económico']))
                    if len(i['elements']) < 6:
                        tabulateLindo(i, headers2)
                    else: 
                        tabulateLindo(controller.recortarLista(i), headers2)
                deltat = f'{deltat:.3f}'
                print(f'Hubo un tiempo de {deltat} ms.')
            elif int(inputs) == 6:
                #print_req_5(control)
                deltat,resp1,resp2 = controller.req_5(control)
                cols = ['Año', 'Código Sector', 'Nombre Sector', 'Código Subsector', 'Nombre Subsector', 
                           'Total de Descuentos Tributarios', 'Total Ingresos Netos', 'Total C&G', 'Total Saldo Por Pagar', 'Total Saldo a Favor']
                #impresion Actitivades econ 
                tabulateLindo(resp1, cols)
                
                for i in resp2['elements']:
                    cols2 = ['Código actividad económica', 'Nombre actividad económica', 'Descuentos tributarios', 'Total ingresos netos','Total costos y gastos', 
                        'Total saldo a pagar','Total saldo a favor']    
                    print("Hay "+str(lt.size(i))+" actividades en el Año " +str(i['elements'][0]['Año']) +" y en Subsector ecomico "+str(i['elements'][0]['Código subsector económico']))
                    if len(i['elements']) < 6:
                        tabulateLindo(i, cols2)
                    else: 
                        tabulateLindo(controller.recortarLista(i), cols2)
                deltat = f'{deltat:.3f}'
                print(f'Hubo un tiempo de {deltat} ms.')
                
            elif int(inputs) == 7:
                year = chooseYear()
                
                datos_ordenados= controller.req_6(control, year)[0]
                w= controller.req_6(control, year)[1]
                x= controller.req_6(control, year)[2]
                delta_t= controller.req_6(control, year)[3]
                headers = ['Código sec','nom sec','tot ing net','Total cyg','Total spp','Total s a fr','Cod sub sec ++','Cod sub sec --']
                print(tabulateLindo(datos_ordenados, headers))
                headers2 = ['codigo Subsector','Total ingresos netos','Nombre subsector','Costos y gastos',
                            'Salgo a pagr','Saldo a Favor','MA','MAS']
                
                print("TABULTE SE NIEGA A FUNCIONAR, SE IMPRIME CRUDO \n")
                
                print(w)
                print(x)
                delta_t = f'{delta_t:.3f}'
                print(f'Hubo un tiempo de {delta_t} ms.')
            elif int(inputs) == 8:
                x = imput_anno_seguridad(control)
                if x == "Error":
                    print("intentelo de nuevo. \n")
                else:
                    Ain, Afn, TOP = x
                    r7, delta_t = controller.req_7(control,Ain, Afn, TOP)
                    headers = ['Año','Código actividad económica', 'Nombre actividad económica',
                            'Código sector económico','Nombre sector económico', 'Código subsector económico',
                            'Nombre subsector económico', 'Total ingresos netos','Total costos y gastos',
                            'Total saldo a pagar','Total saldo a favor']
                    tabulateLindo(r7,headers)
                    delta_t = f'{delta_t:.3f}'
                    print(f'Hubo un tiempo de {delta_t} ms.')
            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)
                
            elif int(inputs) == 11:
                tipo = chooseSortingType()
                delta_t, datos_ordenados = controller.sortGeneral(control['model']['data'], tipo)
                headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico', 
                           'Nombre subsector económico', 'Código subsector económico', 'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 
                           'Total saldo a favor']
                tabulateLindo(controller.recortarLista(datos_ordenados), headers)
                delta_time = f'{delta_t:.3f}'
                print(f'Hubo un tiempo de {delta_time} ms.')

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)



