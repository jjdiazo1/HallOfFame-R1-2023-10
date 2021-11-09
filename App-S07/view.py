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
import time
from DISClib.ADT import list as lt
assert cf

default_limit=1000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la lista de artistas ordenada cronológicamente")
    print("3- Consultar la lista de las adquisiciones ordenada cronológicamente")
    print("4- Consultar las obras de un artista ordenadas por técnica")
    print("5- Consultar la lista de obras clasificadas por la nacionalidad de su creador")
    print("6- Consultar el costo de transportar las obras de un departamento")
    print("7- Consultar la nueva exposición propuesta según el area disponible")
    print("0- Salir")




def museoArrayList():
    return controller.inicatalogArrayList()
def cargarDatos(museo):
    return controller.cargarDatos(museo)
def imprimirDatosObra(obras):
    for obra in obras['elements']:
        x={'Title':obra['Title'],
        'Date':obra['Date'],
        'Medium': obra['Medium'],
        'Dimensions': obra['Dimensions'],
        'fecha adquisicion': obra['DateAcquired']}
        print(x)
def imprimirDatosArtista(artistas):
    for artista in artistas['elements']:
        x={'Nombre': artista['DisplayName'],
        'Año de nacimiento': artista['BeginDate'],
        'Año de fallecimiento': artista['EndDate'],
        'Nacionalidad': artista['Nationality'],
        'Genero': artista['Gender']}
        print(x)
def imprimirDatosObra2(obras):
    for obra in obras['elements']:
        x={'Title': obra['Title'],
        'Date':obra['Date'],
        'Medium': obra['Medium'],
        'Dimensions': obra['Dimensions']}
        print(x)
def imprimirDatosObra3(obras):
    for obra in obras['elements']:
        x={'Title': obra['Title'],
        'Date':obra['Date'],
        'Clasification': obra['Classification'],
        'Medium': obra['Medium'],
        'Dimensions': obra['Dimensions']}
        print(x)
