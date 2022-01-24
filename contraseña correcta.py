'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca
la contraseña correcta.'''

while True:
    palabra = input('Introduzca contraseña: ')

    if palabra == 'contraseña':
        print('Contraseña correcta')
        break
    else:
        palabra = input('Introduzca contraseña: ')