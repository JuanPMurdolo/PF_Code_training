'''Manejo de listas y diccionarios en Python

Escribe una función que encuentre el número más frecuente en una lista.
Implementa una función que combine dos diccionarios sumando los valores de claves repetidas.'''


def most_frequent_number(lista):
    frequency = dict()
    for i in lista:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return max(frequency, key=frequency.get)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9
         , 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(most_frequent_number(lista)) # 1

'''
Implementa una función que revierte una cadena sin usar .reverse().
Escribe una función que cuente la frecuencia de palabras en un texto.
'''

def reverse_string(string):
    return string[::-1]

string = 'Hola Mundo'
print(reverse_string(string)) # odnuM aloH

def word_frequency(text):
    frequency = dict()
    for word in text.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = 'Hola Mundo Hola'
print(word_frequency(text)) # {'Hola': 2, 'Mundo': 1}

'''
Búsqueda y ordenamiento (Conceptos básicos)

Implementa búsqueda binaria en una lista ordenada.
Escribe una función que ordene una lista de números sin usar sorted().
'''

def binary_search(lista):
    lista.sort()
    number = 3
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == number:
            return mid
        elif lista[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return None

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(lista)) # 2

def sort_list(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sort_list(lista)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
