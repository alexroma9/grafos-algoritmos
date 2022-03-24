from grafo import Grafo
import random

def gilbert(n, pr):
  """
  Grafo Gilbert (Método aleatorio)
  n : número de nodos
  pr : probabilidad asignada que se considerá para generar si / no la arista entre dos nodos.
  """
  g = Grafo('Gilbert')
  for i in range(n):
    g.addNodo(str(i))

  Aristas = 1
  for i in range(n):
    for j in range(n):
      if random.random() < pr:
        if (j != i):
          g.addArista(str(Aristas),str(i),str(j))
          Aristas += 1
  return g
 
print ("Modelo Gilbert  ----------")
nodo = int(input("Ingrese número de nodos: "))
prob = float(input("Ingrese la probabilidad de crear la arista: "))
 
gilbert = gilbert(nodo,prob)
gilbert.savedArchivo()

