"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(listtype):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    
    data_structs = {
        'data': lt.newList(listtype),
    }
    return data_structs

def recortarLista(list):
    
    '''
    Funcion que retorna los primeros 3 y los ultimos 3 elementos de una lista dada.
    '''
    
    filtrado = lt.newList() #Lista que contiene las 3 primeras y las 3 ultimas
    first = lt.subList(list, 1, 3) #Mis tres primeros datos
    threelast =lt.size(list)-3 #Mis ultimos 3 datos  
    last = lt.subList(list, threelast, 3) #Sublista con los 3 ultimos 
    
    for element in lt.iterator(first): #Ciclo que une los tres primeros elementos
        lt.addLast(filtrado, element)
        
    for element in lt.iterator(last): #Ciclo que une los ultimos tres elementos
        lt.addLast(filtrado, element)
    return filtrado

def listaPorCadaAnio(list):
    '''
    Funcion que retorna los primeros elementos de cada año de una lista dada.
    '''
    
    filtrado = lt.newList()
    anios_list = lt.newList()
    
    for element in lt.iterator(list):
        
        anio = element['Año']
        
        if not lt.isPresent(anios_list, anio):
            lt.addLast(anios_list, anio)
            lt.addLast(filtrado, element)
        
    return filtrado
    
# Funciones para agregar informacion al modelo

