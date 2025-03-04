'''
1. Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos.
'''

def custom_max (a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Los numeros son iguales"

print(custom_max(5,5))
print(custom_max(5,6))
print(custom_max(6,5))

'''
1. definir una funcion max_de_tres(), que tome tres numeros como argumentos y devuelva el mayor de ellos.

'''

def max_de_tres(n1:int, n2:int, n3:int):
    '''
    Descrip

    Args:
        n1 (int): [description]
        n2 (int): [description]
        n3 (int): [description]
    
    Returns:
        [type]: [description]
    '''
    n = custom_max(n1,n2)
    return custom_max(n,n3)

print(max_de_tres(1,2,3))
print(max_de_tres(3,2,1))
print(max_de_tres(2,3,1))
