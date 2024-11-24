# Funções puras (Princípios da programação funcional)
# Funções que não alteram o estado do programa e não possuem efeitos colaterais (side effects)
# Funções que sempre retornam o mesmo valor para a mesma entrada (determinísticas)
# Funções que não dependem de variáveis globais e retornam um valor que depende apenas dos argumentos passados

# Efeitos colaterais
# Alteram o estado do programa
# Podem alterar variáveis globais
def soma(a, b):
    return a + b

print(soma(3, 4))
print(soma(3, 4))

# Funções de alta ordem
def aplica_duas_vezes(func, valor):
    return func(func(valor))

def incrementa(x):
    return x + 1

def elevar_ao_quadrado(x):
    return x ** 2

def dividir_por_dois(x):
    return x / 2

# print(incrementa(6))
# print(aplica_duas_vezes(incrementa, 6))
# print(aplica_duas_vezes(elevar_ao_quadrado, 6))

numeros = [1, 2, 3, 4, 5, 6]

# list comprehension
def aplica_transformacao(funcao, lista):
    return [funcao(x) for x in lista]

numeros_quadrados = aplica_transformacao(elevar_ao_quadrado, numeros)
numeros_quadrados_divido_por_dois = aplica_transformacao(dividir_por_dois, numeros_quadrados)

print(numeros_quadrados)
print(numeros_quadrados_divido_por_dois)