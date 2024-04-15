# Definir el diccionario
mi_diccionario = {
    "lista1": [1, 2, 3],
    "lista2": ["a", "b", "c"],
    "lista3": ["x", "y", "z"]
}

# Iterar sobre cada par clave-valor en el diccionario
for clave, lista in mi_diccionario.items():
    # Verificar si el elemento 'z' está presente en la lista actual
    if 'z' in lista:
        # Si lo encuentra, obtener el índice del elemento 'z' en la lista
        indice = lista.index('z')
        # Imprimir el índice y la clave
        print(f"El elemento 'z' se encuentra en la lista '{clave}' en el índice {indice}.")
        break  # Salir del bucle una vez que se encuentra el elemento
else:
    # Si el elemento 'z' no se encuentra en ninguna lista
    print("El elemento 'z' no se encuentra en ninguna lista del diccionario.")
