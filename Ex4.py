'''
4. Manipulación de Estructuras de Datos
a) Flatten de una Lista Anidada
Dada una lista anidada, conviértela en una lista plana sin usar librerías externas.

Input: [1, [2, [3, 4]], 5]
Output: [1, 2, 3, 4, 5]
b) Merge de K Listas Enlazadas
Dado k listas enlazadas ordenadas, fusiónalas en una sola lista enlazada ordenada.
'''

input = [1, [2, [3, 4]], 5]

def flatten(input):
    result = []
    for item in input:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(input)

print(flatten(input))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    def merge_two_lists(l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = merge_two_lists(l1.next, l2)
            return l1
        l2.next = merge_two_lists(l1, l2.next)
        return l2

    if not lists:
        return None
    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]

l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

result = merge_k_lists([l1, l2, l3])

while result:
    print(result.val, end=' ')
    result = result.next
# Output

# [1, 2, 3, 4, 5]
# 1 1 2 3 4 4 5 6
