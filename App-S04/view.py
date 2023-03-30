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
from tabulate import tabulate
assert cf
import traceback
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_controller(struc):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(struc)
    return control


def print_menu():
    print("\n{} Bienvenido Al Laboratorio del Grupo 1 {}\n".format("·"*15,"·"*15))
    print("» 1 « Seleccionar la estructura de datos y algoritmo de organización")
    print("» 2 « Seleccionar el tamaño de los datos")
    print("» 3 « Cargar datos sobre impuestos de renta (Personas Juridicas)")
    print("» 4 « (REQ. 1) Listar la actividad económica con mayor total saldo a pagar para todos los años disponibles")
    print("» 5 « (REQ. 2) Listar la actividad económica con mayor total saldo a favor para todos los años disponibles")
    print("» 6 « (REQ. 3) Encontrar el subsector económico con el menor total de retenciones para todos los años disponibles")
    print("» 7 « (REQ. 4) Encontrar el subsector económico con los mayores costos y gastos de nómina para todos los años disponibles")
    print("» 8 « (REQ. 5) Encontrar el subsector económico con los mayores descuentos tributarios para todos los años disponibles")
    print("» 9 « (REQ. 6) Encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico en un año específico")
    print("» 10 « (REQ. 7) Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un periodo de tiempo")
    print("» 11 « (REQ. 8) Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo")
    print("» 12 « Obtener dato dado un ID")
    print("» 0 « Salir")

def data_struc_type():
    print("\nEligue que tipo de carga quieres ejecutar: ") 
    print("   1. Array List")
    print("   2. Single Linked\n")
    o_struc = int(input())
    if o_struc == 1:
        struc='ARRAY_LIST'
    elif o_struc == 2:
        struc='SINGLE_LINKED'
    print("\nEligue que tipo de algoritmo quieres ejecutar: ")
    print("   1. Selection Sort")
    print("   2. Instertion Sort")
    print("   3. Shell Sort")
    print("   4. Merge Sort")
    print("   5. Quick Sort\n")
    op_alg = int(input())
    if op_alg == 1:
        alg = "Selection"
    elif op_alg == 2:
        alg = "Insertion"
    elif op_alg == 3:
        alg = "Shell"
    elif op_alg == 4:
        alg = "Merge"
    elif op_alg == 5:
        alg = "Quick"
    print("Usted eligió " + struc + " y el algoritmo de ordenamiento " + alg + "Sort")
    return new_controller(struc), alg

def load_data(control,arch, alg):
    """
    Carga los datos
    """
    data, delta_time = controller.load_data(control, arch, alg)
    return data, delta_time

def loadDataSteps():
    print("\n¿Qué archivo de datos desea cargar?")
    print("   Salida_agregados_renta_juridicos_AG-")
    print("   1. small.csv")
    print("   2. 5%.csv")
    print("   3. 10%.csv")
    print("   4. 20%.csv")
    print("   5. 30%.csv")
    print("   6. 50%.csv")
    print("   7. 80%.csv")
    print("   8. large.csv\n")
    op = int(input())
    if op == 1:
        arch = "small.csv"
    elif op == 2:
        arch = "5pct.csv"
    elif op == 3:
        arch = "10pct.csv"
    elif op == 4:
        arch = "20pct.csv"
    elif op == 5:
        arch = "30pct.csv"
    elif op == 6:
        arch = "50pct.csv"
    elif op == 7:
        arch = "80pct.csv"
    else:
        arch = "large.csv"
    print("Usted eligió cargar el archivo Salida_agregados_renta_juridicos_AG-" + arch)
    return arch
        
