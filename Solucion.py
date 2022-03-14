from PuzzleState import PuzzleState
from algoritmos_busqueda import bfs_search, dfs_search, A_star_search

class Solucion(object):

    """Contructor de la Solucion"""
    def __init__(self, estado_inicial, objetivo, size,algoritmo="bfs"):
        
        self.estado_inicial = estado_inicial

        if algoritmo == "bfs":
            self.busqueda = bfs_search
        elif algoritmo == "dfs":
            self.busqueda = dfs_search
        elif algoritmo == "ast":
            self.busqueda = A_star_search
        else:
            raise NotImplementedError("Error no se permite ese algoritmo.")
        
        self.puzzle_state = PuzzleState(estado_inicial, size, objetivo, self.calculate_total_cost)

    def calculate_manhattan_dist(self, punto1_x, punto1_y, punto2_x, punto2_y):

        """Para calcular el manhttan restamos los punto y sacamos los valores absolutos y sumamos esos dos valores """

        return abs(punto1_x - punto2_x) + abs(punto1_y - punto2_y)

    def calculate_total_cost(self, estado):

        """Calculamos el total estimado de costos"""

        sum_man = 0

        for i, item in enumerate(estado.config):
            fila_actual      = i // estado.n
            columna_actual   = i % estado.n
            objetivo_idx     = estado.goal.index(item)
            fila_objetivo    = objetivo_idx // estado.n
            columna_objetivo = objetivo_idx % estado.n

            sum_man += self.calculate_manhattan_dist(fila_actual, columna_actual, fila_objetivo, columna_objetivo)
        
        return sum_man + estado.cost

    def writeOutput(self, resultado):

        """Imprimimos los resultado Obtenidos"""

        estado_final, nodos_expandidos, max_search_depth = resultado #Guardamos en variables los datos obtenidos del nodo ganador
        path_to_goal = [estado_final.action] #Almacenamos el movimiento inicial
        cost_of_path = estado_final.cost #Almacenemos el costo
        parent_state = estado_final.parent  #Almacenemos los nodos padres

        #Recoremos los nodos padres para obtener los movimientos o acciones
        while parent_state:
            if parent_state.parent:
                path_to_goal.append(parent_state.action)
            parent_state = parent_state.parent
        
        path_to_goal.reverse()
        search_depth = len(path_to_goal)

        print("******* Resultados *******")
        estado_final.display()
        print("path_to_goal: " + str(path_to_goal))
        print("cost_of_path: " + str(cost_of_path))
        print("nodes_expanded: " + str(nodos_expandidos))
        print("search_depth: " + str(search_depth))
        print("max_search_depth: " + str(max_search_depth))

        file = open('output.txt', 'w')
        file.write("path_to_goal: " + str(path_to_goal))
        file.write("\ncost_of_path: " + str(cost_of_path))
        file.write("\nnodes_expanded: " + str(nodos_expandidos))
        file.write("\nsearch_depth: " + str(search_depth))
        file.write("\nmax_search_depth: " + str(max_search_depth))
        file.close()

    def solucion(self):

        if self.busqueda == A_star_search:
            resultados = A_star_search(self.puzzle_state, self.calculate_total_cost)
        else:
            resultados = self.busqueda(self.puzzle_state)

        self.writeOutput(resultados)