def add_register(data_structs, data):
    lt.addLast(data_structs['data'], data)

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """    
    return useMergeSort(data_structs, cmp_impuestos_by_anio_Saldo)

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    
    return useMergeSort(data_structs, cmp_impuestos_by_anio_Saldo_a_Favor)


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    
    #------ Años unicos -----
    listaA = lt.newList('ARRAY_LIST')
    data_structs = useQuickSort(data_structs['data'], compareYear)
    uniqueYear = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaA, i['Año'])
        if lt.isPresent(uniqueYear, i['Año']) == 0:
           lt.addLast(uniqueYear,i['Año'])
    #-------- codigos subsec unicos------
    listaC = lt.newList('ARRAY_LIST')
    subSectorCodeList = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaC,i['Código subsector económico'])
        if lt.isPresent(subSectorCodeList,i['Código subsector económico']) == 0:
           lt.addLast(subSectorCodeList, i['Código subsector económico'])     
    apa = lt.newList('ARRAY_LIST')
    #------- dicionario de actividades econ por anos-----
    for i in lt.iterator(uniqueYear): #parche :(
        x = lt.newList('ARRAY_LIST')
        for j in lt.iterator(data_structs):
            if j['Año'] == i:
                lt.addLast(x,j)
        x = useQuickSort(x, compareRetencionTotal) 
        lt.addLast(apa, x)
    #----- acumulados ---------
    fin = lt.newList('ARRAY_LIST')
    posAPA = 1
    for j in lt.iterator(uniqueYear):
        fin2 = lt.newList('ARRAY_LIST')
        pos_min = 1
        pos = 1 
        min_ = 100000000000
        for i in lt.iterator(subSectorCodeList):
            b = {}
            b['Año']=0
            b['Codigo sector economico']=0
            b['Nombre del sector economico']=0
            b['Codigo subsector economico']=0
            b['Nombre del subsector económico']=0
            b['Total retenciones subsector economico']=0
            b['Total ingresos netos del subsector economico']=0
            b['Total costos y gastos del subsector economico']=0
            b['Total saldo por pagor del subsector economico']=0
            b['Total saldo a favor del subsector economico']=0
            year = lt.getElement(apa, posAPA)
            for activity in lt.iterator(year):
                if activity['Código subsector económico']== i:
                    if b['Año']==0:
                        b['Año']=j
                        b['Codigo sector economico']=activity['Código sector económico']
                        b['Nombre del sector economico']=activity['Nombre sector económico']
                        b['Codigo subsector economico']=i  
                        b['Nombre del subsector económico'] = activity['Nombre subsector económico']
                    b['Total retenciones subsector economico']+=(int(activity['Total retenciones']))
                    b['Total ingresos netos del subsector economico']+= (int(activity['Total ingresos netos']))
                    b['Total costos y gastos del subsector economico']+= (int(activity['Total costos y gastos']))
                    b['Total saldo por pagor del subsector economico']+= (int(activity['Total saldo a pagar']))
                    b['Total saldo a favor del subsector economico']+= (int(activity['Total saldo a favor'])) 
            lt.addLast(fin2,b) 
            if min_ >= b['Total retenciones subsector economico'] and b['Año'] != 0:
                min_ = b['Total retenciones subsector economico']
                pos_min = pos
            pos += 1   
        lt.addLast(fin, lt.getElement(fin2, pos_min))
        posAPA += 1
    fin3 = lt.newList('ARRAY_LIST')
    mimi = lt.newList('ARRAY_LIST')
    for pos in range(0,(lt.size(uniqueYear))):
        lt.addLast(mimi,pos)
    for i in lt.iterator(mimi):
        fin4 =  lt.newList('ARRAY_LIST')
        codemin = (lt.getElement(fin, i+1))['Codigo subsector economico']
        eco_activity = lt.getElement(apa, i+1)
        for j in eco_activity['elements']:
            if j['Código subsector económico'] == codemin:
                lt.addLast(fin4,j)
        lt.addLast(fin3,fin4)

    return fin, fin3 
         


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    #------ Anos unicos -----
    data_structs = useQuickSort(data_structs['data'], compareYear)
    listaA = lt.newList('ARRAY_LIST')
    aUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaA,i['Año'])
        if lt.isPresent(aUNIC,i['Año']) == 0:
           lt.addLast(aUNIC,i['Año'])
    #-------- codigos subsec unicos------
    listaC = lt.newList('ARRAY_LIST')
    cUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaC,i['Código subsector económico'])
        if lt.isPresent(cUNIC,i['Código subsector económico']) == 0:
           lt.addLast(cUNIC,i['Código subsector económico'])     
    
    #------- lista de actividades econ por anos-----
    apa = lt.newList('ARRAY_LIST')
    for i in lt.iterator(aUNIC): 
        x = lt.newList('ARRAY_LIST')
        for j in lt.iterator(data_structs):
            if j['Año'] == i:
                lt.addLast(x,j)
        x = quk.sort(x,cmp_req_4) 
        lt.addLast(apa,x)
    #------ acumulados ---------
    fin = lt.newList('ARRAY_LIST')
    posAPA = 1 
    for j in lt.iterator(aUNIC):
        fin2 = lt.newList('ARRAY_LIST')
        pos_max = 1
        pos = 1 
        max_ = 0
        for i in lt.iterator(cUNIC):
            b = {}
            b['Año']=0
            b['Código sec']=0
            b['nom sec']=0
            b['Cod sub sec']=0
            b['Nombre subsector económico']=0
            b['tot cyg n']=0
            b['tot ing net']=0
            b['Total cyg']=0
            b['Total spp']=0
            b['Total s a fr']=0
            '''
            for i in range(10):
                lt.addLast(b,0)   
            ''' 
            an = lt.getElement(apa,posAPA)
            for act in lt.iterator(an):
                if act['Código subsector económico']==i:
                    '''
                    if lt.firstElement(b)==0:
                        lt.changeInfo(b,1,j)
                        lt.changeInfo(b,2,act['Código sector económico'])
                        lt.changeInfo(b,3,act['Nombre sector económico'])
                        lt.changeInfo(b,4,i)  
                        lt.changeInfo(b,5,act['Nombre subsector económico'])
                    lt.changeInfo(b,6,(lt.getElement(b,6) + int(act['Costos y gastos nómina'])))
                    lt.changeInfo(b,7,(lt.getElement(b,7) + int(act['Total ingresos netos'])))
                    lt.changeInfo(b,8,(lt.getElement(b,8) + int(act['Total costos y gastos'])))
                    lt.changeInfo(b,9,(lt.getElement(b,9) + int(act['Total saldo a pagar'])))
                    lt.changeInfo(b,10,(lt.getElement(b,10) + int(act['Total saldo a favor'])))
                    '''
                    if b['Año']==0:
                        b['Año']=j
                        b['Código sec']=act['Código sector económico']
                        b['nom sec']=act['Nombre sector económico']
                        b['Cod sub sec']=i  
                        b['Nombre subsector económico'] = act['Nombre subsector económico']
                    b['tot cyg n']+=(int(act['Costos y gastos nómina']))
                    b['tot ing net'] += (int(act['Total ingresos netos']))
                    b['Total cyg']+= (int(act['Total costos y gastos']))
                    b['Total spp']+= (int(act['Total saldo a pagar']))
                    b['Total s a fr']+= (int(act['Total saldo a favor']))

            lt.addLast(fin2,b) 
            '''      
            if max_ < lt.getElement(b,6):
                max_ = lt.getElement(b,6)
                pos_max = pos
            pos += 1   
            '''
            if max_ < b['tot cyg n']:
                max_ = b['tot cyg n']
                pos_max = pos
            pos += 1  
        lt.addLast(fin, lt.getElement(fin2, pos_max))     
        posAPA +=1  
    fin3 = lt.newList('ARRAY_LIST')
    mimi = lt.newList('ARRAY_LIST')
    for pos in range(0,(lt.size(aUNIC))):
        lt.addLast(mimi,pos)
    posAPA2 = 1
    for i in lt.iterator(mimi):
        fin4 =  lt.newList('ARRAY_LIST')
        codemax = (lt.getElement(fin,i+1))['Cod sub sec']
        ac = lt.getElement(apa,i+1)
        for j in ac['elements']:
            if j['Código subsector económico'] == codemax:
                lt.addLast(fin4,j)
        lt.addLast(fin3,fin4)
        posAPA2 += 1 
    return fin,fin3
    
def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    data_structs = merg.sort(data_structs['data'],compareYear)
    listaA = lt.newList('ARRAY_LIST')
    aUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaA,i['Año'])
        if lt.isPresent(aUNIC,i['Año']) == 0:
           lt.addLast(aUNIC,i['Año'])
           
    listaC = lt.newList('ARRAY_LIST')
    cUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaC,i['Código subsector económico'])
        if lt.isPresent(cUNIC,i['Código subsector económico']) == 0:
           lt.addLast(cUNIC,i['Código subsector económico'])     
    apa = lt.newList('ARRAY_LIST')
    
    for i in lt.iterator(aUNIC): 
        x = lt.newList('ARRAY_LIST')
        for j in lt.iterator(data_structs):
            if j['Año'] == i:
                lt.addLast(x,j)
        x = quk.sort(x,cmp_req_5) 
        lt.addLast(apa,x)
         
    fin = lt.newList('ARRAY_LIST')
    posAPA = 1 
    for j in lt.iterator(aUNIC):
        fin2 = lt.newList('ARRAY_LIST')
        pos_max = 1
        pos = 1 
        max_ = 0
        for i in lt.iterator(cUNIC):
            b = {}
            b['Año']=0
            b['Código Sector']=0
            b['Nombre Sector']=0
            b['Código Subsector']=0
            b['Nombre Subsector']=0
            b['Total de Descuentos Tributarios']=0
            b['Total Ingresos Netos']=0
            b['Total C&G']=0
            b['Total Saldo Por Pagar']=0
            b['Total Saldo a Favor']=0
            an = lt.getElement(apa,posAPA)
            
            for act in lt.iterator(an):
                if act['Código subsector económico']==i:
                    if b['Año']==0:
                        b['Año']=j
                        b['Código Sector']=act['Código sector económico']
                        b['Nombre Sector']=act['Nombre sector económico']
                        b['Código Subsector']=i  
                        b['Nombre Subsector'] = act['Nombre subsector económico']
                    b['Total de Descuentos Tributarios']+=(int(act['Descuentos tributarios']))
                    b['Total Ingresos Netos'] += (int(act['Total ingresos netos']))
                    b['Total C&G']+= (int(act['Total costos y gastos']))
                    b['Total Saldo Por Pagar']+= (int(act['Total saldo a pagar']))
                    b['Total Saldo a Favor']+= (int(act['Total saldo a favor']))
            lt.addLast(fin2,b) 
            if max_ < b['Total de Descuentos Tributarios']:
                max_ = b['Total de Descuentos Tributarios']
                pos_max = pos
            pos += 1   
        lt.addLast(fin, lt.getElement(fin2, pos_max))
        posAPA+=1
    fin3 = lt.newList('ARRAY_LIST')
    mimi = lt.newList('ARRAY_LIST')
    for pos in range(0,(lt.size(aUNIC))):
        lt.addLast(mimi,pos)
    posAPA2 = 1
    for i in lt.iterator(mimi):
        fin4 =  lt.newList('ARRAY_LIST')
        codemax = (lt.getElement(fin,i+1))[ 'Código Subsector']
        ac = lt.getElement(apa,i+1)
        for j in ac['elements']:
            if j['Código subsector económico'] == codemax:
                lt.addLast(fin4,j)
        lt.addLast(fin3,fin4)
        
    return fin,fin3




def req_6(data_structs, yearIn):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    #organizar 
    data_structs = merg.sort(data_structs['data'], compareYear)
    lista_sorteada_anosN = lt.newList('ARRAY_LIST')
    
    for elemento in lt.iterator(data_structs):
        if yearIn == elemento['Año']:
            lt.addLast(lista_sorteada_anosN, elemento)
    lista_sorteada_anosN = merg.sort(lista_sorteada_anosN, compareTIN_byEcoSector)
    #Sectores unicos 
    listaC = lt.newList('ARRAY_LIST')
    cUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_sorteada_anosN):
        lt.addLast(listaC,i['Código sector económico'])
        if lt.isPresent(cUNIC,i['Código sector económico']) == 0:
           lt.addLast(cUNIC,i['Código sector económico'])
    
    #-------lista de actividaes por cod sec-------
    apa = lt.newList('ARRAY_LIST')
    for i in lt.iterator(cUNIC): 
        x = lt.newList('ARRAY_LIST')
        for j in lt.iterator(lista_sorteada_anosN):
            if j['Código sector económico'] == i:
                lt.addLast(x,j)
        lt.addLast(apa,x)
    #acumular
    fin = lt.newList('ARRAY_LIST')
    fin2_R = lt.newList('ARRAY_LIST')
    fin3_R = lt.newList('ARRAY_LIST')
    posAPA = 1 
    for j in lt.iterator(cUNIC):
        b = {}
        b['Código sec']=0
        b['nom sec']=0
        b['tot ing net']=0
        b['Total cyg']=0
        b['Total spp']=0
        b['Total s a fr']=0
        b['Cod sub sec ++']=0
        b['Cod sub sec --']=0       
        code = lt.getElement(apa,posAPA)
        for cod in lt.iterator(code):
            if b['Código sec']==0:
                b['Código sec'] = j
                b['nom sec']=cod['Nombre sector económico']
            b['tot ing net'] += (int(cod['Total ingresos netos']))
            b['Total cyg']+= (int(cod['Total costos y gastos']))
            b['Total spp']+= (int(cod['Total saldo a pagar']))
            b['Total s a fr']+= (int(cod['Total saldo a favor']))
        R1,R2, fin2, fin3 = req_6_secundario(lista_sorteada_anosN,apa, j, posAPA)
        b['Cod sub sec ++'] = R1
        b['Cod sub sec --'] = R2
        lt.addLast(fin,b) 
        lt.addLast(fin2_R,fin2)
        lt.addLast(fin3_R,fin3)
        #info tabla mayor 
        
        posAPA +=1
    return fin, fin2_R, fin3_R

def req_6_secundario(lista_sorteada_anosN,apa, j, posAPA):
    #acumular
    #-------- codigos subsec unicos------
    listaCS = lt.newList('ARRAY_LIST')
    csUNICS = lt.newList('ARRAY_LIST')
    for i in lt.iterator(lista_sorteada_anosN):
        if i['Código sector económico']==j:
            lt.addLast(listaCS,i['Código subsector económico'])
            if lt.isPresent(csUNICS,i['Código subsector económico']) == 0:
                lt.addLast(csUNICS,i['Código subsector económico'])
    fin = lt.newList('ARRAY_LIST')    
    pos_max = 1
    pos = 1 
    max_ = 0
    fin2 = lt.newList('ARRAY_LIST')
    fin3 = lt.newList('ARRAY_LIST')
    pos_min = 1 
    pos2 = 1
    min_= 100_000_000_000_000
    for k in lt.iterator(csUNICS):
        b = {}
        b['codigo Subsector'] = 0
        b['Total ingresos netos'] = 0
        b['Nombre subsector'] = 0 
        b['Costos y gastos'] = 0
        b['Salgo a pagr'] = 0
        b['Saldo a Favor'] = 0
        b['Actividad ++'] = "FUNCIONA"
        b['Actividad --'] = "FUNCIONA"
        
        sub = lt.getElement(apa,posAPA)
        for cod in lt.iterator(sub):
            if cod['Código subsector económico'] == k:
                if b['codigo Subsector']==0:
                    b['codigo Subsector'] = k
                    b['Nombre subsector'] = cod['Nombre subsector económico']
                b['Total ingresos netos'] += (int(cod['Total ingresos netos']))
                b['Costos y gastos'] +=  (int(cod['Total costos y gastos']))
                b['Salgo a pagr']+= (int(cod['Total saldo a pagar']))
                b['Saldo a Favor']+= (int(cod['Total saldo a favor']))

        lt.addLast(fin2,b)
        lt.addLast(fin3,b)
        if max_ < b['Total ingresos netos']:
            max_ = b['Total ingresos netos']
            pos_max = pos
        pos += 1
        if min_ >= b['Total ingresos netos'] and b['codigo Subsector'] != 0:
            min_ = b['Total ingresos netos']
            pos_min = pos2
        pos2 += 1
        
    rmax = lt.getElement(fin2, pos_max)
    rfin1 = rmax['codigo Subsector']
    rmin = lt.getElement(fin2, pos_min)    
    rfin2 = rmin['codigo Subsector']     
    #actividaades que mas aportan al mayor
    #FALLO :( SE INENTO 
    '''
    sub = lt.getElement(apa,posAPA)
    #+ apporta mayor sub sect
    for cod in lt.iterator(sub):
        if cod['codigo Subsector'] == rfin1:
            b=lt.getElement(fin2,pos_max) 
            b['Actividad ++'] = cod
            break
    #+ aporta menor sub sect
    for cod in lt.iterator(sub):
        if cod['codigo Subsector'] == rfin2:
            b=lt.getElement(fin3,pos_min) 
            b['Actividad ++'] = cod
            break
    #- aporta al mayor 
    pos_min = 1 
    pos2_min = 1
    min_min= 100_000_000_000_00
    for cod in lt.iterator(sub):
        if cod['codigo Subsector'] == rfin1:
            if min_min >= cod['Total ingresos netos']:
                min_min = cod['Total ingresos netos']
                pos_min_min = pos2_min
        pos2_min += 1
    jjjj = lt.getElement(sub,pos_min_min)    
    b=lt.getElement(fin2,pos_max) 
    b['Actividad ++'] = jjjj
        #- aporta al mayor 
    pos_min_max = 1 
    pos2_min_max = 1
    min_max= 100_000_000_000_00
    for cod in lt.iterator(sub):
        if cod['codigo Subsector'] == rfin1:
            if min_max >= cod['Total ingresos netos']:
                min_max = cod['Total ingresos netos']
                pos_min_max = pos2_min_max
        pos2_min += 1
    kkkk =  lt.getElement(sub,pos_min_min)          
    b=lt.getElement(fin3,pos_min) 
    b['Actividad ++'] = kkkk      
    '''        
    return rfin1,rfin2, fin2, fin3


def req_7(data_structs, Ain, Afn,TOP):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
        # TODO: Realizar el requerimiento 4
    #------ Anos unicos -----
    data_structs = useQuickSort(data_structs['data'], compareYear)
    posI = 0
    posF = 0
    contI = 0
    contF = lt.size(data_structs)-1
    #ciclo posicion ano inicial
    for i in lt.iterator(data_structs):
        if i['Año'] == Ain:
            posI = contI
            break
        contI += 1
    #ciclo posicion ano final
    for i in range(lt.size(data_structs),0, -1):
        el = lt.getElement(data_structs,i)
        if el['Año'] == Afn:
            posF = contF 
            break
        contF -= 1
    fin_0 = lt.subList(data_structs,posI+1,posF-posI+1)
    fin_1 = quk.sort(fin_0, cmp_req_7)
    fin_2 = lt.subList(fin_1,1,int(TOP))
    fin_3 = quk.sort(fin_2, cmp_req_7_tot)
    return fin_3
   
def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass
# funcion de seguridad imput annos 
def anos_unq(data_structs):
    data_structs = useQuickSort(data_structs['data'], compareYear)
    listaA = lt.newList('ARRAY_LIST')
    aUNIC = lt.newList('ARRAY_LIST')
    for i in lt.iterator(data_structs):
        lt.addLast(listaA,i['Año'])
        if lt.isPresent(aUNIC,i['Año']) == 0:
           lt.addLast(aUNIC,i['Año'])
    return aUNIC

# Funciones utilizadas para comparar elementos dentro de una lista
def cmp_req_7(impuesto1, impuesto2):
    return int(impuesto1['Total costos y gastos']) < int(impuesto2['Total costos y gastos'])
def cmp_req_7_1(impuesto1, impuesto2):
    return int(impuesto1['Año']) > int(impuesto2['Año'])
def cmp_req_7_tot(impuesto1, impuesto2):
    """
    Devuelve verdadero si el año de impuesto1 es menor que el de impuesto2 en el caso de que
    sean iguales, se revisa el código de actividad ecoonómica, de lo contrario retorna false.
    
    Arg:
    
    Impuesto1: Información del primer registro que incluye el año y el código de la actividad economica
    Impuesto2: Información del primer registro que incluye el año y el código de la actividad economica
    """
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return cmp_req_7(impuesto1, impuesto2)
    else:
        return cmp_req_7_1(impuesto1, impuesto2)

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

def compareYear(impuesto1, impuesto2):
    
    '''
    Funcion que retorna True si el año del impuesto1 es menor que el del impuesto2.
    '''
    
    return int(impuesto1['Año']) < int(impuesto2['Año'])

def compareCodeEcoActivity(impuesto1, impuesto2):
    '''
    Funcion que retorna True si el codigo de la actividad economica de un impuesto1 es menor que el del impuesto2.
    '''    
    if impuesto1['Código actividad económica'].isnumeric() and impuesto2['Código actividad económica'].isnumeric():
        return int(impuesto1['Código actividad económica']) < int(impuesto2['Código actividad económica'])

def cmp_impuestos_by_anio_retencion_Total(impuesto1, impuesto2):
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return compareRetencionTotal(impuesto1, impuesto2)
    else: 
        return compareYear(impuesto1, impuesto2)

def compareSaldoAPagar(impuesto1, impuesto2):
    '''
    Funcion que retorna True si el saldo a pagar de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    if impuesto1['Total saldo a pagar'].isnumeric() and impuesto2['Total saldo a pagar'].isnumeric():
        return int(impuesto1['Total saldo a pagar']) > int(impuesto2['Total saldo a pagar'])

def compareSaldoAFavor(impuesto1, impuesto2):
    '''
    Funcion que retorna True si el saldo a favor de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    if impuesto1['Total saldo a favor'].isnumeric() and impuesto2['Total saldo a favor'].isnumeric():
        return int(impuesto1['Total saldo a favor']) > int(impuesto2['Total saldo a favor'])
    
def compareRetencionTotal(impuesto1, impuesto2):
    '''
    Funcion que retorna True si la retencion total de la actividad economica de un impuesto1 es menor que el del impuesto2.
    
    Ademas verifica si dicho valor es numerico.
    '''  
    return int(impuesto1['Total retenciones']) < int(impuesto2['Total retenciones'])

def compareTotalIngresosNetos(impuesto1, impuesto2):
    return int(impuesto1['Total ingresos netos']) > int(impuesto2['Total ingresos netos'])
        
def cmp_impuestos_by_anio_Saldo_a_Favor(impuesto1, impuesto2):
    
    """
    Devuelve verdadero si el año de impuesto1 es menor que el de impuesto2 en el caso de que
    sean iguales, se revisa el saldo a favor de actividad ecoonómica, de lo contrario retorna false.
    
    Arg:
    
    Impuesto1: Información del primer registro que incluye el año y el código de la actividad economica
    Impuesto2: Información del primer registro que incluye el año y el código de la actividad economica
    """
    
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return compareSaldoAFavor(impuesto1, impuesto2)
    else: 
        return compareYear(impuesto1, impuesto2)
    

def cmp_impuestos_by_anio_Saldo(impuesto1, impuesto2):
    """
    Devuelve verdadero si el año de impuesto1 es menor que el de impuesto2 en el caso de que
    sean iguales, se revisa el saldo a pagar de actividad ecoonómica, de lo contrario retorna false.
    
    Arg:
    
    Impuesto1: Información del primer registro que incluye el año y el código de la actividad economica
    Impuesto2: Información del primer registro que incluye el año y el código de la actividad economica
    """
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return compareSaldoAPagar(impuesto1, impuesto2)
    else: 
        return compareYear(impuesto1, impuesto2)


def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2):
    """
    Devuelve verdadero si el año de impuesto1 es menor que el de impuesto2 en el caso de que
    sean iguales, se revisa el código de actividad económica, de lo contrario retorna false.
    
    Arg:
    
    Impuesto1: Información del primer registro que incluye el año y el código de la actividad economica
    Impuesto2: Información del primer registro que incluye el año y el código de la actividad economica
    """
    if int(impuesto1['Año']) == int(impuesto2['Año']):
        return compareCodeEcoActivity(impuesto1, impuesto2)
    else:
        return compareYear(impuesto1, impuesto2)

def cmp_req_2(impuesto1, impuesto2):
    return int(impuesto1['Total saldo a favor']) > int(impuesto2['Total saldo a favor'])

def cmp_req_5(impuesto1, impuesto2):
    return int(impuesto1['Descuentos tributarios']) > int(impuesto2['Descuentos tributarios'])

def cmp_req_4(impuesto1, impuesto2):
    return int(impuesto1['Costos y gastos nómina']) < int(impuesto2['Costos y gastos nómina'])

def compareTIN_byEcoSector(impuesto1, impuesto2):
    
    if int(impuesto1['Código sector económico'] == impuesto2['Código sector económico']):
        
        return int(impuesto1['Total ingresos netos']) > int(impuesto2['Total ingresos netos'])
    else:
        return int(impuesto1['Código sector económico']) < int(impuesto2['Código sector económico'])


# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["id"] > data_2["id"]

#Estas funciones sirven de momento para sortear el año, pero toca generalizarlas para que sirvan para cualquier criterio (DONE)

def useSelectionSort(lista, criterio):
    return se.sort(lista, criterio) 

def useInsertionSort(lista, criterio):
    return ins.sort(lista, criterio) 

def useShellSort(lista, criterio):
    return sa.sort(lista, criterio) 

def useMergeSort(lista, criterio):
    return merg.sort(lista, criterio)

def useQuickSort(lista, criterio):
    return quk.sort(lista, criterio)

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs["data"], sort_criteria)
