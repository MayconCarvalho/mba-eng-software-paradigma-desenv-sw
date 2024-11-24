# Recursão

# Entrada -> Função -> Saída (própria função)
# Fatorial de 4 = 4 * 3 * 2 * 1 = 24
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(f'Fatorial de 4: {fatorial(4)}')

# Fibonacci de 8

# A sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Calcular o n-ésimo número da sequência de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f'Fibonacci de 8: {fibonacci(8)}')
