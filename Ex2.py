'''
2. Manipulación de Strings
a) Anagramas en una Lista
Dada una lista de palabras, agrupa aquellas que sean anagramas entre sí. Ejemplo:

Input: ["bat", "tab", "tap", "pat", "cat"]
Output: [["bat", "tab"], ["tap", "pat"], ["cat"]]

b) Decodificación de Expresiones
Dada una string codificada, expande su contenido. Por ejemplo:

Input: "3[a2[c]]"
Output: "accaccacc"
'''


input = ["bat", "tab", "tap", "pat", "cat"]

def anagrams(input):
    anagrams = dict()
    print(anagrams)
    for word in input:
        key = ''.join(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    return list(anagrams.values())

print(input)
print(anagrams(input))

input = "3[a2[c]]"

def decode_string(input):
    stack = []
    current_string = ''
    current_number = 0
    for char in input:
        if char == '[':
            stack.append(current_string)
            stack.append(current_number)
            current_string = ''
            current_number = 0
        elif char == ']':
            number = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + number * current_string
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            current_string += char
    return current_string

print(input)
print(decode_string(input))
