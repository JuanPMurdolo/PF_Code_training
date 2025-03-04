#Python Data Structures

'''
Lists (list)
Description: Ordered and mutable structures that can contain heterogeneous elements (different types).

Use case:
When you need to store and modify a sequence of elements.
For dynamic collections where data may change.
'''
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adds an element

'''
Tuples
Description: Ordered but immutable structures, meaning they cannot be modified after creation.

Use case:
To represent data that should not change, such as coordinates or fixed configurations.
Used in multiple function return values.

'''

coordinates = (10, 20)
x, y = coordinates  # Tuple unpacking

'''
Sets

Description: Unordered collections with unique elements (no duplicates).

Use case:
When you need fast membership checking.
To remove duplicates from a list.
'''
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}

#Turn a list with repeated elements into a set to remove duplicates
numbers = [1, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}


'''
Dictionaries (dict)
Description: Collections of key-value pairs.

Use case:
When you need to store data with unique keys for fast access.
To represent structured objects like JSON.
'''

person = {"name": "John", "age": 30}
print(person["name"])  # "John"

'''
Deque

Description: A double-ended queue, more efficient for adding/removing elements at both ends than a list.

Use case:
When implementing queues or stacks efficiently.
'''

from collections import deque
queue = deque([1, 2, 3])
queue.appendleft(0)  # Adds to the front
queue.pop()  # Removes from the back

'''
named tuple

Description: An alternative to tuples that allows named attributes.

Use case:
To represent structured data more clearly without using a dictionary or a class.
'''

from collections import namedtuple
Person = namedtuple("Person", ["name", "age"])
p = Person("John", 30)
print(p.name)  # "John"

'''
defaultdict

Description: A dictionary that provides default values for missing keys.

Use case:
To avoid errors when accessing undefined keys.
'''
from collections import defaultdict
d = defaultdict(int)
print(d["key"])  # 0 (default value)

'''
Counter

Description: A specialized dictionary for counting elements in a collection.

Use case:
To count the frequency of elements in a list.
'''

from collections import Counter
counter = Counter("banana")
print(counter)  # {'b': 1, 'a': 3, 'n': 2}


'''
OrderedDict

Description: Similar to a dictionary but maintains key insertion order.

Use case:
When you need to maintain the order of dictionary keys.
'''

from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od)  # Keeps insertion order


'''
Heapq

Description: Implements a min-heap structure.

Use case:
When you need to efficiently retrieve the smallest element from a partially sorted collection.
'''
import heapq
heap = [5, 1, 3, 7]
heapq.heapify(heap)
print(heapq.heappop(heap))  # Returns 1 (smallest element)


