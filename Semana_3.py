# lista vacia
# lista_vacia = []
# print(lista_vacia)
# print(type(lista_vacia))

# lista_vacia = list()
# print(lista_vacia)
# print(type(lista_vacia))

lista = [1, "Hola mundo", 1.5, "1", ["otra", "lista"], True, {}]
# print(lista)

print(lista[2])
# agrega un elemento al final
lista.append("nuevo")
print(lista)

# agregar un numero en el indice número 3
lista.insert(3, "Adios mundo")
print(lista)

# eleminar el ultimo elemento por defecto sino ingresar el índice
lista.pop(3)
print(lista)