def imprimirDatosObra4(obras):
    for obra in obras['elements']:
        x={'Title': obra['Title'],
        'Date':obra['Date'],
        'Clasification': obra['Classification'],
        'Medium': obra['Medium'],
        'Dimensions': obra['Dimensions'],
        'Costo': obra['Costo']}
        print(x)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        museo= museoArrayList()
        cargarDatos(museo)
        
        print('Informacion de artistas cargados  ' + str(lt.size(museo['artistas'])))
        print('Información de las obras cargadas  '+ str(lt.size(museo['artistas'])) )
        print('Artistas cargados:   ' + str(lt.size(museo['artistas'])))
        print('Obras cargados:  ' + str(lt.size(museo['obras'])))
        print('Ultimas tres obras  '+ str(controller.darUltimasObras(museo['obras'])))
        print('Ultimos tres artistas   '+ str(controller.darUltimosArtistas(museo['artistas'])))

    elif int(inputs[0]) == 2:
        articulo= 'artistas'
        lista= museo[articulo]
        fechai= input('Inserte el año inicial en el formato AAAA   ')
        fechaf= input('Inserte el año final en el formato AAAA    ')
        start_time = time.process_time()#O(K)
        z= controller.sortArrayListArtistMerge(lista) #linearitmica O(N(logN))

        lista_final= controller.fechasRangoArtist(z, fechai, fechaf) #Lineal O(N)
        stop_time = time.process_time() #O(K)
        elapsed_time_mseg = (stop_time - start_time)*1000 #O(K)
        ultimas=controller.darUltimosArtistas(lista_final) #O(K)
        primeras=controller.darPrimerosArtistas(lista_final)#O(K)

        print("Artistas nacidos en el rango de fechas:   "+ str(lt.size(lista_final)))
        print('Primeros tres artistas:  ')
        imprimirDatosArtista(primeras)
        print('Ultimos tres artistas:   ') 
        imprimirDatosArtista(ultimas)
        print('El ordenamiento tomo   '+ str(elapsed_time_mseg)+ '  tiempo en mseg')
        


    elif int(inputs[0]) == 3:
        articulo= 'obras'
        lista= museo[articulo]
        fechai= input('Inserte la fecha inicial en el formato AAAA-MM-DD   ')
        fechaf= input('Inserte la fecha final en el formato AAAA-MM-DD    ')
        start_time = time.process_time()#O(K)
        z= controller.sortArrayListMerge(lista)#O(N(logN))
        lista_final= controller.fechasRango(z, fechai, fechaf)#O(N)
        
        stop_time = time.process_time()#O(K)
        elapsed_time_mseg = (stop_time - start_time)*1000#O(K)
        primeras=controller.darPrimerasObras(lista_final)#O(K)
        ultimas=controller.darUltimasObras(lista_final)#O(K)
        

        print("Aquisiciones en el rango de fechas:  "+ str(lt.size(lista_final)))
        print("Obras adquiridas por compra:  " + str(controller.obrasPurchase(lista_final)))
        print('Primeras tres obras: ')
        imprimirDatosObra(primeras)
        print('Ultimas tres obras:  ') 
        imprimirDatosObra(ultimas)
        print('El ordenamiento tomo   '+ str(elapsed_time_mseg)+ '  tiempo en mseg')
            
    

    elif int(inputs[0]) == 4:
        nombre= input('Ingrese el nombre del artista que desea consultar  ')
        start_time = time.process_time()#O(K)
        id= controller.artistaID(museo, nombre)#O(N)
        obras = controller.obrasID(museo, id)#O(N)
        numero= lt.size(obras)#O(1)
        tecnicas=controller.listarTecnicas(obras)#O(N)
        listaT = controller.contarTecnicas(tecnicas)#O(N)
        tecnicaMasFrecuente=controller.tecnicaMasFrecuente(listaT)#O(N)
        obrasTecnica= controller.clasificarObrasPorTecnica(obras, lt.firstElement(tecnicaMasFrecuente))#O(N)
        stop_time = time.process_time()#O(K)
        elapsed_time_mseg = (stop_time - start_time)*1000#O(K)

        print('Hay  '+str(numero)+'  obras del artista  '+nombre)
        print('El artista usa '+ str(len(listaT.keys())) +' tecnicas')
        print('La tecnica mas utilizada es: '+ lt.getElement(tecnicaMasFrecuente,1) + " , con un total de:  " + str(lt.getElement(tecnicaMasFrecuente,2)) )
        print('Las obras que utilizan  '+ lt.firstElement(tecnicaMasFrecuente) +' son:')
        imprimirDatosObra2(obrasTecnica)
        print('El ordenamiento tomo   '+ str(elapsed_time_mseg)+ '  tiempo en mseg')


    elif int(inputs[0]) == 5:
        print("Obras clasificadas por la nacionalidad de su creado:")

    elif int(inputs[0]) == 6:
        departamento= input('Inserte el departamento en el que se desea realizar el analisis   ')
        start_time = time.process_time()#O(K)
        obras= controller.obraDepartamento(museo, departamento)#O(N)
        controller.precioObra(obras)#O(N)
        obrasA=controller.sortArrayListMergeDate(obras)#O(N(logN))
        antiguas= controller.darPrimerasObras5(obras)#O(K)
        obrasP=controller.sortArrayListMergeCost(obras)#O(N(logN))
        caras= controller.darUltimasObras5(obrasP)#O(K)
        peso= controller.pesoObra(obras)#O(N)
        precio=controller.sumaPrecios(obras)#O(N)
        stop_time = time.process_time()#O(K)
        elapsed_time_mseg = (stop_time - start_time)*1000#O(K)

        print("El total de obras a transportar es: " +str(lt.size(obras)))
        print("El estimado en USD del precio del servicio es " + str(precio))
        print ("El peso estimado de las obras es: " + str(peso))
        print("Las 5 obras mas antigua a transportar son: ")
        imprimirDatosObra4(antiguas)

        print("Las 5 obras mas costosas para transportar son: " )
        print('/n/')
        imprimirDatosObra4(caras)
        print('El ordenamiento tomo   '+ str(elapsed_time_mseg)+ '  tiempo en mseg')

    elif int(inputs[0]) == 7:
        print("Nueva exposición propuesta según el area disponible:" )
        articulo= 'obras'
        lista= museo[articulo]
        fechai= input('Inserte la fecha inicial en el formato AAAA')
        fechaf= input('Inserte la fecha final en el formato AAAA')
        area= input('ingrese el area disponible para la exposición')
        z= controller.sortArrayListMergeDate(lista)
        listaf=controller.fechasRangoObras(z, fechai, fechaf)
        metrosObras= controller.metrosObras(float(area), listaf)
        primeras= controller.darPrimerasObras5(lt.getElement(metrosObras, 1))
        ultimas=controller.darUltimasObras5(lt.getElement(metrosObras, 1))
        print('Hay'+ str(lt.size(lt.getElement(metrosObras, 1))) + 'obras en la exposición')
        print('Se ocupan aproximadamente' + str(lt.getElement(metrosObras, 2))+ 'metros cuadrados en la exposición')
        print ('Primeras 5 obras:')
        imprimirDatosObra3(primeras)
        print ('Ultimas 5 obras:')
        imprimirDatosObra3(ultimas)


    elif int(inputs[0]) == 0:
        sys.exit(0)

