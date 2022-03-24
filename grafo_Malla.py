from grafo import Grafo

def malla(m, n, dirigido=False):
  """
  Grafo Malla (Método aleatorio)
  m : número de filas
  n : número de columnas
  """
  g = Grafo('Malla')
  Aristas = 1
  Nodos = 1
  for fila in range(m):
    for columna in range(n):  
      if columna < (n-1):
        g.addArista(Aristas, str(Nodos), str(Nodos + 1))    
        Aristas += 1
      if fila < (m-1):
        g.addArista(Aristas, str(Nodos), str(Nodos + 2))
        Aristas += 1      
      Nodos += 1
  return g

print ("Modelo Malla  ----------")
columnas = int(input("Ingrese número de columnas: "))
filas = int(input("Ingrese número de filas: "))

malla = malla(columnas,filas)
malla.savedArchivo()
