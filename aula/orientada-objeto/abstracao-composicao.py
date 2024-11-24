from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    
    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError('Este método deve ser implementado na subclasse')
    
    # @abstractmethod
    # def calcular_perimetro(self):
    #     raise NotImplementedError('Este método deve ser implementado na subclasse')

class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.base = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

circulo_1 = Circulo(raio=10)
circulo_2 = Circulo(raio=2)

print(circulo_1.calcular_area())
print(circulo_2.calcular_area())

retangulo_1 = Retangulo(largura=10, altura=5)

print(retangulo_1.calcular_area())

class Motor:

    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True
        print('Vruuuuuuumm')

class Carro:

    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
    
    def exibir_detahes(self):
        print(f'Carro: {self.marca} {self.modelo}')
    
    def mostrar_potencia_motor(self):
        print(f'Potência do motor: {self.motor.potencia} cv')


motor1 = Motor(potencia=200)
carro1 = Carro(marca='Fiat', modelo='Uno', motor=motor1)

carro1.exibir_detahes()
carro1.mostrar_potencia_motor()