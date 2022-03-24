from nodo import Nodo 
from arista import Arista 
neighbour = 'Vecino'
edge = 'Arista'


class Grafo():
  """
  Clase Grafo
  """
  def __init__(self, nombre):
    """
    Inicializa el grafo.
    nombre : Nombre del grafo.
    nodos
    aristas
    """
    self.id = nombre
    self.nodos = {} 
    self.aristas = {}
  
  def savedArchivo(self):
    """
    Guarda datos de grafo en formato .gv
    Warning : Cuidado ya que sobre escribe una vez ejecutado el grafo solicitado.
    """
    file = open('{}.gv'.format(self.id), 'w')
    file.write('digraph #nombre {' + '\n')
    for arista in self.aristas:
      objetoArista = self.aristas[arista]
      nodoInicial = objetoArista.inicio.id
      nodoFinal = objetoArista.final.id
      file.write('{} -- {};'.format(nodoInicial,nodoFinal) + '\n')
    file.write('}')
    file.close()

  def addNodo(self, nombreNodo):
    """
    Crea nodo , si esta creado no hace nada de lo contrario crea.
    """
    if nombreNodo in self.nodos:
        pass
    else:
      _nodo = Nodo(nombreNodo)
      self.nodos[nombreNodo] = _nodo
    return self.nodos[nombreNodo]
  
  def addArista(self, nombreArista, nombreNodoOrigin, nombreNodoDestino):
    """
    Crea arista, si esta creada no hace nada, de lo contrario crea.
    """
    if nombreArista in self.aristas:
        pass
    else:
        nodoOrigen = self.addNodo(nombreNodoOrigin)
        nodoDestino = self.addNodo(nombreNodoDestino)
        _arista = Arista(nombreArista,self.nodos[nombreNodoOrigin],self.nodos[nombreNodoDestino])
        self.aristas[nombreArista] = _arista
        nodoOrigen.attributos[neighbour].append(nodoDestino)
        nodoDestino.attributos[neighbour].append(nodoOrigen)
        nodoOrigen.attributos[edge].append(_arista)
        nodoDestino.attributos[edge].append(_arista)

  def giveNodo(self, nombre):
    return self.nodos[nombre]
  
  def givedegreesNodo(self, nombreNodo):
    """
    Entrega el grado del nodo considerado.
    """
    if not nombreNodo in self.nodos:
      print('Nodo no existe')

    else:
      _nodo = self.nodos[nombreNodo]
      grado = len(_nodo.attributos[neighbour])
      return grado

