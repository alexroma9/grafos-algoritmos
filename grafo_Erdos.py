from grafo import Grafo
import random

def erdosrenyi(n,m, dirigido=False, auto=False):
  """
  Grafo Erdos-Renyi (método aleatorio)
  n : número de nodos
  m : número de aristas 
  """
  g = Grafo('Erdos-Renyi')
  for i in range(n):
    g.addNodo(str(i))
  for i in range(m):
    u = random.randint(0, n-1)
    v = random.randint(0, n-1)
    if u != v:
      g.addArista(str(i),str(u),str(v))
  return g


print ("Modelo Erdös y Rényi  ----------")
nodo = int(input("Ingrese número de nodos: "))
arista = int(input("Ingrese número de aristas: "))

erdosrenyi = erdosrenyi(nodo,arista)
erdosrenyi.savedArchivo()

