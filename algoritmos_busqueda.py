from priority_queue import PriorityQueue
import queue

def bfs_search(initial_state):

    """ BFS search """

    cola = queue.Queue() #Inicializamos la cola en FIFO (Primero en entrar, primero en salir) 
    cola.put(initial_state) #Ponemos el objeto en cola
    frontera = {} #Creamos Marcador de estado de froteras
    frontera[tuple(initial_state.config)] = True #Marcamos estado visitado
    explorada = set() #Para almacenar los estado visitados
    nodos_expandidos = 0 #Para almacenar la cantidad de nodos expandidos
    max_search_depth = 0 #Para almecenar la profundidad maxima de busqueda

    #Recoremos las fronteras en cola 
    while not cola.empty():
        estado = cola.get() #Obtenemos frontera en cola
        explorada.add(estado.config)#Agremos estado visitado

        #Validado si es el estado ganador
        if estado.is_goal():
            return (estado, nodos_expandidos, max_search_depth)
        
        nodos_expandidos += 1

        #Expandimos a nuevos nodos
        nodos = estado.expand()

        #Recorremos los nuevos nodos
        for nodo in nodos:
            #Validamos si el nodo no esta explorado y no esta en frontera
            if nodo.config not in explorada and tuple(nodo.config) not in frontera:
                cola.put(nodo) #Agregamos nuevo nodo
                frontera[tuple(nodo.config)] = True #Agregamos a frontera
                if nodo.cost > max_search_depth:
                    max_search_depth = nodo.cost
    return None

def dfs_search(initial_state):

    """DFS search"""

    cola = queue.LifoQueue() #Inicializamos la cola en LIFO (Ultimo en entrar, ultimo en salir)
    cola.put(initial_state) #Agregamos el primer objeto a la cola
    frontera = {} #Creamos Marcador de estado de froteras
    frontera[tuple(initial_state.config)] = True #Marcamos estado visitado
    explorada = set() #Para almacenar los estado visitados
    nodos_expandidos = 0 #Para almacenar la cantidad de nodos expandidos
    max_search_depth = 0 #Para almecenar la profundidad maxima de busqueda

    #Recoremos las fronteras en cola
    while not cola.empty():

        estado = cola.get() #Obtenemos frontera en cola
        explorada.add(estado.config) #Agremos estado visitado

        #Validado si es el estado ganador
        if estado.is_goal():
            return (estado, nodos_expandidos, max_search_depth)

        nodos_expandidos += 1

        #Expandimos a nuevos nodos y cambiamos el orden de UDLR a RLDU
        nodos = estado.expand(RLDU = True)

         #Recorremos los nuevos nodos
        for nodo in nodos:
            #Validamos si el nodo no esta explorado y no esta en frontera
            if nodo.config not in explorada and tuple(nodo.config) not in frontera:
                cola.put(nodo) #Agregamos nuevo nodo
                frontera[tuple(nodo.config)] = True #Agregamos a frontera
                if nodo.cost > max_search_depth:
                    max_search_depth = nodo.cost
    return None

def A_star_search(initial_state, calculate_total_cost):
    
    """A * search"""

    cola = PriorityQueue('min', calculate_total_cost) #Inicializamos la cola, cola de prioridad
    cola.append(initial_state) #Agregamos el primer objeto a la cola
    frontera = {} #Creamos Marcador de estado de froteras
    frontera[tuple(initial_state.config)] = True #Marcamos estado visitado
    explorado = set() #Para almacenar los estado visitados
    nodos_expandidos = 0 #Para almacenar la cantidad de nodos expandidos
    max_search_depth = 0 #Para almecenar la profundidad maxima de busqueda

    #Recorremos la cola
    while cola:
        estado = cola.pop()
        explorado.add(estado)

        if estado.is_goal():
            return (estado, nodos_expandidos, max_search_depth)
        
        nodos_expandidos += 1

        nodos = estado.expand()

        for nodo in nodos:
            if nodo not in explorado and tuple(nodo.config) not in frontera:
                cola.append(nodo)
                frontera[tuple(nodo.config)] = True

                if nodo.cost > max_search_depth:
                    max_search_depth = nodo.cost

            elif nodo in cola:
                if calculate_total_cost(nodo) < cola[nodo]:
                    cola.__delitem__(nodo)
                    cola.append(nodo)
    return None




        











