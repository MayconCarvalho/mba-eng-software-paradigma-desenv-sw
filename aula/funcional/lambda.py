# Exemplo de uso de lambda
dobro = lambda x: x * 2

# print(dobro(4))

# valores = [1, 2, 3, 4, 5]

# valores_dobrados = list(map(lambda x: x * 2, valores))

# print(valores_dobrados)

# Exemplo 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_impares = []

# for numero in numeros:
#     if numero % 2 != 0:
#         numeros_impares.append(numero)

# print(numeros_impares)

# Exemplo 3

numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

print(numeros_impares)
