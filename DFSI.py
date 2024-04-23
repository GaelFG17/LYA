# Vuelos con busqueda con profundidad iterativa.
from Arbol import Nodo

def DFS_prof_iter(nodo, solucion):
    for limite in range(0, 100):
        visitados = []
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol != None:
            return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir nodos hijo (ciuades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)

            nodo.set_hijos(lista_hijos)

            for nodo_hijo in nodo.get_hijos():
                if nodo_hijo.get_datos() not in visitados:
                    # Llamada recursiva
                    sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite-1)
                    if sol is not None:
                        return sol
        return None

def DFSI(estado_inicial, solucion):
    global resul
    resul = ""
    global conexiones
    conexiones = {
        'EDO.MEX':{'QRO','SLP','SONORA'},
        'PUEBLA':{'HIDALGO','SLP'},
        'CDMX':{'MICHOACAN'},
        'MICHOACAN':{'SONORA'},
        'GUADALAJARA' : {'HIDALGO'},
        'SLP':{'QRO','PUEBLA','EDO.MEX','SONORA','GUADALAJARA'},
        'QRO':{'EDO.MEX','SLP'},
        'HIDALGO':{'PUEBLA','GUADALAJARA','SONORA'},
        'MONTERREY':{'HIDALGO','SLP'},
        'SONORA':{'MONTERREY','HIDALGO','SLP','EDO.MEX','MICHOACAN'}
    }
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    # Mostrar resultado
    if nodo != None:
        resultado = []
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        resul = resultado
    else:
        resul = "Solución no Encontrada"