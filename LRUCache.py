class LRUCache:
  def __init__(self, n):
    self.cache = dict()
    self.size = n
    self.order = []


  def get(self, key):
    #Si la llave ya existe la renueva y la pushea
    if key in self.cache:
      self.order.remove(key)
      self.order.append(key)
      return self.cache[key]
    return None

  def set(self, key, val):
    # your code goes here
    if len(self.cache) == self.size:
      del self.cache[self.order[0]]
      self.order.pop(0)
    self.cache[key] = val
    self.order.append(key)

# debug your code below
cache = LRUCache(2)
cache.set('user1', 'Alex')
cache.set('user2', 'Pack')
print(cache.get('user1'))
print(cache.get('user2'))
cache.set('user3', 'Peak')
print(cache.get('user1'))
print(cache.get('user2'))
print(cache.get('user3'))
