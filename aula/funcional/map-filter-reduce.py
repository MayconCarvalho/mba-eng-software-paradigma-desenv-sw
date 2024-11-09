from functools import reduce
# Map, Filter e Reduce
# Map: aplica uma função a todos os itens de uma lista
# Filter: filtra os itens de uma lista
# Reduce: aplica uma função a todos os itens de uma lista, de forma cumulativa

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Dobrar os números pares
pares_dobrados = list(map(lambda x: x * 2, pares))
print(pares_dobrados)

# Somar os números pares dobrados
soma_pares_dobrados = reduce(lambda x, y: x + y, pares_dobrados)
print(soma_pares_dobrados)
