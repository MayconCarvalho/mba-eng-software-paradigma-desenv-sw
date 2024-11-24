class ContaBancaria:

    def __init__(self, titular, saldo_inicial = 0):
        self.titular = titular
        self.__saldo = saldo_inicial
    
    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor do depósito deve ser maior que zero')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente ou valor inválido')


conta_a = ContaBancaria(titular='Maria', saldo_inicial=200)
conta_b = ContaBancaria(titular='Alexandre', saldo_inicial=40000)

# print(conta_a.__saldo) # AttributeError: 'ContaBancaria' object has no attribute '__saldo'
# print(conta_a.get_saldo())

conta_a.depositar(2000)
# conta_a.depositar(-200)
conta_a.depositar(100)
conta_a.sacar(2100)

print(conta_a.get_saldo())
print(conta_b.get_saldo())

conta_b.depositar(1000000)
print(conta_b.get_saldo())
