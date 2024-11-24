class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo_do_carro = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f'Carro: {self.marca} {self.modelo_do_carro}, Ano: {self.ano}')
        self.emitir_som()

    def emitir_som(self):
        print('Vruuuuummm ...')

    def acelerar(self):
        print(f'{self.modelo_do_carro} acelerando...')

    def frear(self):
        print(f'{self.modelo_do_carro} freando...')

    def __str__(self):
        return f'{self.modelo_do_carro} {self.cor} {self.ano}'

carro1 = Carro(marca='Toyota', modelo='Corolla', ano=2020)
carro2 = Carro(marca='Honda', modelo='Civic', ano=2021)

# print(carro1.modelo_do_carro)
# print(carro2.modelo_do_carro)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
