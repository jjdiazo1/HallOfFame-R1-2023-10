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
from os import system
from datetime import date, time, datetime
import time
from App import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    system("cls")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronólógica de los artistas")
    print("3- Lista cronológica de las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento ")
    print("7- Crear nueva exposición")

catalogo = None

def initCatalogo():
    """
    Inicializa el catalogo del modelo
    """
    return controller.initCatalogo()

def cargarDatos(catalogo):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.cargarDatos(catalogo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
            
        print("Cargando información de los archivos ....")
        catalogo = controller.initCatalogo(tipo_lista = 'ARRAY_LIST')
        cargarDatos(catalogo)

        system("cls")
        

    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input('Digite un año inicial: '))
        anho_final = int(input('Digite un año final: '))        
        datos = catalogo.copy()
        identificador = 1
        
        info = controller.llamarArtistas(datos, anho_inicial, anho_final, tipo_lista = 'ARRAY_LIST')
        info_ordenada = controller.llamarInsertion(info, identificador)      
        lista_final = info_ordenada[1]
        tiempo = info_ordenada[0]
        
        primeros_3 = lt.subList(lista_final, 1, 3)  
        ultimos_3 = lt.subList(lista_final, (lt.size(lista_final)-2), 3)  
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(lt.size(lista_final), anho_inicial, anho_final)
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(len(lista_final['elements']), anho_inicial, anho_final)
        
        print(resultado_1)
        print('========================================================')
        
        print('Los primeros 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print(' ')  
        print('Los últimos 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print('==================================================================================================')    
        print('El tiempo de ejecución fue de: ', tiempo, ' ms.')

        input()
        system("cls")


    elif int(inputs[0]) == 3:
        
        fecha_inicial_texto = input('Escriba la fecha inicial: ')
        fecha_inicial = datetime.strptime(fecha_inicial_texto, '%Y-%m-%d')
        fecha_final_texto = input('Escriba la fecha final: ')
        fecha_final = datetime.strptime(fecha_final_texto, '%Y-%m-%d')
        datos = lt.subList(catalogo['obras'], 1, lt.size(catalogo['obras']))
        datos = datos.copy()
        identificador = 3
        resultado = controller.llamarQuicksort(datos, identificador)   
        dic=resultado[1]
        tiempo = resultado[0]
        datosArtistas = catalogo['artistas']
        dic_con_artista = controller.llamarAgregarArtistaPorId(dic, datosArtistas)
        lista_rango=lt.newList('ARRAY_LIST')
        
        for elemento in lt.iterator(dic_con_artista):
            if elemento['fecha_adquisicion']=='':
                pass
            else:
                fecha_elemento=datetime.strptime(elemento['fecha_adquisicion'], '%Y-%m-%d')
                if fecha_elemento > fecha_inicial and fecha_elemento < fecha_final:
                  lt.addLast(lista_rango, elemento)

        numero_elementos = lt.size(lista_rango)
        primeros_3 = lt.subList(lista_rango, 1, 3)
        ultimos_3 = lt.subList(lista_rango, (lt.size(lista_rango)-4), 3)
        
        print("El número total de obras adquiridas por compra es de : " + str(controller.obrasAdquiridasPorCompra(lista_rango)))
        print('El número de elementos en el rango es: ' + str(numero_elementos))
        print(' ')
        print('Los tres primeros elementos son:')
        print('        Título         |    Artísta(s)    |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        print('')
        print('Los tres últimos elementos son:')
        print('        Título         |    Artísta(s)    |    Fecha    |     Medio     |       Dimensiones       ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        print(' ')
        print('El tiempo de ejecución fue de: ', tiempo, ' ms.')

        input()
        system("cls")
        
        #print("Para la muestra de", tamanho_muestra, " elementos, el tiempo (mseg) es: ", str(resultado[0]))   
        
    
    elif int(inputs[0]) == 4:
        
        datos = catalogo.copy()
        identificador = 2
        nombreArtista = str(input('Escriba el nombre del artista a consultar: '))
        
        idArtista = controller.llamarConsultarId(datos, nombreArtista)  
        print(idArtista)    
        listaFiltradaPorId = controller.llamarFiltrarObrasPorId(datos, idArtista, tipo_lista = 'ARRAY_LIST')
        print(listaFiltradaPorId)
        listaOrdenadaDeObras = controller.llamarInsertion(listaFiltradaPorId[0], identificador)
        
        mayor = 0
        tecnica_mayor = None
        
        for i in lt.iterator(listaFiltradaPorId[2]):
            cuant = listaFiltradaPorId[1].count(i)
            if cuant > mayor:
                mayor = cuant
                tecnica_mayor = i
                
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombreArtista, idArtista, lt.size(listaOrdenadaDeObras[1])))
        print(('Existen {} medios/técnicas diferentes en su trabajo.').format(lt.size(listaFiltradaPorId[2])))
        print('Su técnica más utilizada es {} con {} obras.'.format(tecnica_mayor, mayor))    
        print('')   
        print('\tTítulo \t |Fecha de la obra|    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')      
        for i in lt.iterator(listaOrdenadaDeObras[1]):
            if i['tecnica'] == tecnica_mayor:
                print('{}\t   {} \t\t {} \t\t {}'.format(i['titulo'], i['fecha'], i['tecnica'], i['dimensiones']))
        print('')
        print('El tiempo de ejecución fue de: ', listaOrdenadaDeObras[0], ' ms.')
        
        input()
        system("cls")
        
    
    elif int(inputs[0]) == 5:

        datos = catalogo.copy()
        print("Clasificando ...")
        lista = controller.llamarListaNacionalidades(datos)
        nacionalidad = lista[0][0]
        lista_obras = controller.llamarBuscarObrasPorNacionalidad(datos, nacionalidad)
        datosArtistas = datos['artistas']
        lista_obras_con_artistas = controller.llamarAgregarArtistaPorId(lista_obras, datosArtistas)
        cont = 0   
        primeras3 = lt.subList(lista_obras_con_artistas, 1, 3) 
        ultimas3 = lt.subList(lista_obras_con_artistas, (lt.size(lista_obras_con_artistas)- 2), 3) 
        
        print(primeras3)     
        print(ultimas3)
        
        print('La lista de nacionalidades ordenadas por el total de obras de mayor a menor (TOP 10) es :')
        print(' ')
        print(lista[0:10])
        print(' ')
        print(f'Las primeras 3 obras de nacionalidad {nacionalidad}')
        
        print('\tTítulo \t |   Artista(s)   |   Fecha de la obra   |    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')
        
        for i in lt.iterator(primeras3):
            print('{}\t   {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        print(' ')
        print(f'Las ultimas 3 obras de nacionalidad {nacionalidad}')
        
        print('\tTítulo \t |   Artista(s)   |   Fecha de la obra   |    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')
        
        for i in lt.iterator(ultimas3):
            print('{}\t   {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['fecha'], i['tecnica'], i['dimensiones']))
        
        input()
        system("cls")
        
    elif (int(inputs[0])) == 6:
        datos = catalogo.copy()
        departamento = input("Escriba el departamento del museo a analizar: ")
        lista_obras_departamento = controller.llamarDarListaObrasDepartamento(datos,departamento)
        print('El número de obras en el departamento es: ' + str(lt.size(lista_obras_departamento)))
        costo = controller.llamarDarPrecioTransporteDepartamento(lista_obras_departamento)
        print('El costo de transportar todo el departamento de obras es de: ' + str(round(costo, 2)) + ' USD')
        peso_total = controller.llamarDarPesoTotalDepartamento(lista_obras_departamento)
        print('El peso total de las obras del departamento es de: ' + str(peso_total) + 'Kg')
        lista_ordenada = controller.llamarQuicksort(lista_obras_departamento, 3)
        datosArtistas = datos['artistas']
        tiempo1 = lista_ordenada[0]
        lista_final = controller.llamarAgregarArtistaPorId(lista_ordenada[1], datosArtistas)
        antiguas5 = lt.subList(lista_final, 1, 5)
        
        print('Las 5 obras mas antiguas son:')
        print('\tTítulo \t |   Artista(s)   |   Clasificación   |    Fecha de la obra   |    Técnica    |  \t\t Dimensiones   | Costo Asociado ')  
        print('===============================================================================================================')
        for i in lt.iterator(antiguas5):
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['clasificacion'], i['fecha'], i['tecnica'], i['dimensiones'], i['costo_transporte']))
        print(' ')
        lista_obras_ordenadas_costo = controller.llamarQuicksort(lista_final, 4)
        costosas5 = lt.subList(lista_obras_ordenadas_costo[1], (lt.size(lista_obras_ordenadas_costo[1])- 4), 5)
        tiempo2 = lista_obras_ordenadas_costo[0]
        print('Las 5 obras mas costosas para transportar son:')
        print('\tTítulo \t |   Artista(s)   |   Clasificación   |    Fecha de la obra   |    Técnica    |  \t\t Dimensiones   | Costo Asociado ')  
        print('===============================================================================================================')
        for i in lt.iterator(costosas5):
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['clasificacion'], i['fecha'], i['tecnica'], i['dimensiones'], i['costo_transporte']))
        print('')
        tiempo_total = tiempo1 + tiempo2
        print('El tiempo de ejecución fue de: ',tiempo_total, ' ms.')
        
        input()
        system("cls")
    
    elif int(inputs[0]) == 7:
        
        tiempo_inicial = time.process_time()
        datos = catalogo.copy()
        anhoInicial = int(input("Digite el año inicial: "))
        anhoFinal = int(input("Digite el año final: "))
        areaDisponible = float(input("Digite el área disponible en m^2: "))
        
        #lista_fechas_modificadas = controller.llamarfiltrarFechasObras(datos['obras'])
        datosArtistas = catalogo['artistas']
        rangoObrasRequerido = controller.llamarObtenerRangoObras(datos, anhoInicial, anhoFinal, tipo_lista = 'ARRAY_LIST')
        nuevaExposicion1 = controller.llamarCrearExposicion(rangoObrasRequerido, areaDisponible, tipo_lista = 'ARRAY_LIST')
        nuevaExposicion = controller.llamarAgregarArtistaPorId(nuevaExposicion1[0], datosArtistas)
        
        ultimas_5 = lt.subList(nuevaExposicion, (lt.size(nuevaExposicion)- 4), 5)
        
        print('El MoMA va a exhibir piezas desde {} hasta {}'.format(anhoInicial, anhoFinal))
        print('Hay {} posibles piezas para un área de {} m^2 '.format(lt.size(rangoObrasRequerido), areaDisponible))
        print('La posible exhibición tiene {} piezas'.format(lt.size(nuevaExposicion)))
        print('Se ocuparon {} m^2 de los {} m^2 disponibles'.format(round(nuevaExposicion1[1], 2), areaDisponible))
        print('Las primeras 5 obras: ')
        print('\tTítulo \t |  Artista(s) |    Fecha    |    Clasificación    |    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================') 
        cont1 = 0
        for i in lt.iterator(nuevaExposicion):
            if cont1 < 5:
                print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['fecha'], i['clasificacion'], i['tecnica'], i['dimensiones']))
            cont1 += 1
        print('')
        print('Las últimas 5 obras: ')
        print('\tTítulo \t |  Artista(s) |    Fecha    |    Clasificación    |    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')  
        for i in lt.iterator(ultimas_5):
            print('{}\t   {} \t\t {} \t\t {} \t\t {} \t\t {}'.format(i['titulo'], i['artista'], i['fecha'], i['clasificacion'], i['tecnica'], i['dimensiones']))      
        tiempo_final = time.process_time()
        duracion = (tiempo_final-tiempo_inicial)*1000
        print('El tiempo de ejecución fue de: ',duracion, ' ms.')
        input()
        system("cls")
        

    else:
        system("cls")
        sys.exit(0)
sys.exit(0)
