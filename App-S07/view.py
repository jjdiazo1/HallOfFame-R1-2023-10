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


# Modificación del límite de recursiones
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(ds):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(ds)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- [Req 1] Listar la actividad económica con mayor total saldo a pagar para todos los años disponibles")
    print("3- [Req 2] Listar la actividad económica con mayor total saldo a favor para todos los años disponibles")
    print("4- [Req 3] Encontrar el subsector económico con el menor total de retenciones para todos los años disponibles")
    print("5- [Req 4] Encontrar el subsector económico con los mayores costos y gastos de nómina para todos los años disponible")
    print("6- [Req 5] Encontrar el subsector económico con los mayores descuentos tributarios para todos los años disponibles")
    print("7- [Req 6] Encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico en un año específico")
    print("8- [Req 7] Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un periodo de tiempo")
    print("9- [Req 8] Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo")
    print("10- Obtener dato dado un código de actividad económica")
    print("0- Salir")
    


def load_data(control, dataPercentage, orderingAlg):
    """
    Carga los datos
    """
    
    data = controller.load_data(control, cf.data_dir + 
                                'DIAN/Salida_agregados_renta_juridicos_AG-' + 
                                controller.selectPercentage(dataPercentage) + '.csv',
                                orderingAlg)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    if data == None:
        print('\nNo hay un dato con el ID \'{0}\'\n'.format(id))
    else:
        print("\nEl dato con el ID", id, "es:", data['data'], '\n')


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 1 ' + '=' * 50)
    #Crea la tabla con la información del requerimiento 1
    diccionario, t = controller.req_1(control)
    grid = []
    for year in diccionario:
        elem = lt.lastElement(diccionario[year])
        tabla = [year,
                elem['Código actividad económica'], elem['Nombre actividad económica'],
                elem['Código sector económico'], elem['Nombre sector económico'],
                elem['Código subsector económico'], elem['Nombre subsector económico'],
                elem['Total ingresos netos'], elem['Total costos y gastos'],
                elem['Total saldo a pagar'], elem['Total saldo a favor']
                ]
        grid.append(tabla)
    Headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 
               'Nombre sector económico', 'Código subsector económico', 'Nombre subsector económico',
               'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
    print(tabulate(grid, Headers, tablefmt="grid", maxcolwidths=12, maxheadercolwidths=12))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 2 ' + '=' * 50)
    # Crea la tabla con la información del requerimiento 2
    diccionario, t = controller.req_2(control)
    grid = []
    for year in diccionario:
        elem = lt.lastElement(diccionario[year])
        tabla = [year,
                elem['Código actividad económica'], elem['Nombre actividad económica'],
                elem['Código sector económico'], elem['Nombre sector económico'],
                elem['Código subsector económico'], elem['Nombre subsector económico'],
                elem['Total ingresos netos'], elem['Total costos y gastos'],
                elem['Total saldo a pagar'], elem['Total saldo a favor']
                ]
        grid.append(tabla)
    Headers = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 
               'Nombre sector económico', 'Código subsector económico', 'Nombre subsector económico',
               'Total ingresos netos', 'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']
    print(tabulate(grid, Headers, tablefmt="grid", maxcolwidths=10, maxheadercolwidths=10))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 3 ' + '=' * 50)    
    # Crea la tabla para el subsector económico con el menor total de retenciones para todos los años.
    diccionario, t = controller.req_3(control)
    grid = []
    for year in diccionario:
        subsector = diccionario[year]['subsectorName']
        infoSubsec = diccionario[year]['subsectors'][subsector]
        infoActivity = infoSubsec['elements'][0]
        yearInfo = [year, 
                    infoActivity['Código sector económico'],
                    infoActivity['Nombre sector económico'], 
                    infoActivity['Código subsector económico'],
                    subsector, 
                    infoSubsec['Total retenciones'],
                    infoSubsec['Total ingresos netos'],
                    infoSubsec['Total costos y gastos'],
                    infoSubsec['Total saldo a pagar'],
                    infoSubsec['Total saldo a favor']]
        grid.append(yearInfo)
    
    TableHeaders = [
                    'Año', 
                    'Código sector económico', 
                    'Nombre sector económico', 
                    'Código subsector\neconómico',
                    'Nombre subsector\neconómico', 
                    'Total de retenciones del\nsubsector económico',
                    'Total ingresos netos\ndel subsector económico', 
                    'Total costos y gastos\ndel subsector económico',
                    'Total saldo a pagar\ndel subsector ecnómico', 
                    'Total saldo a favor\ndel subsector económico'
                    ]
    print(tabulate(grid, TableHeaders, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
    
    # Crea las tablas de las actividades económicas con el menor total de retenciones
    for year in diccionario:
        subsector = diccionario[year]['subsectorName']
        cantidadActividadesEconomicas = diccionario[year]['subsectors'][subsector]['size']
        if cantidadActividadesEconomicas >= 6:
            print('\nEn {0}, las 3 actividades económicas que menos aportaron y las tres que mas son:'.format(year))
            indexes = [1, 2, 3, cantidadActividadesEconomicas - 2, cantidadActividadesEconomicas - 1, cantidadActividadesEconomicas]
        else:
            print('\nEn {0} solo hubo {1} actividades económicas. Estas fueron:'.format(year, cantidadActividadesEconomicas))
            indexes = list(range(1, cantidadActividadesEconomicas + 1))
        
        yearGrid = []
        for i in indexes:
            subSector = lt.getElement(diccionario[year]['subsectors'][subsector], i)
            anoActual = [subSector['Código actividad económica'], 
                         subSector['Nombre actividad económica'],
                         subSector['Total retenciones'], 
                         subSector['Total ingresos netos'],
                         subSector['Total costos y gastos'], 
                         subSector['Total saldo a pagar'], 
                         subSector['Total saldo a favor']]
            yearGrid.append(anoActual)
        headers = ['Código actividad económica', 
                   'Nombre actividad económica', 
                   'Total de retenciones',
                   'Total ingresos netos', 
                   'Total costos\ny gastos', 
                   'Total saldo\na pagar', 
                   'Total saldo\na favor']
        print(tabulate(yearGrid, headers, tablefmt="grid", maxcolwidths=18, maxheadercolwidths=18))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))
    

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 4 ' + '=' * 50)
    diccionario, t = controller.req_4(control)
    # Crea la tabla de subsector con mayores costos y gastos en nómina por año
    grid = []
    for year in diccionario:
        
        subsector = diccionario[year]['noms']
        infosub = diccionario[year]['subsectors'][subsector]
        infob = lt.lastElement(infosub)
        yearInfo = [year, 
                    infob['Código sector económico'],
                    infob['Nombre sector económico'], 
                    infob['Código subsector económico'],
                    subsector, 
                    infosub['Costos y gastos nómina'],
                    infosub['Total ingresos netos'],
                    infosub['Total costos y gastos'],
                    infosub['Total saldo a pagar'],
                    infosub['Total saldo a favor']]
        grid.append(yearInfo)
    headers5 = ['Año', 
                'Código sector económico', 
                'Nombre sector económico', 
                'Código subsector\neconómico',
                'Nombre subsector\neconómico', 
                'Total costos y gastos nómina',
                'Total ingresos netos', 
                'Total costos y gastos',
                'Total saldo a pagar', 
                'Total saldo a favor']
    print(tabulate(grid, headers5, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
    
    # Crea las tablas con las actividades económicas que menos y que más aportaron cada año
    headerst = [ 
                    'Código actividad económica', 
                    'Nombre actividad económica', 
                    'Total costos y gastos nómina',
                    'Total ingresos netos', 
                    'Total costos y gastos',
                    'Total saldo a pagar', 
                    'Total saldo a favor']
    for año in diccionario:
        subsec = diccionario[año]['noms']
        z = diccionario[año]['subsectors'][subsec]['size']
        if z >= 6:
            i = [1, 2, 3, z-2, z-1, z]
            tablamax = []
            tablamin = []
            for num in i:
                elem = lt.getElement(diccionario[año]['subsectors'][subsec], num)
                if num < 4:
                    tabla = [elem["Código actividad económica"],
                    elem["Nombre actividad económica"],
                    elem['Costos y gastos nómina'],
                    elem['Total ingresos netos'],
                    elem['Total costos y gastos'],
                    elem['Total saldo a pagar'],
                    elem['Total saldo a favor']]
                    tablamax.append(tabla)
                else:
                    tabla = [elem["Código actividad económica"],
                    elem["Nombre actividad económica"],
                    elem['Costos y gastos nómina'],
                    elem['Total ingresos netos'],
                    elem['Total costos y gastos'],
                    elem['Total saldo a pagar'],
                    elem['Total saldo a favor']]
                    tablamin.append(tabla)
            print("Las 3 actividades económicas que más contribuyeron a los Costos y gastos de nómina en el año " + str(año) + " en el subsector " + str(diccionario[año]['subsectors'][subsec]["Código subsector económico"]) + " fueron: ")
            print(tabulate(tablamin, headerst, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))    
            print("Las 3 actividades económicas que menos contribuyeron a los Costos y gastos de nómina en el año " + str(año) + " en el subsector " + str(diccionario[año]['subsectors'][subsec]["Código subsector económico"]) + " fueron: ")
            print(tabulate(tablamax, headerst, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
        else:
            i = list(range(1, z+1))
            table = []
            for num in i:
                elem = lt.getElement(diccionario[año]['subsectors'][subsec], num)
                tabla = [elem["Código actividad económica"],
                elem["Nombre actividad económica"],
                elem['Costos y gastos nómina'],
                elem['Total ingresos netos'],
                elem['Total costos y gastos'],
                elem['Total saldo a pagar'],
                elem['Total saldo a favor']]
                table.append(tabla)
            print("There are only " + str(diccionario[año]['subsectors'][subsec]['size']) + " economic activities in " + str(año) + " and in " + str(diccionario[año]['subsectors'][subsec]["Código subsector económico"]) + " subsector.")
            print(tabulate(table, headerst, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
            
            
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 5 ' + '=' * 50)
    print('Subsectores económicos con los mayores descuentos tributarios por año.')
    
    ecoSubSector, t = controller.req_5(control)
    
    # Crea la tabla para el subsector económico con mayores descuentos tributarios por año
    grid = []
    for year in ecoSubSector:
        subsector = ecoSubSector[year]['nameSubsec']
        infoSubsec = ecoSubSector[year]['subsectors'][subsector]
        infoActivity = infoSubsec['elements'][0]
        yearInfo = [year, 
                    infoActivity['Código sector económico'],
                    infoActivity['Nombre sector económico'], 
                    infoActivity['Código subsector económico'],
                    subsector, 
                    infoSubsec['withholdings'],
                    infoSubsec['income'],
                    infoSubsec['spending'],
                    infoSubsec['debt'],
                    infoSubsec['profit']]
        grid.append(yearInfo)
    headers5 = ['Año', 
                'Código sector económico', 
                'Nombre sector económico', 
                'Código subsector\neconómico',
                'Nombre subsector\neconómico', 
                'Total de descuentos\ntributarios del\nsubsector económico',
                'Total ingresos netos\ndel subsector económico', 
                'Total costos y gastos\ndel subsector económico',
                'Total saldo a pagar\ndel subsector ecnómico', 
                'Total saldo a favor\ndel subsector económico']
    print(tabulate(grid, headers5, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
    
    print('\n' + '-' * 40 + ' Contribuciones por actividad económica ' + '-' * 40)
    
    # Crea las tablas de las actividades económicas con mayor contribución a los descuentos tributarios por año
    for year in ecoSubSector:
        subsector = ecoSubSector[year]['nameSubsec']
        nActivities = ecoSubSector[year]['subsectors'][subsector]['size']
        if nActivities >= 6:
            print('\nEn {0}, las 3 actividades económicas que más aportaron y las que menos son:'.format(year))
            indexes = [1, 2, 3, nActivities - 2, nActivities - 1, nActivities]
        else:
            print('\nEn {0} solo hubo {1} actividades económicas. Estas fueron:'.format(year, nActivities))
            indexes = list(range(1, nActivities + 1))
        
        yearGrid = []
        for i in indexes:
            info = lt.getElement(ecoSubSector[year]['subsectors'][subsector], i)
            actYear = [info['Código actividad económica'], info['Nombre actividad económica'],
                       info['Descuentos tributarios'], info['Total ingresos netos'],
                       info['Total costos y gastos'], info['Total saldo a pagar'], 
                       info['Total saldo a favor']]
            yearGrid.append(actYear)
        headers5Act = ['Código actividad económica', 'Nombre actividad económica', 
                       'Total de descuentos\ntributarios de la\nactividad económica',
                       'Total ingresos netos', 'Total costos\ny gastos', 
                       'Total saldo\na pagar', 'Total saldo\na favor']
        print(tabulate(yearGrid, headers5Act, tablefmt="grid", maxcolwidths=18, maxheadercolwidths=18))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))
    

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 6 ' + '=' * 50)
    año = input("Ingrese un año: ")
    
    info, t = controller.req_6(control, año)
    grid1 = []
    grid2 = []
    for x in range (1, info['size']+1):
        sector = lt.getElement(info, x)
        for nombre in sector:
            nomsubmax = sector[nombre]['maxsubnom']
            nomsubmin = sector[nombre]['minsubnom']
            table = [sector[nombre]['Código sector económico'], nombre, sector[nombre]['Total ingresos netos'], 
                     sector[nombre]['Total costos y gastos'], sector[nombre]['Total saldo a pagar'], 
                     sector[nombre]['Total saldo a favor'], sector[nombre]['maxsub'], 
                     sector[nombre]['minsub']]
            for y in range (1, sector[nombre]['size']+1):
                subsector = lt.getElement(sector[nombre], y)
                for nombresu in subsector:
                    if nombresu == nomsubmax or nombresu == nomsubmin:
                        if nombresu == nomsubmax:
                            tabla = [subsector[nombresu]['Código subsector económico'], subsector[nombresu]['Nombre subsector económico'], subsector[nombresu]['Total ingresos netos'], 
                                subsector[nombresu]['Total costos y gastos'], subsector[nombresu]['Total saldo a pagar'], 
                                subsector[nombresu]['Total saldo a favor']]
                            infoactmax = lt.lastElement(subsector[nombresu])
                            tabla_max = tabulate([['Nombre actividad económica', infoactmax['Nombre actividad económica']], 
                                                ['Total ingresos netos', infoactmax['Total ingresos netos']],
                                                ['Total costos y gastos', infoactmax['Total costos y gastos']],
                                                ['Total saldo a pagar', infoactmax['Total saldo a pagar']],
                                                ['Total saldo a favor', infoactmax['Total saldo a favor']]], ['Código actividad económica', infoactmax['Código actividad económica']],
                                                tablefmt="fancy_grid", maxcolwidths=16, maxheadercolwidths=16)
                            tabla.append(tabla_max)
                        
                        if nombresu == nomsubmin:
                            infoactmin = lt.firstElement(subsector[nombresu])
                            tabla_min = tabulate([['Nombre actividad económica', infoactmin['Nombre actividad económica']], 
                                                ['Total ingresos netos', infoactmin['Total ingresos netos']],
                                                ['Total costos y gastos', infoactmin['Total costos y gastos']],
                                                ['Total saldo a pagar', infoactmin['Total saldo a pagar']],
                                                ['Total saldo a favor', infoactmin['Total saldo a favor']]], ['Código actividad económica', infoactmin['Código actividad económica']],
                                                tablefmt="fancy_grid", maxcolwidths=16, maxheadercolwidths=16)
                            
                            tabla.append(tabla_min)
                            
                        grid2.append(tabla)
            grid1.append(table)
    headers1 = ['Código sector económico', 'Nombre sector económico', 'Total ingresos netos del sector económico', 'Total costos y gastos del sector económico',
                'Total saldo a pagar del sector económico', 'Total saldo a favor del sector económico', 'Subsector económico que más aportó', 'Subsector económico que menos aportó']
    headers2 = ['Código subsector económico', 'Nombre subsector económico', 'Total ingresos netos del subsector económico', 'Total costos y gastos del subsector económico',
                'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico', 'Actividad económica que más aportó', 'Actividad económica que menos aportó']
    print(tabulate(grid1, headers1, tablefmt="fancy_grid", maxcolwidths=18, maxheadercolwidths=18))
    print(tabulate(grid2, headers2, tablefmt="fancy_grid", maxcolwidths=[10, 10, 10, 10, 10, 10, 41, 41], maxheadercolwidths=[10, 10, 10, 10, 10, 10, 41, 41]))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 7 ' + '=' * 50)
    n = int(input('Ingrese el número de entradas que desea identificar: '))
    aInicial = int(input('Ingrese el año inicial de búsqueda: '))
    aFinal = int(input('Ingrese el año final de búsqueda: '))
    print('\n')
    
    lesserSpendingList, t = controller.req_7(control, n, aInicial, aFinal)
    
    matrix = []
    for item in lesserSpendingList['elements']:
        matrix.append([item['Año'],
                       item['Código actividad económica'],
                       item['Nombre actividad económica'],
                       item['Código sector económico'],
                       item['Nombre sector económico'],
                       item['Código subsector económico'],
                       item['Nombre subsector económico'],
                       item['Total ingresos netos'],
                       item['Total costos y gastos'],
                       item['Total saldo a pagar'],
                       item['Total saldo a favor']])
    headers7 = ['Año', 'Código actividad económica', 'Nombre actividad económica', 'Código sector económico', 'Nombre sector económico',
                'Código subsector económico', 'Nombre subsector económico', 'Total ingresos netos consolidados para el periodo',
                'Total costos y gastos consolidados para el periodo', 'Total saldo a pagar consolidados para el periodo',
                'Total saldo a favor consolidados para el periodo']
    
    print('El top {0} de actividades económicas con los costos y gastos más bajos para el periodo entre el {1} y el {2}, es:'.format(n, aInicial, aFinal))
    
    print(tabulate(matrix, headers7, tablefmt="grid", maxcolwidths=11, maxheadercolwidths=11))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))
    

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    print('\n' + '=' * 50 + ' Requerimiento 8 ' + '=' * 50)
    n = int(input('Ingrese el número de entradas que desea identificar: '))
    aInicial = int(input('Ingrese el año inicial de búsqueda: '))
    aFinal = int(input('Ingrese el año final de búsqueda: '))
    print('\n')
    
    chargeTaxes, subsectorNames, t = controller.req_8(control, aInicial, aFinal)
    
    # Crea la tabla para todos los subsectores
    matrixSubsectors = []
    for subsector in subsectorNames['elements']:
        sub = chargeTaxes[subsector]
        subInfo = sub['elements'][0]
        matrixSubsectors.append([subInfo['Código sector económico'],
                                 subInfo['Nombre sector económico'],
                                 subInfo['Código subsector económico'],
                                 subInfo['Nombre subsector económico'],
                                 sub['chargeTaxes'],
                                 sub['income'],
                                 sub['spending'],
                                 sub['debt'],
                                 sub['profit']])
    headingsSubsectors = ['Código sector económico', 
                          'Nombre sector económico',
                          'Código subsector económico', 
                          'Nombre subsector económico',
                          'Total de impuestos a cargo para el subsector', 
                          'Total ingresos netos para el subsector', 
                          'Total costos y gastos para el subsector', 
                          'Total saldo a pagar para el subsector',
                          'Total saldo a pagar para el subsector']

    print('Información general de todos los subsectores comprendidos entre {0} y {1}:'.format(aInicial, aFinal))
    print(tabulate(matrixSubsectors, headingsSubsectors, tablefmt="grid", maxcolwidths=13, maxheadercolwidths=13))

    # Crea las tablas para cada subsector individualmente
    print('\n' + '-' * 40 + 'Información subsectores individuales' + '-' * 40)
    headersEcoActivities = ['Código actividad económica', 
                            'Nombre actividad económica', 
                            'Total de impuestos a cargo', 
                            'Total de ingresos netos',
                            'Total costos y gastos', 
                            'Total saldo por pagar', 
                            'Total saldo a favor']
    for subsector in subsectorNames['elements']:
        subsectorMatrix = []
        if lt.size(chargeTaxes[subsector]) < n: x = lt.size(chargeTaxes[subsector])
        else: x = n
        for i in range(1, x + 1):
            elem = lt.getElement(chargeTaxes[subsector], i)
            subsectorMatrix.append([elem['Código actividad económica'],
                                    elem['Nombre actividad económica'],
                                    elem['Total Impuesto a cargo'],
                                    elem['Total ingresos netos'],
                                    elem['Total costos y gastos'],
                                    elem['Total saldo a pagar'],
                                    elem['Total saldo a pagar']])
        
        if x == n:
            print('\nPara el subsector \"{0}\", el top {1} de actividades con mayor aporte al total de impuestos a cargo del subsector, organizados de mayor a menor son:'.format(subsector, str(n)))            
        else:
            print('\nLos {0} registros disponibles de actividades económicas en el subsector \"{1}\", organizados de mayor a menor en aportes son:'.format(lt.size(chargeTaxes[subsector]), subsector))
        print(tabulate(subsectorMatrix, headersEcoActivities,  tablefmt="grid", maxcolwidths=15, maxheadercolwidths=15))
    print('\nEl proceso se ha demorado {0} ms.\n'.format(t))
        

# Crea una instancia del controller
control = new_controller('ARRAY_LIST')

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
                print('¿En qué estructura de datos desea guardar los datos?')
                print('1. SINGLE_LINKED\n2. ARRAY_LIST')
                dataStructType = input()
                if dataStructType == '1':
                    control = new_controller('SINGLE_LINKED')
                elif dataStructType == '2':
                    control = new_controller('ARRAY_LIST')
                
                print('\n¿Qué porcentaje de datos desea cargar?')
                print('1. 1%\n2. 5%\n3. 10%\n4. 20%\n5. 30%\n6. 50%\n7. 80%\n8. 100%')
                dataPercentage = input()
                
                print('\n¿Con qué algorítmo quiere ordenar los datos?')
                print('1. Insertion Sort\n2. Selection Sort\n3. Shell Sort\n4. Merge Sort\n5. Quick Sort')
                orderingAlg = input()
                
                data, t = load_data(control, dataPercentage, orderingAlg)
                datos = data['model']['data']
                tamaño = datos['size']
                datos_por_año = {}
                
                for inx in range (1, tamaño+1):
                    dato = lt.getElement(datos, inx)
                    if dato['data']['Año'] not in datos_por_año:
                        datos_por_año[dato['data']['Año']] = lt.newList(datastructure='ARRAY_LIST')
                    lt.addLast(datos_por_año[dato['data']['Año']], dato)
                tabla= []
                for cada_año in datos_por_año:
                    n = datos_por_año[cada_año]['size']
                    indices = [1, 2, 3, n-2, n-1, n]
                    
                    for num in indices:
                        dat = lt.getElement(datos_por_año[cada_año], num)
                        lista_aux = [dat['data']['Año'], dat['data']['Código actividad económica'], dat['data']['Nombre actividad económica'],
                        dat['data']['Código sector económico'],dat['data']['Nombre sector económico'],dat['data']['Código subsector económico'],
                        dat['data']['Nombre subsector económico'],dat['data']['Total ingresos netos'],dat['data']['Total costos y gastos'],
                        dat['data']['Total saldo a pagar'],dat['data']['Total saldo a favor']]
                        tabla.append(lista_aux)
                
                              
                headers = ["Año", 'Código actividad económica', "Nombre actividad económica", 'Código sector económico', 'Nombre sector económico', 
                           'Código subsector económico', 'Nombre subsector económico', 'Total ingresos netos', 
                           'Total costos y gastos', 'Total saldo a pagar', 'Total saldo a favor']    
                
                print("\n--------------------------------------------------------------------------")
                print("Loaded DIAN info: ")
                print("Total economic activities loaded: " + str(data["model"]["data"]["size"]))
                print("Total loaded features: " + str(len(lt.getElement(data['model']['data'], 1)['data'])))
                print("--------------------------------------------------------------------------")

                print(tabulate(tabla, headers, tablefmt="grid", maxcolwidths=[6, 7, 15, 7, 15, 7, 15, 6, 6, 6, 6], maxheadercolwidths=[6, 7, 15, 7, 15, 7, 15, 6, 6, 6, 6]))
            
                print('\n' + 'La carga de datos se ha demorado ' + str(t) + ' ms\n')
                
                
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
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = int(input("Ingrese un código de actividad económica a consultar: "))
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
