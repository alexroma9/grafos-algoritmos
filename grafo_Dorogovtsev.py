from grafo import Grafo
import random

def dorogovtsev_mendes(n, directed=False):
    """
    Grafo Dorogovtsev (Método aleatorio)
    n : número de nodos.
    """
    g = Grafo('Dorogovtse-Mendes')
    Aristas = 4
    g.addArista(str(1), str(0), str(1))
    g.addArista(str(2), str(0), str(2))
    g.addArista(str(3), str(1), str(2))
    for nAdic in range(3, 3 + n-3):
        num_edges = len(g.aristas)
        random_edges = random.randint(1,num_edges)
        edges_select = g.aristas[str(random_edges)]
        nI = edges_select.inicio
        nF = edges_select.final
        g.addArista(str(Aristas), str(nAdic), str(nI.id))
        Aristas += 1
        g.addArista(str(Aristas), str(nAdic), str(nF.id))
        Aristas += 1
    return g


print ("Modelo Dorogovtsev  ----------")
nodo = int(input("Ingrese número de nodos: "))

grafodorogovtsev_mendes = dorogovtsev_mendes(nodo)
grafodorogovtsev_mendes.savedArchivo()