def print_data(catalog, arch, alg):
    # os.system('cls') para limpiar pantalla
    data, delta_time= load_data(catalog,arch,alg)
    print("\n")
    print("{}".format("·"*20))
    print("Loaded data info: ")
    print("Total loaded rows: "+str(data))
    print("{}".format("·"*20)) 
    print("\nThe first 3 and last 3 titles in content range are...")
    print("Content sorted by tittle:")
    data_carga = controller.data_carga_resumen(catalog)
    filas, headers = data_tabulate(data_carga)
    print(tabulate(filas, headers=headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    print("El tiempo de ejecución es: " + str(round(delta_time, 2)))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1 
    x = float(time.perf_counter()*1000)
    filas, headers = (controller.req_1(control))
    print(tabulate(filas, headers=headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    x = float(time.perf_counter()*1000)
    filas, headers = (controller.req_2(control))
    print(tabulate(filas, headers=headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    x = float(time.perf_counter()*1000)
    lista_años, lista_todos, headers1, headers2 = controller.req_3(control)
    print(tabulate(lista_años, headers=headers1, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    for laño in lista_todos:
        lista_año = lt.newList("ARRAY_LIST")
        tamaño = lt.size(laño)
        
        if tamaño <= 6:
            for elemento in lt.iterator(laño):
                lista = filtro_req3(elemento["info"])
                lt.addLast(lista_año, lista)
            print("Para el año " + str(lt.getElement(laño, 1)["info"]["Año"]) + " hay " + str(lt.size(lista_año)) + " subsectores contribuyentes.")
            print(tabulate(lista_año["elements"], headers=headers2, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
        
        else:
            lista_resumen = lt.newList("ARRAY_LIST")
            lt.addLast(lista_resumen, lt.getElement(laño, 1))
            lt.addLast(lista_resumen, lt.getElement(laño, 2))
            lt.addLast(lista_resumen, lt.getElement(laño, 3))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño) - 2))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño) - 1))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño)))
            for elemento in lt.iterator(lista_resumen):
                lista = filtro_req3(elemento["info"])
                lt.addLast(lista_año, lista)
            print("Para el año " + str(lt.getElement(laño, 1)["info"]["Año"]) + " hay 6 subsectores contribuyentes.")
            print(tabulate(lista_año["elements"], headers=headers2, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
             
        lista_año = None
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))
            
def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    x = float(time.perf_counter()*1000)
    lista_años, lista_todos, headers1, headers2 = controller.req_4(control)
    print("\n{} Req No. 4 Answer {}\n".format("-"*15,"-"*15))
    print("\nEconomic sub-sectors with the lowest total withholdings (Costos y gastos nómina) for each year")
    print(tabulate(lista_años, headers=headers1, tablefmt="grid", maxcolwidths=15, maxheadercolwidths=10))
    for laño in lista_todos:
        lista_año = lt.newList("ARRAY_LIST")
        tamaño = lt.size(laño)
        
        if tamaño < 6:
            for elemento in lt.iterator(laño):
                lista = filtro_req4(elemento["info"])
                lt.addLast(lista_año, lista)
            print("\nThere are only " + str(lt.size(lista_año)) + " economic activities in '" + str(lt.getElement(laño, 1)["info"]["Año"]) + "' and in '" + str(lt.getElement(laño, 1)["info"]["Código subsector económico"]) + "' subsector")
            print(tabulate(lista_año["elements"], headers=headers2, tablefmt="grid", maxcolwidths=15, maxheadercolwidths=10))
        
        else:
            lista_resumen = lt.newList("ARRAY_LIST")
            lt.addLast(lista_resumen, lt.getElement(laño, 1))
            lt.addLast(lista_resumen, lt.getElement(laño, 2))
            lt.addLast(lista_resumen, lt.getElement(laño, 3))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño) - 2))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño) - 1))
            lt.addLast(lista_resumen, lt.getElement(laño, lt.size(laño)))
            for elemento in lt.iterator(lista_resumen):
                lista = filtro_req3(elemento["info"])
                lt.addLast(lista_año, lista)
            print("\nThere are only " + str(lt.size(lista_año)) + " economic activities in '" + str(lt.getElement(laño, 1)["info"]["Año"]) + "' and in '" + str(lt.getElement(laño, 1)["info"]["Código subsector económico"]) + "' subsector")
            print(tabulate(lista_año["elements"], headers=headers2, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
             
        lista_año = None
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    x = float(time.perf_counter()*1000)
    info = controller.req_5(control)
    lista_anios = []
    for a in info["elements"]:
        dic = a["info"]["elements"][0]["info"].copy()
        del dic["actividades_list"]
        lista_anios += [dic]
    print("\nEconomic sub-sectors with the highest total withholdings (Descuentos tributarios) for each year")
    print(tabulate(lista_anios, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    print("\n")
    for z in info["elements"]:
        a = lt.size(z["info"]["elements"][0]["info"]["actividades_list"])
        b = z["info"]["elements"][0]["info"]["Año"]
        c = z["info"]["elements"][0]["info"]["Código subsector económico"]
        actividades_dict_list = z["info"]["elements"][0]["info"]["actividades_list"]
        
        if a < 6:
            print("There are only {} economic activities in '{}' and in '{}' subsector. The economic activities from the least to the most that contributed are:".format(a,b,c))
            lista_sin_filtrar = actividades_dict_list["elements"]
            lista_sectores = []
            for i in lista_sin_filtrar:
                lista_sectores += [i["info"]]
            lista_sectores = lista_sectores[::-1]
        else:
            print("The three economic activities that contributed the least and the most in '{}' and in '{}' subsector are:".format(b,c))
            lista_sectores = [actividades_dict_list["elements"][-1]["info"],
                              actividades_dict_list["elements"][-2]["info"],
                              actividades_dict_list["elements"][-3]["info"],
                              actividades_dict_list["elements"][2]["info"],
                              actividades_dict_list["elements"][1]["info"],
                              actividades_dict_list["elements"][0]["info"]]
        print(tabulate(lista_sectores, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print("\n¡¡ATENCIÓN!! Para ver el resultado esperado se recomienda ampliar la terminal al máximo!")
    anio = 0
    while anio == 0 or anio < 2012 or anio > 2021:
        anio = int(input("\nIngrese el año que desea analizar: "))
        if anio < 2012 or anio > 2021:
            print("\nIngrese un año valido! [2012-2021]")
    x = float(time.perf_counter()*1000)
    print("Finding the economimc activity with the highest total net income for each economic sector in '{}'...\n".format(anio))
    info = controller.req_6(control,anio)
    lista_sectores = []
    for a in info["elements"]:
        dic = a["info"].copy()
        dic["Subsector económico que mas aporto"] = a["info"]["subsectores_list"]["elements"][0]["id"]
        dic["Subsector económico que menos aporto"] = a["info"]["subsectores_list"]["elements"][-1]["id"]
        del dic["subsectores_list"]
        lista_sectores += [dic]
    print(tabulate(lista_sectores, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    # se imprimen los subsectores que mas contribuyeron al sector economico
    print("\nEconomic subsector that contributed the most: \n")
    lista_mayor = []
    for a in info["elements"]:
        dic = a["info"]["subsectores_list"]["elements"][0]["info"].copy()
        actividad_mas = a["info"]["subsectores_list"]["elements"][0]["info"]["actividad_list"]["elements"][0]["info"].copy()
        actividad_menos = a["info"]["subsectores_list"]["elements"][0]["info"]["actividad_list"]["elements"][-1]["info"].copy()
        actividad_mas_lista = []
        actividad_menos_lista = []
        for i in actividad_mas:
            actividad_mas_lista += [[i,actividad_mas[i]]]
        for i in actividad_menos:
            actividad_menos_lista += [[i,actividad_menos[i]]]
        tab_mas = tabulate(actividad_mas_lista, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=4)
        tab_menos = tabulate(actividad_menos_lista, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=4)
        dic["Actividad económica que más aporto"] = tab_mas
        dic["Actividad económica que menos aporto"] = tab_menos
        del dic["actividad_list"]
        lista_mayor += [dic]
    print(tabulate(lista_mayor, headers="keys", tablefmt="grid", maxcolwidths=26, maxheadercolwidths=8))
    
    # se imprimen los subsectores que menos contribuyeron al sector economico
    
    print("\nEconomic subsector that contributed the less: \n")
    lista_menor = []
    for a in info["elements"]:
        dic = a["info"]["subsectores_list"]["elements"][-1]["info"].copy()
        actividad_mas = a["info"]["subsectores_list"]["elements"][-1]["info"]["actividad_list"]["elements"][0]["info"].copy()
        actividad_menos = a["info"]["subsectores_list"]["elements"][-1]["info"]["actividad_list"]["elements"][-1]["info"].copy()
        actividad_mas_lista = []
        actividad_menos_lista = []
        for i in actividad_mas:
            actividad_mas_lista += [[i,actividad_mas[i]]]
        for i in actividad_menos:
            actividad_menos_lista += [[i,actividad_menos[i]]]
        tab_mas = tabulate(actividad_mas_lista, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=4)
        tab_menos = tabulate(actividad_menos_lista, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=4)
        dic["Actividad económica que más aporto"] = tab_mas
        dic["Actividad económica que menos aporto"] = tab_menos
        del dic["actividad_list"]
        lista_menor += [dic]
    print(tabulate(lista_menor, headers="keys", tablefmt="grid", maxcolwidths=26, maxheadercolwidths=8))
    
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    c = False
    while c == False:
        n = int(input("\n Ingrese TOP (N) de actividades económicas que desea identificar (Mín: 1, Max: 20): "))
        bi = int(input("\n Ingrese el límite inferior del periodo de tiempo en años: "))
        bs = int(input("\n Ingrese el límite superior del periodo de tiempo en años: "))
        if int(n) > 20 or int(n) < 0 or int(bi) > int(bs):
            print("\n Ingrese una opción valida!!!")
        else:
            c = True
    x = float(time.perf_counter()*1000)
    print("\nFinding the top '{}' economic activities with the lowest total costs and expenses between '{}' and '{}' ...\n".format(n,bi,bs))
    info = controller.req_7(control,n,bi,bs)
    print(tabulate(info, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))
    


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    c = False
    while c == False:
        n = int(input("\n Ingrese TOP (N) de actividades económicas de cada subsector que desea identificar (Mín: 1, Max: 20): "))
        bi = int(input("\n Ingrese el límite inferior del periodo de tiempo en años: "))
        bs = int(input("\n Ingrese el límite superior del periodo de tiempo en años: "))
        if int(n) > 20 or int(n) < 0 or int(bi) > int(bs):
            print("\n Ingrese una opción valida!!!")
        else:
            c = True
    x = float(time.perf_counter()*1000)
    print("\nFinding the top '{}' economic activities of each sub-sector with the highest total taxes payable between '{}' and '{}' ...\n".format(n,bi,bs))
    info = controller.req_8(control,bi,bs)
    lista_totales = []
    for a in info["elements"]:
        dic = a["info"].copy()
        del dic["list_actividades_sub"]
        lista_totales += [dic]
    print(tabulate(lista_totales, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    for z in info["elements"]:
        a = lt.size(z["info"]["list_actividades_sub"])
        lista_sectores = []
        if a < n:
            print("There are only {} activities in '{}' subsector".format(a,z["info"]["Código subsector económico"]))
            lista_sin_filtrar = z["info"]["list_actividades_sub"]["elements"]
            for i in lista_sin_filtrar:
                lista_sectores += [i["info"]]
        else:
            print("Top '{}' activities in subsector '{}'".format(n,z["info"]["Código subsector económico"]))
            c = 0
            while c < n:
                lista_sectores += [z["info"]["list_actividades_sub"]["elements"][c]["info"]]
                c += 1
        print(tabulate(lista_sectores, headers="keys", tablefmt="grid", maxcolwidths=10, maxheadercolwidths=8))
    y = float(time.perf_counter()*1000)
    print("El tiempo de ejecución es: {} ms".format(round(float(y-x),2)))

def data_tabulate(ldic): 
    filas = []
    headers = ["Año", "Código actividad económica","Nombre actividad económica", 'Código sector económico','Nombre sector económico','Código subector económico','Nombre subsector económico','Total ingresos netos','Total costos y gastos','Total saldo a pagar','Total saldo a favor']
    for fila in ldic:
        temp = []
        for dato in fila.values():
            temp.append(dato)
        filas.append(temp)
    return filas, headers

def print_get_data(control, id):
    info = controller.get_data(control,id)
    if info == None:
        print("\nNo hay algún dato con este ID")
    else:
        print("\n{}".format(info))

def filtro_req3(elemento):
    lista_final = lt.newList("ARRAY_LIST")
    lt.addLast(lista_final, elemento["Código actividad económica"])
    lt.addLast(lista_final, elemento["Nombre actividad económica"])
    lt.addLast(lista_final, elemento["Total retenciones"])
    lt.addLast(lista_final, elemento["Total ingresos netos"])
    lt.addLast(lista_final, elemento["Total costos y gastos"])
    lt.addLast(lista_final, elemento["Total saldo a pagar"])
    lt.addLast(lista_final, elemento["Total saldo a favor"])
    return lista_final["elements"]

def filtro_req4(elemento):
    lista_final = lt.newList("ARRAY_LIST")
    lt.addLast(lista_final, elemento["Código actividad económica"])
    lt.addLast(lista_final, elemento["Nombre actividad económica"])
    lt.addLast(lista_final, elemento["Costos y gastos nómina"])
    lt.addLast(lista_final, elemento["Total ingresos netos"])
    lt.addLast(lista_final, elemento["Total costos y gastos"])
    lt.addLast(lista_final, elemento["Total saldo a pagar"])
    lt.addLast(lista_final, elemento["Total saldo a favor"])
    return lista_final["elements"]
    
    
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
                control,alg = data_struc_type()
            
            elif int(inputs) == 2:
                arch = loadDataSteps()
                
            elif int(inputs) == 3:
                print_data(control, arch, alg)
                
            elif int(inputs) == 4:
                print_req_1(control)

            elif int(inputs) == 5:
                print_req_2(control)

            elif int(inputs) == 6:
                print_req_3(control)

            elif int(inputs) == 7:
                print_req_4(control)

            elif int(inputs) == 8:
                print_req_5(control)

            elif int(inputs) == 9:
                print_req_6(control)

            elif int(inputs) == 10:
                print_req_7(control)

            elif int(inputs) == 11:
                print_req_8(control)

            elif int(inputs) == 12:
                id = input("\nTeniendo en cuenta que el ID de un número construido por 8 dígitos. \
                    \nLos primeros 4 correspondientes al 'Año', y los ultimos 4 correspondientes a el 'Código actividad económica' \
                    \nPor ejemplo: Año:2012, Código actividad económica:1062, ID: 20121062 \
                    \n\nIngrese un ID: ")
                print_get_data(control, id)
                
            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
sys.exit(0)
