from Solucion import Solucion
import math

def run():
    query = input().split(" ")
    sm = query[0].lower()
    begin_state = query[1].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))


    if sm == "bfs":
        solucion = Solucion(begin_state, [0,1,2,3,4,5,6,7,8], size, sm)

    elif sm == "dfs":
        solucion = Solucion(begin_state, [0,1,2,3,4,5,6,7,8], size, sm)

    elif sm == "ast":
        solucion = Solucion(begin_state, [0,1,2,3,4,5,6,7,8], size, sm)

    else:
        print("Introduzca comandos de argumentos válidos!")

    solucion.solucion()


if __name__ == "__main__":
    run()