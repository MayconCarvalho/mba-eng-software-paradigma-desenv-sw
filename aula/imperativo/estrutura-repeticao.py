# SOMAR NÚMEROS ATÉ ATINGIR UM LIMITE
limite = 100
soma = 0
numero = 1

# ENQUANTO A SOMA FOR MENOR QUE O LIMITE, CONTINUE SOMANDO
# while soma < limite:
#     soma += numero
#     numero += 1
#     print(soma)
#     print(numero)

# ENCONTRAR O PRIMEIRO NÚMERO DIVISÍVEL POR 7
# 1 -> 99
# for num in range(1, 100):
#     if num % 7 == 0:
#         print(num)
#         break

# VERIFICAR SE TODOS OS ITENS DA LISTA SÃO POSITIVOS
lista = [1, 2, 3, -4, 5]
todos_positivos = True

for num in lista:
    if num < 0:
        todos_positivos = False
        break

if todos_positivos:
    print("Todos os números são positivos")
else:
    print("Nem todos os números são positivos")
