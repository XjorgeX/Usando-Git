>>> lista = ["abc", 42, 3.1415]
>>> lista[0] # Acceder a un elemento por su �ndice
'abc'
>>> lista[-1] # Acceder a un elemento usando un �ndice negativo
3.1415
>>> lista.append(True) # A�adir un elemento al final de la lista
>>> lista
['abc', 42, 3.1415, True]
>>> del lista[3] # Borra un elemento de la lista usando un �ndice (en este caso: True)
>>> lista[0] = "xyz" # Re-asignar el valor del primer elemento de la lista
>>> lista[0:2] # Mostrar los elementos de la lista del �ndice "0" al "2" (sin incluir este �ltimo)
['xyz', 42]
>>> lista_anidada = [lista, [True, 42L]] # Es posible anidar listas
>>> lista_anidada
[['xyz', 42, 3.1415], [True, 42L]]
>>> lista_anidada[1][0] # Acceder a un elemento de una lista dentro de otra lista (del segundo elemento, mostrar el primer elemento)
True