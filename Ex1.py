'''
1. Estructuras de Datos y Algoritmos
a) LRU Cache
Implementa una caché LRU (Least Recently Used) con las operaciones get(key) y put(key, value), asegurando que la complejidad sea O(1).

b) Algoritmo de Dijkstra
Dado un grafo dirigido con pesos positivos, implementa el algoritmo de Dijkstra para encontrar la ruta más corta desde un nodo origen a todos los demás.

c) Ordenamiento Personalizado
Dado un array de strings, ordénalo basado en la frecuencia de aparición de cada string (de mayor a menor). Si dos strings tienen la misma frecuencia, ordénalos alfabéticamente.
'''

# LRU Cache

class LruCache: 
    def __init__ (self, size):
        self.size = size
        self.cache = dict()
        self.order = []

    #Esto esta revisando si la key esta en el cache, si esta la remueve de la lista y la agrega al final
    #Si no esta, retorna None

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None
    
    #Si el cache esta lleno, remueve el primer elemento de la lista y el primer elemento del cache
    #Agrega el nuevo key y value al cache y lo agrega al final de la lista
    
    def put(self, key, value):
        if len(self.cache) == self.size:
            del self.cache[self.order[0]]
            self.order.pop(0)
        self.cache[key] = value
        self.order.append(key)

# Algoritmo de Dijkstra
import heapq

def dijkstra(graph, start):
    
    #Inicializa las distancias de los nodos en infinito y la distancia del nodo de inicio en 0
    distances = {node: float('infinity') for node in graph}

    #Inicializa la cola con la distancia y el nodo de inicio
    distances[start] = 0

    #Mientras la cola no este vacia, saca el nodo con la menor distancia
    #Si la distancia actual es mayor a la distancia del nodo, continua
    queue = [(0, start)]

    while queue:
        #Extrae el nodo con la menor distancia
        #heapq es una cola de prioridad
        current_distance, current_node = heapq.heappop(queue)

        #Si la distancia actual es mayor a la distancia del nodo, continua
        if current_distance > distances[current_node]:
            continue

        #Itera sobre los vecinos del nodo actual
        #Si la distancia es menor a la distancia del nodo, actualiza la distancia
        #y agrega el nodo a la cola
        for neighbor, weight in graph[current_node].items():
            #Calcula la distancia
            distance = current_distance + weight

            #Si la distancia es menor a la distancia del nodo, actualiza la distancia
            #y agrega el nodo a la cola
            if distance < distances[neighbor]:
                #Actualiza la distancia
                distances[neighbor] = distance
                #Agrega el nodo a la cola
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Ordenamiento Personalizado

def custom_sort(arr):
    freq = dict()
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    arr.sort(key=lambda x: (-freq[x], x))
    arr = list(dict.fromkeys(arr))
    return arr

# Pruebas
cache = LruCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))

arr = ['a', 'b', 'a', 'c', 'b', 'a', 'd', 'e', 'b', 'c', 'z', 'z', 'z', 'z', 'z']
print(custom_sort(arr))

# Output
'''
1
None
None
3
4

{'A': 0, 'B': 1, 'C': 3, 'D': 4}
    
    ['a', 'b', 'c', 'd', 'e']
'''
