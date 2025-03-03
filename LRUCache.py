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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'Node({self.val}, {self.next})'

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
        reverse_list(next)
    return prev
# debug your code below
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(head)
reversed_head = reverse_list(head)
print(reversed_head.val)
print(reversed_head.next.val)

def is_palindrome(s: str) -> bool:
    print (s)
    print (s[::-1])
    return s == s[::-1]



# debug your code below
print(is_palindrome('abcba'))


def print_without_loop(n: int, m: int):
   if n <= m:
      print(n)
      print_without_loop(n + 1, m)
   else:
     return
   
print_without_loop(1 ,23)
      